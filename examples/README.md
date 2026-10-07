<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

# WordPress Role Examples

Project overview and current scope: [Ansible WordPress Enterprise](../README.md).

These playbooks illustrate configurations for the role and separately managed infrastructure. An example's variables do not prove that the role implements every named cloud service, HA feature, or integration.

## Example files

| File | Intended scenario |
| --- | --- |
| [local-development.yml](local-development.yml) | Local evaluation |
| [production-wordpress.yml](production-wordpress.yml) | Host deployment configuration |
| [cloudflare-only.yml](cloudflare-only.yml) | Cloudflare-related configuration |
| [digitalocean-full.yml](digitalocean-full.yml) | DigitalOcean-related configuration |
| [hybrid-cloudflare-digitalocean.yml](hybrid-cloudflare-digitalocean.yml) | Combined provider configuration |
| [google-cloud-platform.yml](google-cloud-platform.yml) | Google Cloud-related configuration |
| [microsoft-azure.yml](microsoft-azure.yml) | Azure-related configuration |
| [oracle-cloud.yml](oracle-cloud.yml) | Oracle Cloud-related configuration |
| [aws-compatible.yml](aws-compatible.yml) | AWS-related configuration |
| [multi-cloud-ha.yml](multi-cloud-ha.yml) | Proposed topology using external HA services |
| [vault-template.yml](vault-template.yml) | Placeholder secret-variable names |

## Before using a playbook

Check every variable against [the defaults](../defaults/main.yml) and [task implementation](../tasks). A variable that appears only in an example has no effect unless some task or external system consumes it. In particular, the multi-cloud example is not evidence of automated failover, measured uptime, or tested active-active deployment.

Provide an inventory, working provider infrastructure, and the required Vault variables. Adjust role names to the name used when installing the role. Review the playbook and test on an isolated host before using it for a deployment.

## Validation

Use the repository [test guide](../TESTING.md) for available checks. Documented examples require separate integration validation for the target provider, OS, and optional services. No latency, availability, cost-saving, or provider-coverage benchmark is asserted here.
