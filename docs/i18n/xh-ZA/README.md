<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · **isiXhosa** · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
- **Africa:** [Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · **isiXhosa** · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)
- **Asia:** [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [עברית](../he/README.md) · [मराठी](../mr/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [Bahasa Melayu](../ms/README.md) · [Filipino](../fil/README.md)

</details>
<!-- translations:end -->

# Ansible WordPress Enterprise

[![CI](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_ansible-wordpress-enterprise&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_ansible-wordpress-enterprise)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/ansible-wordpress-enterprise)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/releases)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/ansible-wordpress-enterprise/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/ansible-wordpress-enterprise)

Indima ye-Ansible yokuqwalasela abancedisi be-WordPress nge-PHP, umncedisi wewebhu, kunye nesiseko sedatha sasekhaya okanye sangaphandle. Uqinisekiso lweqonga kunye nolwazi olungenisiweyo luqhutywa phambi kwezigaba zokufakela, ngelixa imida yemisebenzi igcina ukufakelwa, uqwalaselo, kunye nokuqinisekiswa kunokuphononongwa ngokwahlukeneyo.

## Isivumelwano sokufakelwa esixhaswayo

[meta/platform_support.yml](../../../meta/platform_support.yml) ngugunyaziwe womgaqo-nkqubo wenkxaso. Uluhlu oluzinzileyo lwe-Molecule luquka i-Ubuntu 24.04/PHP 8.3 kunye ne-Ubuntu 26.04/PHP 8.5 nge-Nginx, i-Debian 13/PHP 8.4 nge-Nginx, kunye ne-Rocky Linux 9 kunye ne-10/PHP 8.3 nge-Apache. Indlela nganye ivavanywa nge-HTTP nange-HTTPS. Ezi zizibini ze-OS/PHP ezivavanyiweyo; utshintsho kwi-inventory oluya kwizibini ezingavavanywanga luyasilela phambi kotshintsho lweephakheji. Amagama ezibizo e-EL abelana ngomgaqo-nkqubo, kodwa ubungqina bokusebenza buvela kwizikhongozeli ze-Rocky Linux.

Izilawuli ze-Python 3.12 zisebenzisa i-Ansible 14.6 okanye entsha kumgca we-14.x kunye ne-ansible-core 2.21.6 okanye entsha kumgca we-2.21. Izilawuli ze-Python 3.13 kunye ne-3.14 zisebenzisa i-Ansible 15.x kunye ne-ansible-core 2.22.x. Isitshixo seemfuno esine-hash sikhetha isibini esifanele umtoliki wesilawuli. Iimfuno zomtoliki wendawo elawulwayo zahlukile. Jonga umgaqo-nkqubo phambi kokukhetha iinguqulelo; amaqonga amadala kunye neenguqulelo ze-PHP ezixhaswa kuphela ngumthombo oyintloko azamkelwa ngokuzenzekelayo.

## Ukuvuthwa kweempawu

Ulandelelwano lwemisebenzi engundoqo luchazwe kwi-[tasks/main.yml](../../../tasks/main.yml). Amaqela okubeka iliso, ukugcina iikopi zokhuseleko, i-Fail2ban, ukhuseleko, ugcino lwethutyana, kunye ne-firewall anezivumelwano zeetemplate ezingekhoyo ezirekhodwe kwi-[tests/unit/missing_templates.yml](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/tests/unit/missing_templates.yml). Iiflegi zazo zihlala zicinyiwe ngokungagqibekanga kwaye uqinisekiso luyala ukuvulwa kwamaqela angagqibekanga. Amagama emisebenzi kunye neziguquguquki zemizekelo akufuneki ziboniswe njengeenkqubo ezisebenzayo zezo mpawu.

I-TLS, iinkcukacha zokungena kwisiseko sedatha, iimfihlo ze-WordPress ezivelisiweyo, izikhuseli zeendlela, kunye nokuphathwa okukhethekileyo kwe-OS kufuna uqwalaselo olubhaliweyo kunye novavanyo lwexesha lokusebenza. Akukho kubuyela ngokuzenzekelayo xa kukho ukusilela, i-SLA yokufumaneka kwilifu lonke, okanye ibango lokulungela ukuvelisa jikelele elenziwayo apha.

## Ukuqalisa ngokukhawuleza

Faka indima ukusuka kumthombo wayo we-repository kunye nezinto ezixhomekeke kuzo zengqokelela:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git,HEAD,wordpress_enterprise
ansible-galaxy collection install -r requirements.yml
```

Qhuba umyalelo wengqokelela ukusuka kule kope yekhowudi. Phonononga i-[defaults/main.yml](../../../defaults/main.yml) kunye [nemizekelo](../../../examples/README.md) phambi kokufakela. Sebenzisa indawo yokungena exhaswayo endaweni yokubiza izigaba zemisebenzi zangaphakathi ngokuthe ngqo.

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

Nikezela ngeemfihlo ekubhekiselwe kuzo nge-Ansible Vault okanye ngomlawuli weemfihlo okhoyo. Qwalasela izatifikethi kunye nokuguqulelwa kwegama lomncedisi kulo mncedisi ekujoliswe kuye phambi kokuqhuba ufakelo. Gcina amaqela eempawu angagqibekanga ecinyiwe.

## Uphuhliso novavanyo

I-[Makefile](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/Makefile), i-[CONTRIBUTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/CONTRIBUTING.md), kunye ne-[TESTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/TESTING.md) zichaza useto lwezinto ezixhomekeke kuzo ezine-hash, uhlolo lwe-lint, uvavanyo lweeyunithi, kunye nezivumelwano ze-Docker/Molecule ezilahlwayo. Uvavanyo lweeyunithi kunye ne-lint azisiqinisekisi isiphumo esinempumelelo sokufakela.

```bash
make lint
```

Sebenzisa isikhokelo sovavanyo kwiimeko ezizinzileyo ze-`default` ne-`tls` kunye neemfuno zazo zangaphambili. Imisebenzi yokufakela kumncedisi, uhlaziyo, ukucoca, kunye nokubuyisela itshintsha oomatshini abakhethiweyo; sebenzisa ii-inventory zovavanyo ezizodwa ukuqinisekisa.

## Ulawulo lweenguqulelo neepakethe zokukhupha

Ukukhutshwa kweprojekthi kusebenzisa inguqulelo epheleleyo ye-SemVer ekwi-`VERSION`, ngokuzimeleyo
kwinguqulelo encinci ye-Ansible ekwi-`meta/main.yml`. Tyhala ithegi ehambelanayo `v2.22.1` kwi-main
ukuqalisa i-Release, okanye uyiqhube ngesandla ukusuka kwi-main emva kokwenza ithegi ehambelanayo.
Inkqubo yokusebenza iqinisekisa ukuba ithegi ekhoyo ikhomba kumthombo ohloliweyo, iqhuba uluhlu olupheleleyo lwe-CI
(kubandakanya zonke iimeko ezine ze-Molecule), kwaye ipapasha ugcino lwendima oluhambelana
ne-Galaxy, ipakethe ye-Debian, i-RPM, i-`release.json` kunye ne-`SHA256SUMS`.
Ukupapasha kusebenzisa loo thegi ekhoyo eqinisekisiweyo ngaphandle kokutshintsha indawo ekujoliswe kuyo
esisiseko ye-API yokukhupha, ukuze uhlaziyo lwenkqubo yokusebenza olulandelayo kwi-main lungafuni iimvume
ezibanzi zokubhala kwinkqubo yokusebenza. Ithegi engekho okanye engahambelaniyo iyasilela phambi kovavanyo.

Qinisekisa izinto ezikhutshelweyo nge-`sha256sum --check SHA256SUMS`. Faka iipakethe zemveli
nge-`sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` kwi-Ubuntu
24.04 okanye nge-`sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` kwi-Rocky
Linux 9. Zombini zifaka indima phantsi kwe-`/usr/share/ansible/roles/wordpress_enterprise`;
nikezela ngesilawuli se-Ansible esixhaswayo uze ufake i-`requirements.yml` ngokwahlukeneyo.
Ugcino lunokufakwa nge-`ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz,,wordpress_enterprise`.
Iipakethe zemveli ziqulethe imithombo yendima kunye namaxwebhu kwaye aziqhubi naziphi na izikripthi
zokufakela ngexesha lofakelo. I-CI iyazifaka, iyazihlola kwaye iyazisusa zombini ezi fomathi.

## Ukhuseleko nelayisenisi

Jonga i-[SECURITY.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/SECURITY.md) kunye [nelayisenisi ye-MIT](../../../LICENSE). Imetadata yephakheji, umgaqo-nkqubo wenkxaso yeqonga, kunye noqinisekiso lokukhupha kufuneka zihlale zihambelana nendima ethunyelwayo.
