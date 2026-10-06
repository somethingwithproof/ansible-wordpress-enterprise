<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

# Contributing to WordPress Enterprise Ansible Role

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Contribute](#how-to-contribute)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

This project follows the [Ansible Community Code of Conduct](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html). By participating, you are expected to uphold this code.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/ansible-wordpress-enterprise.git
   cd ansible-wordpress-enterprise
   ```

3. **Add upstream remote**:
   ```bash
   git remote add upstream https://github.com/somethingwithproof/ansible-wordpress-enterprise.git
   ```

4. **Create a branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Setup

### Prerequisites

- Maintained Python 3.12–3.14
- Docker and Docker Compose
- ansible-core 2.21
- Make (optional, for using Makefile commands)

### Quick Setup

```bash
# Install dependencies
make install
make galaxy-install

# Or manually:
pip install -r requirements.txt
ansible-galaxy collection install -r requirements.yml
```

### Docker Development Environment

```bash
# Start development environment
make docker-dev

# Access services:
# - WordPress: http://localhost:8080
# - MySQL: localhost:3307
# - Redis: localhost:6380
# - MailHog: http://localhost:8025

# Access container shell
make shell

# View logs
make logs

# Stop environment
make stop
```

## How to Contribute

### Reporting Bugs

Before creating bug reports, please check existing issues. When creating a bug report, include:

- **Clear title** and description
- **Steps to reproduce** the problem
- **Expected behavior**
- **Actual behavior**
- **Environment details** (OS, Ansible version, etc.)
- **Relevant logs** or error messages

### Suggesting Enhancements

Enhancement suggestions are welcome! Please include:

- **Clear use case** for the enhancement
- **Proposed solution** or implementation approach
- **Alternative approaches** you've considered
- **Impact** on existing functionality

### Adding Cloud Provider Support

To add a new cloud provider:

1. Update `defaults/main.yml` with provider-specific variables
2. Create provider-specific tasks (if needed)
3. Update templates to support the provider
4. Add example playbook in `examples/`
5. Update documentation
6. Add tests

## Coding Standards

### Ansible Best Practices

- **Variable naming**: Use `wordpress_` prefix for all variables
- **Task names**: Clear, descriptive, starting with a verb
- **Idempotency**: All tasks must be idempotent
- **Tags**: Add appropriate tags to tasks
- **Handlers**: Use handlers for service restarts
- **Documentation**: Add comments for complex logic

### YAML Style

```yaml
---
# Use 2-space indentation
- name: Example task with proper formatting
  ansible.builtin.package:
    name: "{{ item }}"
    state: present
  loop:
    - package1
    - package2
  when: condition_is_true
  tags:
    - wordpress
    - wordpress:packages
```

### File Structure

```
tasks/
  ├── main.yml           # Main orchestration
  ├── validate.yml       # Input validation
  ├── feature.yml        # Feature-specific tasks
  └── ...

templates/
  ├── config.j2          # Jinja2 templates
  └── ...

vars/
  ├── RedHat.yml         # OS-specific variables
  └── Debian.yml
```

### Variable Organization

Group variables by functionality in `defaults/main.yml`:

```yaml
# ============================================================================
# Section Title
# ============================================================================
wordpress_feature_enabled: true
wordpress_feature_option: "value"
```

## Testing

### Linting

```bash
# Run all linters
make lint

# Or individually:
yamllint .
ansible-lint
```

### Molecule Tests

```bash
# Run all tests
make test

# Run the stable Ubuntu 24/Nginx and Rocky 9/Apache contract
mise exec python@3.12 -- molecule test --scenario-name default
```

### Docker Tests

```bash
# Build test images
make docker-build

# Run tests in Docker
make docker-test
```

### Manual Testing

```bash
# Start dev environment
make docker-dev

# Run playbook
ansible-playbook examples/local-development.yml
```

## Pull Request Process

### Before Submitting

1. **Update documentation** for any changed functionality
2. **Add tests** for new features
3. **Run linters**: `make lint`
4. **Run tests**: `make test`
5. **Update CHANGELOG.md** if applicable
6. **Squash commits** if necessary

### PR Requirements

- [ ] Code follows project style guidelines
- [ ] All tests pass
- [ ] Documentation is updated
- [ ] Changelog is updated (if applicable)
- [ ] Commit messages are clear and descriptive

### PR Title Format

```
type(scope): brief description

Types:
  feat:     New feature
  fix:      Bug fix
  docs:     Documentation changes
  style:    Code style changes
  refactor: Code refactoring
  test:     Test additions/changes
  chore:    Build/tooling changes

Examples:
  feat(plugins): add WooCommerce support
  fix(database): resolve connection timeout issue
  docs(examples): add Azure deployment guide
```

### PR Description Template

```markdown
## Description
Brief description of changes

## Motivation
Why this change is needed

## Changes
- Change 1
- Change 2

## Testing
How the changes were tested

## Checklist
- [ ] Tests pass
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] No breaking changes (or documented)
```

### Review Process

1. **Automated checks** must pass (CI/CD)
2. **Code review** by maintainer(s)
3. **Testing** in various scenarios
4. **Approval** and merge

## Commit Message Guidelines

### Format

```
type(scope): subject

body (optional)

footer (optional)
```

### Examples

```
feat(cloudflare): add support for cache purging

Implement automatic cache purging when WordPress content
is updated or published.

Closes #123
```

```
fix(database): resolve SSL connection issue

Update database connection to properly handle SSL certificates
for external database providers.

Fixes #456
```

## Development Workflow

### Adding a New Feature

1. **Create issue** describing the feature
2. **Discuss approach** with maintainers (if major)
3. **Create branch**: `git checkout -b feat/feature-name`
4. **Implement feature** with tests
5. **Update documentation**
6. **Submit PR**

### Fixing a Bug

1. **Create issue** (if not exists)
2. **Create branch**: `git checkout -b fix/bug-description`
3. **Fix bug** and add test
4. **Verify fix** doesn't break existing functionality
5. **Submit PR** with reference to issue

### Updating Documentation

1. **Create branch**: `git checkout -b docs/what-you-update`
2. **Make changes**
3. **Preview locally** (if applicable)
4. **Submit PR**

## Release Process

Releases are automated via GitHub Actions when changes are merged to `main`:

1. Version in `meta/main.yml` is checked
2. If version is new, a GitHub release is created
3. Role is published to Ansible Galaxy

## Getting Help

- **GitHub Issues**: https://github.com/somethingwithproof/ansible-wordpress-enterprise/issues
- **Discussions**: https://github.com/somethingwithproof/ansible-wordpress-enterprise/discussions
- **Documentation**: [README.md](README.md)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to WordPress Enterprise Ansible Role! 🎉
