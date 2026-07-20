#!/bin/bash

# WordPress Enterprise End-to-End Test Runner
# This script runs comprehensive tests for the WordPress Enterprise Ansible role

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
TEST_DIR="$PROJECT_DIR/tests"
REPORTS_DIR="$TEST_DIR/reports"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
TEST_RUN_ID="test_run_$TIMESTAMP"
COMPOSE_FILE="$PROJECT_DIR/docker-compose.test.yml"

# Test configuration
UBUNTU_TESTS=true
CENTOS_TESTS=true
CLEANUP_AFTER=true
VERBOSE="${VERBOSE:-false}"
SPECIFIC_TEST=""
SKIP_BUILD=false

# Function to print colored output
print_color() {
    local color=$1
    shift
    echo -e "${color}$*${NC}"
}

# Function to print section headers
print_header() {
    echo
    print_color $PURPLE "=================================="
    print_color $PURPLE "$1"
    print_color $PURPLE "=================================="
    echo
}

# Function to print status
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

# Function to show usage
usage() {
    echo "WordPress Enterprise Test Runner"
    echo ""
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  -h, --help              Show this help message"
    echo "  -v, --verbose           Enable verbose output"
    echo "  -u, --ubuntu-only       Run only Ubuntu tests"
    echo "  -c, --centos-only       Run only CentOS tests"
    echo "  -t, --test SCENARIO     Run specific test scenario (01, 02, 03)"
    echo "  -s, --skip-build        Skip Docker image building"
    echo "  -n, --no-cleanup        Don't cleanup containers after tests"
    echo ""
    echo "Examples:"
    echo "  $0                      Run all tests"
    echo "  $0 -u -v               Run Ubuntu tests with verbose output"
    echo "  $0 -t 01                Run only basic installation test"
    echo "  $0 --skip-build         Skip building Docker images"
    echo ""
    exit 0
}

# Function to parse command line arguments
parse_args() {
    while [[ $# -gt 0 ]]; do
        case $1 in
            -h|--help)
                usage
                ;;
            -v|--verbose)
                VERBOSE=true
                shift
                ;;
            -u|--ubuntu-only)
                UBUNTU_TESTS=true
                CENTOS_TESTS=false
                shift
                ;;
            -c|--centos-only)
                UBUNTU_TESTS=false
                CENTOS_TESTS=true
                shift
                ;;
            -t|--test)
                SPECIFIC_TEST="$2"
                shift 2
                ;;
            -s|--skip-build)
                SKIP_BUILD=true
                shift
                ;;
            -n|--no-cleanup)
                CLEANUP_AFTER=false
                shift
                ;;
            *)
                print_error "Unknown option: $1"
                usage
                ;;
        esac
    done
}

# Function to check prerequisites
check_prerequisites() {
    print_header "Checking Prerequisites"
    
    # Check if Docker is running
    if ! docker info >/dev/null 2>&1; then
        print_error "Docker is not running. Please start Docker and try again."
        exit 1
    fi
    print_success "Docker is running"
    
    # Check if docker-compose is available
    if ! command -v docker-compose >/dev/null 2>&1; then
        print_error "docker-compose is not installed or not in PATH"
        exit 1
    fi
    print_success "docker-compose is available"
    
    # Check if test compose file exists
    if [[ ! -f "$COMPOSE_FILE" ]]; then
        print_error "Test compose file not found: $COMPOSE_FILE"
        exit 1
    fi
    print_success "Test compose file found"
    
    # Create reports directory
    mkdir -p "$REPORTS_DIR"
    print_success "Reports directory ready: $REPORTS_DIR"
}

# Function to build Docker images
build_images() {
    if [[ "$SKIP_BUILD" == "true" ]]; then
        print_warning "Skipping Docker image build"
        return
    fi
    
    print_header "Building Docker Images"
    
    print_status "Building test environment images..."
    cd "$PROJECT_DIR"
    
    if [[ "$VERBOSE" == "true" ]]; then
        docker-compose -f "$COMPOSE_FILE" build --no-cache
    else
        docker-compose -f "$COMPOSE_FILE" build --no-cache >/dev/null 2>&1
    fi
    
    print_success "Docker images built successfully"
}

# Function to start test environment
start_environment() {
    print_header "Starting Test Environment"
    
    cd "$PROJECT_DIR"
    
    # Stop any existing containers
    docker-compose -f "$COMPOSE_FILE" down --remove-orphans >/dev/null 2>&1 || true
    
    print_status "Starting services..."
    if [[ "$VERBOSE" == "true" ]]; then
        docker-compose -f "$COMPOSE_FILE" up -d
    else
        docker-compose -f "$COMPOSE_FILE" up -d >/dev/null 2>&1
    fi
    
    # Wait for services to be healthy
    print_status "Waiting for services to be ready..."
    local max_wait=120
    local count=0
    
    while [[ $count -lt $max_wait ]]; do
        if docker-compose -f "$COMPOSE_FILE" ps | grep -q "Up (healthy)"; then
            break
        fi
        sleep 2
        ((count += 2))
        if [[ $((count % 10)) -eq 0 ]]; then
            print_status "Still waiting for services... ($count/${max_wait}s)"
        fi
    done
    
    if [[ $count -ge $max_wait ]]; then
        print_error "Services failed to become healthy within $max_wait seconds"
        docker-compose -f "$COMPOSE_FILE" ps
        exit 1
    fi
    
    print_success "Test environment is ready"
    
    # Show service status
    if [[ "$VERBOSE" == "true" ]]; then
        docker-compose -f "$COMPOSE_FILE" ps
    fi
}

# Function to wait for SSH connectivity
wait_for_ssh() {
    local target=$1
    local max_wait=60
    local count=0
    
    print_status "Waiting for SSH connectivity to $target..."
    
    while [[ $count -lt $max_wait ]]; do
        if docker exec wp-test-runner ssh -o ConnectTimeout=5 -o BatchMode=yes root@$target echo "SSH OK" >/dev/null 2>&1; then
            print_success "SSH connectivity to $target established"
            return 0
        fi
        sleep 2
        ((count += 2))
    done
    
    print_error "Failed to establish SSH connectivity to $target"
    return 1
}

# Function to run a specific test scenario
run_test_scenario() {
    local scenario=$1
    local target=$2
    local inventory=$3
    local scenario_name=$4
    
    print_header "Running $scenario_name on $target"
    
    local log_file="$REPORTS_DIR/${TEST_RUN_ID}_${target}_${scenario}.log"
    local report_file="$REPORTS_DIR/${TEST_RUN_ID}_${target}_${scenario}_report.json"
    
    print_status "Test target: $target"
    print_status "Inventory: $inventory"
    print_status "Scenario: $scenario"
    print_status "Log file: $log_file"
    
    # Wait for SSH connectivity
    if ! wait_for_ssh "$target"; then
        return 1
    fi
    
    # Run the test
    local start_time=$(date +%s)
    local test_result=0
    
    if [[ "$VERBOSE" == "true" ]]; then
        docker exec wp-test-runner ansible-playbook \
            -i "tests/inventories/$inventory" \
            "tests/scenarios/$scenario" \
            --extra-vars "test_run_id=$TEST_RUN_ID" \
            -v 2>&1 | tee "$log_file"
        test_result=${PIPESTATUS[0]}
    else
        docker exec wp-test-runner ansible-playbook \
            -i "tests/inventories/$inventory" \
            "tests/scenarios/$scenario" \
            --extra-vars "test_run_id=$TEST_RUN_ID" \
            >"$log_file" 2>&1
        test_result=$?
    fi
    
    local end_time=$(date +%s)
    local duration=$((end_time - start_time))
    
    # Create test report
    cat > "$report_file" << EOF
{
  "test_run_id": "$TEST_RUN_ID",
  "scenario": "$scenario",
  "scenario_name": "$scenario_name",
  "target": "$target",
  "inventory": "$inventory",
  "start_time": "$start_time",
  "end_time": "$end_time",
  "duration_seconds": $duration,
  "result": "$([ $test_result -eq 0 ] && echo "PASS" || echo "FAIL")",
  "log_file": "$log_file",
  "timestamp": "$(date -Iseconds)"
}
EOF
    
    if [[ $test_result -eq 0 ]]; then
        print_success "$scenario_name completed successfully ($duration seconds)"
        return 0
    else
        print_error "$scenario_name failed ($duration seconds)"
        if [[ "$VERBOSE" != "true" ]]; then
            print_status "Check log file for details: $log_file"
        fi
        return 1
    fi
}

# Function to run all tests
run_tests() {
    print_header "Executing Test Scenarios"
    
    local total_tests=0
    local passed_tests=0
    local failed_tests=0
    
    # Test scenarios to run
    local scenarios=(
        "01-basic-installation.yml:Basic WordPress Installation with Nginx"
        "02-apache-installation.yml:WordPress Installation with Apache"
        "03-validation-security.yml:Validation and Security Features"
        "04-security-hardening.yml:Comprehensive Security Hardening"
        "05-security-edge-cases.yml:Security Edge Cases and Error Handling"
    )
    
    # If specific test is requested
    if [[ -n "$SPECIFIC_TEST" ]]; then
        case "$SPECIFIC_TEST" in
            "01"|"1")
                scenarios=("01-basic-installation.yml:Basic WordPress Installation with Nginx")
                ;;
            "02"|"2")
                scenarios=("02-apache-installation.yml:WordPress Installation with Apache")
                ;;
            "03"|"3")
                scenarios=("03-validation-security.yml:Validation and Security Features")
                ;;
            "04"|"4")
                scenarios=("04-security-hardening.yml:Comprehensive Security Hardening")
                ;;
            "05"|"5")
                scenarios=("05-security-edge-cases.yml:Security Edge Cases and Error Handling")
                ;;
            *)
                print_error "Unknown test scenario: $SPECIFIC_TEST"
                print_status "Available scenarios: 01, 02, 03, 04, 05"
                exit 1
                ;;
        esac
    fi
    
    # Run tests on Ubuntu
    if [[ "$UBUNTU_TESTS" == "true" ]]; then
        for scenario_info in "${scenarios[@]}"; do
            IFS=':' read -r scenario scenario_name <<< "$scenario_info"
            ((total_tests++))
            
            if run_test_scenario "$scenario" "wp-test-ubuntu" "ubuntu.ini" "$scenario_name"; then
                ((passed_tests++))
            else
                ((failed_tests++))
            fi
        done
    fi
    
    # Run tests on CentOS
    if [[ "$CENTOS_TESTS" == "true" ]]; then
        for scenario_info in "${scenarios[@]}"; do
            IFS=':' read -r scenario scenario_name <<< "$scenario_info"
            ((total_tests++))
            
            if run_test_scenario "$scenario" "wp-test-centos" "centos.ini" "$scenario_name"; then
                ((passed_tests++))
            else
                ((failed_tests++))
            fi
        done
    fi
    
    # Generate summary report
    generate_summary_report "$total_tests" "$passed_tests" "$failed_tests"
}

# Function to generate summary report
generate_summary_report() {
    local total=$1
    local passed=$2
    local failed=$3
    
    local summary_file="$REPORTS_DIR/${TEST_RUN_ID}_summary.json"
    local success_rate=0
    
    if [[ $total -gt 0 ]]; then
        success_rate=$(echo "scale=2; $passed * 100 / $total" | bc -l 2>/dev/null || echo "0")
    fi
    
    cat > "$summary_file" << EOF
{
  "test_run_id": "$TEST_RUN_ID",
  "timestamp": "$(date -Iseconds)",
  "total_tests": $total,
  "passed_tests": $passed,
  "failed_tests": $failed,
  "success_rate": "$success_rate%",
  "ubuntu_tests_enabled": $UBUNTU_TESTS,
  "centos_tests_enabled": $CENTOS_TESTS,
  "reports_directory": "$REPORTS_DIR"
}
EOF
    
    print_header "Test Summary"
    print_status "Test Run ID: $TEST_RUN_ID"
    print_status "Total Tests: $total"
    print_success "Passed: $passed"
    if [[ $failed -gt 0 ]]; then
        print_error "Failed: $failed"
    else
        print_success "Failed: $failed"
    fi
    print_status "Success Rate: $success_rate%"
    print_status "Summary Report: $summary_file"
    
    return $failed
}

# Function to cleanup test environment
cleanup_environment() {
    if [[ "$CLEANUP_AFTER" != "true" ]]; then
        print_warning "Skipping cleanup (--no-cleanup specified)"
        return
    fi
    
    print_header "Cleaning Up Test Environment"
    
    cd "$PROJECT_DIR"
    
    print_status "Stopping and removing containers..."
    if [[ "$VERBOSE" == "true" ]]; then
        docker-compose -f "$COMPOSE_FILE" down --remove-orphans --volumes
    else
        docker-compose -f "$COMPOSE_FILE" down --remove-orphans --volumes >/dev/null 2>&1
    fi
    
    print_success "Test environment cleaned up"
}

# Main execution
main() {
    print_header "WordPress Enterprise End-to-End Test Runner"
    print_status "Starting test run: $TEST_RUN_ID"
    
    parse_args "$@"
    check_prerequisites
    build_images
    start_environment
    
    # Run tests and capture exit code
    local test_exit_code=0
    run_tests || test_exit_code=$?
    
    cleanup_environment
    
    print_header "Test Run Complete"
    if [[ $test_exit_code -eq 0 ]]; then
        print_success "All tests passed! 🎉"
    else
        print_error "Some tests failed. Check the reports for details."
    fi
    
    print_status "Reports available in: $REPORTS_DIR"
    
    exit $test_exit_code
}

# Run main function with all arguments
main "$@"
