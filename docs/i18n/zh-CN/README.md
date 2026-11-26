<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · **简体中文** · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · **简体中文** · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
- **Africa:** [Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)
- **Asia:** [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [עברית](../he/README.md) · [मराठी](../mr/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [Bahasa Melayu](../ms/README.md) · [Filipino](../fil/README.md)

</details>
<!-- translations:end -->

# Ansible WordPress Enterprise

[![CI](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_ansible-wordpress-enterprise&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_ansible-wordpress-enterprise)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/ansible-wordpress-enterprise)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/releases)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/ansible-wordpress-enterprise/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/ansible-wordpress-enterprise)

一个用于为 WordPress 主机配置 PHP、Web 服务器以及本地或外部数据库的 Ansible 角色。平台和输入验证在部署阶段之前运行，而任务边界使安装、配置和验证可以分别审查。

## 支持的部署契约

[meta/platform_support.yml](../../../meta/platform_support.yml) 是支持策略的权威依据。稳定的 Molecule 矩阵涵盖搭配 Nginx 的 Ubuntu 24.04/PHP 8.3 和 Ubuntu 26.04/PHP 8.5、搭配 Nginx 的 Debian 13/PHP 8.4，以及搭配 Apache 的 Rocky Linux 9 和 10/PHP 8.3。每条路径都经过 HTTP 和 HTTPS 测试。这些是经过测试的操作系统/PHP 组合；清单中覆盖为未经测试的组合将在软件包变更前失败。EL 别名共享此策略，但运行时依据来自 Rocky Linux 容器。

Python 3.12 控制节点使用 14.x 系列的 Ansible 14.6 或更高版本，搭配 2.21 系列的 ansible-core 2.21.6 或更高版本。Python 3.13 和 3.14 控制节点使用 Ansible 15.x 搭配 ansible-core 2.22.x。带哈希校验的依赖锁定文件会为控制节点解释器选择对应组合。受管节点的解释器要求另行独立。选择版本前请参阅策略；较旧平台和仅受上游支持的 PHP 版本不会被自动采纳。

## 功能成熟度

核心任务序列定义在 [tasks/main.yml](../../../tasks/main.yml) 中。监控、备份、Fail2ban、安全、缓存和防火墙分组存在缺失的模板契约，记录在 [tests/unit/missing_templates.yml](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/tests/unit/missing_templates.yml) 中。它们的开关默认保持关闭，验证逻辑会拒绝启用未完成的分组。任务名称和示例变量不得被视为这些功能的可用实现。

TLS、数据库凭据、生成的 WordPress 密钥、路径保护和特定于操作系统的处理均需要按文档要求进行配置和运行时检查。此处不声明自动故障转移、跨云可用性 SLA 或通用的生产就绪性。

## 快速开始

从代码仓库源安装该角色及其集合依赖：

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git,HEAD,wordpress_enterprise
ansible-galaxy collection install -r requirements.yml
```

在当前检出目录中运行集合安装命令。部署前请审查 [defaults/main.yml](../../../defaults/main.yml) 和 [示例](../../../examples/README.md)。请使用受支持的入口点，而不要直接调用内部任务阶段。

```yaml
- hosts: wordpress_test_hosts
  become: true
  vars:
    wordpress_web_server: nginx
    wordpress_site_url: "https://wordpress.example.com"
    wordpress_enable_ssl: true
    wordpress_server_name: wordpress.example.com
    wordpress_admin_password: "{{ vault_wordpress_admin_password }}"
    wordpress_db_password: "{{ vault_wordpress_db_password }}"
    wordpress_db_root_password: "{{ vault_wordpress_db_root_password }}"
  roles:
    - wordpress_enterprise
```

通过 Ansible Vault 或现有的密钥管理器提供所引用的密钥。在运行部署前，请为目标主机配置证书和主机名解析。保持未完成的功能分组处于禁用状态。

## 开发与测试

[Makefile](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/Makefile)、[CONTRIBUTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/CONTRIBUTING.md) 和 [TESTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/TESTING.md) 定义了带哈希校验的依赖设置、代码规范检查、单元测试以及一次性的 Docker/Molecule 契约。单元测试和规范检查并不证明部署成功。

```bash
make lint
```

请参阅测试指南，了解稳定的 `default` 和 `tls` 场景及其前置条件。主机安装、升级、清理和恢复任务会修改所选机器；请使用隔离的测试清单进行验证。

## 版本控制与发布包

项目发布使用 `VERSION` 中的完整 SemVer 版本号，独立于 `meta/main.yml` 中的最低 Ansible 版本。向 main 分支推送匹配的 `v2.22.1` 标签以触发 Release，或在创建匹配标签后从 main 分支手动运行。工作流会验证现有标签是否指向检出的源代码，运行完整的 CI 测试套件（包括全部四个 Molecule 场景），并发布兼容 Galaxy 的角色归档、Debian 软件包、RPM、`release.json` 和 `SHA256SUMS`。发布过程直接使用该已验证的现有标签，不会覆盖发布 API 的默认目标，因此后续在 main 上更新工作流时无需更宽泛的工作流写入凭据。缺失或不匹配的标签会在测试前失败。

使用 `sha256sum --check SHA256SUMS` 验证下载文件。在 Ubuntu 24.04 上使用 `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb`，或在 Rocky Linux 9 上使用 `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` 安装原生软件包。两者都会将角色安装到 `/usr/share/ansible/roles/wordpress_enterprise` 下；请自行提供受支持的 Ansible 控制节点并单独安装 `requirements.yml`。归档文件可使用 `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz,,wordpress_enterprise` 安装。原生软件包仅包含角色源代码和文档，在安装期间不运行任何部署脚本。CI 会安装、检查并卸载这两种格式。

## 安全与许可证

请参阅 [SECURITY.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/SECURITY.md) 和 [MIT 许可证](../../../LICENSE)。软件包元数据、平台支持策略和发布验证必须与随附的角色保持一致。
