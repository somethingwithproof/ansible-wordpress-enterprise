# Ansible WordPress Enterprise

[![CI](https://github.com/thomasvincent/ansible-wordpress-enterprise/workflows/CI/badge.svg)](https://github.com/thomasvincent/ansible-wordpress-enterprise/actions)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-wordpress__enterprise-blue.svg)](https://galaxy.ansible.com/thomasvincent/wordpress_enterprise)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Ansible](https://img.shields.io/badge/ansible-%3E%3D2.14-blue)](https://docs.ansible.com/)
[![Platform](https://img.shields.io/badge/platform-Ubuntu%20%7C%20RHEL%20%7C%20Rocky-lightgrey)](https://github.com/thomasvincent/ansible-wordpress-enterprise)

🚀 **Production-ready Ansible role for deploying and managing WordPress at scale** - Enterprise-grade WordPress deployment with support for multiple cloud providers, high availability, advanced security, and comprehensive monitoring.

## 📚 Table of Contents

- [Features](#-features)
- [Quick Start](#-quick-start)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Usage Examples](#-usage-examples)
- [Cloud Provider Configurations](#-cloud-provider-configurations)
- [Advanced Configurations](#-advanced-configurations)
- [Security](#-security)
- [Performance Tuning](#-performance-tuning)
- [High Availability](#-high-availability)
- [Monitoring & Logging](#-monitoring--logging)
- [Backup & Recovery](#-backup--recovery)
- [Testing](#-testing)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [Support](#-support)
- [License](#-license)

## 🌟 Features

### Core Capabilities

✅ **Multi-Platform Support**
- Ubuntu 20.04 LTS, 22.04 LTS, 24.04 LTS
- RHEL 9 / Rocky Linux 9 / AlmaLinux 9
- CentOS Stream 9

  Enterprise Linux 8 is not supported: its platform Python is 3.6, below
  ansible-core's floor of 3.9 for a managed node, and no `python39-dnf`
  package exists, so no interpreter satisfies both ansible-core and the
  `dnf` module.
- Debian 11, 12

✅ **Web Server Options**
- **Nginx**: FastCGI cache, HTTP/2, SSL/TLS, rate limiting
- **Apache**: mod_php/PHP-FPM, ModSecurity WAF, HTTP/2

✅ **PHP Support**
- PHP versions: 7.4, 8.0, 8.1, 8.2, 8.3
- OPcache optimization
- PHP-FPM tuning
- Multiple PHP version support

✅ **Database Engines**
- MySQL 8.0+
- MariaDB 10.6+
- Percona Server 8.0+
- External database support (RDS, Cloud SQL, Azure Database)

### Enterprise Features

🏢 **High Availability**
- Load balancer integration (HAProxy, Nginx)
- Database clustering (Galera, Group Replication)
- Shared storage (NFS, GlusterFS, Object Storage)
- Session persistence

🔒 **Security**
- SSL/TLS with Let's Encrypt or custom certificates
- Web Application Firewall (ModSecurity)
- Fail2ban with WordPress-specific rules
- Security headers (HSTS, CSP, X-Frame-Options)
- File integrity monitoring
- Automated security updates
- SELinux/AppArmor support

⚡ **Performance**
- Redis/Memcached object caching
- FastCGI/proxy caching
- CDN integration (Cloudflare, CloudFront, Fastly)
- Image optimization (WebP, AVIF)
- Database query optimization
- HTTP/2 with Server Push
- Brotli compression

📊 **Monitoring & Logging**
- Comprehensive logging (access, error, slow query)
- Health checks and uptime monitoring
- Performance metrics collection
- Log aggregation support
- Alert notifications

### Cloud Provider Support

☁️ **Native Cloud Integration**

| Provider | Features |
|----------|----------|
| **AWS** | EC2, RDS/Aurora, ElastiCache, S3, CloudFront, Route53, SES |
| **Google Cloud** | Compute Engine, Cloud SQL, Memorystore, Cloud Storage, Cloud CDN |
| **Microsoft Azure** | VMs, Azure Database, Azure Cache, Blob Storage, Azure CDN |
| **DigitalOcean** | Droplets, Managed Database, Spaces, CDN |
| **Cloudflare** | DNS, CDN, DDoS Protection, Workers, Page Rules |
| **Oracle Cloud** | Compute, Autonomous Database, Object Storage |

## 🚀 Quick Start

### Basic Installation

```bash
# Install from Ansible Galaxy
ansible-galaxy install thomasvincent.wordpress_enterprise

# Clone from GitHub
git clone https://github.com/thomasvincent/ansible-wordpress-enterprise.git
```

### Minimal Playbook

```yaml
---
- name: Deploy WordPress
  hosts: wordpress_servers
  become: true
  roles:
    - role: thomasvincent.wordpress_enterprise
      vars:
        wordpress_site_url: "https://example.com"
        wordpress_site_title: "My WordPress Site"
        wordpress_admin_user: "admin"
        wordpress_admin_email: "admin@example.com"
```

### Production Deployment

```yaml
---
- name: Production WordPress Deployment
  hosts: wordpress_production
  become: true

  vars_files:
    - vars/production.yml
    - vault/secrets.yml

  roles:
    - role: thomasvincent.wordpress_enterprise
      vars:
        # Basic Configuration
        wordpress_version: "6.4.2"
        wordpress_site_url: "https://{{ ansible_fqdn }}"
        wordpress_site_title: "Enterprise WordPress"
        wordpress_environment: "production"

        # Web Server & PHP
        wordpress_web_server: "nginx"
        wordpress_php_version: "8.2"
        wordpress_php_memory_limit: "512M"

        # Database
        wordpress_db_engine: "mysql"
        wordpress_use_external_db: true
        wordpress_external_db_host: "{{ vault_db_host }}"

        # Caching
        wordpress_enable_redis: true
        wordpress_enable_object_cache: true

        # Security
        wordpress_enable_ssl: true
        wordpress_use_letsencrypt: true
        wordpress_enable_fail2ban: true
        wordpress_configure_firewall: true

        # Performance
        wordpress_enable_cdn: true
        wordpress_cdn_provider: "cloudflare"

        # Monitoring
        wordpress_enable_monitoring: true
        wordpress_enable_backups: true
```

## 📋 Requirements

### System Requirements

- **Control Node**
  - Ansible 2.15 or higher
  - Python 3.8+

- **Target Nodes**
  - Supported OS (see platform support)
  - Python 3.6+
  - Sudo/root access
  - Minimum 2GB RAM
  - 20GB disk space

### Dependencies

**Required Ansible Collections:**

```bash
ansible-galaxy collection install community.general
ansible-galaxy collection install community.mysql
ansible-galaxy collection install ansible.posix
```

**Python Dependencies:**

```bash
pip install -r requirements.txt
```

## 📦 Installation

### Method 1: Ansible Galaxy (Recommended)

```bash
# Install the role
ansible-galaxy install thomasvincent.wordpress_enterprise

# Install with specific version
ansible-galaxy install thomasvincent.wordpress_enterprise,v1.0.0

# Update to latest version
ansible-galaxy install thomasvincent.wordpress_enterprise --force
```

### Method 2: Requirements File

Create `requirements.yml`:

```yaml
---
roles:
  - name: thomasvincent.wordpress_enterprise
    version: v1.0.0

collections:
  - name: community.general
  - name: community.mysql
  - name: ansible.posix
```

Install:

```bash
ansible-galaxy install -r requirements.yml
```

### Method 3: Git Submodule

```bash
# Add as submodule
git submodule add https://github.com/thomasvincent/ansible-wordpress-enterprise.git roles/wordpress_enterprise

# Update submodule
git submodule update --remote roles/wordpress_enterprise
```

## 📖 Usage

### Development Environment

```yaml
---
- name: WordPress Development Environment
  hosts: localhost
  connection: local
  become: true

  roles:
    - role: wordpress_enterprise
      vars:
        wordpress_site_url: "http://localhost:8080"
        wordpress_site_title: "Development Site"
        wordpress_debug: true
        wordpress_debug_log: true
        wordpress_debug_display: true
        wordpress_environment: "development"

        # Use SQLite for development
        wordpress_db_engine: "sqlite"

        # Disable production features
        wordpress_enable_ssl: false
        wordpress_enable_fail2ban: false
        wordpress_configure_firewall: false
        wordpress_enable_backups: false
```

### Staging Environment

```yaml
---
- name: WordPress Staging Deployment
  hosts: staging_servers
  become: true

  vars_files:
    - vars/staging.yml

  roles:
    - role: thomasvincent.wordpress_enterprise
      vars:
        wordpress_environment: "staging"
        wordpress_site_url: "https://staging.example.com"

        # Enable debugging for staging
        wordpress_debug: true
        wordpress_debug_log: true
        wordpress_debug_display: false

        # Use production-like configuration
        wordpress_web_server: "nginx"
        wordpress_php_version: "8.2"
        wordpress_enable_ssl: true
        wordpress_use_letsencrypt: true

        # Basic security
        wordpress_enable_fail2ban: true
        wordpress_configure_firewall: true

        # Enable monitoring
        wordpress_enable_monitoring: true
```

## ☁️ Cloud Provider Configurations

### AWS Configuration

```yaml
---
wordpress_cloud_provider: "aws"

# EC2 Configuration
wordpress_aws_region: "us-east-1"
wordpress_aws_instance_type: "t3.medium"

# RDS Configuration
wordpress_use_external_db: true
wordpress_aws_rds_enabled: true
wordpress_external_db_host: "wordpress.cluster-xxxxx.us-east-1.rds.amazonaws.com"
wordpress_external_db_port: 3306
wordpress_external_db_name: "wordpress_prod"
wordpress_external_db_user: "{{ vault_aws_db_user }}"
wordpress_external_db_password: "{{ vault_aws_db_password }}"
wordpress_external_db_ssl_enabled: true

# ElastiCache Redis
wordpress_use_external_cache: true
wordpress_aws_elasticache_enabled: true
wordpress_redis_host: "wordpress-redis.xxxxx.cache.amazonaws.com"
wordpress_redis_port: 6379

# S3 Media Storage
wordpress_aws_s3_enabled: true
wordpress_aws_s3_bucket: "wordpress-media-prod"
wordpress_aws_s3_region: "us-east-1"
wordpress_aws_s3_access_key: "{{ vault_aws_s3_access_key }}"
wordpress_aws_s3_secret_key: "{{ vault_aws_s3_secret_key }}"

# CloudFront CDN
wordpress_aws_cloudfront_enabled: true
wordpress_aws_cloudfront_distribution_id: "EXXXXXXXXXXXXX"
wordpress_cdn_url: "https://dxxxxx.cloudfront.net"

# SES Email
wordpress_smtp_enabled: true
wordpress_smtp_provider: "ses"
wordpress_smtp_host: "email-smtp.us-east-1.amazonaws.com"
wordpress_smtp_port: 587
wordpress_smtp_user: "{{ vault_aws_ses_user }}"
wordpress_smtp_password: "{{ vault_aws_ses_password }}"
```

### Google Cloud Platform Configuration

```yaml
---
wordpress_cloud_provider: "google"

# GCP Project
wordpress_gcp_project_id: "my-wordpress-project"
wordpress_gcp_region: "us-central1"
wordpress_gcp_zone: "us-central1-a"

# Cloud SQL
wordpress_use_external_db: true
wordpress_gcp_cloudsql_enabled: true
wordpress_gcp_cloudsql_instance: "wordpress-mysql"
wordpress_gcp_cloudsql_tier: "db-n1-standard-2"
wordpress_external_db_host: "127.0.0.1"  # Via Cloud SQL Proxy
wordpress_external_db_port: 3306
wordpress_gcp_cloudsql_proxy_enabled: true

# Memorystore Redis
wordpress_use_external_cache: true
wordpress_gcp_memorystore_enabled: true
wordpress_gcp_memorystore_instance: "wordpress-redis"
wordpress_redis_host: "10.0.0.4"
wordpress_redis_port: 6379

# Cloud Storage
wordpress_gcp_storage_enabled: true
wordpress_gcp_storage_bucket: "wordpress-media-prod"
wordpress_gcp_storage_service_account_key: "{{ vault_gcp_sa_key }}"

# Cloud CDN
wordpress_gcp_cdn_enabled: true
wordpress_cdn_url: "https://cdn.example.com"

# Cloud Load Balancing
wordpress_gcp_load_balancer_enabled: true
wordpress_gcp_backend_service: "wordpress-backend"
```

### Cloudflare Configuration

```yaml
---
wordpress_cloudflare_enabled: true
wordpress_cloudflare_api_token: "{{ vault_cloudflare_api_token }}"
wordpress_cloudflare_zone_id: "{{ vault_cloudflare_zone_id }}"
wordpress_cloudflare_account_id: "{{ vault_cloudflare_account_id }}"

# DNS Management
wordpress_cloudflare_dns_records:
  - name: "{{ wordpress_server_name }}"
    type: "A"
    value: "{{ ansible_default_ipv4.address }}"
    proxied: true
  - name: "www.{{ wordpress_server_name }}"
    type: "CNAME"
    value: "{{ wordpress_server_name }}"
    proxied: true

# Security Settings
wordpress_cloudflare_security_level: "medium"
wordpress_cloudflare_ssl_mode: "full_strict"
wordpress_cloudflare_always_https: true
wordpress_cloudflare_hsts_enabled: true
wordpress_cloudflare_hsts_max_age: 31536000

# Performance
wordpress_cloudflare_cdn_enabled: true
wordpress_cloudflare_cache_level: "standard"
wordpress_cloudflare_browser_cache_ttl: 14400
wordpress_cloudflare_auto_minify:
  js: true
  css: true
  html: true

# Page Rules
wordpress_cloudflare_page_rules:
  - target: "*/wp-admin/*"
    actions:
      cache_level: "bypass"
      security_level: "high"
  - target: "*/wp-login.php"
    actions:
      cache_level: "bypass"
      security_level: "high"

# Workers (Optional)
wordpress_cloudflare_workers_enabled: false
wordpress_cloudflare_workers_route: "*/api/*"
wordpress_cloudflare_workers_script: "wordpress-api-handler"
```

## 🔧 Advanced Configurations

### Multi-Site Network

```yaml
---
wordpress_multisite_enabled: true
wordpress_multisite_type: "subdomain"  # or "subdirectory"
wordpress_multisite_domain: "example.com"

wordpress_multisite_sites:
  - domain: "blog.example.com"
    title: "Company Blog"
    admin_email: "blog@example.com"
  - domain: "shop.example.com"
    title: "Online Store"
    admin_email: "shop@example.com"
```

### Custom PHP Configuration

```yaml
---
# PHP Version Management
wordpress_php_version: "8.2"
wordpress_php_versions_available:
  - "7.4"
  - "8.0"
  - "8.1"
  - "8.2"
  - "8.3"

# PHP-FPM Pool Configuration
wordpress_php_fpm_pm: "dynamic"
wordpress_php_fpm_max_children: 50
wordpress_php_fpm_start_servers: 5
wordpress_php_fpm_min_spare_servers: 5
wordpress_php_fpm_max_spare_servers: 35
wordpress_php_fpm_max_requests: 500

# PHP Settings
wordpress_php_memory_limit: "512M"
wordpress_php_max_execution_time: 300
wordpress_php_max_input_time: 300
wordpress_php_max_input_vars: 5000
wordpress_php_upload_max_filesize: "256M"
wordpress_php_post_max_size: "256M"

# OPcache Settings
wordpress_opcache_enable: true
wordpress_opcache_memory: 256
wordpress_opcache_max_files: 10000
wordpress_opcache_validate_timestamps: 0  # 0 for production
wordpress_opcache_revalidate_freq: 0
```

### Database Optimization

```yaml
---
# MySQL/MariaDB Tuning
wordpress_mysql_innodb_buffer_pool_size: "1G"
wordpress_mysql_innodb_log_file_size: "256M"
wordpress_mysql_innodb_flush_method: "O_DIRECT"
wordpress_mysql_innodb_file_per_table: true
wordpress_mysql_query_cache_size: "128M"
wordpress_mysql_query_cache_type: 1
wordpress_mysql_max_connections: 500
wordpress_mysql_thread_cache_size: 50
wordpress_mysql_table_open_cache: 4000

# Slow Query Logging
wordpress_mysql_slow_query_log: true
wordpress_mysql_slow_query_log_file: "/var/log/mysql/slow-query.log"
wordpress_mysql_long_query_time: 2

# Database Maintenance
wordpress_db_optimize_schedule: "weekly"
wordpress_db_backup_before_optimize: true
```

## 🔒 Security

### Security Hardening Configuration

```yaml
---
# WordPress Security
wordpress_disable_file_edit: true
wordpress_disable_file_mods: false
wordpress_force_ssl_admin: true
wordpress_disable_xmlrpc: true
wordpress_disable_rest_api_public: true

# File Permissions
wordpress_secure_file_permissions: true
wordpress_files_owner: "www-data"
wordpress_files_group: "www-data"
wordpress_files_mode: "0644"
wordpress_dirs_mode: "0755"

# Security Headers
wordpress_security_headers:
  - name: "X-Frame-Options"
    value: "SAMEORIGIN"
  - name: "X-Content-Type-Options"
    value: "nosniff"
  - name: "X-XSS-Protection"
    value: "1; mode=block"
  - name: "Referrer-Policy"
    value: "strict-origin-when-cross-origin"
  - name: "Content-Security-Policy"
    value: "default-src 'self' https: data: 'unsafe-inline' 'unsafe-eval'"

# Fail2ban Configuration
wordpress_fail2ban_enabled: true
wordpress_fail2ban_maxretry: 5
wordpress_fail2ban_findtime: "10m"
wordpress_fail2ban_bantime: "1h"
wordpress_fail2ban_ignoreips:
  - "127.0.0.1/8"
  - "192.168.0.0/16"

# ModSecurity WAF (Apache only)
wordpress_modsecurity_enabled: true
wordpress_modsecurity_ruleset: "OWASP CRS 3.3"
wordpress_modsecurity_custom_rules: []

# File Integrity Monitoring
wordpress_aide_enabled: true
wordpress_aide_email: "security@example.com"
wordpress_aide_schedule: "daily"
```

### SSL/TLS Configuration

```yaml
---
# Certificate Management
wordpress_ssl_provider: "letsencrypt"  # or "custom", "self-signed"
wordpress_ssl_cert_path: "/etc/ssl/certs/{{ wordpress_server_name }}.crt"
wordpress_ssl_key_path: "/etc/ssl/private/{{ wordpress_server_name }}.key"

# Let's Encrypt
wordpress_letsencrypt_email: "{{ wordpress_admin_email }}"
wordpress_letsencrypt_staging: false
wordpress_letsencrypt_webroot: "/var/www/letsencrypt"

# SSL Configuration
wordpress_ssl_protocols: "TLSv1.2 TLSv1.3"
wordpress_ssl_ciphers: >-
  ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:
  ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384
wordpress_ssl_prefer_server_ciphers: true
wordpress_ssl_session_cache: "shared:SSL:50m"
wordpress_ssl_session_timeout: "1d"
wordpress_ssl_stapling: true
wordpress_ssl_stapling_verify: true

# HSTS
wordpress_hsts_enabled: true
wordpress_hsts_max_age: 31536000
wordpress_hsts_include_subdomains: true
wordpress_hsts_preload: true
```

## ⚡ Performance Tuning

### Caching Configuration

```yaml
---
# Object Caching
wordpress_object_cache_provider: "redis"  # or "memcached"
wordpress_redis_maxmemory: "512mb"
wordpress_redis_maxmemory_policy: "allkeys-lru"
wordpress_redis_databases: 16
wordpress_redis_timeout: 5
wordpress_redis_persistent: true

# Page Caching (Nginx)
wordpress_fastcgi_cache_enabled: true
wordpress_fastcgi_cache_size: "256m"
wordpress_fastcgi_cache_inactive: "60m"
wordpress_fastcgi_cache_valid: "60m"
wordpress_fastcgi_cache_methods: ["GET", "HEAD"]
wordpress_fastcgi_cache_bypass_cookies:
  - "wordpress_logged_in_"
  - "wp-postpass_"
  - "wordpress_no_cache"

# Browser Caching
wordpress_browser_cache_enabled: true
wordpress_browser_cache_max_age: 31536000
wordpress_browser_cache_types:
  - "image/jpeg"
  - "image/png"
  - "image/gif"
  - "image/webp"
  - "image/svg+xml"
  - "text/css"
  - "application/javascript"
  - "font/woff2"
```

### CDN Integration

```yaml
---
# CDN Configuration
wordpress_cdn_enabled: true
wordpress_cdn_provider: "cloudflare"  # or "cloudfront", "fastly", "bunnycdn"
wordpress_cdn_url: "https://cdn.example.com"
wordpress_cdn_push_enabled: true

# Asset Optimization
wordpress_cdn_minify_html: true
wordpress_cdn_minify_css: true
wordpress_cdn_minify_js: true
wordpress_cdn_combine_css: false
wordpress_cdn_combine_js: false

# Image Optimization
wordpress_cdn_image_optimization: true
wordpress_cdn_webp_enabled: true
wordpress_cdn_avif_enabled: true
wordpress_cdn_lazy_load: true
wordpress_cdn_responsive_images: true
```

## 🔄 High Availability

### Load Balancer Configuration

```yaml
---
wordpress_ha_enabled: true
wordpress_ha_load_balancer: "haproxy"  # or "nginx"

# Backend Servers
wordpress_ha_backends:
  - name: "web1"
    address: "10.0.1.10:80"
    weight: 1
    max_connections: 100
  - name: "web2"
    address: "10.0.1.11:80"
    weight: 1
    max_connections: 100
  - name: "web3"
    address: "10.0.1.12:80"
    weight: 1
    max_connections: 100

# Health Checks
wordpress_ha_health_check_interval: 2000
wordpress_ha_health_check_timeout: 5000
wordpress_ha_health_check_retries: 3
wordpress_ha_health_check_uri: "/health"

# Session Persistence
wordpress_ha_session_persistence: true
wordpress_ha_session_cookie: "SERVERID"
wordpress_ha_session_storage: "redis"  # Shared session storage
```

### Database Clustering

```yaml
---
# Galera Cluster (MariaDB)
wordpress_db_cluster_enabled: true
wordpress_db_cluster_type: "galera"
wordpress_db_cluster_nodes:
  - host: "db1.example.com"
    port: 3306
  - host: "db2.example.com"
    port: 3306
  - host: "db3.example.com"
    port: 3306

wordpress_db_cluster_sst_method: "rsync"
wordpress_db_cluster_wsrep_provider: "/usr/lib/galera/libgalera_smm.so"

# ProxySQL for connection pooling
wordpress_proxysql_enabled: true
wordpress_proxysql_admin_password: "{{ vault_proxysql_admin_password }}"
wordpress_proxysql_monitor_password: "{{ vault_proxysql_monitor_password }}"
```

## 📊 Monitoring & Logging

### Monitoring Configuration

```yaml
---
# Monitoring Tools
wordpress_monitoring_provider: "prometheus"  # or "datadog", "newrelic"

# Prometheus Exporters
wordpress_prometheus_node_exporter: true
wordpress_prometheus_mysql_exporter: true
wordpress_prometheus_nginx_exporter: true
wordpress_prometheus_php_fpm_exporter: true

# Health Checks
wordpress_health_check_enabled: true
wordpress_health_check_path: "/health"
wordpress_health_check_response: "OK"

# Custom Metrics
wordpress_custom_metrics:
  - name: "wordpress_posts_total"
    query: "SELECT COUNT(*) FROM wp_posts WHERE post_status = 'publish'"
  - name: "wordpress_users_total"
    query: "SELECT COUNT(*) FROM wp_users"
  - name: "wordpress_comments_total"
    query: "SELECT COUNT(*) FROM wp_comments WHERE comment_approved = '1'"
```

### Logging Configuration

```yaml
---
# Log Management
wordpress_log_aggregator: "elasticsearch"  # or "splunk", "cloudwatch"
wordpress_log_level: "info"
wordpress_log_format: "json"

# Log Paths
wordpress_logs_dir: "/var/log/wordpress"
wordpress_access_log: "{{ wordpress_logs_dir }}/access.log"
wordpress_error_log: "{{ wordpress_logs_dir }}/error.log"
wordpress_debug_log: "{{ wordpress_logs_dir }}/debug.log"

# Log Rotation
wordpress_logrotate_enabled: true
wordpress_logrotate_frequency: "daily"
wordpress_logrotate_retention: 30
wordpress_logrotate_compress: true

# Audit Logging
wordpress_audit_log_enabled: true
wordpress_audit_log_events:
  - "user_login"
  - "user_logout"
  - "post_published"
  - "plugin_activated"
  - "theme_changed"
```

## 💾 Backup & Recovery

### Backup Configuration

```yaml
---
# Backup Settings
wordpress_backup_enabled: true
wordpress_backup_dir: "/var/backups/wordpress"
wordpress_backup_retention_days: 30
wordpress_backup_compression: "gzip"

# Backup Schedule
wordpress_backup_schedule:
  - type: "full"
    frequency: "weekly"
    day: "sunday"
    hour: 2
  - type: "incremental"
    frequency: "daily"
    hour: 3

# Backup Destinations
wordpress_backup_destinations:
  - type: "local"
    path: "/var/backups/wordpress"
  - type: "s3"
    bucket: "wordpress-backups"
    region: "us-east-1"
    access_key: "{{ vault_aws_backup_access_key }}"
    secret_key: "{{ vault_aws_backup_secret_key }}"
  - type: "rsync"
    host: "backup.example.com"
    path: "/backups/wordpress"
    ssh_key: "/root/.ssh/backup_rsa"

# Backup Verification
wordpress_backup_verify: true
wordpress_backup_test_restore: true
wordpress_backup_notification_email: "admin@example.com"
```

### Disaster Recovery

```yaml
---
# Disaster Recovery Plan
wordpress_dr_enabled: true
wordpress_dr_site: "dr.example.com"
wordpress_dr_sync_interval: "15m"

# Recovery Time Objective (RTO)
wordpress_dr_rto_hours: 4

# Recovery Point Objective (RPO)
wordpress_dr_rpo_minutes: 15

# Automated Failover
wordpress_dr_auto_failover: false
wordpress_dr_health_check_failures: 3
wordpress_dr_notification_channels:
  - "email:ops@example.com"
  - "slack:#incidents"
  - "pagerduty:service-key"
```

## 🛠️ Troubleshooting

### Common Issues and Solutions

#### Issue: White Screen of Death

```yaml
# Enable WordPress debugging
wordpress_debug: true
wordpress_debug_log: true
wordpress_debug_display: true

# Check PHP errors
wordpress_php_display_errors: true
wordpress_php_error_reporting: "E_ALL"
```

#### Issue: Database Connection Errors

```bash
# Test database connectivity
ansible wordpress_servers -m mysql_info -a "login_host={{ wordpress_db_host }} login_user={{ wordpress_db_user }} login_password={{ wordpress_db_password }}"

# Check database variables
ansible wordpress_servers -m mysql_variables -a "variable=max_connections"
```

#### Issue: Slow Performance

```yaml
# Enable query monitoring
wordpress_mysql_slow_query_log: true
wordpress_mysql_long_query_time: 1

# Enable performance profiling
wordpress_newrelic_enabled: true
wordpress_newrelic_app_name: "WordPress Production"
wordpress_newrelic_license_key: "{{ vault_newrelic_license }}"
```

#### Issue: Plugin Conflicts

```yaml
# Safe mode - disable all plugins
wordpress_safe_mode: true
wordpress_disabled_plugins:
  - "problematic-plugin"
  - "conflicting-plugin"
```

### Debug Commands

```bash
# Check WordPress installation
ansible wordpress_servers -m command -a "wp core verify-checksums --path={{ wordpress_path }}"

# List active plugins
ansible wordpress_servers -m command -a "wp plugin list --status=active --path={{ wordpress_path }}"

# Check database status
ansible wordpress_servers -m command -a "wp db check --path={{ wordpress_path }}"

# Clear cache
ansible wordpress_servers -m command -a "wp cache flush --path={{ wordpress_path }}"

# Run WordPress cron
ansible wordpress_servers -m command -a "wp cron run --path={{ wordpress_path }}"
```

## 📈 Performance Benchmarking

### Load Testing

```yaml
---
# Apache Bench Testing
wordpress_benchmark_ab_requests: 1000
wordpress_benchmark_ab_concurrency: 100

# Siege Testing
wordpress_benchmark_siege_users: 50
wordpress_benchmark_siege_time: "5M"

# Custom Test URLs
wordpress_benchmark_urls:
  - "/"
  - "/shop/"
  - "/blog/"
  - "/api/v1/posts"
```

### Performance Metrics

```yaml
---
# Target Metrics
wordpress_performance_targets:
  page_load_time: 2.0  # seconds
  time_to_first_byte: 0.5  # seconds
  requests_per_second: 100
  concurrent_users: 500
  uptime_percentage: 99.9
```

## 🔌 Plugin Management

### Essential Plugins

```yaml
---
wordpress_plugins:
  # Security
  - name: "wordfence"
    version: "latest"
    activate: true
    config:
      scan_schedule: "daily"
      firewall_mode: "extended"

  # Performance
  - name: "wp-rocket"
    version: "3.15"
    activate: true
    license_key: "{{ vault_wp_rocket_license }}"

  # SEO
  - name: "wordpress-seo"
    version: "latest"
    activate: true
    config:
      enable_xml_sitemap: true
      enable_schema: true

  # Backup
  - name: "updraftplus"
    version: "latest"
    activate: true
    config:
      backup_schedule: "daily"
      remote_storage: "s3"
```

### Theme Management

```yaml
---
wordpress_themes:
  - name: "twentytwentyfour"
    version: "latest"
    activate: false

  - name: "custom-theme"
    source: "https://example.com/themes/custom-theme.zip"
    activate: true

wordpress_child_theme:
  parent: "custom-theme"
  name: "custom-theme-child"
  activate: true
```

## 🧪 Testing

### Molecule Testing

The role includes comprehensive Molecule testing scenarios for multiple platforms:

```bash
# Install testing dependencies
pip install molecule molecule-plugins[docker] ansible-lint yamllint

# Run all tests (default scenario with Ubuntu 22, 24 and Rocky 9)
molecule test

# Run specific scenario
molecule test -s default  # Ubuntu 22, 24 and Rocky Linux 9
molecule test -s ubuntu   # Ubuntu 22.04 and 24.04
molecule test -s debian   # Debian 11 and 12
molecule test -s rhel     # Rocky Linux 9

# Interactive testing
molecule converge          # Deploy the role
molecule verify           # Run verification tests
molecule destroy          # Clean up test environment

# Run idempotency test
molecule test --destroy=never
molecule idempotence
```

#### Test Scenarios

| Scenario | Platforms | Purpose |
|----------|-----------|---------|
| **default** | Ubuntu 22.04, 24.04, Rocky Linux 9 | Quick testing across major platforms |
| **ubuntu** | Ubuntu 22.04, 24.04 | Ubuntu-specific testing |
| **debian** | Debian 11, 12 | Debian-specific testing |
| **rhel** | Rocky Linux 9 | RHEL/CentOS-compatible testing |

All scenarios include:
- ✅ Syntax checking
- ✅ Role deployment
- ✅ Idempotency verification
- ✅ Comprehensive validation tests

📖 **For detailed testing documentation, see [TESTING.md](TESTING.md)**

### Integration Tests

```yaml
---
# Test configuration in tests/integration/playbook.yml
- name: Test WordPress Installation
  hosts: test_servers
  tasks:
    - name: Check WordPress is accessible
      uri:
        url: "https://{{ wordpress_site_url }}"
        status_code: 200

    - name: Verify database connection
      command: wp db check --path={{ wordpress_path }}
      become_user: "{{ wordpress_user }}"

    - name: Test admin login
      uri:
        url: "https://{{ wordpress_site_url }}/wp-login.php"
        method: POST
        body_format: form-urlencoded
        body:
          log: "{{ wordpress_admin_user }}"
          pwd: "{{ wordpress_admin_password }}"
        status_code: 302
```

## 🛠️ Development

### Development Setup

```bash
# Fork and clone the repository
git clone https://github.com/YOUR_USERNAME/ansible-wordpress-enterprise.git
cd ansible-wordpress-enterprise

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install development dependencies
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install

# Run tests
molecule test

# Run linters
ansible-lint
yamllint .
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Support

- **Documentation**: [Wiki](https://github.com/thomasvincent/ansible-wordpress-enterprise/wiki)
- **Issues**: [GitHub Issues](https://github.com/thomasvincent/ansible-wordpress-enterprise/issues)
- **Discussions**: [GitHub Discussions](https://github.com/thomasvincent/ansible-wordpress-enterprise/discussions)
- **Security**: Report security vulnerabilities to security@example.com

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Thomas Vincent**
- GitHub: [@thomasvincent](https://github.com/thomasvincent)
- Email: thomasvincent@users.noreply.github.com

## 🙏 Acknowledgments

- WordPress Community
- Ansible Community
- Cloud Provider Documentation Teams
- All contributors to this project

## 📊 Stats

![GitHub stars](https://img.shields.io/github/stars/thomasvincent/ansible-wordpress-enterprise?style=social)
![GitHub forks](https://img.shields.io/github/forks/thomasvincent/ansible-wordpress-enterprise?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/thomasvincent/ansible-wordpress-enterprise?style=social)

---

**Made with ❤️ by the open source community**

⭐ Star this project if you find it helpful!
