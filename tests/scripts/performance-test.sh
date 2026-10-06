#!/bin/bash
# SPDX-FileCopyrightText: 2025 Thomas Vincent
# SPDX-License-Identifier: MIT

# WordPress Enterprise Performance Testing Script
# Runs load tests and performance benchmarks against deployed WordPress instances

set -e

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
REPORTS_DIR="$PROJECT_DIR/tests/reports/performance"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
PERF_RUN_ID="perf_$TIMESTAMP"

# Test parameters
CONCURRENT_USERS=${CONCURRENT_USERS:-10}
TOTAL_REQUESTS=${TOTAL_REQUESTS:-1000}
TEST_DURATION=${TEST_DURATION:-60}
RAMP_UP_TIME=${RAMP_UP_TIME:-30}

# WordPress endpoints to test
ENDPOINTS=(
    "/"
    "/wp-admin/"
    "/wp-login.php"
    "/xmlrpc.php"
    "/wp-json/wp/v2/posts"
)

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

usage() {
    echo "WordPress Performance Testing Script"
    echo ""
    echo "Usage: $0 [OPTIONS] TARGET_URL"
    echo ""
    echo "Options:"
    echo "  -h, --help              Show this help"
    echo "  -c, --concurrent N      Concurrent users (default: 10)"
    echo "  -n, --requests N        Total requests (default: 1000)"
    echo "  -t, --duration N        Test duration in seconds (default: 60)"
    echo "  -r, --rampup N          Ramp-up time in seconds (default: 30)"
    echo "  -v, --verbose           Verbose output"
    echo ""
    echo "Environment Variables:"
    echo "  CONCURRENT_USERS        Override concurrent users"
    echo "  TOTAL_REQUESTS         Override total requests"
    echo "  TEST_DURATION          Override test duration"
    echo ""
    echo "Examples:"
    echo "  $0 http://localhost:8080"
    echo "  $0 -c 20 -n 2000 http://wordpress.test"
    exit 0
}

check_dependencies() {
    print_header "Checking Dependencies"

    # Check for performance testing tools
    local missing_tools=()

    if ! command -v ab >/dev/null 2>&1; then
        if command -v brew >/dev/null 2>&1; then
            print_status "Installing Apache Bench (ab)..."
            brew install httpd
        else
            missing_tools+=("ab (Apache Bench)")
        fi
    fi

    if ! command -v curl >/dev/null 2>&1; then
        missing_tools+=("curl")
    fi

    if ! command -v jq >/dev/null 2>&1; then
        missing_tools+=("jq")
    fi

    # Try to install wrk if available
    if ! command -v wrk >/dev/null 2>&1 && command -v brew >/dev/null 2>&1; then
        print_status "Installing wrk for advanced load testing..."
        brew install wrk || print_status "wrk installation failed, will use ab instead"
    fi

    if [[ ${#missing_tools[@]} -gt 0 ]]; then
        print_error "Missing required tools: ${missing_tools[*]}"
        print_status "Install with: brew install httpd curl jq wrk"
        exit 1
    fi

    print_success "All dependencies available"
    mkdir -p "$REPORTS_DIR"
}

get_wordpress_info() {
    local base_url="$1"
    local info_file="$REPORTS_DIR/${PERF_RUN_ID}_wp_info.json"

    print_status "Gathering WordPress information..."

    local wp_version=""
    local theme_info=""

    # Try to get WordPress version from generator meta tag
    wp_version=$(curl -s "$base_url" | grep -o 'WordPress [0-9.]*' | head -1 || echo "Unknown")

    # Try to get active theme info
    theme_info=$(curl -s "$base_url" | grep -o 'wp-content/themes/[^/]*' | head -1 | cut -d'/' -f3 || echo "Unknown")

    # Create WordPress info JSON
    cat > "$info_file" << EOF
{
  "target_url": "$base_url",
  "wordpress_version": "$wp_version",
  "active_theme": "$theme_info",
  "test_timestamp": "$(date -Iseconds)",
  "test_parameters": {
    "concurrent_users": $CONCURRENT_USERS,
    "total_requests": $TOTAL_REQUESTS,
    "test_duration": $TEST_DURATION,
    "ramp_up_time": $RAMP_UP_TIME
  }
}
EOF

    print_success "WordPress info saved to $info_file"
}

run_apache_bench_test() {
    local url="$1"
    local endpoint="$2"
    local test_name="$3"

    local ab_output="$REPORTS_DIR/${PERF_RUN_ID}_ab_${test_name}.txt"
    local ab_json="$REPORTS_DIR/${PERF_RUN_ID}_ab_${test_name}.json"

    print_status "Running Apache Bench test for $test_name..."

    # Run Apache Bench
    ab -n "$TOTAL_REQUESTS" -c "$CONCURRENT_USERS" -g "$REPORTS_DIR/${PERF_RUN_ID}_ab_${test_name}.gnuplot" \
       "$url$endpoint" > "$ab_output" 2>&1 || true

    # Parse Apache Bench output to JSON
    if [[ -f "$ab_output" ]]; then
        local requests_per_sec time_per_request transfer_rate failed_requests
        requests_per_sec=$(grep "Requests per second:" "$ab_output" | awk '{print $4}' || echo "0")
        time_per_request=$(grep "Time per request:" "$ab_output" | head -1 | awk '{print $4}' || echo "0")
        transfer_rate=$(grep "Transfer rate:" "$ab_output" | awk '{print $3}' || echo "0")
        failed_requests=$(grep "Failed requests:" "$ab_output" | awk '{print $3}' || echo "0")

        cat > "$ab_json" << EOF
{
  "test_name": "$test_name",
  "endpoint": "$endpoint",
  "requests_per_second": $requests_per_sec,
  "time_per_request_ms": $time_per_request,
  "transfer_rate_kbps": $transfer_rate,
  "failed_requests": $failed_requests,
  "total_requests": $TOTAL_REQUESTS,
  "concurrent_users": $CONCURRENT_USERS
}
EOF
    fi
}

run_wrk_test() {
    local url="$1"
    local endpoint="$2"
    local test_name="$3"

    if ! command -v wrk >/dev/null 2>&1; then
        return
    fi

    local wrk_output="$REPORTS_DIR/${PERF_RUN_ID}_wrk_${test_name}.txt"
    local wrk_json="$REPORTS_DIR/${PERF_RUN_ID}_wrk_${test_name}.json"

    print_status "Running wrk test for $test_name..."

    # Run wrk with custom Lua script for detailed stats
    wrk -t4 -c"$CONCURRENT_USERS" -d"${TEST_DURATION}s" --timeout 30s \
        "$url$endpoint" > "$wrk_output" 2>&1 || true

    # Parse wrk output to JSON (simplified)
    if [[ -f "$wrk_output" ]]; then
        local requests_per_sec avg_latency transfer_rate
        requests_per_sec=$(grep "Requests/sec:" "$wrk_output" | awk '{print $2}' || echo "0")
        avg_latency=$(grep "Latency" "$wrk_output" | awk '{print $2}' || echo "0")
        transfer_rate=$(grep "Transfer/sec:" "$wrk_output" | awk '{print $2}' || echo "0")

        cat > "$wrk_json" << EOF
{
  "test_name": "$test_name",
  "endpoint": "$endpoint",
  "requests_per_second": $requests_per_sec,
  "average_latency": "$avg_latency",
  "transfer_rate": "$transfer_rate",
  "test_duration": $TEST_DURATION,
  "concurrent_users": $CONCURRENT_USERS
}
EOF
    fi
}

run_response_time_test() {
    local url="$1"
    local endpoint="$2"
    local test_name="$3"

    print_status "Measuring detailed response times for $test_name..."

    local response_times=()
    local status_codes=()

    # Take 10 samples for detailed timing
    for i in {1..10}; do
        local result
        result=$(curl -o /dev/null -s -w "%{http_code},%{time_total},%{time_connect},%{time_starttransfer}" "$url$endpoint")

        local status_code time_total time_connect time_starttransfer
        IFS=',' read -r status_code time_total time_connect time_starttransfer <<< "$result"

        response_times+=("$time_total")
        status_codes+=("$status_code")

        sleep 0.5
    done

    # Calculate statistics
    local min_time max_time avg_time
    min_time=$(printf '%s\n' "${response_times[@]}" | sort -n | head -1)
    max_time=$(printf '%s\n' "${response_times[@]}" | sort -n | tail -1)
    avg_time=$(printf '%s\n' "${response_times[@]}" | awk '{sum+=$1} END {print sum/NR}')

    # Save detailed timing results
    cat > "$REPORTS_DIR/${PERF_RUN_ID}_timing_${test_name}.json" << EOF
{
  "test_name": "$test_name",
  "endpoint": "$endpoint",
  "samples": 10,
  "response_times": [$(IFS=,; echo "${response_times[*]}")],
  "status_codes": [$(IFS=,; echo "${status_codes[*]}")],
  "statistics": {
    "min_time_seconds": $min_time,
    "max_time_seconds": $max_time,
    "average_time_seconds": $avg_time
  }
}
EOF
}

generate_performance_report() {
    print_header "Generating Performance Report"

    local summary_report="$REPORTS_DIR/${PERF_RUN_ID}_summary.json"
    local html_report="$REPORTS_DIR/${PERF_RUN_ID}_report.html"

    # Combine all JSON results
    local combined_results="[]"

    for json_file in "$REPORTS_DIR"/${PERF_RUN_ID}_*.json; do
        if [[ -f "$json_file" ]]; then
            local content
            content=$(cat "$json_file")
            combined_results=$(echo "$combined_results" | jq ". += [$content]")
        fi
    done

    # Create summary report
    cat > "$summary_report" << EOF
{
  "performance_test_id": "$PERF_RUN_ID",
  "timestamp": "$(date -Iseconds)",
  "test_results": $combined_results
}
EOF

    # Generate HTML report
    cat > "$html_report" << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>WordPress Performance Test Report</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .header { background: #2271b1; color: white; padding: 20px; border-radius: 5px; }
        .metric { background: #f6f7f7; padding: 15px; margin: 10px 0; border-radius: 5px; }
        .good { border-left: 4px solid #46b450; }
        .warning { border-left: 4px solid #ffb900; }
        .error { border-left: 4px solid #dc3232; }
        table { width: 100%; border-collapse: collapse; margin: 20px 0; }
        th, td { padding: 10px; text-align: left; border-bottom: 1px solid #ddd; }
        th { background-color: #f6f7f7; }
    </style>
</head>
<body>
    <div class="header">
        <h1>WordPress Performance Test Report</h1>
        <p>Test Run ID: PERF_RUN_ID</p>
        <p>Generated: TIMESTAMP</p>
    </div>

    <h2>Test Summary</h2>
    <div id="summary">
        <!-- Summary will be populated by JavaScript -->
    </div>

    <h2>Detailed Results</h2>
    <div id="details">
        <!-- Details will be populated by JavaScript -->
    </div>

    <script>
        // Load and display performance data
        // This would be populated with actual test results
    </script>
</body>
</html>
EOF

    # Replace placeholders in HTML
    sed -i '' "s/PERF_RUN_ID/$PERF_RUN_ID/g" "$html_report"
    sed -i '' "s/TIMESTAMP/$(date)/g" "$html_report"

    print_success "Performance report generated:"
    print_status "JSON: $summary_report"
    print_status "HTML: $html_report"
}

run_performance_tests() {
    local target_url="$1"

    print_header "Running Performance Tests"
    print_status "Target: $target_url"
    print_status "Parameters: $CONCURRENT_USERS concurrent users, $TOTAL_REQUESTS requests"

    get_wordpress_info "$target_url"

    # Test each endpoint
    for endpoint in "${ENDPOINTS[@]}"; do
        local test_name
        test_name=$(echo "$endpoint" | tr '/' '_' | tr -d '.')
        test_name="${test_name#_}"  # Remove leading underscore
        test_name="${test_name:-homepage}"  # Default name for root

        print_status "Testing endpoint: $endpoint"

        # Run different types of performance tests
        run_apache_bench_test "$target_url" "$endpoint" "$test_name"
        run_wrk_test "$target_url" "$endpoint" "$test_name"
        run_response_time_test "$target_url" "$endpoint" "$test_name"
    done

    generate_performance_report
}

# Parse arguments
VERBOSE=false
TARGET_URL=""

while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help)
            usage
            ;;
        -c|--concurrent)
            CONCURRENT_USERS="$2"
            shift 2
            ;;
        -n|--requests)
            TOTAL_REQUESTS="$2"
            shift 2
            ;;
        -t|--duration)
            TEST_DURATION="$2"
            shift 2
            ;;
        -r|--rampup)
            RAMP_UP_TIME="$2"
            shift 2
            ;;
        -v|--verbose)
            VERBOSE=true
            shift
            ;;
        -*)
            print_error "Unknown option: $1"
            usage
            ;;
        *)
            TARGET_URL="$1"
            shift
            ;;
    esac
done

if [[ -z "$TARGET_URL" ]]; then
    print_error "Target URL is required"
    usage
fi

# Main execution
main() {
    print_header "WordPress Enterprise Performance Testing"
    print_status "Performance test run: $PERF_RUN_ID"

    check_dependencies
    run_performance_tests "$TARGET_URL"

    print_header "Performance Testing Complete"
    print_success "Results saved to: $REPORTS_DIR"

    # macOS notification
    if command -v osascript >/dev/null 2>&1; then
        osascript -e "display notification \"Performance testing completed\" with title \"WordPress Tests\""
    fi
}

main
