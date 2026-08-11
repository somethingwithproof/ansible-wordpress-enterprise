# docker compose v2 ships as a docker plugin; the standalone v1 binary was
# removed from the GitHub runner images, which broke check-test-prereqs.
# Prefer v2 and fall back to v1 so existing local setups keep working.
COMPOSE := $(shell if docker compose version >/dev/null 2>&1; then echo 'docker compose'; else echo 'docker-compose'; fi)

.PHONY: help build test lint clean docker-test install galaxy-install test-all test-ubuntu test-centos test-single analyze reports clean-test

# Variables
TEST_SCRIPTS_DIR := tests/scripts
REPORTS_DIR := tests/reports

# Colors for output
GREEN := \033[0;32m
YELLOW := \033[1;33m
BLUE := \033[0;34m
RED := \033[0;31m
NC := \033[0m

help:
	@echo "WordPress Enterprise Ansible Role - Available Commands"
	@echo ""
	@echo "Development Commands:"
	@echo "  make install          - Install Ansible and dependencies"
	@echo "  make galaxy-install   - Install Ansible Galaxy collections"
	@echo "  make lint             - Run linters (yamllint, ansible-lint)"
	@echo "  make docker-dev       - Start development environment"
	@echo ""
	@echo "Testing Commands (End-to-End):"
	@echo "  make test-all         - Run all end-to-end tests"
	@echo "  make test-ubuntu      - Run Ubuntu tests only"
	@echo "  make test-centos      - Run CentOS tests only"
	@echo "  make test-single      - Run single test (SCENARIO=01 TARGET=ubuntu)"
	@echo "  make test-scenario-04 - Run comprehensive security hardening test"
	@echo "  make test-scenario-05 - Run security edge cases test"
	@echo "  make test-security-unit - Run security unit tests"
	@echo "  make test-security-all - Run all security tests"
	@echo "  make test-coverage-report - Generate comprehensive test coverage report"
	@echo "  make analyze          - Analyze latest test results"
	@echo "  make reports          - Show all test runs summary"
	@echo ""
	@echo "Legacy Testing:"
	@echo "  make test             - Run Molecule tests"
	@echo "  make docker-test      - Run tests in Docker containers"
	@echo ""
	@echo "Cleanup Commands:"
	@echo "  make clean-test       - Clean up test environment"
	@echo "  make docker-clean     - Clean Docker resources"
	@echo "  make clean            - Clean temporary files"
	@echo ""
	@echo "Examples:"
	@echo "  make test-single SCENARIO=01 TARGET=ubuntu"
	@echo "  make analyze"

install:
	@echo "Installing Ansible and dependencies..."
	pip install --upgrade pip
	pip install ansible>=2.14 ansible-lint yamllint molecule molecule-plugins[docker] pytest-testinfra

galaxy-install:
	@echo "Installing Ansible Galaxy collections..."
	ansible-galaxy collection install community.general
	ansible-galaxy collection install community.mysql
	ansible-galaxy collection install ansible.posix

lint:
	@echo "Running linters..."
	yamllint .
	ansible-lint

test:
	@echo "Running Molecule tests..."
	molecule test

docker-build:
	@echo "Building Docker images..."
	$(COMPOSE) build ubuntu-22 ubuntu-24 rocky-9

docker-test:
	@echo "Running tests in Docker..."
	$(COMPOSE) run --rm molecule

docker-dev:
	@echo "Starting development environment..."
	$(COMPOSE) up -d wordpress-dev mysql redis mailhog
	@echo ""
	@echo "Services available:"
	@echo "  WordPress: http://localhost:8080"
	@echo "  MySQL: localhost:3307"
	@echo "  Redis: localhost:6380"
	@echo "  MailHog: http://localhost:8025"
	@echo ""
	@echo "To access WordPress container:"
	@echo "  $(COMPOSE) exec wordpress-dev bash"

docker-logs:
	$(COMPOSE) logs -f wordpress-dev

docker-stop:
	$(COMPOSE) down

docker-clean:
	@echo "Cleaning Docker resources..."
	$(COMPOSE) down -v
	docker system prune -f

clean:
	@echo "Cleaning temporary files..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".tox" -exec rm -rf {} + 2>/dev/null || true
	rm -rf molecule/default/.molecule

# Development shortcuts
dev: docker-dev

stop: docker-stop

logs: docker-logs

shell:
	$(COMPOSE) exec wordpress-dev bash

mysql-shell:
	$(COMPOSE) exec mysql mysql -uroot -proot wordpress

redis-cli:
	$(COMPOSE) exec redis redis-cli

# End-to-End Test Automation Commands
check-test-prereqs:
	@echo "$(BLUE)Checking test prerequisites...$(NC)"
	@command -v docker >/dev/null 2>&1 || { echo "$(RED)Error: Docker is not installed$(NC)"; exit 1; }
	@docker info >/dev/null 2>&1 || { echo "$(RED)Error: Docker is not running$(NC)"; exit 1; }
	@$(COMPOSE) version >/dev/null 2>&1 || { echo "$(RED)Error: docker compose is not available$(NC)"; exit 1; }
	@command -v jq >/dev/null 2>&1 || { echo "$(RED)Error: jq is not installed (brew install jq)$(NC)"; exit 1; }
	@test -f docker-compose.test.yml || { echo "$(RED)Error: docker-compose.test.yml not found$(NC)"; exit 1; }
	@echo "$(GREEN)✅ All test prerequisites are met$(NC)"

test-all: check-test-prereqs
	@echo "$(BLUE)Running all end-to-end tests...$(NC)"
	@$(TEST_SCRIPTS_DIR)/run-all-tests.sh

test-ubuntu: check-test-prereqs
	@echo "$(BLUE)Running Ubuntu tests...$(NC)"
	@$(TEST_SCRIPTS_DIR)/run-all-tests.sh --ubuntu-only

test-centos: check-test-prereqs
	@echo "$(BLUE)Running CentOS tests...$(NC)"
	@$(TEST_SCRIPTS_DIR)/run-all-tests.sh --centos-only

test-single: check-test-prereqs
ifndef SCENARIO
	@echo "$(RED)Error: SCENARIO variable is required$(NC)"
	@echo "Usage: make test-single SCENARIO=01 TARGET=ubuntu"
	@echo "Available scenarios: 01, 02, 03, 04, 05"
	@echo "Available targets: ubuntu, centos"
	@exit 1
endif
ifndef TARGET
	@echo "$(RED)Error: TARGET variable is required$(NC)"
	@echo "Usage: make test-single SCENARIO=01 TARGET=ubuntu"
	@echo "Available scenarios: 01, 02, 03, 04, 05"
	@echo "Available targets: ubuntu, centos"
	@exit 1
endif
	@echo "$(BLUE)Running single test: scenario $(SCENARIO) on $(TARGET)...$(NC)"
	@$(TEST_SCRIPTS_DIR)/run-single-test.sh -t $(TARGET) -s 0$(SCENARIO)-*.yml

test-verbose: check-test-prereqs
	@echo "$(BLUE)Running all tests (verbose)...$(NC)"
	@$(TEST_SCRIPTS_DIR)/run-all-tests.sh --verbose

analyze:
	@echo "$(BLUE)Analyzing test results...$(NC)"
	@$(TEST_SCRIPTS_DIR)/analyze-results.sh

analyze-details:
	@echo "$(BLUE)Analyzing test results (detailed)...$(NC)"
	@$(TEST_SCRIPTS_DIR)/analyze-results.sh --details --logs

reports:
	@echo "$(BLUE)Showing all test runs...$(NC)"
	@$(TEST_SCRIPTS_DIR)/analyze-results.sh --all-runs

clean-test:
	@echo "$(BLUE)Cleaning up test environment...$(NC)"
	@$(TEST_SCRIPTS_DIR)/cleanup.sh --force

clean-test-all:
	@echo "$(BLUE)Cleaning up everything (containers, images, reports)...$(NC)"
	@$(TEST_SCRIPTS_DIR)/cleanup.sh --all --force

test-scenario-04: check-test-prereqs
	@echo "$(BLUE)Running comprehensive security hardening test...$(NC)"
	@$(TEST_SCRIPTS_DIR)/run-all-tests.sh --test 04

test-scenario-05: check-test-prereqs
	@echo "$(BLUE)Running security edge cases test...$(NC)"
	@$(TEST_SCRIPTS_DIR)/run-all-tests.sh --test 05

# The suite asserts on a provisioned host (installed scripts, LSM state,
# firewall, cron), so it has to run inside a target the role has configured,
# not on the machine driving the tests.
test-security-unit: check-test-prereqs
	@echo "$(BLUE)Running security unit tests...$(NC)"
	@docker exec wp-test-ubuntu bash /ansible-workspace/tests/scripts/security-unit-tests.sh

test-security-all: check-test-prereqs
	@echo "$(BLUE)Running all security tests (scenarios + unit tests)...$(NC)"
	@$(TEST_SCRIPTS_DIR)/run-all-tests.sh --test 04
	@$(TEST_SCRIPTS_DIR)/run-all-tests.sh --test 05
	@$(TEST_SCRIPTS_DIR)/security-unit-tests.sh

test-coverage-report:
	@echo "$(BLUE)Generating comprehensive test coverage report...$(NC)"
	@$(TEST_SCRIPTS_DIR)/generate-coverage-report.sh

test-status:
	@echo "$(BLUE)Test environment status:$(NC)"
	@echo ""
	@echo "$(YELLOW)Docker containers:$(NC)"
	@docker ps -a --filter "name=wp-test" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}" 2>/dev/null || echo "No test containers found"
	@echo ""
	@echo "$(YELLOW)Test reports:$(NC)"
	@if [ -d "$(REPORTS_DIR)" ]; then \
		find $(REPORTS_DIR) -name "*.json" -o -name "*.log" | wc -l | xargs printf "Found %s report files\n"; \
	else \
		echo "No reports directory found"; \
	fi
