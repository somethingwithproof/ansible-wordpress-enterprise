#!/bin/bash
# SPDX-FileCopyrightText: 2025 Thomas Vincent
# SPDX-License-Identifier: MIT

# WordPress Enterprise Test Results Analyzer
# This script analyzes test results and generates comprehensive reports

set -e

readonly JQ_SCENARIO='.scenario'
readonly JQ_TARGET='.target'
readonly JQ_RESULT='.result'
readonly JQ_LOG_FILE='.log_file'

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
REPORTS_DIR="$PROJECT_DIR/tests/reports"

# Options
SHOW_DETAILS=false
SHOW_LOGS=false
TEST_RUN_ID=""
OUTPUT_FORMAT="table"

# Function to print colored output
print_color() {
    local color=$1
    shift
    echo -e "${color}$*${NC}"
}

# Function to print section headers
print_header() {
    local message="$1"
    echo
    print_color $PURPLE "=================================="
    print_color $PURPLE "${message}"
    print_color $PURPLE "=================================="
    echo
}

# Function to print status
print_status() {
    local message="$1"
    print_color $BLUE "ℹ️  ${message}"
}

print_success() {
    local message="$1"
    print_color $GREEN "✅ ${message}"
}

print_warning() {
    local message="$1"
    print_color $YELLOW "⚠️  ${message}"
}

print_error() {
    local message="$1"
    print_color $RED "❌ ${message}"
}

# Function to show usage
usage() {
    echo "WordPress Enterprise Test Results Analyzer"
    echo ""
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  -h, --help              Show this help message"
    echo "  -d, --details           Show detailed test information"
    echo "  -l, --logs              Show log excerpts for failed tests"
    echo "  -r, --run-id RUN_ID     Analyze specific test run"
    echo "  -f, --format FORMAT     Output format (table, json, csv)"
    echo "  -a, --all-runs          Show summary of all test runs"
    echo ""
    echo "Examples:"
    echo "  $0                      Show latest test results"
    echo "  $0 -d                   Show detailed results"
    echo "  $0 -r test_run_20231201_123456  Analyze specific test run"
    echo "  $0 --format json        Output results in JSON format"
    echo "  $0 --all-runs          Show summary of all test runs"
    echo ""
    exit 0
}

# Function to parse command line arguments
parse_args() {
    local option
    while [[ $# -gt 0 ]]; do
        option="$1"
        case "$option" in
            -h|--help)
                usage
                ;;
            -d|--details)
                SHOW_DETAILS=true
                shift
                ;;
            -l|--logs)
                SHOW_LOGS=true
                shift
                ;;
            -r|--run-id)
                TEST_RUN_ID="$2"
                shift 2
                ;;
            -f|--format)
                OUTPUT_FORMAT="$2"
                shift 2
                ;;
            -a|--all-runs)
                show_all_runs
                exit 0
                ;;
            *)
                print_error "Unknown option: $option"
                usage
                ;;
        esac
    done
}

# Function to validate output format
validate_format() {
    case "$OUTPUT_FORMAT" in
        table|json|csv)
            ;;
        *)
            print_error "Invalid output format: $OUTPUT_FORMAT"
            print_status "Valid formats: table, json, csv"
            exit 1
            ;;
    esac
}

# Function to check if reports directory exists
check_reports_dir() {
    if [[ ! -d "$REPORTS_DIR" ]]; then
        print_error "Reports directory not found: $REPORTS_DIR"
        print_status "No test results available. Run tests first."
        exit 1
    fi
}

# Function to find latest test run
find_latest_run() {
    if [[ -n "$TEST_RUN_ID" ]]; then
        echo "$TEST_RUN_ID"
        return
    fi

    local latest_summary
    latest_summary=$(ls -t "$REPORTS_DIR"/*_summary.json 2>/dev/null | head -1)

    if [[ -z "$latest_summary" ]]; then
        print_error "No test results found in $REPORTS_DIR"
        exit 1
    fi

    basename "$latest_summary" | sed 's/_summary\.json$//'
}

# Function to get test run summary
get_test_summary() {
    local run_id="$1"
    local summary_file="$REPORTS_DIR/${run_id}_summary.json"

    if [[ ! -f "$summary_file" ]]; then
        print_error "Summary file not found: $summary_file"
        exit 1
    fi

    cat "$summary_file"
}

# Function to get individual test reports
get_test_reports() {
    local run_id="$1"
    local reports=()

    while IFS= read -r -d '' file; do
        if [[ "$file" =~ ${run_id}_.*_report\.json$ ]]; then
            reports+=("$file")
        fi
    done < <(find "$REPORTS_DIR" -name "*_report.json" -print0 2>/dev/null)

    printf '%s\n' "${reports[@]}" | sort
}

# Function to format duration
format_duration() {
    local duration=$1
    local hours=$((duration / 3600))
    local minutes=$(((duration % 3600) / 60))
    local seconds=$((duration % 60))

    if [[ $hours -gt 0 ]]; then
        printf "%02d:%02d:%02d" "$hours" "$minutes" "$seconds"
    elif [[ $minutes -gt 0 ]]; then
        printf "%02d:%02d" "$minutes" "$seconds"
    else
        printf "%ds" "$seconds"
    fi
}

# Function to show results in table format
show_table_results() {
    local run_id="$1"
    local summary_json="$2"

    # Parse summary
    local total_tests passed_tests failed_tests success_rate timestamp
    total_tests=$(echo "$summary_json" | jq -r '.total_tests')
    passed_tests=$(echo "$summary_json" | jq -r '.passed_tests')
    failed_tests=$(echo "$summary_json" | jq -r '.failed_tests')
    success_rate=$(echo "$summary_json" | jq -r '.success_rate')
    timestamp=$(echo "$summary_json" | jq -r '.timestamp')

    print_header "Test Run Summary: $run_id"

    echo "Timestamp:     $timestamp"
    echo "Total Tests:   $total_tests"
    echo "Passed:        $passed_tests"
    echo "Failed:        $failed_tests"
    echo "Success Rate:  $success_rate"
    echo

    # Show individual test results
    print_header "Individual Test Results"

    printf "%-35s %-15s %-10s %-10s %-8s\n" "Test" "Target" "Result" "Duration" "Log"
    printf "%-35s %-15s %-10s %-10s %-8s\n" "---" "---" "---" "---" "---"

    local reports
    mapfile -t reports < <(get_test_reports "$run_id")

    for report_file in "${reports[@]}"; do
        if [[ -f "$report_file" ]]; then
            local report_json scenario target result duration_seconds log_file
            report_json=$(cat "$report_file")
            scenario=$(echo "$report_json" | jq -r "$JQ_SCENARIO" | sed 's/\.yml$//')
            target=$(echo "$report_json" | jq -r "$JQ_TARGET")
            result=$(echo "$report_json" | jq -r "$JQ_RESULT")
            duration_seconds=$(echo "$report_json" | jq -r '.duration_seconds')
            log_file=$(echo "$report_json" | jq -r "$JQ_LOG_FILE" | xargs basename)

            local duration_formatted result_colored log_indicator
            duration_formatted=$(format_duration "$duration_seconds")

            case "$result" in
                PASS)
                    result_colored="${GREEN}PASS${NC}"
                    log_indicator="📄"
                    ;;
                FAIL)
                    result_colored="${RED}FAIL${NC}"
                    log_indicator="📄"
                    ;;
                *)
                    result_colored="$result"
                    log_indicator="📄"
                    ;;
            esac

            printf "%-35s %-15s %-20s %-10s %-8s\n" \
                "$scenario" "$target" "$result_colored" "$duration_formatted" "$log_indicator"
        fi
    done

    echo

    # Show failure details if requested
    if [[ "$SHOW_DETAILS" == "true" ]]; then
        show_failure_details "$run_id"
    fi

    # Show log excerpts if requested
    if [[ "$SHOW_LOGS" == "true" ]]; then
        show_log_excerpts "$run_id"
    fi
}

# Function to show failure details
show_failure_details() {
    local run_id="$1"
    local failed_tests=()

    local reports
    mapfile -t reports < <(get_test_reports "$run_id")

    for report_file in "${reports[@]}"; do
        if [[ -f "$report_file" ]]; then
            local result
            result=$(jq -r "$JQ_RESULT" "$report_file")
            if [[ "$result" == "FAIL" ]]; then
                failed_tests+=("$report_file")
            fi
        fi
    done

    if [[ ${#failed_tests[@]} -gt 0 ]]; then
        print_header "Failed Test Details"

        for report_file in "${failed_tests[@]}"; do
            local report_json scenario target duration_seconds log_file
            report_json=$(cat "$report_file")
            scenario=$(echo "$report_json" | jq -r "$JQ_SCENARIO")
            target=$(echo "$report_json" | jq -r "$JQ_TARGET")
            duration_seconds=$(echo "$report_json" | jq -r '.duration_seconds')
            log_file=$(echo "$report_json" | jq -r "$JQ_LOG_FILE")

            print_color $RED "❌ $scenario on $target"
            echo "   Duration: $(format_duration "$duration_seconds")"
            echo "   Log file: $log_file"
            echo
        done
    fi
}

# Function to show log excerpts for failed tests
show_log_excerpts() {
    local run_id="$1"
    local failed_tests=()

    local reports
    mapfile -t reports < <(get_test_reports "$run_id")

    for report_file in "${reports[@]}"; do
        if [[ -f "$report_file" ]]; then
            local result
            result=$(jq -r "$JQ_RESULT" "$report_file")
            if [[ "$result" == "FAIL" ]]; then
                failed_tests+=("$report_file")
            fi
        fi
    done

    if [[ ${#failed_tests[@]} -gt 0 ]]; then
        print_header "Failed Test Log Excerpts"

        for report_file in "${failed_tests[@]}"; do
            local report_json scenario target log_file
            report_json=$(cat "$report_file")
            scenario=$(echo "$report_json" | jq -r "$JQ_SCENARIO")
            target=$(echo "$report_json" | jq -r "$JQ_TARGET")
            log_file=$(echo "$report_json" | jq -r "$JQ_LOG_FILE")

            print_color $RED "❌ $scenario on $target"
            echo

            if [[ -f "$log_file" ]]; then
                echo "Last 20 lines of log:"
                echo "----------------------"
                tail -20 "$log_file" | sed 's/^/    /'
                echo
            else
                echo "    Log file not found: $log_file"
                echo
            fi
        done
    fi
}

# Function to show results in JSON format
show_json_results() {
    local run_id="$1"
    local summary_json="$2"

    local reports
    mapfile -t reports < <(get_test_reports "$run_id")

    local individual_results="[]"
    for report_file in "${reports[@]}"; do
        if [[ -f "$report_file" ]]; then
            local report_json
            report_json=$(cat "$report_file")
            individual_results=$(echo "$individual_results" | jq ". += [$report_json]")
        fi
    done

    # Combine summary and individual results
    jq -n \
        --argjson summary "$summary_json" \
        --argjson individual "$individual_results" \
        '{
            summary: $summary,
            individual_results: $individual
        }'
}

# Function to show results in CSV format
show_csv_results() {
    local run_id="$1"

    echo "scenario,target,result,duration_seconds,start_time,end_time,log_file"

    local reports
    mapfile -t reports < <(get_test_reports "$run_id")

    for report_file in "${reports[@]}"; do
        if [[ -f "$report_file" ]]; then
            local report_json scenario target result duration_seconds start_time end_time log_file
            report_json=$(cat "$report_file")
            scenario=$(echo "$report_json" | jq -r "$JQ_SCENARIO")
            target=$(echo "$report_json" | jq -r "$JQ_TARGET")
            result=$(echo "$report_json" | jq -r "$JQ_RESULT")
            duration_seconds=$(echo "$report_json" | jq -r '.duration_seconds')
            start_time=$(echo "$report_json" | jq -r '.start_time')
            end_time=$(echo "$report_json" | jq -r '.end_time')
            log_file=$(echo "$report_json" | jq -r "$JQ_LOG_FILE")

            echo "$scenario,$target,$result,$duration_seconds,$start_time,$end_time,$log_file"
        fi
    done
}

# Function to show all test runs summary
show_all_runs() {
    print_header "All Test Runs Summary"

    local summary_files
    mapfile -t summary_files < <(find "$REPORTS_DIR" -name "*_summary.json" -type f 2>/dev/null | sort -r)

    if [[ ${#summary_files[@]} -eq 0 ]]; then
        print_warning "No test runs found"
        return
    fi

    printf "%-25s %-20s %-6s %-6s %-6s %-10s\n" "Run ID" "Timestamp" "Total" "Pass" "Fail" "Success"
    printf "%-25s %-20s %-6s %-6s %-6s %-10s\n" "---" "---" "---" "---" "---" "---"

    for summary_file in "${summary_files[@]}"; do
        local summary_json run_id timestamp total_tests passed_tests failed_tests success_rate
        summary_json=$(cat "$summary_file")
        run_id=$(echo "$summary_json" | jq -r '.test_run_id')
        timestamp=$(echo "$summary_json" | jq -r '.timestamp' | cut -d'T' -f1)
        total_tests=$(echo "$summary_json" | jq -r '.total_tests')
        passed_tests=$(echo "$summary_json" | jq -r '.passed_tests')
        failed_tests=$(echo "$summary_json" | jq -r '.failed_tests')
        success_rate=$(echo "$summary_json" | jq -r '.success_rate')

        printf "%-25s %-20s %-6s %-6s %-6s %-10s\n" \
            "$run_id" "$timestamp" "$total_tests" "$passed_tests" "$failed_tests" "$success_rate"
    done

    echo
}

# Main execution
main() {
    parse_args "$@"
    validate_format
    check_reports_dir

    local run_id
    run_id=$(find_latest_run)

    if [[ -z "$run_id" ]]; then
        print_error "No test run found"
        exit 1
    fi

    local summary_json
    summary_json=$(get_test_summary "$run_id")

    case "$OUTPUT_FORMAT" in
        table)
            show_table_results "$run_id" "$summary_json"
            ;;
        json)
            show_json_results "$run_id" "$summary_json"
            ;;
        csv)
            show_csv_results "$run_id"
            ;;
        *)
            print_error "Unsupported output format: $OUTPUT_FORMAT"
            return 1
            ;;
    esac
}

# Check if jq is available
if ! command -v jq >/dev/null 2>&1; then
    print_error "jq is required but not installed"
    print_status "Install jq: brew install jq (macOS) or apt-get install jq (Ubuntu)"
    exit 1
fi

# Run main function with all arguments
main "$@"
