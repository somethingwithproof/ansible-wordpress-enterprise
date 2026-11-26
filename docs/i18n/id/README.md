<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · **Bahasa Indonesia** · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · **Bahasa Indonesia**
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

Peran Ansible untuk mengonfigurasi host WordPress dengan PHP, server web, dan basis data lokal atau eksternal. Validasi platform dan masukan dijalankan sebelum fase penerapan, sementara pemisahan tugas menjaga agar pemasangan, konfigurasi, dan verifikasi dapat ditinjau secara terpisah.

## Kontrak penerapan yang didukung

[meta/platform_support.yml](../../../meta/platform_support.yml) adalah rujukan resmi kebijakan dukungan. Matriks Molecule yang stabil mencakup Ubuntu 24.04/PHP 8.3 dan Ubuntu 26.04/PHP 8.5 dengan Nginx, Debian 13/PHP 8.4 dengan Nginx, serta Rocky Linux 9 dan 10/PHP 8.3 dengan Apache. Setiap jalur diuji melalui HTTP dan HTTPS. Ini adalah pasangan OS/PHP yang telah diuji; penimpaan inventaris ke pasangan yang belum diuji akan gagal sebelum perubahan paket dilakukan. Alias EL berbagi kebijakan yang sama, tetapi bukti runtime berasal dari kontainer Rocky Linux.

Controller Python 3.12 menggunakan Ansible 14.6 atau lebih baru pada lini 14.x dengan ansible-core 2.21.6 atau lebih baru pada lini 2.21. Controller Python 3.13 dan 3.14 menggunakan Ansible 15.x dengan ansible-core 2.22.x. Berkas kunci dependensi ber-hash memilih pasangan yang sesuai untuk interpreter controller. Persyaratan interpreter untuk managed node bersifat terpisah. Periksa kebijakan tersebut sebelum memilih versi; platform yang lebih lama dan versi PHP yang hanya didukung di hulu tidak otomatis diadopsi.

## Kematangan fitur

Urutan tugas inti didefinisikan di [tasks/main.yml](../../../tasks/main.yml). Grup pemantauan, pencadangan, Fail2ban, keamanan, caching, dan firewall memiliki kontrak templat yang belum lengkap dan tercatat di [tests/unit/missing_templates.yml](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/tests/unit/missing_templates.yml). Flag untuk grup tersebut tetap nonaktif secara default, dan grup belum lengkap yang diaktifkan hanya berhenti saat tugasnya dijalankan, setelah fase-fase sebelumnya berjalan. Nama tugas dan contoh variabel tidak boleh disajikan sebagai implementasi yang berfungsi dari fitur-fitur tersebut.

TLS, kredensial basis data, rahasia WordPress yang dihasilkan, pengaman jalur, dan penanganan khusus OS memerlukan konfigurasi serta pemeriksaan runtime sesuai dokumentasi. Tidak ada klaim failover otomatis, SLA ketersediaan lintas cloud, atau kesiapan produksi universal yang dibuat di sini.

## Mulai cepat

Pasang peran ini dari sumber repositorinya beserta dependensi koleksinya:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git,HEAD,wordpress_enterprise
ansible-galaxy collection install -r requirements.yml
```

Jalankan perintah koleksi dari salinan repositori ini. Tinjau [defaults/main.yml](../../../defaults/main.yml) dan [contoh](../../../examples/README.md) sebelum penerapan. Gunakan titik masuk yang didukung alih-alih memanggil fase tugas internal secara langsung.

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

Sediakan rahasia yang dirujuk melalui Ansible Vault atau pengelola rahasia yang sudah ada. Konfigurasikan sertifikat dan resolusi nama host untuk host target sebelum menjalankan penerapan. Biarkan grup fitur yang belum lengkap tetap nonaktif.

## Pengembangan dan pengujian

[Makefile](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/Makefile), [CONTRIBUTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/CONTRIBUTING.md), dan [TESTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/TESTING.md) mendefinisikan penyiapan dependensi ber-hash, pemeriksaan lint, pengujian unit, serta kontrak Docker/Molecule sementara. Pengujian unit dan lint tidak menjamin keberhasilan penerapan.

```bash
make lint
```

Gunakan panduan pengujian untuk skenario stabil `default` dan `tls` beserta prasyaratnya. Tugas pemasangan, pemutakhiran, pembersihan, dan pemulihan host akan mengubah mesin yang dipilih; gunakan inventaris pengujian terisolasi untuk validasi.

## Pemversian dan paket rilis

Rilis proyek menggunakan versi SemVer lengkap di `VERSION`, terpisah
dari versi minimum Ansible di `meta/main.yml`. Dorong tag `v2.22.1` yang sesuai di branch main
untuk memicu Release, atau jalankan secara manual dari main setelah membuat tag yang sesuai.
Alur kerja ini memvalidasi bahwa tag yang ada menunjuk ke sumber yang diperiksa, menjalankan rangkaian CI
lengkap (termasuk keempat skenario Molecule), serta menerbitkan arsip peran yang kompatibel dengan
Galaxy, paket Debian, RPM, `release.json`, dan `SHA256SUMS`.
Penerbitan menggunakan tag terverifikasi tersebut tanpa menimpa target default API rilis,
sehingga pembaruan alur kerja berikutnya di main tidak memerlukan kredensial
tulis alur kerja yang lebih luas. Tag yang hilang atau tidak cocok akan gagal sebelum pengujian.

Verifikasi unduhan dengan `sha256sum --check SHA256SUMS`. Pasang paket asli
dengan `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` pada Ubuntu
24.04 atau `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` pada
Rocky Linux 9. Keduanya memasang peran di bawah
`/usr/share/ansible/roles/wordpress_enterprise`; sediakan controller Ansible
yang didukung dan pasang `requirements.yml` secara terpisah. Arsip dapat
dipasang dengan `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz,,wordpress_enterprise`.
Paket asli berisi kode sumber peran dan dokumentasi serta tidak menjalankan skrip
penerapan saat pemasangan. CI memasang, memeriksa, dan menghapus kedua format tersebut.

## Keamanan dan lisensi

Lihat [SECURITY.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/SECURITY.md) dan [lisensi MIT](../../../LICENSE). Metadata paket, kebijakan dukungan platform, dan validasi rilis harus tetap selaras dengan peran yang dikirimkan.
