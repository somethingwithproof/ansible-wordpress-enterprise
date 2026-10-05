# Security Policy

## Supported Versions

We release patches for security vulnerabilities. Which versions are eligible for receiving such patches depends on the CVSS v3.0 Rating:

| Version | Supported          |
| ------- | ------------------ |
| 1.x.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

Please report (suspected) security vulnerabilities to **[security@example.com](mailto:security@example.com)**. You will receive a response from us within 48 hours. If the issue is confirmed, we will release a patch as soon as possible depending on complexity but historically within a few days.

### Preferred Languages

We prefer all communications to be in English.

### Disclosure Policy

When we receive a security bug report, we will assign it to a primary handler. This person will coordinate the fix and release process, involving the following steps:

1. Confirm the problem and determine the affected versions.
2. Audit code to find any potential similar problems.
3. Prepare fixes for all releases still under maintenance.
4. Release new versions of all affected versions.

## Security Best Practices

When using this Ansible role, please follow these security best practices:

1. **Always use Ansible Vault** for sensitive data:
   ```bash
   ansible-vault encrypt_string 'your-secret' --name 'wordpress_db_password'
   ```

2. **Keep dependencies updated**:
   ```bash
   pip install --upgrade -r requirements.txt
   ```

3. **Use the latest stable version** of this role:
   ```bash
   ansible-galaxy install thomasvincent.wordpress_enterprise --force
   ```

4. **Enable all security features** in production:
   ```yaml
   wordpress_enable_ssl: true
   wordpress_enable_fail2ban: true
   wordpress_configure_firewall: true
   wordpress_enable_security_headers: true
   ```

5. **Regularly audit your deployment**:
   ```bash
   ansible-playbook -i inventory security-audit.yml
   ```

## Dependencies

This role uses the following dependencies with known security considerations:

- **Ansible**: Version 8.5.0+ required (addresses CVE-2023-5764)
- **ansible-core**: Version 2.15.0+ required
- **Python**: Version 3.8+ recommended
- **WordPress**: Always use the latest stable version

## Security Features

This role implements the following security features:

- SSL/TLS configuration with modern ciphers
- Fail2ban with WordPress-specific rules
- Firewall configuration (firewalld/ufw)
- Security headers (HSTS, CSP, X-Frame-Options)
- File integrity monitoring
- Automated security updates
- WordPress hardening
- Database security
- SSH hardening (when configured)
