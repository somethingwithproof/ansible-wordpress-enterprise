<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · **Filipino** · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
- **Africa:** [Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)
- **Asia:** [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [עברית](../he/README.md) · [मराठी](../mr/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [Bahasa Melayu](../ms/README.md) · **Filipino**

</details>
<!-- translations:end -->

# Ansible WordPress Enterprise

[![CI](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_ansible-wordpress-enterprise&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_ansible-wordpress-enterprise)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/ansible-wordpress-enterprise)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/releases)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/ansible-wordpress-enterprise/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/ansible-wordpress-enterprise)

Isang Ansible role para sa pag-configure ng mga host ng WordPress na may PHP, web server, at lokal o panlabas na database. Tumatakbo muna ang pagpapatunay ng platform at input bago ang mga yugto ng deployment, habang pinananatili ng mga hangganan ng gawain na hiwalay na masusuri ang pag-install, pag-configure, at pagberipika.

## Sinusuportahang kontrata ng deployment

Ang [meta/platform_support.yml](../../../meta/platform_support.yml) ang awtoridad para sa patakaran sa suporta. Saklaw ng matatag na Molecule matrix ang Ubuntu 24.04/PHP 8.3 at Ubuntu 26.04/PHP 8.5 na may Nginx, Debian 13/PHP 8.4 na may Nginx, at Rocky Linux 9 at 10/PHP 8.3 na may Apache. Sinusubukan ang bawat path sa HTTP at HTTPS. Ito ang mga nasubukang pares ng OS/PHP; ang mga override ng inventory sa mga hindi nasubukang pares ay mabibigo bago magkaroon ng mga pagbabago sa package. Nagbabahagi ng patakaran ang mga alias ng EL, ngunit ang runtime na ebidensya ay nagmumula sa mga container ng Rocky Linux.

Gumagamit ang mga controller ng Python 3.12 ng Ansible 14.6 o mas bago sa linyang 14.x na may ansible-core 2.21.6 o mas bago sa linyang 2.21. Gumagamit ang mga controller ng Python 3.13 at 3.14 ng Ansible 15.x na may ansible-core 2.22.x. Pinipili ng hashed requirements lock ang pares para sa interpreter ng controller. Hiwalay ang mga kinakailangan sa interpreter ng managed node. Sumangguni sa patakaran bago pumili ng mga bersyon; hindi awtomatikong tinatanggap ang mga mas lumang platform at ang mga bersyon ng PHP na sinusuportahan lamang sa upstream.

## Kahandaan ng mga feature

Tinutukoy ang pangunahing pagkakasunod-sunod ng gawain sa [tasks/main.yml](../../../tasks/main.yml). Ang mga pangkat ng monitoring, backup, Fail2ban, security, caching, at firewall ay may mga kulang na kontrata ng template na nakatala sa [tests/unit/missing_templates.yml](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/tests/unit/missing_templates.yml). Nananatiling naka-off bilang default ang kanilang mga flag at tinatanggihan ng pagpapatunay ang pag-enable sa mga hindi kumpletong pangkat. Hindi dapat ipakita ang mga pangalan ng gawain at mga halimbawang variable bilang gumaganang implementasyon ng mga feature na iyon.

Ang TLS, mga kredensyal ng database, mga nalikhang sikreto ng WordPress, mga path guard, at ang pangangasiwang partikular sa OS ay nangangailangan ng dokumentadong konfigurasyon at mga runtime check. Walang inaangking awtomatikong failover, SLA ng availability sa buong cloud, o pangkalahatang kahandaan sa produksiyon dito.

## Mabilisang pagsisimula

I-install ang role mula sa repository source nito at ang mga dependency ng koleksiyon nito:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git,HEAD,wordpress_enterprise
ansible-galaxy collection install -r requirements.yml
```

Patakbuhin ang command ng koleksiyon mula sa checkout na ito. Suriin ang [defaults/main.yml](../../../defaults/main.yml) at [mga halimbawa](../../../examples/README.md) bago ang deployment. Gamitin ang sinusuportahang entry point sa halip na direktang tawagin ang mga panloob na yugto ng gawain.

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

Ibigay ang mga tinutukoy na sikreto sa pamamagitan ng Ansible Vault o isang umiiral na secret manager. I-configure ang mga sertipiko at hostname resolution para sa target na host bago magpatakbo ng deployment. Panatilihing naka-disable ang mga hindi kumpletong pangkat ng feature.

## Pag-develop at pagsusuri

Tinutukoy ng [Makefile](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/Makefile), [CONTRIBUTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/CONTRIBUTING.md), at [TESTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/TESTING.md) ang hashed dependency setup, mga lint check, mga unit test, at mga disposable na kontrata ng Docker/Molecule. Hindi nagpapatunay ng matagumpay na deployment ang mga unit test at lint.

```bash
make lint
```

Gamitin ang gabay sa pagsusuri para sa matatag na mga senaryong `default` at `tls` at ang mga kinakailangan ng mga ito. Binabago ng mga gawain sa pag-install ng host, pag-upgrade, paglilinis, at pag-restore ang mga napiling makina; gumamit ng mga nakahiwalay na test inventory para sa pagpapatunay.

## Paglalagay ng bersyon at mga release package

Gumagamit ang mga release ng proyekto ng kumpletong bersyon ng SemVer sa `VERSION`, nang hiwalay
sa minimum na bersyon ng Ansible ng `meta/main.yml`. Mag-push ng tumutugmang tag na `v2.22.1` sa main
upang i-trigger ang Release, o patakbuhin ito nang manu-mano mula sa main pagkatapos gawin ang tumutugmang tag.
Pinapatunayan ng workflow na ang umiiral na tag ay tumuturo sa sinuring source, pinatatakbo ang buong CI
suite (kabilang ang lahat ng apat na senaryo ng Molecule), at naglalathala ng Galaxy-compatible
na role archive, Debian package, RPM, `release.json` at `SHA256SUMS`.
Ginagamit ng paglalathala ang naberipikang umiiral na tag na iyon nang hindi ino-override ang default na
target ng release API, kaya ang isang mas huling update ng workflow sa main ay hindi nangangailangan ng mas malawak
na mga kredensyal sa pagsulat ng workflow. Ang nawawala o hindi tumutugmang tag ay nabibigo bago pa ang pagsusuri.

Beripikahin ang mga download gamit ang `sha256sum --check SHA256SUMS`. I-install ang mga native na package
gamit ang `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` sa Ubuntu
24.04 o `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` sa
Rocky Linux 9. Pareho nitong ini-install ang role sa ilalim ng
`/usr/share/ansible/roles/wordpress_enterprise`; magbigay ng sinusuportahang Ansible
controller at hiwalay na i-install ang `requirements.yml`. Maaaring i-install ang archive
gamit ang `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz,,wordpress_enterprise`.
Naglalaman ang mga native na package ng mga source at dokumentasyon ng role at walang pinatatakbong deployment
script sa panahon ng pag-install. Ini-install, sinusuri, at tinatanggal ng CI ang parehong format.

## Seguridad at lisensya

Tingnan ang [SECURITY.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/SECURITY.md) at ang [lisensyang MIT](../../../LICENSE). Dapat manatiling nakaayon sa ibinahaging role ang metadata ng package, patakaran sa suporta ng platform, at pagpapatunay ng release.
