<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

# Oracle Cloud Infrastructure (OCI) Deployment Guide

> Release contract: Ubuntu 24.04/Nginx and EL9/Apache with PHP 8.3, plus verified
> certificate provisioning and HTTPS. Only vendor-maintained platforms are supported.
> Backup, monitoring, HA, advanced-security, CDN and object-storage template sets
> remain incomplete and fail closed when enabled. Examples for those features are
> design references, not executable release guarantees. See [../README.md](../README.md)
> and the missing-template inventory before enabling optional features.

## Overview

This guide provides comprehensive instructions for deploying WordPress on Oracle Cloud Infrastructure (OCI) using the ansible-wordpress-enterprise role. The deployment is optimized for OCI Free Tier resources and supports PAUSATF WordPress hosting requirements.

## Features

### OCI Compute Instance Provisioning
- Flexible compute shapes (VM.Standard.E4.Flex)
- Configurable OCPUs and memory
- Automated instance provisioning
- Support for multiple availability domains

### OCI Block Storage
- Persistent data storage for WordPress
- Configurable volume sizes (100GB default)
- Multiple performance tiers:
  - Balanced (default)
  - Higher Performance
  - Ultra High Performance
- Automated backup policies (bronze, silver, gold)

### OCI Load Balancer Integration
- Flexible load balancer shapes
- Configurable bandwidth (10-100 Mbps)
- Health check configuration
- SSL/TLS termination support
- Backend set policies:
  - ROUND_ROBIN (default)
  - LEAST_CONNECTIONS
  - IP_HASH

### OCI Object Storage
- Media file storage (wp-content/uploads)
- Automated backup storage
- Standard and Archive storage tiers
- Integration with WordPress media library

### OCI Autonomous Database
- Managed MySQL database service
- SSL/TLS encrypted connections
- Automated backups and patching
- High availability and scalability

## Prerequisites

### OCI Account Setup
1. Oracle Cloud account with appropriate permissions
2. Compartment created for WordPress resources
3. Virtual Cloud Network (VCN) configured
4. Subnet with internet access
5. Security lists/Network Security Groups configured

### Required OCI Resources
- Compartment OCID
- VCN and Subnet OCIDs
- Availability Domain identifier
- API signing key pair generated

### Local Requirements
- ansible-core 2.21 (use the hashed requirements.lock)
- Python 3.12 or higher (maintained releases only)
- OCI CLI configured (optional but recommended)
- OCI Python SDK (for advanced features)

## Configuration

### 1. OCI API Keys

Generate an API signing key pair:

```bash
mkdir -p ~/.oci
openssl genrsa -out ~/.oci/oci_api_key.pem 2048
chmod 600 ~/.oci/oci_api_key.pem
openssl rsa -pubout -in ~/.oci/oci_api_key.pem -out ~/.oci/oci_api_key_public.pem
```

Add the public key to your OCI user account:
1. Log in to OCI Console
2. Navigate to User Settings
3. Click "API Keys" → "Add API Key"
4. Upload `oci_api_key_public.pem`
5. Note the fingerprint displayed

### 2. Inventory Configuration

Create an inventory file using the template at `tests/inventories/oci.ini`:

```ini
[wordpress_servers]
oci-wp-web1 ansible_host=10.0.1.10 ansible_user=opc ansible_ssh_private_key_file=~/.ssh/oci_key

[wordpress_servers:vars]
ansible_python_interpreter=/usr/bin/python3
oci_compartment_id=ocid1.compartment.oc1..your-compartment-id
oci_availability_domain=AD-1
oci_subnet_id=ocid1.subnet.oc1.your-region.your-subnet-id
oci_shape=VM.Standard.E4.Flex
oci_ocpus=2
oci_memory_gb=16
```

### 3. Ansible Vault Configuration

Create a vault file with your OCI credentials:

```bash
ansible-vault create vault.yml
```

Add the following content:

```yaml
---
# WordPress Credentials
vault_wp_admin_user: "admin"
vault_wp_admin_password: "your-strong-password"
vault_wp_db_password: "your-db-password"

# OCI Authentication
vault_oci_tenancy: "ocid1.tenancy.oc1..your-tenancy-id"
vault_oci_user: "ocid1.user.oc1..your-user-id"
vault_oci_fingerprint: "aa:bb:cc:dd:ee:ff:gg:hh:ii:jj:kk:ll:mm:nn:oo:pp"
vault_oci_region: "us-ashburn-1"
vault_oci_namespace: "your-namespace"

# OCI Compute
vault_oci_compartment_id: "ocid1.compartment.oc1..your-compartment-id"
vault_oci_availability_domain: "AD-1"
vault_oci_subnet_id: "ocid1.subnet.oc1.region.your-subnet-id"

# OCI Database
vault_oci_db_host: "your-db.sub.region.oraclevcn.com"
vault_oci_db_user: "ADMIN"
vault_oci_db_password: "your-database-password"

# OCI Load Balancer
vault_oci_lb_id: "ocid1.loadbalancer.oc1.region.your-lb-id"

# OCI Object Storage
vault_oci_bucket_name: "wordpress-media"
vault_oci_backup_bucket_name: "wordpress-backups"

# SendGrid (for email)
vault_sendgrid_api_key: "SG.your-sendgrid-api-key"
```

### 4. Playbook Configuration

Use the `examples/oracle-cloud.yml` playbook or create your own:

```yaml
---
- name: Deploy WordPress on Oracle Cloud Infrastructure
  hosts: wordpress_servers
  become: true
  gather_facts: true

  vars_files:
    - vault.yml

  vars:
    # WordPress Core
    wordpress_version: "6.4.2"
    wordpress_site_url: "https://blog.example.com"
    wordpress_site_title: "OCI-Powered WordPress"

    # OCI Configuration
    wordpress_cloud_provider: "oracle"
    wordpress_oci_enabled: true
    wordpress_oci_tenancy: "{{ vault_oci_tenancy }}"
    wordpress_oci_user: "{{ vault_oci_user }}"
    wordpress_oci_fingerprint: "{{ vault_oci_fingerprint }}"
    wordpress_oci_region: "us-ashburn-1"

    # OCI Compute
    wordpress_oci_compartment_id: "{{ vault_oci_compartment_id }}"
    wordpress_oci_shape: "VM.Standard.E4.Flex"
    wordpress_oci_ocpus: 2
    wordpress_oci_memory_gb: 16

    # OCI Block Storage
    wordpress_oci_block_storage_enabled: true
    wordpress_oci_block_volume_size_gb: 100
    wordpress_oci_block_volume_performance: "Balanced"

    # OCI Load Balancer
    wordpress_oci_load_balancer_enabled: true
    wordpress_oci_lb_shape: "flexible"
    wordpress_oci_lb_min_bandwidth_mbps: 10
    wordpress_oci_lb_max_bandwidth_mbps: 100

    # OCI Object Storage
    wordpress_oci_object_storage_enabled: true
    wordpress_oci_object_storage_bucket: "{{ vault_oci_bucket_name }}"
    wordpress_oci_backup_bucket: "{{ vault_oci_backup_bucket_name }}"

  roles:
    - role: thomasvincent.wordpress_enterprise
```

## Deployment

### Basic Deployment

```bash
# Deploy WordPress to OCI
ansible-playbook -i inventories/oci.ini examples/oracle-cloud.yml --ask-vault-pass
```

### Advanced Deployment Options

```bash
# Deploy with specific tags
ansible-playbook -i inventories/oci.ini examples/oracle-cloud.yml \
  --tags wordpress:install --ask-vault-pass

# Deploy with extra variables
ansible-playbook -i inventories/oci.ini examples/oracle-cloud.yml \
  -e "wordpress_php_version=8.3" --ask-vault-pass

# Dry run (check mode)
ansible-playbook -i inventories/oci.ini examples/oracle-cloud.yml \
  --check --ask-vault-pass
```

## OCI Free Tier Optimization

### Always Free Resources
Oracle Cloud offers generous Always Free resources:
- 2x AMD-based Compute VMs (1/8 OCPU, 1GB RAM each)
- OR 4x Arm-based Ampere A1 Compute VMs (4 OCPUs, 24GB RAM total)
- 2x Block Volumes (200GB total)
- 10GB Object Storage (Standard)
- 10GB Archive Storage
- Load Balancer (10 Mbps)

### Recommended Configuration for Free Tier

```yaml
# Use Arm-based compute for better performance on free tier
wordpress_oci_shape: "VM.Standard.A1.Flex"
wordpress_oci_ocpus: 2
wordpress_oci_memory_gb: 12

# Optimize block storage
wordpress_oci_block_volume_size_gb: 50
wordpress_oci_block_volume_performance: "Balanced"

# Use minimal load balancer bandwidth
wordpress_oci_lb_min_bandwidth_mbps: 10
wordpress_oci_lb_max_bandwidth_mbps: 10
```

## OCI-Specific Variables

### Compute Variables
| Variable | Default | Description |
|----------|---------|-------------|
| `wordpress_oci_compartment_id` | `""` | OCI Compartment OCID |
| `wordpress_oci_availability_domain` | `""` | Availability Domain (AD-1, AD-2, AD-3) |
| `wordpress_oci_subnet_id` | `""` | Subnet OCID for compute instances |
| `wordpress_oci_shape` | `"VM.Standard.E4.Flex"` | Compute instance shape |
| `wordpress_oci_ocpus` | `2` | Number of OCPUs (for flexible shapes) |
| `wordpress_oci_memory_gb` | `16` | Memory in GB (for flexible shapes) |
| `wordpress_oci_boot_volume_size_gb` | `50` | Boot volume size in GB |

### Block Storage Variables
| Variable | Default | Description |
|----------|---------|-------------|
| `wordpress_oci_block_storage_enabled` | `false` | Enable Block Storage attachment |
| `wordpress_oci_block_volume_size_gb` | `100` | Block volume size in GB |
| `wordpress_oci_block_volume_performance` | `"Balanced"` | Performance tier |
| `wordpress_oci_block_volume_mount_point` | `"/var/www/wordpress"` | Mount point path |
| `wordpress_oci_block_volume_backup_policy` | `"bronze"` | Backup policy (bronze/silver/gold) |

### Load Balancer Variables
| Variable | Default | Description |
|----------|---------|-------------|
| `wordpress_oci_load_balancer_enabled` | `false` | Enable Load Balancer |
| `wordpress_oci_lb_shape` | `"flexible"` | Load balancer shape |
| `wordpress_oci_lb_min_bandwidth_mbps` | `10` | Minimum bandwidth in Mbps |
| `wordpress_oci_lb_max_bandwidth_mbps` | `100` | Maximum bandwidth in Mbps |
| `wordpress_oci_lb_backend_set_policy` | `"ROUND_ROBIN"` | Load balancing policy |
| `wordpress_oci_lb_health_check_path` | `"/wp-admin/install.php"` | Health check path |
| `wordpress_oci_lb_health_check_port` | `443` | Health check port |

### Object Storage Variables
| Variable | Default | Description |
|----------|---------|-------------|
| `wordpress_oci_object_storage_enabled` | `false` | Enable Object Storage |
| `wordpress_oci_object_storage_bucket` | `""` | Main bucket name |
| `wordpress_oci_object_storage_namespace` | `""` | OCI namespace |
| `wordpress_oci_object_storage_tier` | `"Standard"` | Storage tier (Standard/Archive) |
| `wordpress_oci_media_bucket` | `""` | Bucket for WordPress media |
| `wordpress_oci_backup_bucket` | `"wordpress-backups"` | Bucket for backups |

## Security Considerations

### Network Security
1. Configure Security Lists/NSGs to allow only necessary traffic:
   - Ingress: HTTP (80), HTTPS (443), SSH (22 - restricted IPs)
   - Egress: Allow all for updates and external API calls

2. Use private subnets for database and cache servers

3. Enable OCI Web Application Firewall (WAF) for additional protection

### Database Security
1. Use SSL/TLS for database connections
2. Enable Autonomous Database wallet authentication
3. Restrict database access to VCN only
4. Enable database encryption at rest

### Storage Security
1. Enable Object Storage encryption
2. Use pre-authenticated requests for limited-time access
3. Configure bucket policies for access control
4. Enable versioning for backup buckets

## Troubleshooting

### Common Issues

#### 1. API Authentication Errors
```
Error: 401 Unauthorized
```
**Solution:** Verify API key fingerprint and ensure the public key is added to your OCI user account.

#### 2. Compartment Access Issues
```
Error: Not authorized to access compartment
```
**Solution:** Verify IAM policies grant required permissions to your user/group.

#### 3. Subnet Connectivity
```
Error: Instance cannot reach internet
```
**Solution:** Ensure subnet has a route to Internet Gateway and Security Lists allow outbound traffic.

#### 4. Load Balancer Health Checks Failing
```
Error: Backend set unhealthy
```
**Solution:** Verify health check path is accessible and Security Lists allow load balancer to reach instances.

### Debugging Tips

Enable verbose Ansible output:
```bash
ansible-playbook -vvv -i inventories/oci.ini examples/oracle-cloud.yml --ask-vault-pass
```

Check OCI resource status:
```bash
oci compute instance list --compartment-id <compartment-ocid>
oci lb load-balancer list --compartment-id <compartment-ocid>
oci os bucket list --namespace <namespace> --compartment-id <compartment-ocid>
```

## Performance Tuning

### Compute Optimization
- Use VM.Standard.E4.Flex shapes for cost-effective performance
- Consider Arm-based A1 shapes for better price/performance
- Enable burstable instances for variable workloads

### Storage Optimization
- Use Ultra High Performance volumes for database workloads
- Implement caching with Redis for object cache
- Configure OPcache for PHP performance

### Network Optimization
- Place load balancer and compute instances in same AD
- Use OCI FastConnect for on-premises connectivity
- Enable HTTP/2 on load balancer and web server

## Backup and Recovery

### Automated Backups
- Block Volume backups (bronze: weekly, silver: daily, gold: hourly)
- Object Storage lifecycle policies for backup retention
- Database automated backups (configurable retention)

### Manual Backup
```bash
# Trigger on-demand backup via Ansible
ansible-playbook -i inventories/oci.ini examples/oracle-cloud.yml \
  --tags backup --ask-vault-pass
```

### Recovery Procedures
1. Restore from Block Volume backup
2. Restore database from automated backup
3. Restore media files from Object Storage
4. Reconfigure WordPress if necessary

## Monitoring and Logging

### OCI Monitoring
- Enable OCI Monitoring service for metrics
- Configure alarms for resource utilization
- Use OCI Logging service for centralized logs

### Application Monitoring
- WordPress debug logs: `/var/log/wordpress/`
- Web server logs: `/var/log/nginx/` or `/var/log/apache2/`
- PHP-FPM logs: `/var/log/php/`

## Cost Optimization

### Tips for Reducing Costs
1. Use Always Free tier resources when possible
2. Right-size compute instances based on actual usage
3. Use Archive storage tier for old backups
4. Enable auto-scaling for variable workloads
5. Schedule non-production instances to stop during off-hours

### Estimated Monthly Costs (Beyond Free Tier)
- Compute: $0.04/hour for E4.Flex (2 OCPUs, 16GB)
- Block Storage: $0.0255/GB-month
- Load Balancer: $0.0095/Mbps-hour
- Object Storage: $0.0255/GB-month (Standard)
- Data Transfer: Free within region, $0.0085/GB egress

## Support and Resources

### OCI Documentation
- [OCI Compute Documentation](https://docs.oracle.com/en-us/iaas/Content/Compute/home.htm)
- [OCI Block Storage](https://docs.oracle.com/en-us/iaas/Content/Block/home.htm)
- [OCI Load Balancer](https://docs.oracle.com/en-us/iaas/Content/Balance/home.htm)
- [OCI Object Storage](https://docs.oracle.com/en-us/iaas/Content/Object/home.htm)

### Ansible Role
- [GitHub Repository](https://github.com/somethingwithproof/ansible-wordpress-enterprise)
- [Issue Tracker](https://github.com/somethingwithproof/ansible-wordpress-enterprise/issues)

## License

MIT License
