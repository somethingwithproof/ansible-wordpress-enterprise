<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · **Kinyarwanda** · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
- **Africa:** [Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · **Kinyarwanda** · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)
- **Asia:** [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [עברית](../he/README.md) · [मराठी](../mr/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [Bahasa Melayu](../ms/README.md) · [Filipino](../fil/README.md)

</details>
<!-- translations:end -->

# Ansible WordPress Enterprise

[![CI](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_ansible-wordpress-enterprise&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_ansible-wordpress-enterprise)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/ansible-wordpress-enterprise)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/releases)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/ansible-wordpress-enterprise/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/ansible-wordpress-enterprise)

Inshingano ya Ansible igenewe gutegura imashini za WordPress zifite PHP, seriveri y'urubuga, n'ububiko bw'amakuru bw'imbere cyangwa bwo hanze. Igenzura ry'urubuga n'amakuru yinjijwe rikorwa mbere y'ibyiciro byo gushyira mu bikorwa, mu gihe imipaka y'imirimo ituma ishyiraho, igenamiterere, n'igenzura bisuzumwa buri kimwe ukwayo.

## Amasezerano y'ishyirwa mu bikorwa yemewe

[meta/platform_support.yml](../../../meta/platform_support.yml) ni yo ifite ububasha ku politiki y'ubufasha. Urutonde ruhamye rwa Molecule rureba Ubuntu 24.04/PHP 8.3 na Ubuntu 26.04/PHP 8.5 hamwe na Nginx, Debian 13/PHP 8.4 hamwe na Nginx, na Rocky Linux 9 na 10/PHP 8.3 hamwe na Apache. Buri nzira igeragezwa kuri HTTP na HTTPS. Aya ni yo matsinda ya OS/PHP yageragejwe; guhindura urutonde rw'imashini werekeza ku matsinda atarageragejwe bitsindwa mbere y'impinduka za paki. Amazina ahagarariye EL ahuje iyi politiki, ariko ibimenyetso by'imikorere bituruka kuri container za Rocky Linux.

Abagenzuzi ba Python 3.12 bakoresha Ansible 14.6 cyangwa nshya mu cyiciro cya 14.x hamwe na ansible-core 2.21.6 cyangwa nshya mu cyiciro cya 2.21. Abagenzuzi ba Python 3.13 na 3.14 bakoresha Ansible 15.x hamwe na ansible-core 2.22.x. Ifungwa ry'ibisabwa rifite hash rihitamo itsinda rikwiye kuri interpreter y'umugenzuzi. Ibisabwa kuri interpreter y'imashini igenzurwa biratandukanye. Reba politiki mbere yo guhitamo verisiyo; imbuga zishaje na verisiyo za PHP zishyigikiwe gusa ku isoko y'ibanze ntizihita zemerwa.

## Urwego rw'ubukure bw'ibiranga

Urukurikirane rw'imirimo y'ibanze rusobanurwa muri [tasks/main.yml](../../../tasks/main.yml). Amatsinda yo kugenzura imikorere, kubika ikopi, Fail2ban, umutekano, kubika by'agateganyo, na firewall afite amasezerano y'inyandikorugero abura yanditswe muri [tests/unit/missing_templates.yml](../../../tests/unit/missing_templates.yml). Ibimenyetso byayo biguma bifunze mu buryo mbanziriza kandi igenzura ryanga gufungura amatsinda atuzuye. Amazina y'imirimo n'ibihindagurika by'urugero ntibigomba kugaragazwa nk'ishyirwa mu bikorwa rikora ry'ibyo biranga.

TLS, amakuru yo kwinjira mu bubiko bw'amakuru, amabanga ya WordPress yakozwe, uburinzi bw'inzira, n'imikorere yihariye ya OS bisaba igenamiterere ryanditswe n'igenzura mu gihe cy'imikorere. Nta kwimuka kwikora igihe habayeho ikibazo, nta masezerano y'ukuboneka kuri cloud yose (SLA), cyangwa icyemezo rusange cyo kuba biteguye gukoreshwa mu mikorere nyayo bitangwa hano.

## Gutangira byihuse

Shyiraho inshingano uhereye ku isoko y'ububiko bwayo n'ibyo ikenera byo mu matsinda:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git
ansible-galaxy collection install -r requirements.yml
```

Koresha itegeko ry'itsinda uhereye kuri iyi kopi y'ububiko. Suzuma [defaults/main.yml](../../../defaults/main.yml) n'[ingero](../../../examples/README.md) mbere yo gushyira mu bikorwa. Koresha uburyo bwo kwinjira bwemewe aho guhamagara ibyiciro by'imirimo y'imbere mu buryo butaziguye.

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

Tanga amabanga yavuzwe binyuze muri Ansible Vault cyangwa igikoresho gisanzwe gicunga amabanga. Tegura ibyemezo by'umutekano n'isobanura ry'izina ry'imashini igamijwe mbere yo gutangiza ishyirwa mu bikorwa. Gumisha amatsinda y'ibiranga atuzuye afunze.

## Iterambere n'igerageza

[Makefile](../../../Makefile), [CONTRIBUTING.md](../../../CONTRIBUTING.md), na [TESTING.md](../../../TESTING.md) bisobanura itegurwa ry'ibikenerwa bifite hash, igenzura rya lint, amagerageza y'ibice, n'amasezerano ya Docker/Molecule akoreshwa rimwe. Amagerageza y'ibice na lint ntibyemeza ko ishyirwa mu bikorwa rigenda neza.

```bash
make lint
```

Koresha inyandiko ifasha mu igerageza ku byitegererezo bihamye bya `default` na `tls` n'ibyo bisaba mbere. Imirimo yo gushyiraho ku mashini, kuvugurura, gusukura, no gusubizaho ihindura imashini zahiswemo; koresha urutonde rw'imashini z'igerageza zitandukanyijwe mu igenzura.

## Itangwa rya verisiyo na paki zisohorwa

Isohorwa ry'umushinga rikoresha verisiyo yuzuye ya SemVer iri muri `VERSION`, bitagendeye
kuri verisiyo ntoya ya Ansible iri muri `meta/main.yml`. Ohereza tag ihuye ya `v2.22.1` kuri main
kugira ngo utangize Release, cyangwa uyikoreshe n'intoki uhereye kuri main nyuma yo gukora tag ihuye.
Urukurikirane rw'ibikorwa rugenzura ko tag ihari yerekeza ku isoko yagenzuwe, rugakora urutonde rwose rwa CI
(harimo ibyitegererezo byose bine bya Molecule), kandi rugatangaza dosiye y'ububiko bw'inshingano
ikorana na Galaxy, paki ya Debian, RPM, `release.json` na `SHA256SUMS`.
Gutangaza bikoresha iyo tag isanzwe yagenzuwe bitahinduye intego mbanziriza ya API y'isohorwa,
kugira ngo ivugurura ry'urukurikirane rw'ibikorwa kuri main rizaza nyuma ritazasaba uburenganzira bwagutse
bwo kwandika ku rukurikirane rw'ibikorwa. Tag ibura cyangwa idahuye itsindwa mbere y'igerageza.

Genzura ibyamanuwe ukoresheje `sha256sum --check SHA256SUMS`. Shyiraho paki gakondo
ukoresheje `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` kuri Ubuntu
24.04 cyangwa `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` kuri
Rocky Linux 9. Zombi zishyira inshingano muri
`/usr/share/ansible/roles/wordpress_enterprise`; tanga umugenzuzi wa Ansible
wemewe kandi ushyireho `requirements.yml` ukwayo. Dosiye y'ububiko ishobora
gushyirwaho ukoresheje `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz`.
Paki gakondo zirimo inkomoko y'inshingano n'inyandiko kandi ntizikoresha inyandiko zo gushyira mu bikorwa
mu gihe cyo gushyiraho. CI ishyiraho, ikagenzura kandi igakuraho uburyo bwombi.

## Umutekano n'uruhushya

Reba [SECURITY.md](../../../SECURITY.md) n'[uruhushya rwa MIT](../../../LICENSE). Amakuru aranga paki, politiki y'ubufasha bw'urubuga, n'igenzura ry'isohorwa bigomba guhora bihuye n'inshingano yatanzwe.
