<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · **Türkçe** · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · **Türkçe** · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
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

WordPress ana bilgisayarlarını PHP, bir web sunucusu ve yerel veya harici bir veritabanıyla yapılandırmak için bir Ansible rolü. Platform ve girdi doğrulaması dağıtım aşamalarından önce çalışırken, görev sınırları kurulum, yapılandırma ve doğrulama aşamalarının ayrı ayrı incelenebilmesini sağlar.

## Desteklenen dağıtım sözleşmesi

[meta/platform_support.yml](../../../meta/platform_support.yml) destek politikasının yetkili kaynağıdır. Kararlı Molecule matrisi; Nginx ile Ubuntu 24.04/PHP 8.3 ve Ubuntu 26.04/PHP 8.5, Nginx ile Debian 13/PHP 8.4 ve Apache ile Rocky Linux 9 ve 10/PHP 8.3 yapılandırmalarını kapsar. Her yol HTTP ve HTTPS üzerinden test edilir. Bunlar test edilmiş işletim sistemi/PHP çiftleridir; test edilmemiş çiftlere yönelik envanter geçersiz kılmaları paket değişikliklerinden önce başarısız olur. EL takma adları aynı politikayı paylaşır, ancak çalışma zamanı kanıtları Rocky Linux kapsayıcılarından elde edilir.

Python 3.12 denetleyicileri, 14.x serisinde Ansible 14.6 veya üzeri ile 2.21 serisinde ansible-core 2.21.6 veya üzerini kullanır. Python 3.13 ve 3.14 denetleyicileri ise ansible-core 2.22.x ile Ansible 15.x kullanır. Karma doğrulamalı gereksinim kilidi, denetleyici yorumlayıcısına uygun çifti seçer. Yönetilen düğüm yorumlayıcı gereksinimleri ayrıdır. Sürümleri seçmeden önce politikaya başvurun; daha eski platformlar ve yalnızca yukarı akışta desteklenen PHP sürümleri otomatik olarak benimsenmez.

## Özellik olgunluğu

Temel görev sırası [tasks/main.yml](../../../tasks/main.yml) dosyasında tanımlanmıştır. İzleme, yedekleme, Fail2ban, güvenlik, önbellekleme ve güvenlik duvarı gruplarının eksik şablon sözleşmeleri [tests/unit/missing_templates.yml](../../../tests/unit/missing_templates.yml) dosyasında kayıtlıdır. Bu grupların bayrakları varsayılan olarak kapalıdır ve doğrulama, tamamlanmamış grupların etkinleştirilmesini reddeder. Görev adları ve örnek değişkenler bu özelliklerin çalışan uygulamaları olarak sunulmamalıdır.

TLS, veritabanı kimlik bilgileri, oluşturulan WordPress gizli anahtarları, yol korumaları ve işletim sistemine özgü işlemler belgelenmiş yapılandırma ve çalışma zamanı kontrollerini gerektirir. Burada otomatik yük devretme, bulut genelinde erişilebilirlik SLA'sı veya evrensel üretim hazır olma iddiası sunulmamaktadır.

## Hızlı başlangıç

Rolü depo kaynağından ve koleksiyon bağımlılıklarıyla birlikte kurun:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git
ansible-galaxy collection install -r requirements.yml
```

Koleksiyon komutunu bu çalışma kopyasından çalıştırın. Dağıtımdan önce [defaults/main.yml](../../../defaults/main.yml) ve [örnekler](../../../examples/README.md) belgelerini inceleyin. Dahili görev aşamalarını doğrudan çağırmak yerine desteklenen giriş noktasını kullanın.

```yaml
- hosts: wordpress_test_hosts
  become: true
  vars:
    wordpress_web_server: nginx
    wordpress_site_url: "https://wordpress.example.com"
    wordpress_server_name: wordpress.example.com
    wordpress_admin_password: "{{ vault_wordpress_admin_password }}"
    wordpress_db_password: "{{ vault_wordpress_db_password }}"
    wordpress_db_root_password: "{{ vault_wordpress_db_root_password }}"
  roles:
    - ansible-wordpress-enterprise
```

Başvurulan gizli bilgileri Ansible Vault veya mevcut bir gizli bilgi yöneticisi aracılığıyla sağlayın. Bir dağıtım çalıştırmadan önce hedef ana bilgisayar için sertifikaları ve ana bilgisayar adı çözümlemesini yapılandırın. Tamamlanmamış özellik gruplarını devre dışı bırakın.

## Geliştirme ve test

[Makefile](../../../Makefile), [CONTRIBUTING.md](../../../CONTRIBUTING.md) ve [TESTING.md](../../../TESTING.md) dosyaları karma doğrulamalı bağımlılık kurulumunu, lint kontrollerini, birim testlerini ve tek kullanımlık Docker/Molecule sözleşmelerini tanımlar. Birim testleri ve lint kontrolleri başarılı bir dağıtımı garanti etmez.

```bash
make lint
```

Kararlı `default` ve `tls` senaryoları ile ön koşulları için test kılavuzunu kullanın. Ana bilgisayar kurulum, yükseltme, temizleme ve geri yükleme görevleri seçilen makineleri değiştirir; doğrulama için yalıtılmış test envanterleri kullanın.

## Sürümleme ve yayın paketleri

Proje sürümleri, `meta/main.yml` dosyasındaki minimum Ansible sürümünden bağımsız olarak `VERSION` dosyasındaki tam SemVer sürümünü kullanır. Release iş akışını tetiklemek için main dalında eşleşen bir `v2.22.1` etiketi gönderin veya eşleşen etiketi oluşturduktan sonra iş akışını main üzerinden elle çalıştırın. İş akışı mevcut etiketin denetlenen kaynağa işaret ettiğini doğrular, tam CI paketini (dört Molecule senaryosunun tamamı dahil) çalıştırır ve Galaxy uyumlu bir rol arşivi, Debian paketi, RPM, `release.json` ve `SHA256SUMS` dosyalarını yayınlar. Yayınlama, sürüm API'sinin varsayılan hedefini geçersiz kılmadan bu doğrulanmış mevcut etiketi kullanır; böylece main dalındaki daha sonraki bir iş akışı güncellemesi daha geniş iş akışı yazma kimlik bilgileri gerektirmez. Eksik veya eşleşmeyen bir etiket, test aşamasından önce başarısız olur.

İndirilen dosyaları `sha256sum --check SHA256SUMS` ile doğrulayın. Yerel paketleri Ubuntu 24.04 üzerinde `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` veya Rocky Linux 9 üzerinde `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` komutuyla kurun. Her ikisi de rolü `/usr/share/ansible/roles/wordpress_enterprise` altına kurar; desteklenen bir Ansible denetleyicisi sağlayın ve `requirements.yml` dosyasını ayrı olarak kurun. Arşiv `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz` ile kurulabilir. Yerel paketler rol kaynaklarını ve belgelerini içerir; kurulum sırasında hiçbir dağıtım betiği çalıştırmaz. CI her iki biçimi de kurar, kontrol eder ve kaldırır.

## Güvenlik ve lisans

[SECURITY.md](../../../SECURITY.md) ve [MIT lisansı](../../../LICENSE) belgelerine bakın. Paket üst verileri, platform destek politikası ve sürüm doğrulaması, sunulan rolle uyumlu kalmalıdır.
