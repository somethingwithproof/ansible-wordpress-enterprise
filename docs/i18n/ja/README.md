<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · **日本語** · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · **日本語** · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
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

PHP、Web サーバー、およびローカルまたは外部データベースを用いて WordPress ホストを構成するための Ansible ロールです。デプロイフェーズの前にプラットフォームと入力値の検証を実行し、インストール・設定・検証の各工程をタスク境界で分離して個別にレビューできるようにしています。

## サポート対象のデプロイ要件

[meta/platform_support.yml](../../../meta/platform_support.yml) がサポートポリシーの正式な定義元です。安定版の Molecule マトリクスでは、Nginx を用いた Ubuntu 24.04/PHP 8.3、Ubuntu 26.04/PHP 8.5、Debian 13/PHP 8.4、および Apache を用いた Rocky Linux 9・10/PHP 8.3 をカバーしています。すべての経路について HTTP および HTTPS で検証を行っています。これらがテスト済みの OS/PHP の組み合わせであり、インベントリで未テストの組み合わせに上書きした場合は、パッケージ変更の前に失敗します。EL 系のエイリアスも同じポリシーを共有しますが、実行時の検証根拠は Rocky Linux コンテナに基づいています。

Python 3.12 コントローラーでは、14.x 系の Ansible 14.6 以降および 2.21 系の ansible-core 2.21.6 以降を使用します。Python 3.13 および 3.14 コントローラーでは、Ansible 15.x および ansible-core 2.22.x を使用します。ハッシュ付きの requirements ロックファイルにより、コントローラーのインタープリターに適した組み合わせが選択されます。管理対象ノードのインタープリター要件は別途定められています。バージョンを選択する前にポリシーを確認してください。古いプラットフォームや、アップストリームでサポートされているだけの PHP バージョンは自動的には採用されません。

## 機能の成熟度

コアタスクの実行順序は [tasks/main.yml](../../../tasks/main.yml) で定義されています。監視、バックアップ、Fail2ban、セキュリティ、キャッシュ、ファイアウォールの各グループには未実装のテンプレート契約があり、[tests/unit/missing_templates.yml](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/tests/unit/missing_templates.yml) に記録されています。これらのフラグはデフォルトで無効のままになっており、未完成のグループを有効にしようとすると検証で拒否されます。タスク名や設定例変数を、これらの機能が動作する実装として扱わないでください。

TLS、データベース認証情報、生成される WordPress シークレット、パスガード、および OS 固有の処理には、ドキュメントに記載された設定と実行時チェックが必要です。ここでは自動フェイルオーバー、クラウド全体の可用性 SLA、またはあらゆる環境での本番運用対応を保証するものではありません。

## クイックスタート

リポジトリソースからロールおよび依存するコレクションをインストールします。

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git,HEAD,wordpress_enterprise
ansible-galaxy collection install -r requirements.yml
```

コレクションのインストールコマンドは、このチェックアウトディレクトリから実行してください。デプロイ前に [defaults/main.yml](../../../defaults/main.yml) および [使用例](../../../examples/README.md) を確認してください。内部のタスクフェーズを直接呼び出すのではなく、サポートされているエントリーポイントを使用してください。

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

参照されるシークレットは、Ansible Vault または既存のシークレットマネージャーを通じて提供してください。デプロイを実行する前に、対象ホストの証明書とホスト名解決を設定してください。未完成の機能グループは無効のままにしてください。

## 開発とテスト

[Makefile](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/Makefile)、[CONTRIBUTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/CONTRIBUTING.md)、および [TESTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/TESTING.md) では、ハッシュ検証付きの依存関係セットアップ、リントチェック、単体テスト、および使い捨ての Docker/Molecule テスト要件が定義されています。単体テストやリントの通過は、デプロイの成功を保証するものではありません。

```bash
make lint
```

安定版の `default` および `tls` シナリオとその前提条件については、テストガイドを参照してください。ホストへのインストール、アップグレード、クリーンアップ、復元の各タスクは対象マシンに変更を加えるため、検証には隔離されたテスト用インベントリを使用してください。

## バージョニングとリリースパッケージ

プロジェクトのリリースでは、`meta/main.yml` に記載された最小 Ansible バージョンとは独立して、`VERSION` ファイル内の完全な SemVer バージョンを使用します。main ブランチに一致する `v2.22.1` タグをプッシュして Release ワークフローを起動するか、一致するタグを作成した後に main から手動で実行してください。ワークフローは、既存のタグがチェック対象のソースを指していることを検証し、4 つの Molecule シナリオすべてを含む完全な CI スイートを実行したうえで、Galaxy 互換のロールアーカイブ、Debian パッケージ、RPM、`release.json`、および `SHA256SUMS` を公開します。公開処理ではリリース API のデフォルトターゲットを上書きせずに検証済みの既存タグを使用するため、後続の main でのワークフロー更新時に広範なワークフロー書き込み権限を必要としません。タグが存在しないか一致しない場合は、テスト実行前に失敗します。

ダウンロードしたファイルは `sha256sum --check SHA256SUMS` で検証してください。ネイティブパッケージは、Ubuntu 24.04 では `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb`、Rocky Linux 9 では `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` でインストールできます。どちらも `/usr/share/ansible/roles/wordpress_enterprise` 配下にロールをインストールします。サポートされている Ansible コントローラーを用意し、`requirements.yml` を別途インストールしてください。アーカイブは `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz,,wordpress_enterprise` でインストールできます。ネイティブパッケージにはロールのソースとドキュメントが含まれており、インストール時にデプロイスクリプトは実行されません。CI では両方の形式についてインストール、検証、およびアンインストールを行っています。

## セキュリティとライセンス

[SECURITY.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/SECURITY.md) および [MIT ライセンス](../../../LICENSE) を参照してください。パッケージメタデータ、プラットフォームサポートポリシー、およびリリース検証は、提供されるロールと常に整合している必要があります。
