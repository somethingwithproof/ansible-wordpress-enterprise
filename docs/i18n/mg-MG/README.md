<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · **Malagasy** · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
- **Africa:** [Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [Igbo](../ig-NG/README.md) · **Malagasy** · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)
- **Asia:** [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [עברית](../he/README.md) · [मराठी](../mr/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [Bahasa Melayu](../ms/README.md) · [Filipino](../fil/README.md)

</details>
<!-- translations:end -->

# Ansible WordPress Enterprise

[![CI](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_ansible-wordpress-enterprise&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_ansible-wordpress-enterprise)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/ansible-wordpress-enterprise)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/releases)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/ansible-wordpress-enterprise/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/ansible-wordpress-enterprise)

Anjara asa Ansible natao handrindrana mpampiantrano WordPress miaraka amin'ny PHP, mpizara tranonkala (web server), ary angon-drakitra eo an-toerana na ivelany. Ny fanamarinana ny sehatra sy ny fampidirana dia mandeha alohan'ny dingana fametrahana, ary ny fetran'ny asa dia mitazona ny fametrahana, ny fandrindrana, ary ny fanamarinana ho azo jerena mitokana.

## Fifanarahana fametrahana tohanana

Ny [meta/platform_support.yml](../../../meta/platform_support.yml) no loharanom-pahefana momba ny politikan'ny fanohanana. Ny lasitra Molecule marin-toerana dia mahafaoka ny Ubuntu 24.04/PHP 8.3 sy Ubuntu 26.04/PHP 8.5 miaraka amin'ny Nginx, Debian 13/PHP 8.4 miaraka amin'ny Nginx, ary Rocky Linux 9 sy 10/PHP 8.3 miaraka amin'ny Apache. Ny lalana tsirairay dia tsapaina amin'ny HTTP sy HTTPS. Ireo no mpivady OS/PHP voatsapa; ny fanovana lisitra mpampiantrano (inventory) ho amin'ny mpivady tsy voatsapa dia tsy hahomby alohan'ny fanovana fonosana. Ny solonanarana EL dia mizara ny politika ihany, fa ny porofo mandritra ny fampandehanana dia avy amin'ny kaontenera Rocky Linux.

Ny mpibaiko (controller) Python 3.12 dia mampiasa Ansible 14.6 na vaovao kokoa ao amin'ny andiany 14.x miaraka amin'ny ansible-core 2.21.6 na vaovao kokoa ao amin'ny andiany 2.21. Ny mpibaiko Python 3.13 sy 3.14 dia mampiasa Ansible 15.x miaraka amin'ny ansible-core 2.22.x. Ny rakitra fihazonana fepetra misy hash (hashed requirements lock) no misafidy ny mpivady mifanaraka amin'ny mpandika tenin'ny mpibaiko. Misaraka ny fepetran'ny mpandika teny ho an'ny lohamilina tantanana. Jereo ny politika alohan'ny hisafidianana dika; ny sehatra taloha sy ny dika PHP tohanan'ny loharano ambony fotsiny dia tsy raisina ho azy.

## Fahamatoran'ny endri-javatra

Ny filaharan'ny asa fototra dia voafaritra ao amin'ny [tasks/main.yml](../../../tasks/main.yml). Ny vondrona fanaraha-maso, tahiry fiarovana (backup), Fail2ban, fiarovana, cache, ary aro-afo (firewall) dia manana fifanarahana modely tsy ampy voarakitra ao amin'ny [tests/unit/missing_templates.yml](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/tests/unit/missing_templates.yml). Mijanona ho maty ho azy ny saina (flags) mifandray amin'izy ireo ary mandà ny fampandehanana vondrona tsy feno ny fanamarinana. Tsy tokony haseho ho fampiharana miasa an'ireo endri-javatra ireo ny anaran'asa sy ny ohatra miovaova (variables).

Ny TLS, ny fahazoan-dalana miditra amin'ny angon-drakitra, ny tsiambaratelo WordPress vokarina, ny fiarovana lalana, ary ny fikirakirana manokana isaky ny OS dia mitaky ny fandrindrana voarakitra an-tsoratra sy ny fanamarinana mandritra ny fampandehanana. Tsy misy filazana momba ny fiverenana ho azy (automatic failover), SLA fisiana manerana ny rahona, na fahavononana ho an'ny famokarana maneran-tany atao eto.

## Fanombohana haingana

Apetraho ny anjara asa avy amin'ny loharanon'ny tahiry sy ny angona ilainy:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git,HEAD,wordpress_enterprise
ansible-galaxy collection install -r requirements.yml
```

Alefaso avy amin'ity dika nalaina ity ny baiko ho an'ny angona. Jereo ny [defaults/main.yml](../../../defaults/main.yml) sy ny [ohatra](../../../examples/README.md) alohan'ny fametrahana. Ampiasao ny teboka fidirana tohanana fa aza miantso mivantana ny dingana anatiny.

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

Omeo amin'ny alalan'ny Ansible Vault na mpitantana tsiambaratelo efa misy ireo tsiambaratelo voatondro. Rindrio ny taratasy fanamarinana (certificates) sy ny famahana anaran'ny mpampiantrano (hostname resolution) ho an'ny mpampiantrano kendrena alohan'ny hampandehanana fametrahana. Tazony ho maty ireo vondrona endri-javatra tsy feno.

## Fampandrosoana sy fitsapana

Ny [Makefile](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/Makefile), [CONTRIBUTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/CONTRIBUTING.md), ary [TESTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/TESTING.md) no mamaritra ny fametrahana fiankinan-doha misy hash, fanamarinana lint, fitsapana singa (unit tests), ary fifanarahana Docker/Molecule azo ariana. Ny fitsapana singa sy ny lint dia tsy manaporofo fametrahana mahomby.

```bash
make lint
```

Ampiasao ny torolalana fitsapana ho an'ireo sehatra fitsapana marin-toerana `default` sy `tls` ary ny fepetra takiany mialoha. Ny asa fametrahana, fanavaozana, fanadiovana, ary famerenana amin'ny mpampiantrano dia manova ireo milina voafidy; mampiasà lisitra mpampiantrano fitsapana mitokana ho an'ny fanamarinana.

## Fanomezana dika sy fonosana famoahana

Ny famoahana ny tetikasa dia mampiasa ny dika SemVer feno ao amin'ny `VERSION`, mahaleo tena amin'ny dika Ansible farany ambany ao amin'ny `meta/main.yml`. Alefaso ny marika `v2.22.1` mifanaraka aminy ao amin'ny main hanombohana ny Release, na alefaso tanana avy ao amin'ny main aorian'ny famoronana ilay marika mifanaraka aminy. Manamarina ny fizotran'asa fa manondro ny loharano nojerena ilay marika efa misy, mandefa ny andian-tsapana CI feno (anisan'izany ireo sehatra fitsapana Molecule efatra), ary mamoaka arsiva anjara asa mifanaraka amin'ny Galaxy, fonosana Debian, RPM, `release.json` ary `SHA256SUMS`. Mampiasa izany marika efa misy voamarina izany ny famoahana nefa tsy manolo ny tanjona fototry ny API famoahana, ka ny fanavaozana fizotran'asa ao amin'ny main aty aoriana dia tsy mitaky alalana fanoratana fizotran'asa midadasika kokoa. Tsy mahomby alohan'ny fitsapana ny marika tsy ampy na tsy mifanaraka.

Hamarino ny rakitra nalaina amin'ny `sha256sum --check SHA256SUMS`. Apetraho ny fonosana voajanahary amin'ny `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` amin'ny Ubuntu 24.04 na `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` amin'ny Rocky Linux 9. Samy mametraka ny anjara asa ao amin'ny `/usr/share/ansible/roles/wordpress_enterprise` izy roa; omeo mpibaiko Ansible tohanana ary apetraho mitokana ny `requirements.yml`. Azo apetraka amin'ny `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz,,wordpress_enterprise` ny arsiva. Ny fonosana voajanahary dia ahitana ny loharanon'ny anjara asa sy ny antontan-taratasy ary tsy mandefa soratra fametrahana (deployment scripts) mandritra ny fametrahana. Ny CI dia mametraka, manamarina ary manala ireo endrika roa ireo.

## Fiarovana sy fahazoan-dalana

Jereo ny [SECURITY.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/SECURITY.md) sy ny [fahazoan-dalana MIT](../../../LICENSE). Ny metadata-n'ny fonosana, ny politikan'ny fanohanana sehatra, ary ny fanamarinana famoahana dia tsy maintsy mijanona ho mifanaraka amin'ny anjara asa aterina.
