#!/bin/bash

# WordPress Enterprise Test Environment Cleanup Script
# This script cleans up the test environment and removes containers, images, and volumes

set -e

# docker compose v2 is a plugin; the v1 binary is gone from CI runners.
if docker compose version >/dev/null 2>&1; then
    COMPOSE="docker compose"
else
    COMPOSE="docker-compose"
fi


# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m' # No Color

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
COMPOSE_FILE="$PROJECT_DIR/docker-compose.test.yml"

# Cleanup options
REMOVE_IMAGES=false
REMOVE_REPORTS=false
FORCE_CLEANUP=false
VERBOSE=false

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
    echo "WordPress Enterprise Test Environment Cleanup"
    echo ""
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  -h, --help              Show this help message"
    echo "  -v, --verbose           Enable verbose output"
    echo "  -i, --remove-images     Remove Docker images as well"
    echo "  -r, --remove-reports    Remove test reports and logs"
    echo "  -f, --force             Force cleanup without confirmation"
    echo "  -a, --all               Remove everything (containers, images, reports)"
    echo ""
    echo "Examples:"
    echo "  $0                      Basic cleanup (containers and volumes)"
    echo "  $0 -i                   Cleanup containers, volumes, and images"
    echo "  $0 -r                   Cleanup and remove test reports"
    echo "  $0 --all --force        Remove everything without asking"
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
            -i|--remove-images)
                REMOVE_IMAGES=true
                shift
                ;;
            -r|--remove-reports)
                REMOVE_REPORTS=true
                shift
                ;;
            -f|--force)
                FORCE_CLEANUP=true
                shift
                ;;
            -a|--all)
                REMOVE_IMAGES=true
                REMOVE_REPORTS=true
                shift
                ;;
            *)
                print_error "Unknown option: $1"
                usage
                ;;
        esac
    done
}

# Function to confirm cleanup
confirm_cleanup() {
    if [[ "$FORCE_CLEANUP" == "true" ]]; then
        return 0
    fi

    print_header "Cleanup Confirmation"

    echo "The following actions will be performed:"
    echo "  • Stop and remove test containers"
    echo "  • Remove test volumes"

    if [[ "$REMOVE_IMAGES" == "true" ]]; then
        echo "  • Remove Docker images"
    fi

    if [[ "$REMOVE_REPORTS" == "true" ]]; then
        echo "  • Remove test reports and logs"
    fi

    echo
    read -p "Do you want to continue? (y/N): " -r
    echo

    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        print_status "Cleanup cancelled"
        exit 0
    fi
}

# Function to check prerequisites
check_prerequisites() {
    print_header "Checking Prerequisites"

    # Check if Docker is running
    if ! docker info >/dev/null 2>&1; then
        print_error "Docker is not running. Please start Docker to cleanup properly."
        exit 1
    fi
    print_success "Docker is running"

    # Check if $COMPOSE is available
    if ! $COMPOSE version >/dev/null 2>&1; then
        print_error "$COMPOSE is not installed or not in PATH"
        exit 1
    fi
    print_success "$COMPOSE is available"

    # Check if compose file exists
    if [[ ! -f "$COMPOSE_FILE" ]]; then
        print_warning "Test compose file not found: $COMPOSE_FILE"
        print_status "Will skip Docker compose cleanup"
        return 1
    fi
    print_success "Test compose file found"

    return 0
}

# Function to stop and remove containers
cleanup_containers() {
    print_header "Cleaning Up Containers and Volumes"

    cd "$PROJECT_DIR"

    # Stop and remove containers with volumes
    print_status "Stopping and removing test containers..."

    if [[ "$VERBOSE" == "true" ]]; then
        $COMPOSE -f "$COMPOSE_FILE" down --remove-orphans --volumes
    else
        $COMPOSE -f "$COMPOSE_FILE" down --remove-orphans --volumes >/dev/null 2>&1
    fi

    print_success "Containers and volumes removed"

    # Additional cleanup of any leftover containers
    print_status "Checking for leftover WordPress test containers..."

    local leftover_containers
    leftover_containers=$(docker ps -a --filter "name=wp-test" --filter "name=wordpress-test" -q 2>/dev/null || true)

    if [[ -n "$leftover_containers" ]]; then
        print_status "Removing leftover containers..."
        if [[ "$VERBOSE" == "true" ]]; then
            docker rm -f $leftover_containers
        else
            docker rm -f $leftover_containers >/dev/null 2>&1
        fi
        print_success "Leftover containers removed"
    else
        print_success "No leftover containers found"
    fi
}

# Function to remove Docker images
cleanup_images() {
    if [[ "$REMOVE_IMAGES" != "true" ]]; then
        return
    fi

    print_header "Cleaning Up Docker Images"

    # Get image names from compose file
    local test_images
    test_images=$($COMPOSE -f "$COMPOSE_FILE" config --services 2>/dev/null | while read -r service; do
        $COMPOSE -f "$COMPOSE_FILE" config | grep -A 10 "^  $service:" | grep "image:" | cut -d':' -f2- | xargs
    done)

    # Also look for built images
    local built_images
    built_images=$(docker images --filter "label=com.docker.compose.project=wordpress-test" -q 2>/dev/null || true)

    # Remove WordPress test related images
    local wp_test_images
    wp_test_images=$(docker images --filter "reference=*wp-test*" --filter "reference=*wordpress-test*" -q 2>/dev/null || true)

    local all_images="$test_images $built_images $wp_test_images"

    if [[ -n "$all_images" ]]; then
        print_status "Removing WordPress test Docker images..."

        # Remove duplicates and empty strings
        local unique_images
        unique_images=$(echo "$all_images" | tr ' ' '\n' | sort -u | grep -v '^$' || true)

        if [[ -n "$unique_images" ]]; then
            if [[ "$VERBOSE" == "true" ]]; then
                echo "$unique_images" | xargs -r docker rmi -f
            else
                echo "$unique_images" | xargs -r docker rmi -f >/dev/null 2>&1 || true
            fi
            print_success "WordPress test images removed"
        else
            print_success "No test images to remove"
        fi
    else
        print_success "No test images found"
    fi

    # Clean up dangling images
    print_status "Removing dangling images..."
    local dangling_images
    dangling_images=$(docker images -f "dangling=true" -q 2>/dev/null || true)

    if [[ -n "$dangling_images" ]]; then
        if [[ "$VERBOSE" == "true" ]]; then
            docker rmi $dangling_images
        else
            docker rmi $dangling_images >/dev/null 2>&1 || true
        fi
        print_success "Dangling images removed"
    else
        print_success "No dangling images found"
    fi
}

# Function to remove test reports
cleanup_reports() {
    if [[ "$REMOVE_REPORTS" != "true" ]]; then
        return
    fi

    print_header "Cleaning Up Test Reports"

    local reports_dir="$PROJECT_DIR/tests/reports"

    if [[ -d "$reports_dir" ]]; then
        local report_count
        report_count=$(find "$reports_dir" -type f \( -name "*.log" -o -name "*.json" \) | wc -l | xargs)

        if [[ "$report_count" -gt 0 ]]; then
            print_status "Removing $report_count test report files..."

            if [[ "$VERBOSE" == "true" ]]; then
                find "$reports_dir" -type f \( -name "*.log" -o -name "*.json" \) -delete -print
            else
                find "$reports_dir" -type f \( -name "*.log" -o -name "*.json" \) -delete
            fi

            print_success "Test reports removed"
        else
            print_success "No test reports found"
        fi

        # Remove empty reports directory if it exists
        if [[ -d "$reports_dir" ]] && [[ -z "$(ls -A "$reports_dir" 2>/dev/null)" ]]; then
            rmdir "$reports_dir"
            print_success "Empty reports directory removed"
        fi
    else
        print_success "No reports directory found"
    fi
}

# Function to cleanup Docker system
cleanup_docker_system() {
    print_header "Docker System Cleanup"

    print_status "Running Docker system prune..."

    if [[ "$VERBOSE" == "true" ]]; then
        docker system prune -f
    else
        docker system prune -f >/dev/null 2>&1
    fi

    print_success "Docker system cleanup completed"
}

# Function to show cleanup summary
show_summary() {
    print_header "Cleanup Summary"

    # Check remaining containers
    local remaining_containers
    remaining_containers=$(docker ps -a --filter "name=wp-test" --filter "name=wordpress-test" --format "table {{.Names}}\t{{.Status}}" 2>/dev/null | grep -v "NAMES" || true)

    if [[ -n "$remaining_containers" ]]; then
        print_warning "Some containers may still exist:"
        echo "$remaining_containers"
    else
        print_success "No WordPress test containers remaining"
    fi

    # Check remaining images if we tried to remove them
    if [[ "$REMOVE_IMAGES" == "true" ]]; then
        local remaining_images
        remaining_images=$(docker images --filter "reference=*wp-test*" --filter "reference=*wordpress-test*" --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}" 2>/dev/null | grep -v "REPOSITORY" || true)

        if [[ -n "$remaining_images" ]]; then
            print_warning "Some test images may still exist:"
            echo "$remaining_images"
        else
            print_success "No WordPress test images remaining"
        fi
    fi

    # Check reports directory
    local reports_dir="$PROJECT_DIR/tests/reports"
    if [[ "$REMOVE_REPORTS" == "true" ]]; then
        if [[ -d "$reports_dir" ]] && [[ -n "$(ls -A "$reports_dir" 2>/dev/null)" ]]; then
            print_warning "Reports directory still contains files"
        else
            print_success "Test reports cleaned up"
        fi
    fi

    print_status "Cleanup completed successfully!"
}

# Main execution
main() {
    print_header "WordPress Enterprise Test Environment Cleanup"

    parse_args "$@"
    confirm_cleanup

    local compose_available=true
    check_prerequisites || compose_available=false

    # Perform cleanup steps
    if [[ "$compose_available" == "true" ]]; then
        cleanup_containers
    else
        print_warning "Skipping container cleanup (no compose file found)"
    fi

    cleanup_images
    cleanup_reports
    cleanup_docker_system
    show_summary

    print_header "Cleanup Complete"
    print_success "WordPress Enterprise test environment has been cleaned up! 🧹"
}

# Run main function with all arguments
main "$@"
