<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · **Bahasa Melayu** · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
- **Africa:** [Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)
- **Asia:** [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [עברית](../he/README.md) · [मराठी](../mr/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · **Bahasa Melayu** · [Filipino](../fil/README.md)

</details>
<!-- translations:end -->

# Ansible WordPress Enterprise

[![CI](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_ansible-wordpress-enterprise&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_ansible-wordpress-enterprise)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/ansible-wordpress-enterprise)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/releases)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/ansible-wordpress-enterprise/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/ansible-wordpress-enterprise)

Peranan Ansible untuk mengkonfigurasikan hos WordPress dengan PHP, pelayan web, dan pangkalan data tempatan atau luaran. Pengesahan platform dan input dijalankan sebelum fasa pengerahan, manakala sempadan tugas memastikan pemasangan, konfigurasi, dan penentusahan boleh disemak secara berasingan.

## Kontrak pengerahan yang disokong

[meta/platform_support.yml](../../../meta/platform_support.yml) ialah rujukan rasmi dasar sokongan. Matriks Molecule yang stabil merangkumi Ubuntu 24.04/PHP 8.3 dan Ubuntu 26.04/PHP 8.5 dengan Nginx, Debian 13/PHP 8.4 dengan Nginx, serta Rocky Linux 9 dan 10/PHP 8.3 dengan Apache. Setiap laluan diuji melalui HTTP dan HTTPS. Ini ialah pasangan OS/PHP yang diuji; penggantian inventori kepada pasangan yang tidak diuji akan gagal sebelum perubahan pakej dilakukan. Alias EL berkongsi dasar yang sama, tetapi bukti masa jalan diperoleh daripada kontena Rocky Linux.

Pengawal Python 3.12 menggunakan Ansible 14.6 atau lebih baharu dalam siri 14.x dengan ansible-core 2.21.6 atau lebih baharu dalam siri 2.21. Pengawal Python 3.13 dan 3.14 menggunakan Ansible 15.x dengan ansible-core 2.22.x. Kunci keperluan tercincang memilih pasangan tersebut untuk pentafsir pengawal. Keperluan pentafsir nod terurus adalah berasingan. Rujuk dasar tersebut sebelum memilih versi; platform yang lebih lama dan versi PHP yang hanya disokong di huluan tidak diguna pakai secara automatik.

## Kematangan ciri

Jujukan tugas teras ditakrifkan dalam [tasks/main.yml](../../../tasks/main.yml). Kumpulan pemantauan, sandaran, Fail2ban, keselamatan, cache, dan tembok api mempunyai kontrak templat yang tiada yang direkodkan dalam [tests/unit/missing_templates.yml](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/tests/unit/missing_templates.yml). Benderanya kekal dimatikan secara lalai dan pengesahan menolak pengaktifan kumpulan yang tidak lengkap. Nama tugas dan pemboleh ubah contoh tidak boleh dipersembahkan sebagai pelaksanaan yang berfungsi bagi ciri-ciri tersebut.

TLS, bukti kelayakan pangkalan data, rahsia WordPress yang dijana, semakan pelindung laluan, dan pengendalian khusus OS memerlukan konfigurasi serta semakan masa jalan yang didokumenkan. Tiada tuntutan gagal alih automatik, SLA ketersediaan merentas awan, atau kesediaan pengeluaran sejagat dibuat di sini.

## Mula pantas

Pasang peranan ini daripada sumber repositorinya berserta kebergantungan koleksinya:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git,HEAD,wordpress_enterprise
ansible-galaxy collection install -r requirements.yml
```

Jalankan arahan koleksi daripada salinan semak keluar ini. Semak [defaults/main.yml](../../../defaults/main.yml) dan [contoh](../../../examples/README.md) sebelum pengerahan. Gunakan titik masuk yang disokong dan bukannya memanggil fasa tugas dalaman secara langsung.

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

Sediakan rahsia yang dirujuk melalui Ansible Vault atau pengurus rahsia sedia ada. Konfigurasikan sijil dan peleraian nama hos untuk hos sasaran sebelum menjalankan pengerahan. Kekalkan kumpulan ciri yang tidak lengkap dalam keadaan dilumpuhkan.

## Pembangunan dan pengujian

[Makefile](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/Makefile), [CONTRIBUTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/CONTRIBUTING.md), dan [TESTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/TESTING.md) mentakrifkan persediaan kebergantungan tercincang, semakan lint, ujian unit, dan kontrak Docker/Molecule pakai buang. Ujian unit dan semakan lint tidak membuktikan pengerahan yang berjaya.

```bash
make lint
```

Gunakan panduan pengujian untuk senario `default` dan `tls` yang stabil serta prasyaratnya. Tugas pemasangan, naik taraf, pembersihan, dan pemulihan hos mengubah suai mesin yang dipilih; gunakan inventori ujian yang terasing untuk pengesahan.

## Penomboran versi dan pakej keluaran

Keluaran projek menggunakan versi SemVer lengkap dalam `VERSION`, secara bebas daripada versi Ansible minimum dalam `meta/main.yml`. Tolak teg `v2.22.1` yang sepadan pada cabang main untuk mencetuskan Release, atau jalankannya secara manual daripada main selepas mencipta teg yang sepadan. Aliran kerja ini mengesahkan bahawa teg sedia ada menunjuk kepada sumber yang disemak keluar, menjalankan keseluruhan suit CI (termasuk keempat-empat senario Molecule), dan menerbitkan arkib peranan yang serasi dengan Galaxy, pakej Debian, RPM, `release.json` dan `SHA256SUMS`. Penerbitan menggunakan teg sedia ada yang telah ditentusahkan itu tanpa menggantikan sasaran lalai API keluaran, supaya kemas kini aliran kerja seterusnya pada main tidak memerlukan bukti kelayakan tulis-aliran-kerja yang lebih luas. Teg yang tiada atau tidak sepadan akan gagal sebelum pengujian.

Tentusahkan muat turun dengan `sha256sum --check SHA256SUMS`. Pasang pakej asli dengan `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` pada Ubuntu 24.04 atau `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` pada Rocky Linux 9. Kedua-duanya memasang peranan di bawah `/usr/share/ansible/roles/wordpress_enterprise`; sediakan pengawal Ansible yang disokong dan pasang `requirements.yml` secara berasingan. Arkib tersebut boleh dipasang dengan `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz,,wordpress_enterprise`. Pakej asli mengandungi sumber peranan serta dokumentasi dan tidak menjalankan sebarang skrip pengerahan semasa pemasangan. CI memasang, menyemak dan membuang kedua-dua format tersebut.

## Keselamatan dan lesen

Lihat [SECURITY.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/SECURITY.md) dan [lesen MIT](../../../LICENSE). Metadata pakej, dasar sokongan platform, dan pengesahan keluaran mesti kekal selaras dengan peranan yang diedarkan.
