<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · **繁體中文** · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · **繁體中文** · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
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

一個用於設定 WordPress 主機（包含 PHP、網頁伺服器以及本機或外部資料庫）的 Ansible 角色。平台與輸入驗證會在部署階段之前執行，而工作邊界讓安裝、設定與驗證階段得以各自獨立檢視。

## 支援的部署契約

[meta/platform_support.yml](../../../meta/platform_support.yml) 為支援政策的權威依據。穩定的 Molecule 測試矩陣涵蓋搭載 Nginx 的 Ubuntu 24.04/PHP 8.3 與 Ubuntu 26.04/PHP 8.5、搭載 Nginx 的 Debian 13/PHP 8.4，以及搭載 Apache 的 Rocky Linux 9 與 10/PHP 8.3。每條路徑皆經過 HTTP 與 HTTPS 測試。以上為經過測試的作業系統／PHP 組合；若在主機清單（inventory）中覆寫為未經測試的組合，會在套件變更前即失敗。EL 別名共用同一套政策，但執行時期的驗證證據來自 Rocky Linux 容器。

Python 3.12 控制器使用 14.x 系列的 Ansible 14.6 或更新版本，搭配 2.21 系列的 ansible-core 2.21.6 或更新版本。Python 3.13 與 3.14 控制器使用 Ansible 15.x 搭配 ansible-core 2.22.x。附帶雜湊值的相依套件鎖定檔會針對控制器直譯器選取對應組合。受管節點的直譯器需求則另行獨立計算。選取版本前請先查閱支援政策；較舊的平台以及僅獲上游支援的 PHP 版本不會自動納入支援。

## 功能成熟度

核心工作順序定義於 [tasks/main.yml](../../../tasks/main.yml)。監控、備份、Fail2ban、安全性、快取與防火牆群組尚有缺失的範本契約，均記錄於 [tests/unit/missing_templates.yml](../../../tests/unit/missing_templates.yml)。這些群組的旗標預設為關閉，且驗證流程會拒絕啟用尚未完成的群組。不得將工作名稱與範例變數視為上述功能的可用實作。

TLS、資料庫認證資訊、產生的 WordPress 機密金鑰、路徑保護機制以及特定作業系統的處理方式，皆須符合文件記載的設定與執行時期檢查。本專案不提供自動容錯移轉、跨雲端可用性 SLA，亦不宣稱適用於所有正式環境。

## 快速開始

從儲存庫來源安裝此角色及其 collection 相依項目：

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git,HEAD,wordpress_enterprise
ansible-galaxy collection install -r requirements.yml
```

請於此檢出目錄中執行 collection 指令。部署前請先檢視 [defaults/main.yml](../../../defaults/main.yml) 與 [範例](../../../examples/README.md)。請使用受支援的進入點，切勿直接呼叫內部工作階段。

```yaml
- hosts: wordpress_test_hosts
  become: true
  vars:
    wordpress_web_server: nginx
    wordpress_site_url: "http://wordpress.example.com"
    wordpress_server_name: wordpress.example.com
    wordpress_admin_password: "{{ vault_wordpress_admin_password }}"
    wordpress_db_password: "{{ vault_wordpress_db_password }}"
    wordpress_db_root_password: "{{ vault_wordpress_db_root_password }}"
  roles:
    - wordpress_enterprise
```

請透過 Ansible Vault 或現有的機密管理服務提供所參照的機密資訊。執行部署前，請先為目標主機設定憑證與主機名稱解析。請保持未完成的功能群組為停用狀態。

## 開發與測試

[Makefile](../../../Makefile)、[CONTRIBUTING.md](../../../CONTRIBUTING.md) 與 [TESTING.md](../../../TESTING.md) 定義了附帶雜湊值的相依套件設定、lint 檢查、單元測試，以及可拋棄式 Docker／Molecule 契約。通過單元測試與 lint 並不代表部署必定成功。

```bash
make lint
```

請參閱測試指南以了解穩定的 `default` 與 `tls` 情境及其先決條件。主機安裝、升級、清理與還原工作會修改所選定的機器；驗證時請使用隔離的測試主機清單。

## 版本控制與發行套件

專案發行採用 `VERSION` 中的完整 SemVer 版本號，獨立於 `meta/main.yml` 的最低 Ansible 版本要求。在 main 分支推送對應的 `v2.22.1` 標籤以觸發 Release 工作流程，或在建立對應標籤後從 main 手動執行。該工作流程會驗證既有標籤是否指向受檢核的原始碼、執行完整的 CI 測試套件（包含全部四個 Molecule 情境），並發布與 Galaxy 相容的角色封存檔、Debian 套件、RPM、`release.json` 與 `SHA256SUMS`。發布流程直接使用該已驗證的既有標籤，而不覆寫發行 API 的預設目標，因此日後在 main 上更新工作流程時，不需要更廣泛的 workflow 寫入權限。若標籤缺失或不符，流程會在測試之前即告失敗。

請使用 `sha256sum --check SHA256SUMS` 驗證下載檔案。在 Ubuntu 24.04 上請使用 `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb`，或在 Rocky Linux 9 上使用 `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` 安裝原生套件。兩者皆會將角色安裝於 `/usr/share/ansible/roles/wordpress_enterprise`；請自行提供受支援的 Ansible 控制器並另行安裝 `requirements.yml`。封存檔可使用 `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz,,wordpress_enterprise` 進行安裝。原生套件僅包含角色原始碼與文件，安裝期間不會執行任何部署腳本。CI 會針對兩種格式執行安裝、檢查與移除驗證。

## 安全性與授權

請參閱 [SECURITY.md](../../../SECURITY.md) 與 [MIT 授權條款](../../../LICENSE)。套件中繼資料、平台支援政策與發行驗證必須與隨附的角色保持一致。
