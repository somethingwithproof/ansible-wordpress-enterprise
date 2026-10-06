<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

# WordPress Enterprise Role - Example Configurations

> Release contract: Ubuntu 24.04/Nginx and EL9/Apache with PHP 8.3, plus verified
> certificate provisioning and HTTPS. Only vendor-maintained platforms are supported.
> Backup, monitoring, HA, advanced-security, CDN and object-storage template sets
> remain incomplete and fail closed when enabled. Examples for those features are
> design references, not executable release guarantees. See [../README.md](../README.md)
> and the missing-template inventory before enabling optional features.

This directory contains comprehensive example playbooks demonstrating various deployment scenarios for the WordPress Enterprise Ansible role.

## 📁 Available Examples

### Single Cloud Provider Examples

#### 1. **cloudflare-only.yml**
Uses Cloudflare for DNS, CDN, and DDoS protection with local infrastructure.

**Features:**
- Cloudflare DNS management
- Cloudflare CDN with cache purging
- Local MariaDB database
- Local Redis cache
- Let's Encrypt SSL
- Perfect for: Small to medium sites wanting Cloudflare's edge network

**Quick Start:**
```bash
ansible-playbook examples/cloudflare-only.yml --ask-vault-pass
```

---

#### 2. **digitalocean-full.yml**
Complete DigitalOcean stack using all managed services.

**Features:**
- DO Managed MySQL Database (with SSL)
- DO Managed Redis
- DO Spaces (S3-compatible object storage)
- DO CDN
- SendGrid email integration
- Perfect for: All-in-one DigitalOcean infrastructure

**Quick Start:**
```bash
ansible-playbook examples/digitalocean-full.yml --ask-vault-pass
```

---

#### 3. **google-cloud-platform.yml**
Google Cloud Platform full stack deployment.

**Features:**
- Cloud SQL (Managed MySQL) with Cloud SQL Proxy
- Memorystore (Managed Redis)
- Cloud Storage
- Cloud CDN
- Stackdriver monitoring
- Perfect for: GCP-native deployments

**Quick Start:**
```bash
ansible-playbook examples/google-cloud-platform.yml --ask-vault-pass
```

---

#### 4. **microsoft-azure.yml**
Microsoft Azure complete deployment.

**Features:**
- Azure Database for MySQL
- Azure Cache for Redis (SSL enabled)
- Azure Blob Storage
- Azure CDN
- SendGrid (Azure Marketplace)
- Azure Monitor integration
- Perfect for: Azure-centric infrastructure

**Quick Start:**
```bash
ansible-playbook examples/microsoft-azure.yml --ask-vault-pass
```

---

#### 5. **oracle-cloud.yml**
Oracle Cloud Infrastructure deployment.

**Features:**
- OCI Compute Instance provisioning (VM.Standard.E4.Flex)
- OCI Autonomous Database (MySQL)
- OCI Block Storage for persistent data
- OCI Load Balancer integration (Flexible shape)
- OCI Object Storage for media and backups
- OCI Free Tier optimization
- PAUSATF WordPress deployment support
- Perfect for: OCI infrastructure and Always Free tier

**Quick Start:**
```bash
ansible-playbook examples/oracle-cloud.yml --ask-vault-pass
```

**OCI-Specific Configuration:**
- Compartment-based resource isolation
- Flexible compute shapes (2 OCPUs, 16GB RAM)
- Block volume backup policies (bronze, silver, gold)
- Load balancer health checks and SSL termination
- Object storage for WordPress media and automated backups

---

#### 6. **aws-compatible.yml**
AWS-compatible services deployment.

**Features:**
- AWS RDS/Aurora Database
- ElastiCache Redis
- S3 Object Storage
- CloudFront CDN
- Amazon SES email
- CloudWatch monitoring
- Perfect for: AWS infrastructure

**Quick Start:**
```bash
ansible-playbook examples/aws-compatible.yml --ask-vault-pass
```

---

### Hybrid/Multi-Cloud Examples

#### 7. **hybrid-cloudflare-digitalocean.yml**
Best of both worlds: Cloudflare edge + DigitalOcean infrastructure.

**Features:**
- Cloudflare for DNS, CDN, DDoS protection, WAF
- DO Managed Database (MySQL)
- DO Managed Redis
- DO Spaces for media storage
- SendGrid email
- Multi-layered security
- **Perfect for: Cost-effective high-performance setup**

**Architecture:**
```
Internet → Cloudflare Edge → DigitalOcean Droplet
                                    ├── DO Managed MySQL
                                    ├── DO Managed Redis
                                    └── DO Spaces (via CDN)
```

**Quick Start:**
```bash
ansible-playbook examples/hybrid-cloudflare-digitalocean.yml --ask-vault-pass
```

**Benefits:**
- Cloudflare's global CDN (300+ cities)
- DDoS protection and WAF
- DigitalOcean's cost-effective managed services
- Excellent performance/cost ratio

---

#### 8. **multi-cloud-ha.yml**
Enterprise-grade high availability across multiple cloud providers.

**Features:**
- Active-active multi-region deployment
- Cloudflare Global Load Balancer
- 3+ web nodes across regions/providers
- Google Cloud SQL with read replicas
- Redis Sentinel for cache failover
- Multi-destination backups (Spaces, GCS, S3)
- Email failover (SendGrid → SES)
- 99.99% uptime target
- **Perfect for: Mission-critical applications**

**Architecture:**
```
                    Cloudflare Global Load Balancer
                              ↓
         ┌────────────────────┼────────────────────┐
         ↓                    ↓                    ↓
    Web1 (US-East)      Web2 (US-West)      Web3 (EU)
    DigitalOcean        DigitalOcean        Google Cloud
         └──────────────────┬─────────────────────┘
                            ↓
                  Google Cloud SQL (Primary)
                  ├── Read Replica (US)
                  └── Read Replica (EU)
                            ↓
                  Redis Sentinel Cluster
                            ↓
              Object Storage (Multi-provider)
```

**Quick Start:**
```bash
ansible-playbook examples/multi-cloud-ha.yml --ask-vault-pass
```

**Benefits:**
- Geographic redundancy
- Provider redundancy
- Automatic failover
- 99.99% uptime SLA

---

### Development/Testing

#### 9. **local-development.yml**
Local development environment setup.

**Features:**
- Local database (MariaDB)
- Local Redis
- Self-signed SSL certificate
- Debug mode enabled
- MailHog for email testing
- Development plugins (Query Monitor, Debug Bar)
- No security restrictions
- Perfect for: Local development and testing

**Quick Start:**
```bash
ansible-playbook examples/local-development.yml
```

**Post-Setup:**
- Add `127.0.0.1 wordpress.local` to `/etc/hosts`
- Install MailHog for email testing: `brew install mailhog`
- Access site: https://wordpress.local
- Admin panel: https://wordpress.local/wp-admin
- Email viewer: http://localhost:8025

---

#### 10. **production-wordpress.yml**
Complete production deployment (reference from main examples).

**Features:**
- All production best practices
- Cloudflare + DigitalOcean
- Complete security hardening
- Comprehensive monitoring
- Multi-destination backups
- Perfect for: Production reference

---

## 🚀 Quick Deployment Guide

### Prerequisites

1. **Install Ansible**
   ```bash
   pip install ansible
   ```

2. **Install Required Collections**
   ```bash
   ansible-galaxy collection install community.general
   ansible-galaxy collection install community.mysql
   ansible-galaxy collection install ansible.posix
   ```

3. **Install the Role**
   ```bash
   ansible-galaxy install thomasvincent.wordpress_enterprise
   ```

### Create Ansible Vault

Create `vault.yml` in the examples directory:

```bash
ansible-vault create vault.yml
```

Add your secrets:

```yaml
---
# WordPress
vault_wp_admin_user: "admin"
vault_wp_admin_password: "strong-password-here"
vault_wp_db_password: "database-password"

# Cloudflare
vault_cloudflare_api_token: "your-api-token"
vault_cloudflare_zone_id: "your-zone-id"

# DigitalOcean
vault_do_token: "your-do-token"
vault_do_db_host: "your-db-host.db.ondigitalocean.com"
vault_do_db_user: "doadmin"
vault_do_db_password: "your-db-password"
vault_do_redis_host: "your-redis.db.ondigitalocean.com"
vault_do_redis_password: "your-redis-password"
vault_do_spaces_key: "your-spaces-key"
vault_do_spaces_secret: "your-spaces-secret"

# SendGrid
vault_sendgrid_api_key: "your-sendgrid-api-key"

# Add other cloud provider credentials as needed
```

### Deploy

```bash
# Deploy with vault password prompt
ansible-playbook examples/hybrid-cloudflare-digitalocean.yml --ask-vault-pass

# Deploy with vault password file
ansible-playbook examples/hybrid-cloudflare-digitalocean.yml --vault-password-file ~/.vault-pass

# Deploy to specific host
ansible-playbook -i inventory.ini examples/digitalocean-full.yml --ask-vault-pass

# Deploy with tags (only specific tasks)
ansible-playbook examples/production-wordpress.yml --tags wordpress:plugins --ask-vault-pass
```

## 📊 Comparison Matrix

| Feature | Cloudflare Only | DO Full | GCP | Azure | Hybrid CF+DO | Multi-Cloud HA |
|---------|----------------|---------|-----|-------|--------------|----------------|
| **Cost** | 💰 Low | 💰💰 Medium | 💰💰💰 High | 💰💰💰 High | 💰💰 Medium | 💰💰💰💰 Very High |
| **Performance** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Complexity** | Simple | Simple | Medium | Medium | Medium | Complex |
| **HA Support** | ❌ | ❌ | ✅ | ✅ | ⚠️ Limited | ✅ Full |
| **Global CDN** | ✅ | ⚠️ Limited | ✅ | ✅ | ✅ | ✅ |
| **Managed DB** | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Managed Cache** | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Best For** | Small sites | Medium sites | Enterprise | Enterprise | Production | Mission-critical |

## 🎯 Recommendation by Use Case

### Small Business Website (< 10k visitors/month)
→ **cloudflare-only.yml** or **digitalocean-full.yml**
- Cost-effective
- Easy to manage
- Cloudflare free tier available

### Medium Business Website (10k - 100k visitors/month)
→ **hybrid-cloudflare-digitalocean.yml**
- Best performance/cost ratio
- Global CDN
- Managed services
- Excellent security

### Large Business / Enterprise (100k+ visitors/month)
→ **google-cloud-platform.yml** or **microsoft-azure.yml**
- Enterprise SLAs
- Advanced features
- Compliance certifications
- Full cloud ecosystem

### Mission-Critical Application (99.99% uptime required)
→ **multi-cloud-ha.yml**
- Multi-region redundancy
- Provider redundancy
- Automatic failover
- 99.99% uptime SLA

### E-commerce Site
→ **hybrid-cloudflare-digitalocean.yml** or **google-cloud-platform.yml**
- PCI compliance support
- DDoS protection
- High performance
- Secure transactions

### Development/Staging
→ **local-development.yml**
- Quick setup
- Debug tools
- No cloud costs
- Easy testing

## 🔧 Customization

All examples can be customized by:

1. **Modifying Variables**
   ```yaml
   wordpress_php_version: "8.3"  # Use PHP 8.3
   wordpress_php_memory_limit: "1024M"  # Increase memory
   ```

2. **Adding Plugins**
   ```yaml
   wordpress_plugins:
     - name: "woocommerce"
       version: "latest"
       state: "present"
   ```

3. **Changing Themes**
   ```yaml
   wordpress_themes:
     - name: "your-theme"
       version: "1.0.0"
       state: "present"
       activate: true
   ```

4. **Adding Custom Configurations**
   ```yaml
   wordpress_additional_constants:
     MY_CUSTOM_CONSTANT: "value"
   ```

## 📖 Further Reading

- [Main README](../README.md) - Complete documentation
- [Ansible Best Practices](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html)
- [WordPress Codex](https://codex.wordpress.org/)
- [Cloud Provider Documentation](#)

## 💡 Tips

1. **Always use Ansible Vault** for sensitive data
2. **Test in staging** before production deployment
3. **Pin versions** in production (`wordpress_version: "6.4.2"`)
4. **Enable backups** for production sites
5. **Monitor** your sites with health checks
6. **Update regularly** but test first

## 🆘 Troubleshooting

### Common Issues

**Issue**: Vault password error
```bash
# Solution: Verify vault password file or use --ask-vault-pass
ansible-playbook playbook.yml --ask-vault-pass
```

**Issue**: Connection timeout
```bash
# Solution: Check SSH connectivity
ansible all -m ping
```

**Issue**: Database connection failed
```bash
# Solution: Verify database credentials in vault.yml
# Check external_db_host and firewall rules
```

## 📞 Support

- GitHub Issues: https://github.com/somethingwithproof/ansible-wordpress-enterprise/issues
- Documentation: https://github.com/somethingwithproof/ansible-wordpress-enterprise

## 📄 License

MIT License
