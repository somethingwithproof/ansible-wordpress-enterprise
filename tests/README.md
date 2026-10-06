<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

# WordPress Enterprise Test Automation

This directory contains comprehensive end-to-end test automation for the WordPress Enterprise Ansible role. The testing framework provides isolated, reproducible testing environments using Docker containers and supports multiple operating systems and configurations.

## Quick Start

### Prerequisites

- Docker and docker-compose
- jq (for JSON processing)
- Make (optional, for convenience commands)

Install prerequisites on macOS:
```bash
brew install docker docker-compose jq
```

### Running Tests

```bash
# Run all tests
make test-all

# Or directly:
./tests/scripts/run-all-tests.sh
```

## Test Framework Overview

### Architecture

The test framework consists of:

1. **Docker Compose Environment** (`docker-compose.test.yml`)
   - Multi-container testing environment
   - Isolated services (MySQL, Redis, MailHog, etc.)
   - Two test targets: Ubuntu 22.04 and CentOS Stream 9

2. **Test Scripts** (`tests/scripts/`)
   - `run-all-tests.sh` - Main test runner
   - `run-single-test.sh` - Single test execution
   - `analyze-results.sh` - Result analysis and reporting
   - `cleanup.sh` - Environment cleanup

3. **Test Scenarios** (`tests/scenarios/`)
   - `01-basic-installation.yml` - Basic WordPress with Nginx
   - `02-apache-installation.yml` - WordPress with Apache
   - `03-validation-security.yml` - Security and validation features

4. **Test Infrastructure** (`tests/docker/`, `tests/fixtures/`, etc.)
   - Docker images and configurations
   - Test data and fixtures
   - Inventory files for different targets

## Test Scenarios

### 01: Basic Installation (Ubuntu + Nginx)

Tests core WordPress functionality:
- Prerequisites and system packages
- User and directory creation
- WordPress download and configuration
- Nginx web server setup
- PHP-FPM configuration
- Redis caching integration
- MySQL database setup
- Plugin and theme management
- SSL certificate generation

**Target:** Ubuntu 22.04
**Web Server:** Nginx
**Caching:** Redis
**Database:** MySQL 8.0

### 02: Apache Installation (CentOS + Apache)

Tests WordPress with Apache:
- CentOS/RHEL compatibility
- Apache web server configuration
- Memcached caching
- Advanced PHP settings
- Repository management (EPEL, Remi, etc.)
- SELinux compatibility
- Firewall configuration

**Target:** CentOS Stream 9
**Web Server:** Apache
**Caching:** Memcached
**Database:** MariaDB 10.6

### 03: Validation and Security

Tests validation and security features:
- Input validation and error handling
- Security hardening
- SSL/TLS certificate management
- Security plugin installation
- File permission validation
- Service health checks
- Configuration validation

**Target:** Both Ubuntu and CentOS
**Focus:** Security and validation

## Usage Examples

### Basic Test Execution

```bash
# Run all tests
./tests/scripts/run-all-tests.sh

# Run Ubuntu tests only
./tests/scripts/run-all-tests.sh --ubuntu-only

# Run specific test scenario
./tests/scripts/run-all-tests.sh --test 01

# Run with verbose output
./tests/scripts/run-all-tests.sh --verbose
```

### Single Test Execution

```bash
# Run specific test on specific target
./tests/scripts/run-single-test.sh -t ubuntu -s 01-basic-installation.yml

# Run with verbose output and no cleanup
./tests/scripts/run-single-test.sh -t centos -s 02-apache-installation.yml -v --no-cleanup
```

### Result Analysis

```bash
# Analyze latest test results
./tests/scripts/analyze-results.sh

# Show detailed results with log excerpts
./tests/scripts/analyze-results.sh --details --logs

# Show all test runs
./tests/scripts/analyze-results.sh --all-runs

# Export results as JSON
./tests/scripts/analyze-results.sh --format json > results.json
```

### Environment Management

```bash
# Check test environment status
make test-status

# Clean up test environment
./tests/scripts/cleanup.sh

# Complete cleanup (including images and reports)
./tests/scripts/cleanup.sh --all
```

## Makefile Commands

The project includes convenient Makefile targets:

```bash
# Test Commands
make test-all                    # Run all tests
make test-ubuntu                 # Run Ubuntu tests only
make test-centos                 # Run CentOS tests only
make test-single SCENARIO=01 TARGET=ubuntu  # Run specific test

# Analysis Commands
make analyze                     # Analyze latest results
make analyze-details             # Detailed analysis with logs
make reports                     # Show all test runs

# Management Commands
make test-status                 # Show environment status
make clean-test                  # Clean test environment
make clean-test-all             # Complete cleanup
```

## Directory Structure

```
tests/
├── README.md                   # This file
├── docker/                     # Docker configurations
│   ├── test-runner/           # Test runner container
│   ├── ubuntu-target/         # Ubuntu test target
│   └── centos-target/         # CentOS test target
├── scenarios/                  # Test playbooks
│   ├── 01-basic-installation.yml
│   ├── 02-apache-installation.yml
│   └── 03-validation-security.yml
├── inventories/               # Ansible inventories
│   ├── ubuntu.ini
│   └── centos.ini
├── fixtures/                  # Test data and fixtures
│   ├── mysql/
│   └── wordpress/
├── scripts/                   # Test automation scripts
│   ├── run-all-tests.sh
│   ├── run-single-test.sh
│   ├── analyze-results.sh
│   └── cleanup.sh
└── reports/                   # Test results (generated)
    ├── test_run_*/
    └── *.json, *.log
```

## Test Environment

### Services

The test environment includes:

- **MySQL 8.0** - Primary database
- **MariaDB 10.6** - Alternative database for CentOS tests
- **Redis 7** - Caching service
- **Memcached** - Alternative caching for Apache tests
- **MailHog** - Email testing service
- **Test Runner** - Ansible execution environment
- **Ubuntu Target** - Ubuntu 22.04 test host
- **CentOS Target** - CentOS Stream 9 test host

### Networking

All containers run on an isolated Docker network (`wordpress-test-network`) with:
- Internal DNS resolution
- No external network access for targets (security)
- Exposed ports for development access

### Volumes

- Role source code mounted in test runner
- Persistent MySQL/MariaDB data
- Shared test fixtures and results

## Test Reports

Tests generate comprehensive reports:

### JSON Reports
- Individual test results with timing
- Summary statistics
- Log file references
- Structured data for CI/CD integration

### Log Files
- Complete Ansible output
- Error details and stack traces
- Debug information

### Analysis Tools
- Success/failure summaries
- Performance metrics
- Historical comparisons
- Log excerpt extraction

## Debugging

### Container Access

```bash
# Access test runner container
docker exec -it wp-test-runner bash

# Access Ubuntu test target
docker exec -it wp-test-ubuntu bash

# Access CentOS test target
docker exec -it wp-test-centos bash
```

### Log Examination

```bash
# View container logs
docker logs wp-test-ubuntu
docker logs wp-test-runner

# View test logs
tail -f tests/reports/*/test_run_*.log
```

### Manual Test Execution

```bash
# Run specific tasks manually
docker exec wp-test-runner ansible-playbook -i tests/inventories/ubuntu.ini tests/scenarios/01-basic-installation.yml -v
```

## CI/CD Integration

### GitHub Actions

```yaml
- name: Run WordPress Tests
  run: |
    make test-all
    make analyze --format json > test-results.json

- name: Upload Test Results
  uses: actions/upload-artifact@v3
  with:
    name: test-results
    path: test-results.json
```

### Exit Codes

- `0` - All tests passed
- `1` - Some tests failed
- `2` - Environment setup error

## Troubleshooting

### Common Issues

1. **Docker not running**
   ```bash
   # Start Docker Desktop or service
   systemctl start docker  # Linux
   ```

2. **Port conflicts**
   ```bash
   # Check for conflicting services
   lsof -i :3306 -i :6379 -i :8025
   ```

3. **Insufficient resources**
   - Ensure Docker has adequate CPU/memory
   - Default requirements: 4GB RAM, 2 CPU cores

4. **Permission issues**
   ```bash
   # Fix script permissions
   chmod +x tests/scripts/*.sh
   ```

### Getting Help

1. Check test status: `make test-status`
2. View recent logs: `docker logs wp-test-runner`
3. Run debug analysis: `./tests/scripts/analyze-results.sh --details --logs`
4. Clean and retry: `make clean-test && make test-all`

## Development

### Adding New Tests

1. Create test scenario in `tests/scenarios/`
2. Update inventories if needed
3. Add to test runner script
4. Update documentation

### Modifying Environment

1. Edit `docker-compose.test.yml`
2. Update Docker configurations in `tests/docker/`
3. Rebuild images: `docker-compose -f docker-compose.test.yml build`

### Contributing

1. Follow existing patterns and conventions
2. Test changes across all scenarios
3. Update documentation
4. Ensure cleanup works properly

---

This test automation framework provides comprehensive validation of the WordPress Enterprise Ansible role across multiple operating systems and configurations, ensuring reliable deployments in diverse environments.
