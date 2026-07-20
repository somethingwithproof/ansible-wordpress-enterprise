#!/bin/bash

# WordPress Enterprise Single Test Runner
# This script runs a single test scenario for the WordPress Enterprise Ansible role

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
TEST_RUN_ID="single_test_$TIMESTAMP"
COMPOSE_FILE="$PROJECT_DIR/docker-compose.test.yml"

# Default values
TARGET=""
SCENARIO=""
INVENTORY=""
VERBOSE="${VERBOSE:-false}"
NO_CLEANUP=false
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
    echo "WordPress Enterprise Single Test Runner"
    echo ""
    echo "Usage: $0 -t TARGET -s SCENARIO [OPTIONS]"
    echo ""
    echo "Required:"
    echo "  -t, --target TARGET     Target system (ubuntu or centos)"
    echo "  -s, --scenario SCENARIO Test scenario file (01-basic-installation.yml, etc.)"
    echo ""
    echo "Options:"
    echo "  -h, --help              Show this help message"
    echo "  -v, --verbose           Enable verbose output"
    echo "  -i, --inventory INV     Custom inventory file (auto-detected if not specified)"
    echo "  --skip-build            Skip Docker image building"
    echo "  --no-cleanup            Don't cleanup containers after test"
    echo ""
    echo "Examples:"
    echo "  $0 -t ubuntu -s 01-basic-installation.yml"
    echo "  $0 -t centos -s 02-apache-installation.yml -v"
    echo "  $0 -t ubuntu -s 03-validation-security.yml --no-cleanup"
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
            -t|--target)
                TARGET="$2"
                shift 2
                ;;
            -s|--scenario)
                SCENARIO="$2"
                shift 2
                ;;
            -i|--inventory)
                INVENTORY="$2"
                shift 2
                ;;
            -v|--verbose)
                VERBOSE=true
                shift
                ;;
            --skip-build)
                SKIP_BUILD=true
                shift
                ;;
            --no-cleanup)
                NO_CLEANUP=true
                shift
                ;;
            *)
                print_error "Unknown option: $1"
                usage
                ;;
        esac
    done

    # Validate required arguments
    if [[ -z "$TARGET" ]]; then
        print_error "Target system is required. Use -t ubuntu or -t centos"
        usage
    fi

    if [[ -z "$SCENARIO" ]]; then
        print_error "Test scenario is required. Use -s with a scenario file name"
        usage
    fi

    # Validate target
    if [[ "$TARGET" != "ubuntu" && "$TARGET" != "centos" ]]; then
        print_error "Invalid target: $TARGET. Use 'ubuntu' or 'centos'"
        exit 1
    fi

    # Auto-detect inventory if not specified
    if [[ -z "$INVENTORY" ]]; then
        case "$TARGET" in
            ubuntu)
                INVENTORY="ubuntu.ini"
                ;;
            centos)
                INVENTORY="centos.ini"
                ;;
        esac
    fi

    # Validate scenario file exists
    if [[ ! -f "$TEST_DIR/scenarios/$SCENARIO" ]]; then
        print_error "Scenario file not found: $TEST_DIR/scenarios/$SCENARIO"
        exit 1
    fi

    # Validate inventory file exists
    if [[ ! -f "$TEST_DIR/inventories/$INVENTORY" ]]; then
        print_error "Inventory file not found: $TEST_DIR/inventories/$INVENTORY"
        exit 1
    fi
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
    local target_host=$1
    local max_wait=60
    local count=0

    print_status "Waiting for SSH connectivity to $target_host..."

    while [[ $count -lt $max_wait ]]; do
        if docker exec wp-test-runner sshpass -p testroot123 ssh -o ConnectTimeout=5 root@"$target_host" echo "SSH OK" >/dev/null 2>&1; then
            print_success "SSH connectivity to $target_host established"
            return 0
        fi
        sleep 2
        ((count += 2))
    done

    print_error "Failed to establish SSH connectivity to $target_host"
    return 1
}

# Function to run the test scenario
run_test() {
    print_header "Running Test Scenario"

    # Determine target hostname
    local target_host
    case "$TARGET" in
        ubuntu)
            target_host="wp-test-ubuntu"
            ;;
        centos)
            target_host="wp-test-centos"
            ;;
    esac

    local log_file="$REPORTS_DIR/${TEST_RUN_ID}_${TARGET}_${SCENARIO}.log"
    local report_file="$REPORTS_DIR/${TEST_RUN_ID}_${TARGET}_${SCENARIO}_report.json"

    print_status "Target: $TARGET ($target_host)"
    print_status "Scenario: $SCENARIO"
    print_status "Inventory: $INVENTORY"
    print_status "Log file: $log_file"
    print_status "Report file: $report_file"

    # Wait for SSH connectivity
    if ! wait_for_ssh "$target_host"; then
        return 1
    fi

    # Run the test
    local start_time=$(date +%s)
    local test_result=0

    print_status "Executing Ansible playbook..."

    if [[ "$VERBOSE" == "true" ]]; then
        docker exec wp-test-runner ansible-playbook \
            -i "tests/inventories/$INVENTORY" \
            "tests/scenarios/$SCENARIO" \
            --extra-vars "test_run_id=$TEST_RUN_ID" \
            -v 2>&1 | tee "$log_file"
        test_result=${PIPESTATUS[0]}
    else
        docker exec wp-test-runner ansible-playbook \
            -i "tests/inventories/$INVENTORY" \
            "tests/scenarios/$SCENARIO" \
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
  "scenario": "$SCENARIO",
  "target": "$TARGET",
  "target_host": "$target_host",
  "inventory": "$INVENTORY",
  "start_time": "$start_time",
  "end_time": "$end_time",
  "duration_seconds": $duration,
  "result": "$([ $test_result -eq 0 ] && echo "PASS" || echo "FAIL")",
  "log_file": "$log_file",
  "timestamp": "$(date -Iseconds)"
}
EOF

    if [[ $test_result -eq 0 ]]; then
        print_success "Test completed successfully! ($duration seconds)"
        print_status "Report saved to: $report_file"
        return 0
    else
        print_error "Test failed! ($duration seconds)"
        print_status "Report saved to: $report_file"
        if [[ "$VERBOSE" != "true" ]]; then
            print_status "Check log file for details: $log_file"
        fi
        return 1
    fi
}

# Function to cleanup test environment
cleanup_environment() {
    if [[ "$NO_CLEANUP" == "true" ]]; then
        print_warning "Skipping cleanup (--no-cleanup specified)"
        print_status "To manually cleanup later, run:"
        print_status "cd $PROJECT_DIR && docker-compose -f docker-compose.test.yml down --remove-orphans --volumes"
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
    print_header "WordPress Enterprise Single Test Runner"
    print_status "Test Run ID: $TEST_RUN_ID"

    parse_args "$@"
    check_prerequisites
    build_images
    start_environment

    # Run test and capture exit code
    local test_exit_code=0
    run_test || test_exit_code=$?

    cleanup_environment

    print_header "Test Complete"
    if [[ $test_exit_code -eq 0 ]]; then
        print_success "Test passed! 🎉"
    else
        print_error "Test failed. Check the log file for details."
    fi

    print_status "Reports available in: $REPORTS_DIR"

    exit $test_exit_code
}

# Run main function with all arguments
main "$@"
