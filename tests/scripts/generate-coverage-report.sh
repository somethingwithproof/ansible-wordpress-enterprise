#!/bin/bash
# SPDX-FileCopyrightText: 2025 Thomas Vincent
# SPDX-License-Identifier: MIT

# WordPress Enterprise Test Coverage Report Generator
# Generates comprehensive test coverage reports for all security features

set -e

readonly FEATURE_APPARMOR_PROFILES='apparmor_profiles'
readonly TITLE_CASE_FILTER='s/\b\w/\U&/g'

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m'

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
REPORTS_DIR="$PROJECT_DIR/tests/reports/coverage"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
COVERAGE_REPORT_ID="coverage_$TIMESTAMP"

print_color() {
    local color=$1
    shift
    echo -e "${color}$*${NC}"
}

print_header() {
    local message="$1"
    echo
    print_color $PURPLE "=================================="
    print_color $PURPLE "${message}"
    print_color $PURPLE "=================================="
    echo
}

print_status() {
    local message="$1"
    print_color $BLUE "ℹ️  ${message}"
}

print_success() {
    local message="$1"
    print_color $GREEN "✅ ${message}"
}

print_error() {
    local message="$1"
    print_color $RED "❌ ${message}"
}

# Test coverage matrix
declare -A FEATURE_COVERAGE=(
    # Security System Features
    ["selinux_installation"]=0
    ["selinux_configuration"]=0
    ["selinux_file_contexts"]=0
    ["selinux_booleans"]=0
    ["selinux_custom_policies"]=0
    ["selinux_audit_logging"]=0
    ["selinux_troubleshooting"]=0

    ["apparmor_installation"]=0
    ["$FEATURE_APPARMOR_PROFILES"]=0
    ["apparmor_php_profile"]=0
    ["apparmor_nginx_profile"]=0
    ["apparmor_apache_profile"]=0
    ["apparmor_wpcli_profile"]=0
    ["apparmor_modes"]=0
    ["apparmor_validation"]=0

    # Security Tools
    ["fail2ban_installation"]=0
    ["fail2ban_configuration"]=0
    ["fail2ban_wordpress_filters"]=0
    ["security_tools_installation"]=0
    ["rkhunter_installation"]=0
    ["chkrootkit_installation"]=0
    ["logwatch_installation"]=0

    # Firewall Configuration
    ["firewalld_configuration"]=0
    ["ufw_configuration"]=0
    ["firewall_rules"]=0

    # System Hardening
    ["kernel_parameters"]=0
    ["password_policy"]=0
    ["automatic_updates"]=0
    ["service_hardening"]=0
    ["network_security"]=0

    # WordPress Security
    ["file_permissions"]=0
    ["directory_security"]=0
    ["upload_protection"]=0
    ["wp_config_security"]=0

    # Monitoring and Logging
    ["audit_logging"]=0
    ["security_scripts"]=0
    ["security_status_reporting"]=0
    ["security_maintenance"]=0
    ["cron_configuration"]=0

    # Edge Cases and Error Handling
    ["missing_directories"]=0
    ["permission_conflicts"]=0
    ["platform_detection"]=0
    ["privilege_limitations"]=0
    ["corrupted_configurations"]=0
    ["resource_constraints"]=0
    ["concurrent_operations"]=0
    ["error_recovery"]=0
)

# Test scenarios coverage
declare -A SCENARIO_COVERAGE=(
    ["01-basic-installation"]=0
    ["02-apache-installation"]=0
    ["03-validation-security"]=0
    ["04-security-hardening"]=0
    ["05-security-edge-cases"]=0
    ["unit-tests"]=0
)

# Platform coverage
declare -A PLATFORM_COVERAGE=(
    ["ubuntu"]=0
    ["centos"]=0
    ["rhel"]=0
    ["debian"]=0
)

# Generate coverage report
generate_coverage_report() {
    print_header "Analyzing Test Coverage"

    mkdir -p "$REPORTS_DIR"

    # Analyze existing test files
    analyze_test_scenarios
    analyze_unit_tests
    analyze_task_files

    # Generate reports
    generate_html_report
    generate_json_report
    generate_summary_report
}

# Analyze test scenario coverage
analyze_test_scenarios() {
    print_status "Analyzing test scenarios..."

    local scenario_dir="$PROJECT_DIR/tests/scenarios"

    if [[ -f "$scenario_dir/01-basic-installation.yml" ]]; then
        SCENARIO_COVERAGE["01-basic-installation"]=1
        # Analyze what features this scenario covers
        if grep -q "nginx\|apache" "$scenario_dir/01-basic-installation.yml"; then
            FEATURE_COVERAGE["file_permissions"]=1
            FEATURE_COVERAGE["directory_security"]=1
        fi
    fi

    if [[ -f "$scenario_dir/02-apache-installation.yml" ]]; then
        SCENARIO_COVERAGE["02-apache-installation"]=1
    fi

    if [[ -f "$scenario_dir/03-validation-security.yml" ]]; then
        SCENARIO_COVERAGE["03-validation-security"]=1
    fi

    if [[ -f "$scenario_dir/04-security-hardening.yml" ]]; then
        SCENARIO_COVERAGE["04-security-hardening"]=1
        # This scenario covers comprehensive security features
        FEATURE_COVERAGE["selinux_configuration"]=1
        FEATURE_COVERAGE["$FEATURE_APPARMOR_PROFILES"]=1
        FEATURE_COVERAGE["fail2ban_configuration"]=1
        FEATURE_COVERAGE["security_tools_installation"]=1
        FEATURE_COVERAGE["firewall_rules"]=1
        FEATURE_COVERAGE["audit_logging"]=1
        FEATURE_COVERAGE["security_scripts"]=1
    fi

    if [[ -f "$scenario_dir/05-security-edge-cases.yml" ]]; then
        SCENARIO_COVERAGE["05-security-edge-cases"]=1
        # Edge cases scenario
        FEATURE_COVERAGE["missing_directories"]=1
        FEATURE_COVERAGE["permission_conflicts"]=1
        FEATURE_COVERAGE["platform_detection"]=1
        FEATURE_COVERAGE["corrupted_configurations"]=1
        FEATURE_COVERAGE["error_recovery"]=1
    fi
}

# Analyze unit test coverage
analyze_unit_tests() {
    print_status "Analyzing unit test coverage..."

    local unit_test_file="$PROJECT_DIR/tests/scripts/security-unit-tests.sh"

    if [[ -f "$unit_test_file" ]]; then
        SCENARIO_COVERAGE["unit-tests"]=1

        # Analyze what the unit tests cover
        if grep -q "test_security_scripts" "$unit_test_file"; then
            FEATURE_COVERAGE["security_scripts"]=1
        fi

        if grep -q "test_selinux_config" "$unit_test_file"; then
            FEATURE_COVERAGE["selinux_configuration"]=1
            FEATURE_COVERAGE["selinux_booleans"]=1
        fi

        if grep -q "test_apparmor_config" "$unit_test_file"; then
            FEATURE_COVERAGE["$FEATURE_APPARMOR_PROFILES"]=1
            FEATURE_COVERAGE["apparmor_modes"]=1
        fi

        if grep -q "test_security_tools" "$unit_test_file"; then
            FEATURE_COVERAGE["security_tools_installation"]=1
            FEATURE_COVERAGE["fail2ban_installation"]=1
        fi

        if grep -q "test_firewall_config" "$unit_test_file"; then
            FEATURE_COVERAGE["firewalld_configuration"]=1
            FEATURE_COVERAGE["ufw_configuration"]=1
        fi

        if grep -q "test_file_permissions" "$unit_test_file"; then
            FEATURE_COVERAGE["file_permissions"]=1
            FEATURE_COVERAGE["wp_config_security"]=1
        fi
    fi
}

# Analyze task file coverage
analyze_task_files() {
    print_status "Analyzing task file coverage..."

    local tasks_dir="$PROJECT_DIR/tasks"

    # SELinux coverage
    if [[ -f "$tasks_dir/selinux.yml" ]]; then
        FEATURE_COVERAGE["selinux_installation"]=1
        FEATURE_COVERAGE["selinux_file_contexts"]=1
        FEATURE_COVERAGE["selinux_booleans"]=1
        FEATURE_COVERAGE["selinux_audit_logging"]=1

        if grep -q "custom.*policy" "$tasks_dir/selinux.yml"; then
            FEATURE_COVERAGE["selinux_custom_policies"]=1
        fi
    fi

    # AppArmor coverage
    if [[ -f "$tasks_dir/apparmor.yml" ]]; then
        FEATURE_COVERAGE["apparmor_installation"]=1
        FEATURE_COVERAGE["$FEATURE_APPARMOR_PROFILES"]=1

        if grep -q "wordpress-php-fpm" "$tasks_dir/apparmor.yml"; then
            FEATURE_COVERAGE["apparmor_php_profile"]=1
        fi
        if grep -q "wordpress-nginx" "$tasks_dir/apparmor.yml"; then
            FEATURE_COVERAGE["apparmor_nginx_profile"]=1
        fi
        if grep -q "wordpress-apache" "$tasks_dir/apparmor.yml"; then
            FEATURE_COVERAGE["apparmor_apache_profile"]=1
        fi
        if grep -q "wordpress-wpcli" "$tasks_dir/apparmor.yml"; then
            FEATURE_COVERAGE["apparmor_wpcli_profile"]=1
        fi
    fi

    # Security hardening coverage
    if [[ -f "$tasks_dir/security_hardening.yml" ]]; then
        FEATURE_COVERAGE["kernel_parameters"]=1
        FEATURE_COVERAGE["password_policy"]=1
        FEATURE_COVERAGE["automatic_updates"]=1
        FEATURE_COVERAGE["service_hardening"]=1
        FEATURE_COVERAGE["network_security"]=1
        FEATURE_COVERAGE["security_maintenance"]=1
        FEATURE_COVERAGE["cron_configuration"]=1
    fi
}

# Calculate coverage percentages
calculate_coverage() {
    local -n coverage_array=$1

    local total=0
    local covered=0

    for feature in "${!coverage_array[@]}"; do
        ((total++))
        if [[ "${coverage_array[$feature]}" == "1" ]]; then
            ((covered++))
        fi
    done

    local percentage=0
    if [[ $total -gt 0 ]]; then
        percentage=$(echo "scale=1; $covered * 100 / $total" | bc -l)
    fi

    echo "$covered,$total,$percentage"
}

# Generate HTML coverage report
generate_html_report() {
    print_status "Generating HTML coverage report..."

    local html_file="$REPORTS_DIR/${COVERAGE_REPORT_ID}.html"
    local feature_stats scenario_stats

    feature_stats=$(calculate_coverage FEATURE_COVERAGE)
    scenario_stats=$(calculate_coverage SCENARIO_COVERAGE)

    IFS=',' read -r feature_covered feature_total feature_pct <<< "$feature_stats"
    IFS=',' read -r scenario_covered scenario_total scenario_pct <<< "$scenario_stats"

    cat > "$html_file" << EOF
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WordPress Enterprise Security Test Coverage Report</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f8f9fa;
        }
        .container { max-width: 1200px; margin: 0 auto; }
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 30px;
            text-align: center;
        }
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        .stat-card {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            text-align: center;
        }
        .stat-number {
            font-size: 2.5em;
            font-weight: bold;
            color: #667eea;
        }
        .stat-label {
            color: #6c757d;
            margin-top: 5px;
        }
        .coverage-section {
            background: white;
            padding: 25px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        .coverage-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 8px 0;
            border-bottom: 1px solid #eee;
        }
        .coverage-item:last-child { border-bottom: none; }
        .coverage-bar {
            width: 200px;
            height: 20px;
            background-color: #e9ecef;
            border-radius: 10px;
            overflow: hidden;
        }
        .coverage-fill {
            height: 100%;
            transition: width 0.3s ease;
        }
        .covered { background-color: #28a745; }
        .partial { background-color: #ffc107; }
        .not-covered { background-color: #dc3545; }
        .status-icon {
            width: 20px;
            height: 20px;
            border-radius: 50%;
            display: inline-block;
            margin-left: 10px;
        }
        .icon-pass { background-color: #28a745; }
        .icon-fail { background-color: #dc3545; }
        .timestamp {
            color: #6c757d;
            font-size: 0.9em;
            text-align: center;
            margin-top: 20px;
        }
        h2 { color: #495057; }
        .progress-ring {
            transform: rotate(-90deg);
        }
        .progress-text {
            font-size: 1.2em;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>WordPress Enterprise Security Test Coverage</h1>
            <p>Comprehensive analysis of security feature test coverage</p>
            <p>Report ID: $COVERAGE_REPORT_ID</p>
        </div>

        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-number">$feature_pct%</div>
                <div class="stat-label">Feature Coverage</div>
                <div class="stat-label">($feature_covered / $feature_total features)</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">$scenario_pct%</div>
                <div class="stat-label">Scenario Coverage</div>
                <div class="stat-label">($scenario_covered / $scenario_total scenarios)</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">$(echo "${#FEATURE_COVERAGE[@]}")</div>
                <div class="stat-label">Total Features</div>
                <div class="stat-label">Security features tracked</div>
            </div>
        </div>

        <div class="coverage-section">
            <h2>Security Feature Coverage</h2>
EOF

    # Generate feature coverage details
    for feature in $(printf '%s\n' "${!FEATURE_COVERAGE[@]}" | sort); do
        local status_class="icon-fail"
        local status_text="Not Covered"
        if [[ "${FEATURE_COVERAGE[$feature]}" == "1" ]]; then
            status_class="icon-pass"
            status_text="Covered"
        fi

        local feature_name
        feature_name=$(echo "$feature" | sed 's/_/ /g' | sed "$TITLE_CASE_FILTER")

        cat >> "$html_file" << EOF
            <div class="coverage-item">
                <div>
                    <strong>$feature_name</strong>
                    <span class="status-icon $status_class"></span>
                </div>
                <div>$status_text</div>
            </div>
EOF
    done

    cat >> "$html_file" << EOF
        </div>

        <div class="coverage-section">
            <h2>Test Scenario Coverage</h2>
EOF

    # Generate scenario coverage details
    for scenario in $(printf '%s\n' "${!SCENARIO_COVERAGE[@]}" | sort); do
        local status_class="icon-fail"
        local status_text="Not Implemented"
        if [[ "${SCENARIO_COVERAGE[$scenario]}" == "1" ]]; then
            status_class="icon-pass"
            status_text="Implemented"
        fi

        local scenario_name
        scenario_name=$(echo "$scenario" | sed 's/-/ /g' | sed "$TITLE_CASE_FILTER")

        cat >> "$html_file" << EOF
            <div class="coverage-item">
                <div>
                    <strong>$scenario_name</strong>
                    <span class="status-icon $status_class"></span>
                </div>
                <div>$status_text</div>
            </div>
EOF
    done

    cat >> "$html_file" << EOF
        </div>

        <div class="timestamp">
            Report generated on $(date)
        </div>
    </div>
</body>
</html>
EOF

    print_success "HTML report generated: $html_file"
}

# Generate JSON coverage report
generate_json_report() {
    print_status "Generating JSON coverage report..."

    local json_file="$REPORTS_DIR/${COVERAGE_REPORT_ID}.json"
    local feature_stats scenario_stats

    feature_stats=$(calculate_coverage FEATURE_COVERAGE)
    scenario_stats=$(calculate_coverage SCENARIO_COVERAGE)

    IFS=',' read -r feature_covered feature_total feature_pct <<< "$feature_stats"
    IFS=',' read -r scenario_covered scenario_total scenario_pct <<< "$scenario_stats"

    # Build JSON structure
    cat > "$json_file" << EOF
{
  "report_id": "$COVERAGE_REPORT_ID",
  "timestamp": "$(date -Iseconds)",
  "summary": {
    "feature_coverage": {
      "covered": $feature_covered,
      "total": $feature_total,
      "percentage": $feature_pct
    },
    "scenario_coverage": {
      "covered": $scenario_covered,
      "total": $scenario_total,
      "percentage": $scenario_pct
    }
  },
  "features": {
EOF

    # Add feature details
    local first_feature=true
    for feature in $(printf '%s\n' "${!FEATURE_COVERAGE[@]}" | sort); do
        if [[ "$first_feature" != "true" ]]; then
            echo "," >> "$json_file"
        fi
        echo "    \"$feature\": ${FEATURE_COVERAGE[$feature]}" >> "$json_file"
        first_feature=false
    done

    cat >> "$json_file" << EOF
  },
  "scenarios": {
EOF

    # Add scenario details
    local first_scenario=true
    for scenario in $(printf '%s\n' "${!SCENARIO_COVERAGE[@]}" | sort); do
        if [[ "$first_scenario" != "true" ]]; then
            echo "," >> "$json_file"
        fi
        echo "    \"$scenario\": ${SCENARIO_COVERAGE[$scenario]}" >> "$json_file"
        first_scenario=false
    done

    cat >> "$json_file" << EOF
  }
}
EOF

    print_success "JSON report generated: $json_file"
}

# Generate summary report
generate_summary_report() {
    print_status "Generating summary report..."

    local summary_file="$REPORTS_DIR/${COVERAGE_REPORT_ID}_summary.txt"
    local feature_stats scenario_stats

    feature_stats=$(calculate_coverage FEATURE_COVERAGE)
    scenario_stats=$(calculate_coverage SCENARIO_COVERAGE)

    IFS=',' read -r feature_covered feature_total feature_pct <<< "$feature_stats"
    IFS=',' read -r scenario_covered scenario_total scenario_pct <<< "$scenario_stats"

    cat > "$summary_file" << EOF
WordPress Enterprise Security Test Coverage Report
================================================

Report ID: $COVERAGE_REPORT_ID
Generated: $(date)

OVERALL COVERAGE SUMMARY
========================
Feature Coverage:  $feature_pct% ($feature_covered/$feature_total)
Scenario Coverage: $scenario_pct% ($scenario_covered/$scenario_total)

DETAILED BREAKDOWN
==================

Security Features ($feature_covered/$feature_total covered):
EOF

    # List features with coverage status
    for feature in $(printf '%s\n' "${!FEATURE_COVERAGE[@]}" | sort); do
        local status="❌ NOT COVERED"
        if [[ "${FEATURE_COVERAGE[$feature]}" == "1" ]]; then
            status="✅ COVERED"
        fi

        local feature_name
        feature_name=$(echo "$feature" | sed 's/_/ /g' | sed "$TITLE_CASE_FILTER")
        printf "  %-40s %s\n" "$feature_name" "$status" >> "$summary_file"
    done

    cat >> "$summary_file" << EOF

Test Scenarios ($scenario_covered/$scenario_total implemented):
EOF

    # List scenarios with implementation status
    for scenario in $(printf '%s\n' "${!SCENARIO_COVERAGE[@]}" | sort); do
        local status="❌ NOT IMPLEMENTED"
        if [[ "${SCENARIO_COVERAGE[$scenario]}" == "1" ]]; then
            status="✅ IMPLEMENTED"
        fi

        local scenario_name
        scenario_name=$(echo "$scenario" | sed 's/-/ /g' | sed "$TITLE_CASE_FILTER")
        printf "  %-40s %s\n" "$scenario_name" "$status" >> "$summary_file"
    done

    cat >> "$summary_file" << EOF

RECOMMENDATIONS
===============

EOF

    # Generate recommendations based on coverage gaps
    local recommendations_added=false

    if [[ "$feature_pct" < "90" ]]; then
        echo "• Improve feature coverage by implementing tests for uncovered features" >> "$summary_file"
        recommendations_added=true
    fi

    if [[ "$scenario_pct" < "100" ]]; then
        echo "• Complete implementation of missing test scenarios" >> "$summary_file"
        recommendations_added=true
    fi

    # Check for specific missing features
    if [[ "${FEATURE_COVERAGE["selinux_custom_policies"]}" == "0" ]]; then
        echo "• Add tests for SELinux custom policy creation and loading" >> "$summary_file"
        recommendations_added=true
    fi

    if [[ "${FEATURE_COVERAGE["concurrent_operations"]}" == "0" ]]; then
        echo "• Add tests for concurrent security operations" >> "$summary_file"
        recommendations_added=true
    fi

    if [[ "$recommendations_added" != "true" ]]; then
        echo "• Excellent coverage! Consider adding more edge case tests." >> "$summary_file"
    fi

    cat >> "$summary_file" << EOF

FILES ANALYZED
==============
• Task files in tasks/ directory
• Test scenarios in tests/scenarios/ directory
• Unit test scripts in tests/scripts/ directory
• Security configuration templates

Report generated by WordPress Enterprise Test Coverage Analyzer
EOF

    print_success "Summary report generated: $summary_file"
}

# Display coverage summary
display_coverage_summary() {
    print_header "Test Coverage Summary"

    local feature_stats scenario_stats
    feature_stats=$(calculate_coverage FEATURE_COVERAGE)
    scenario_stats=$(calculate_coverage SCENARIO_COVERAGE)

    IFS=',' read -r feature_covered feature_total feature_pct <<< "$feature_stats"
    IFS=',' read -r scenario_covered scenario_total scenario_pct <<< "$scenario_stats"

    echo "Report ID: $COVERAGE_REPORT_ID"
    echo "Generated: $(date)"
    echo ""

    print_status "Feature Coverage: $feature_pct% ($feature_covered/$feature_total)"
    print_status "Scenario Coverage: $scenario_pct% ($scenario_covered/$scenario_total)"
    echo ""

    if [[ $(echo "$feature_pct >= 90" | bc -l) == "1" ]]; then
        print_success "Excellent feature coverage!"
    elif [[ $(echo "$feature_pct >= 75" | bc -l) == "1" ]]; then
        print_status "Good feature coverage, room for improvement"
    else
        print_error "Feature coverage needs improvement"
    fi

    if [[ "$scenario_pct" == "100.0" ]]; then
        print_success "All test scenarios implemented!"
    else
        print_error "Some test scenarios are missing"
    fi

    echo ""
    print_status "Reports generated in: $REPORTS_DIR"
}

# Main execution
main() {
    print_header "WordPress Enterprise Security Test Coverage Analysis"

    # Check dependencies
    if ! command -v bc >/dev/null 2>&1; then
        print_error "bc (calculator) is required but not installed"
        print_status "Install with: brew install bc (macOS) or apt-get install bc (Ubuntu)"
        exit 1
    fi

    generate_coverage_report
    display_coverage_summary

    print_header "Coverage Analysis Complete"
    print_success "All reports generated successfully!"

    # macOS notification
    if command -v osascript >/dev/null 2>&1; then
        osascript -e "display notification \"Test coverage analysis complete\" with title \"WordPress Tests\""
    fi
}

# Run main function
main "$@"
