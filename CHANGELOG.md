<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

# Changelog

## 2.22.0 — 2026-10-06

Verified certificate preparation, real HTTPS contracts and SemVer role archives/DEB/RPM releases.

Documentation includes migration, installation, release checks, SVG project branding and operational diagrams.

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- The role now fails closed before package changes unless the managed node is
  Ubuntu 24.04 LTS or Enterprise Linux 9 (Red Hat, Rocky, or AlmaLinux). Debian,
  CentOS, EL8, other Ubuntu releases, and unlisted distributions are no longer
  accepted.
- PHP 8.3 is now the only supported branch because it is available and tested
  on every supported platform. PHP 7.4, 8.0, and 8.1 are rejected because
  upstream security support ended; 8.2 and 8.4 are rejected because Ubuntu
  24.04 cannot install them from its standard archive.
- The default PHP branch changes from 8.2 to 8.3. Existing deployments must
  plan this runtime migration; the role does not remove an older versioned
  PHP-FPM installation automatically.
- `ansible-core` is constrained to the maintained 2.21 release line. These
  platform and runtime removals are breaking changes and require the next major
  role release. `meta/platform_support.yml` is the authoritative lifecycle
  policy.

### Added
- Comprehensive enterprise-grade WordPress deployment role
- Multi-cloud provider support (AWS, GCP, Azure, DigitalOcean, Oracle Cloud)
- Cloudflare integration for CDN and security
- High availability configurations
- Advanced security features
- Performance optimization
- Monitoring and logging
- Backup and disaster recovery

## [1.0.0] - 2025-01-24

### Added

#### Core Features
- Multi-platform support (Ubuntu, RHEL, Rocky, Debian, CentOS)
- Web server options (Nginx with FastCGI, Apache with mod_php/PHP-FPM)
- PHP support (7.4, 8.0, 8.1, 8.2, 8.3)
- Database engines (MySQL 8.0+, MariaDB 10.6+, Percona Server 8.0+)
- External database support (AWS RDS, GCP Cloud SQL, Azure Database)

#### Enterprise Features
- High availability with load balancer integration
- Database clustering (Galera, Group Replication)
- Shared storage support (NFS, GlusterFS, Object Storage)
- Session persistence
- SSL/TLS with Let's Encrypt or custom certificates
- Web Application Firewall (ModSecurity)
- Fail2ban with WordPress-specific rules
- Security headers (HSTS, CSP, X-Frame-Options)
- File integrity monitoring
- Automated security updates
- SELinux/AppArmor support

#### Performance
- Redis/Memcached object caching
- FastCGI/proxy caching
- CDN integration (Cloudflare, CloudFront, Fastly)
- Image optimization (WebP, AVIF)
- Database query optimization
- HTTP/2 with Server Push
- Brotli compression

#### Monitoring & Logging
- Comprehensive logging (access, error, slow query)
- Health checks and uptime monitoring
- Performance metrics collection
- Log aggregation support
- Alert notifications

#### Cloud Provider Integration
- **AWS**: EC2, RDS/Aurora, ElastiCache, S3, CloudFront, Route53, SES
- **Google Cloud**: Compute Engine, Cloud SQL, Memorystore, Cloud Storage, Cloud CDN
- **Microsoft Azure**: VMs, Azure Database, Azure Cache, Blob Storage, Azure CDN
- **DigitalOcean**: Droplets, Managed Database, Spaces, CDN
- **Cloudflare**: DNS, CDN, DDoS Protection, Workers, Page Rules
- **Oracle Cloud**: Compute, Autonomous Database, Object Storage

#### Example Configurations
- `examples/aws-compatible.yml` - AWS deployment
- `examples/google-cloud-platform.yml` - GCP deployment
- `examples/microsoft-azure.yml` - Azure deployment
- `examples/cloudflare-only.yml` - Cloudflare integration
- `examples/oracle-cloud.yml` - Oracle Cloud deployment
- `examples/multi-cloud-ha.yml` - Multi-cloud HA setup
- `examples/production-wordpress.yml` - Production configuration
- `examples/local-development.yml` - Local development setup

#### Testing
- Molecule testing framework
- Docker-based testing
- Pre-commit hooks
- ansible-lint configuration
- yamllint configuration
- CI/CD pipeline with GitHub Actions

#### Documentation
- Comprehensive README (1165+ lines)
- Cloud provider configuration guides
- Security hardening documentation
- Performance tuning guides
- High availability setup
- Monitoring and logging setup
- Backup and disaster recovery procedures
- Troubleshooting guide
- Contributing guidelines
- Security policy

#### Tasks
- `tasks/prerequisites.yml` - System prerequisites
- `tasks/repositories.yml` - Package repositories
- `tasks/php.yml` - PHP installation and configuration
- `tasks/webserver_nginx.yml` - Nginx configuration
- `tasks/webserver_apache.yml` - Apache configuration
- `tasks/database.yml` - Database setup
- `tasks/wordpress_install.yml` - WordPress installation
- `tasks/wordpress_configure.yml` - WordPress configuration
- `tasks/plugins.yml` - Plugin management
- `tasks/themes.yml` - Theme management
- `tasks/caching.yml` - Caching configuration
- `tasks/ssl.yml` - SSL/TLS setup
- `tasks/security.yml` - Security hardening
- `tasks/firewall.yml` - Firewall configuration
- `tasks/fail2ban.yml` - Fail2ban setup
- `tasks/monitoring.yml` - Monitoring setup
- `tasks/backups.yml` - Backup configuration
- `tasks/validate.yml` - Configuration validation
- `tasks/verify.yml` - Installation verification

#### Variables
- 200+ configurable variables
- OS-specific variables (Debian, RedHat)
- Comprehensive defaults in `defaults/main.yml`
- Ansible Vault integration for secrets

### Infrastructure as Code
- Docker Compose configuration for development
- Molecule scenarios for testing
- Pre-commit hooks for code quality
- GitHub Actions CI workflow

### Security
- Security policy documented in SECURITY.md
- Secrets management guidelines
- SSL/TLS best practices
- Database security configuration
- WordPress security hardening
- File permission management
- Fail2ban configuration
- ModSecurity WAF rules

### Quality Assurance
- Comprehensive linting (ansible-lint, yamllint)
- Automated testing with Molecule
- Multi-platform testing
- CI/CD integration
- Code review process

[Unreleased]: https://github.com/somethingwithproof/ansible-wordpress-enterprise/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/somethingwithproof/ansible-wordpress-enterprise/releases/tag/v1.0.0
