#!/bin/bash

# WordPress Enterprise Security Unit Tests
# Comprehensive unit testing for security hardening functions

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m'

# Test configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
TEST_DIR="$PROJECT_DIR/tests"
REPORTS_DIR="$TEST_DIR/reports/unit-tests"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
TEST_RUN_ID="security_unit_test_$TIMESTAMP"

# Test results tracking
TOTAL_TESTS=0
PASSED_TESTS=0
FAILED_TESTS=0
SKIPPED_TESTS=0

# Function to print colored output
print_color() {
    local color=$1
    shift
    echo -e "${color}$*${NC}"
}

print_header() {
    echo
    print_color $PURPLE "=================================="
    print_color $PURPLE "$1"
    print_color $PURPLE "=================================="
    echo
}

print_status() {
    print_color $BLUE "ℹ️  $1"
}

print_success() {
    print_color $GREEN "✅ $1"
}

print_warning() {
    print_color $YELLOW "⚠️  $1"
}

print_error() {
    print_color $RED "❌ $1"
}

# Test result tracking functions
test_pass() {
    ((TOTAL_TESTS += 1))
    ((PASSED_TESTS += 1))
    print_success "$1"
}

test_fail() {
    ((TOTAL_TESTS += 1))
    ((FAILED_TESTS += 1))
    print_error "$1"
}

test_skip() {
    ((TOTAL_TESTS += 1))
    ((SKIPPED_TESTS += 1))
    print_warning "$1 (SKIPPED)"
}

# Setup test environment
setup_test_environment() {
    print_header "Setting Up Test Environment"

    mkdir -p "$REPORTS_DIR"
    mkdir -p "/tmp/security-unit-tests"

    # Create test log file
    TEST_LOG="$REPORTS_DIR/${TEST_RUN_ID}.log"
    touch "$TEST_LOG"

    print_success "Test environment ready"
    print_status "Test Run ID: $TEST_RUN_ID"
    print_status "Reports Directory: $REPORTS_DIR"
}

# Test 1: Security script existence and permissions
test_security_scripts() {
    print_header "Testing Security Script Installation"

    local scripts=(
        "/usr/local/bin/wordpress-security-status"
        "/usr/local/bin/wordpress-security-maintenance"
    )

    # Add platform-specific scripts
    if [[ -f /etc/redhat-release ]] || [[ -f /etc/centos-release ]]; then
        scripts+=(
            "/usr/local/bin/wordpress-selinux-status"
            "/usr/local/bin/wordpress-selinux-troubleshoot"
        )
    elif [[ -f /etc/debian_version ]]; then
        scripts+=(
            "/usr/local/bin/wordpress-apparmor-status"
            "/usr/local/bin/wordpress-apparmor-troubleshoot"
        )
    fi

    for script in "${scripts[@]}"; do
        if [[ -f "$script" ]]; then
            if [[ -x "$script" ]]; then
                test_pass "Script exists and is executable: $script"
            else
                test_fail "Script exists but is not executable: $script"
            fi
        else
            test_fail "Script missing: $script"
        fi
    done
}

# Test 2: Security configuration files
test_security_configs() {
    print_header "Testing Security Configuration Files"

    # Test fail2ban configuration
    if [[ -f /etc/fail2ban/jail.d/wordpress.conf ]]; then
        if grep -q "wordpress-auth" /etc/fail2ban/jail.d/wordpress.conf; then
            test_pass "WordPress fail2ban configuration exists and contains expected content"
        else
            test_fail "WordPress fail2ban configuration exists but missing expected content"
        fi
    else
        test_fail "WordPress fail2ban configuration missing"
    fi

    # Test audit rules (RHEL/CentOS)
    if [[ -f /etc/redhat-release ]] || [[ -f /etc/centos-release ]]; then
        if [[ -f /etc/audit/rules.d/wordpress.rules ]]; then
            if grep -q "wordpress" /etc/audit/rules.d/wordpress.rules; then
                test_pass "WordPress audit rules exist and contain expected content"
            else
                test_fail "WordPress audit rules exist but missing expected content"
            fi
        else
            test_fail "WordPress audit rules missing on RHEL/CentOS system"
        fi
    else
        test_skip "WordPress audit rules (RHEL/CentOS specific)"
    fi

    # Test AppArmor profiles (Ubuntu/Debian)
    if [[ -f /etc/debian_version ]]; then
        local profiles=(
            "/etc/apparmor.d/wordpress-php-fpm"
            "/etc/apparmor.d/wordpress-nginx"
            "/etc/apparmor.d/wordpress-apache"
            "/etc/apparmor.d/wordpress-wpcli"
        )

        for profile in "${profiles[@]}"; do
            if [[ -f "$profile" ]]; then
                if grep -q "# WordPress" "$profile"; then
                    test_pass "AppArmor profile exists and valid: $(basename "$profile")"
                else
                    test_fail "AppArmor profile exists but invalid: $(basename "$profile")"
                fi
            else
                test_skip "AppArmor profile: $(basename "$profile")"
            fi
        done
    else
        test_skip "AppArmor profiles (Ubuntu/Debian specific)"
    fi
}

# Test 3: SELinux configuration (RHEL/CentOS)
test_selinux_config() {
    print_header "Testing SELinux Configuration"

    if [[ -f /etc/redhat-release ]] || [[ -f /etc/centos-release ]]; then
        # Check if SELinux is available
        if command -v getenforce >/dev/null 2>&1; then
            local selinux_status
            selinux_status=$(getenforce)

            if [[ "$selinux_status" == "Enforcing" ]] || [[ "$selinux_status" == "Permissive" ]]; then
                test_pass "SELinux is active: $selinux_status"

                # Test SELinux booleans
                local booleans=(
                    "httpd_can_network_connect"
                    "httpd_can_network_connect_db"
                    "httpd_builtin_scripting"
                )

                for boolean in "${booleans[@]}"; do
                    if getsebool "$boolean" | grep -q "on"; then
                        test_pass "SELinux boolean enabled: $boolean"
                    else
                        test_fail "SELinux boolean disabled: $boolean"
                    fi
                done

                # Test file contexts
                if ls -Z /var/www >/dev/null 2>&1; then
                    test_pass "SELinux file contexts are queryable"
                else
                    test_fail "Cannot query SELinux file contexts"
                fi
            else
                test_fail "SELinux is disabled"
            fi
        else
            test_fail "SELinux commands not available on RHEL/CentOS system"
        fi
    else
        test_skip "SELinux tests (RHEL/CentOS specific)"
    fi
}

# Test 4: AppArmor configuration (Ubuntu/Debian)
test_apparmor_config() {
    print_header "Testing AppArmor Configuration"

    if [[ -f /etc/debian_version ]]; then
        # Check if AppArmor is available
        if command -v aa-status >/dev/null 2>&1; then
            if aa-status --enabled; then
                test_pass "AppArmor is enabled"

                # Test profile loading
                local aa_output
                aa_output=$(aa-status)

                if echo "$aa_output" | grep -q "profiles are in enforce mode"; then
                    test_pass "AppArmor profiles are in enforce mode"
                elif echo "$aa_output" | grep -q "profiles are in complain mode"; then
                    test_pass "AppArmor profiles are in complain mode"
                else
                    test_fail "No AppArmor profiles detected"
                fi

                # Test WordPress-specific profiles
                if echo "$aa_output" | grep -q "wordpress"; then
                    test_pass "WordPress AppArmor profiles are loaded"
                else
                    test_skip "WordPress AppArmor profiles not loaded"
                fi
            else
                test_fail "AppArmor is not enabled"
            fi
        else
            test_fail "AppArmor commands not available on Ubuntu/Debian system"
        fi
    else
        test_skip "AppArmor tests (Ubuntu/Debian specific)"
    fi
}

# Test 5: Security tools installation
test_security_tools() {
    print_header "Testing Security Tools Installation"

    local tools=(
        "fail2ban"
        "rkhunter"
        "chkrootkit"
        "logwatch"
    )

    for tool in "${tools[@]}"; do
        if command -v "$tool" >/dev/null 2>&1; then
            test_pass "Security tool installed: $tool"
        else
            test_fail "Security tool missing: $tool"
        fi
    done

    # Test service status
    local services=("fail2ban" "auditd")

    for service in "${services[@]}"; do
        if systemctl is-active --quiet "$service"; then
            test_pass "Security service active: $service"
        else
            test_fail "Security service inactive: $service"
        fi
    done
}

# Test 6: Firewall configuration
test_firewall_config() {
    print_header "Testing Firewall Configuration"

    if [[ -f /etc/redhat-release ]] || [[ -f /etc/centos-release ]]; then
        # Test firewalld on RHEL/CentOS
        if systemctl is-active --quiet firewalld; then
            test_pass "firewalld is active"

            if firewall-cmd --state >/dev/null 2>&1; then
                test_pass "firewalld is running"
            else
                test_fail "firewalld state check failed"
            fi
        else
            test_fail "firewalld is not active"
        fi
    elif [[ -f /etc/debian_version ]]; then
        # Test ufw on Ubuntu/Debian
        if command -v ufw >/dev/null 2>&1; then
            if ufw status | grep -q "Status: active"; then
                test_pass "UFW is active"
            else
                test_fail "UFW is not active"
            fi
        else
            test_fail "UFW is not installed"
        fi
    else
        test_skip "Firewall tests (unknown OS)"
    fi
}

# Test 7: Automatic updates configuration
test_auto_updates() {
    print_header "Testing Automatic Updates Configuration"

    if [[ -f /etc/redhat-release ]] || [[ -f /etc/centos-release ]]; then
        # Test yum-cron on RHEL/CentOS
        if systemctl is-enabled --quiet yum-cron 2>/dev/null; then
            test_pass "yum-cron is enabled for automatic updates"
        else
            test_fail "yum-cron is not enabled"
        fi
    elif [[ -f /etc/debian_version ]]; then
        # Test unattended-upgrades on Ubuntu/Debian
        if dpkg -l unattended-upgrades >/dev/null 2>&1; then
            test_pass "unattended-upgrades is installed"
        else
            test_fail "unattended-upgrades is not installed"
        fi
    else
        test_skip "Automatic updates tests (unknown OS)"
    fi
}

# Test 8: File permissions and ownership
test_file_permissions() {
    print_header "Testing File Permissions and Ownership"

    # Test WordPress directory (if exists)
    if [[ -d "/var/www/html/wordpress" ]]; then
        local wp_perms
        wp_perms=$(stat -c "%a" /var/www/html/wordpress)

        if [[ "$wp_perms" == "755" ]]; then
            test_pass "WordPress directory has correct permissions (755)"
        else
            test_fail "WordPress directory has incorrect permissions: $wp_perms"
        fi

        # Test wp-config.php (if exists)
        if [[ -f "/var/www/html/wordpress/wp-config.php" ]]; then
            local config_perms
            config_perms=$(stat -c "%a" /var/www/html/wordpress/wp-config.php)

            if [[ "$config_perms" == "644" ]]; then
                test_pass "wp-config.php has correct permissions (644)"
            else
                test_fail "wp-config.php has incorrect permissions: $config_perms"
            fi
        else
            test_skip "wp-config.php permissions (file not found)"
        fi
    else
        test_skip "WordPress directory permissions (directory not found)"
    fi
}

# Test 9: Security script functionality
test_security_script_functions() {
    print_header "Testing Security Script Functionality"

    # Test security status script
    if [[ -x "/usr/local/bin/wordpress-security-status" ]]; then
        if /usr/local/bin/wordpress-security-status >/dev/null 2>&1; then
            test_pass "wordpress-security-status script executes successfully"
        else
            test_fail "wordpress-security-status script execution failed"
        fi
    else
        test_fail "wordpress-security-status script not executable"
    fi

    # Test platform-specific scripts
    if [[ -f /etc/redhat-release ]] || [[ -f /etc/centos-release ]]; then
        if [[ -x "/usr/local/bin/wordpress-selinux-status" ]]; then
            if /usr/local/bin/wordpress-selinux-status >/dev/null 2>&1; then
                test_pass "wordpress-selinux-status script executes successfully"
            else
                test_fail "wordpress-selinux-status script execution failed"
            fi
        else
            test_fail "wordpress-selinux-status script not executable"
        fi
    elif [[ -f /etc/debian_version ]]; then
        if [[ -x "/usr/local/bin/wordpress-apparmor-status" ]]; then
            if /usr/local/bin/wordpress-apparmor-status >/dev/null 2>&1; then
                test_pass "wordpress-apparmor-status script executes successfully"
            else
                test_fail "wordpress-apparmor-status script execution failed"
            fi
        else
            test_fail "wordpress-apparmor-status script not executable"
        fi
    fi
}

# Test 10: Cron job configuration
test_cron_configuration() {
    print_header "Testing Security Cron Job Configuration"

    if crontab -l 2>/dev/null | grep -q "wordpress-security-maintenance"; then
        test_pass "WordPress security maintenance cron job is configured"
    else
        test_fail "WordPress security maintenance cron job is not configured"
    fi
}

# Test 11: Log file creation and permissions
test_log_files() {
    print_header "Testing Security Log Files"

    # Test audit log (RHEL/CentOS)
    if [[ -f /etc/redhat-release ]] || [[ -f /etc/centos-release ]]; then
        if [[ -f /var/log/audit/audit.log ]]; then
            if [[ -r /var/log/audit/audit.log ]]; then
                test_pass "Audit log exists and is readable"
            else
                test_fail "Audit log exists but is not readable"
            fi
        else
            test_fail "Audit log does not exist"
        fi
    else
        test_skip "Audit log tests (RHEL/CentOS specific)"
    fi

    # Test fail2ban log
    if [[ -f /var/log/fail2ban.log ]]; then
        if [[ -r /var/log/fail2ban.log ]]; then
            test_pass "fail2ban log exists and is readable"
        else
            test_fail "fail2ban log exists but is not readable"
        fi
    else
        test_skip "fail2ban log (may not exist if no activity)"
    fi
}

# Test 12: Network security settings
test_network_security() {
    print_header "Testing Network Security Settings"

    # Test kernel parameters
    local sysctl_params=(
        "net.ipv4.ip_forward=0"
        "net.ipv4.conf.all.send_redirects=0"
        "net.ipv4.conf.all.accept_source_route=0"
    )

    for param in "${sysctl_params[@]}"; do
        local key value expected_value
        IFS='=' read -r key expected_value <<< "$param"
        value=$(sysctl -n "$key" 2>/dev/null || echo "unknown")

        if [[ "$value" == "$expected_value" ]]; then
            test_pass "Kernel parameter correctly set: $key = $value"
        else
            test_fail "Kernel parameter incorrectly set: $key = $value (expected $expected_value)"
        fi
    done
}

# Test 13: Password policy configuration
test_password_policy() {
    print_header "Testing Password Policy Configuration"

    if [[ -f /etc/login.defs ]]; then
        local policies=(
            "PASS_MAX_DAYS"
            "PASS_MIN_DAYS"
            "PASS_MIN_LEN"
            "PASS_WARN_AGE"
        )

        for policy in "${policies[@]}"; do
            if grep -q "^$policy" /etc/login.defs; then
                local value
                value=$(grep "^$policy" /etc/login.defs | awk '{print $2}')
                test_pass "Password policy configured: $policy = $value"
            else
                test_fail "Password policy not configured: $policy"
            fi
        done
    else
        test_fail "/etc/login.defs not found"
    fi
}

# Test 14: Security context validation
test_security_contexts() {
    print_header "Testing Security Context Validation"

    if [[ -f /etc/redhat-release ]] || [[ -f /etc/centos-release ]]; then
        # Test SELinux contexts
        if command -v getenforce >/dev/null 2>&1 && [[ "$(getenforce)" != "Disabled" ]]; then
            # Test some common contexts
            if ls -Z /var/www >/dev/null 2>&1; then
                local context
                context=$(ls -Z /var/www | head -1 | awk '{print $1}')
                if [[ -n "$context" ]] && [[ "$context" != "?" ]]; then
                    test_pass "SELinux contexts are properly set"
                else
                    test_fail "SELinux contexts are not properly set"
                fi
            else
                test_fail "Cannot query SELinux contexts"
            fi
        else
            test_skip "SELinux context validation (SELinux disabled)"
        fi
    elif [[ -f /etc/debian_version ]]; then
        # Test AppArmor profiles
        if command -v aa-status >/dev/null 2>&1; then
            local profile_count
            profile_count=$(aa-status | grep -c "profiles are loaded" || echo "0")
            if [[ "$profile_count" -gt 0 ]]; then
                test_pass "AppArmor profiles are loaded and active"
            else
                test_fail "No AppArmor profiles are loaded"
            fi
        else
            test_skip "AppArmor profile validation (AppArmor not available)"
        fi
    else
        test_skip "Security context validation (unknown OS)"
    fi
}

# Test 15: Error handling and edge cases
test_error_handling() {
    print_header "Testing Error Handling and Edge Cases"

    # Test script behavior with missing files
    local test_script="/tmp/test-security-error-handling.sh"
    cat > "$test_script" << 'EOF'
#!/bin/bash
# Test script for error handling
if [[ -f "/nonexistent/file" ]]; then
    echo "File exists"
    exit 0
else
    echo "File does not exist"
    exit 1
fi
EOF
    chmod +x "$test_script"

    if "$test_script" >/dev/null 2>&1; then
        test_fail "Error handling test should have failed but passed"
    else
        test_pass "Error handling test correctly failed for missing file"
    fi

    rm -f "$test_script"

    # Test with invalid permissions
    local test_file="/tmp/test-invalid-perms"
    touch "$test_file"
    chmod 000 "$test_file"

    if [[ -r "$test_file" ]]; then
        test_fail "Invalid permissions test should not be readable"
    else
        test_pass "Invalid permissions correctly prevent reading"
    fi

    chmod 644 "$test_file"
    rm -f "$test_file"
}

# Generate comprehensive test report
generate_test_report() {
    print_header "Generating Test Report"

    local success_rate=0
    if [[ $TOTAL_TESTS -gt 0 ]]; then
        success_rate=$(echo "scale=2; $PASSED_TESTS * 100 / $TOTAL_TESTS" | bc -l 2>/dev/null || echo "0")
    fi

    local report_file="$REPORTS_DIR/${TEST_RUN_ID}_report.json"

    cat > "$report_file" << EOF
{
  "test_run_id": "$TEST_RUN_ID",
  "timestamp": "$(date -Iseconds)",
  "total_tests": $TOTAL_TESTS,
  "passed_tests": $PASSED_TESTS,
  "failed_tests": $FAILED_TESTS,
  "skipped_tests": $SKIPPED_TESTS,
  "success_rate": "$success_rate%",
  "os_family": "$(uname -s)",
  "os_version": "$(uname -r)",
  "test_categories": [
    "security_scripts",
    "security_configs",
    "selinux_config",
    "apparmor_config",
    "security_tools",
    "firewall_config",
    "auto_updates",
    "file_permissions",
    "script_functions",
    "cron_configuration",
    "log_files",
    "network_security",
    "password_policy",
    "security_contexts",
    "error_handling"
  ]
}
EOF

    print_success "Test report saved: $report_file"
}

# Display test summary
display_test_summary() {
    print_header "Security Unit Test Summary"

    echo "Test Run ID: $TEST_RUN_ID"
    echo "Total Tests: $TOTAL_TESTS"
    print_success "Passed: $PASSED_TESTS"
    if [[ $FAILED_TESTS -gt 0 ]]; then
        print_error "Failed: $FAILED_TESTS"
    else
        print_success "Failed: $FAILED_TESTS"
    fi
    print_warning "Skipped: $SKIPPED_TESTS"

    local success_rate=0
    if [[ $TOTAL_TESTS -gt 0 ]]; then
        success_rate=$(echo "scale=2; $PASSED_TESTS * 100 / $TOTAL_TESTS" | bc -l 2>/dev/null || echo "0")
    fi

    echo "Success Rate: $success_rate%"

    if [[ $FAILED_TESTS -eq 0 ]]; then
        print_success "🎉 All security unit tests passed!"
    else
        print_error "⚠️  Some security unit tests failed. Check the logs for details."
    fi
}

# Cleanup test environment
cleanup_test_environment() {
    print_header "Cleaning Up Test Environment"

    rm -rf "/tmp/security-unit-tests"

    print_success "Test environment cleaned up"
}

# Main execution
main() {
    print_header "WordPress Enterprise Security Unit Tests"
    print_status "Starting security unit test run: $TEST_RUN_ID"

    setup_test_environment

    # Run all test suites
    test_security_scripts
    test_security_configs
    test_selinux_config
    test_apparmor_config
    test_security_tools
    test_firewall_config
    test_auto_updates
    test_file_permissions
    test_security_script_functions
    test_cron_configuration
    test_log_files
    test_network_security
    test_password_policy
    test_security_contexts
    test_error_handling

    generate_test_report
    display_test_summary
    cleanup_test_environment

    # Exit with appropriate code
    if [[ $FAILED_TESTS -gt 0 ]]; then
        exit 1
    else
        exit 0
    fi
}

# Check dependencies
if ! command -v bc >/dev/null 2>&1; then
    print_error "bc (calculator) is required but not installed"
    print_status "Install with: apt-get install bc (Ubuntu) or yum install bc (CentOS)"
    exit 1
fi

# Run main function
main "$@"
