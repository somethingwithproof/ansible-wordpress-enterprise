<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · **Igbo** · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
- **Africa:** [Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · **Igbo** · [Malagasy](../mg-MG/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)
- **Asia:** [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [עברית](../he/README.md) · [मराठी](../mr/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [Bahasa Melayu](../ms/README.md) · [Filipino](../fil/README.md)

</details>
<!-- translations:end -->

# Ansible WordPress Enterprise

[![CI](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_ansible-wordpress-enterprise&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_ansible-wordpress-enterprise)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/ansible-wordpress-enterprise)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/releases)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/ansible-wordpress-enterprise/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/ansible-wordpress-enterprise)

Ọrụ Ansible maka ịhazi host WordPress nwere PHP, sava weebụ, na nchekwa data dị n'ime ma ọ bụ nke mpụga. Nnyocha nke ikpo okwu na ntinye data na-agba ọsọ tupu ọkwa ntinye n'ọrụ, ebe oke ọrụ na-eme ka nwụnye, nhazi, na nkwenye dị iche iche maka nyocha.

## Nkwekọrịta ntinye n'ọrụ a kwadoro

[meta/platform_support.yml](../../../meta/platform_support.yml) bụ isi ikike maka atụmatụ nkwado. Usoro nnwale Molecule kwụsịrị ike na-ekpuchi Ubuntu 24.04/PHP 8.3 na Ubuntu 26.04/PHP 8.5 na Nginx, Debian 13/PHP 8.4 na Nginx, yana Rocky Linux 9 na 10/PHP 8.3 na Apache. A na-anwale ụzọ ọ bụla site na HTTP na HTTPS. Ndị a bụ njikọta OS/PHP a nwalere; ngbanwe ndepụta gaa na njikọta a na-anwalebeghị na-ada tupu mgbanwe ngwugwu. Aha ndị ọzọ nke EL na-ekerịta atụmatụ ahụ, mana ihe akaebe oge ọrụ sitere na container Rocky Linux.

Controller Python 3.12 na-eji Ansible 14.6 ma ọ bụ nke ọhụrụ karịa n'ahịrị 14.x yana ansible-core 2.21.6 ma ọ bụ nke ọhụrụ karịa n'ahịrị 2.21. Controller Python 3.13 na 3.14 na-eji Ansible 15.x yana ansible-core 2.22.x. Mkpọchi ihe a chọrọ nwere hash na-ahọrọ njikọta maka interpreter nke controller. Ihe a chọrọ maka interpreter nke nọọdụ a na-achịkwa dị iche. Lelee atụmatụ ahụ tupu ịhọrọ ụdị; a naghị anabata ikpo okwu ochie na ụdị PHP nke naanị upstream kwadoro n'akpaghị aka.

## Ntozuoke nke atụmatụ ọrụ

A kọwara usoro ọrụ bụ isi na [tasks/main.yml](../../../tasks/main.yml). Otu nlekọta, nchekwa ndabere, Fail2ban, nchekwa, caching, na firewall nwere nkwekọrịta ndebiri na-efu e dekọrọ na [tests/unit/missing_templates.yml](../../../tests/unit/missing_templates.yml). Flag ha ka gbanyụrụ na ndabara ma nnyocha na-ajụ ịgbanye otu ndị ezughị oke. E kwesịghị igosi aha ọrụ na variable ihe atụ dị ka mmejupụta na-arụ ọrụ nke atụmatụ ndị ahụ.

TLS, nzere nchekwa data, ihe nzuzo WordPress a rụpụtara, nchedo ụzọ faịlụ, na njikwa pụrụ iche maka OS chọrọ nhazi e dere ede na nnyocha oge ọrụ. Enweghị nkwupụta e mere ebe a maka mgbanwe ọdịda n'akpaghị aka, SLA nnweta n'igwe ojii niile, ma ọ bụ njikere mmepụta maka ebe niile.

## Mmalite ngwa ngwa

Wụnye ọrụ a site n'isi mmalite ebe nchekwa ya na ndabere mkpokọta ya:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git
ansible-galaxy collection install -r requirements.yml
```

Gbaa iwu mkpokọta ahụ site na nkopi koodu a. Lelee [defaults/main.yml](../../../defaults/main.yml) na [ihe atụ](../../../examples/README.md) tupu ntinye n'ọrụ. Jiri ebe mbanye a kwadoro kama ịkpọ ọkwa ọrụ dị n'ime ozugbo.

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

Nye ihe nzuzo ndị e zoro aka na ha site na Ansible Vault ma ọ bụ njikwa ihe nzuzo dịbu. Hazie asambodo na mkpebi hostname maka host e zubere tupu ịgba ntinye n'ọrụ. Dobe otu atụmatụ ndị ezughị oke ka ha gbanyụọ.

## Mmepe na nnwale

[Makefile](../../../Makefile), [CONTRIBUTING.md](../../../CONTRIBUTING.md), na [TESTING.md](../../../TESTING.md) na-akọwa nhazi ndabere nwere hash, nnyocha lint, nnwale ngalaba, na nkwekọrịta Docker/Molecule a na-ekpofu ekpofu. Nnwale ngalaba na lint egosighị na ntinye n'ọrụ ga-aga nke ọma.

```bash
make lint
```

Jiri ntụziaka nnwale maka ọnọdụ `default` na `tls` kwụsịrị ike na ihe ndị e buru ụzọ chọọ maka ha. Ọrụ nwụnye host, nkwalite, nhicha, na iweghachi na-agbanwe igwe ndị a họọrọ; jiri ndepụta nnwale kewapụrụ iche maka nnyocha.

## Nhazi ụdị na ngwugwu ntọhapụ

Ntọhapụ ọrụ na-eji ụdị SemVer zuru oke dị na `VERSION`, n'adabereghị
n'ụdị Ansible kacha nta dị na `meta/main.yml`. Ziga mkpado `v2.22.1` dabara adaba na main
iji kpalite Release, ma ọ bụ gbaa ya n'aka site na main mgbe i mepụtara mkpado dabara adaba.
Usoro ọrụ ahụ na-enyocha na mkpado dịbu na-ezo aka n'isi mmalite a nyochara, na-agba usoro CI
zuru oke (gụnyere ọnọdụ Molecule anọ niile), ma na-ebipụta archive ọrụ
dabara na Galaxy, ngwugwu Debian, RPM, `release.json` na `SHA256SUMS`.
Mbipụta na-eji mkpado ahụ dịbu e kwadoro n'agbanweghị ebumnuche ndabara nke API ntọhapụ,
ka mmelite usoro ọrụ ọzọ na main ghara ịchọ
nzere ide usoro ọrụ sara mbara karịa. Mkpado na-efu ma ọ bụ nke na-adabaghị na-ada tupu nnwale.

Nyochaa faịlụ e budatara site na `sha256sum --check SHA256SUMS`. Wụnye ngwugwu nke sistemụ
site na `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` na Ubuntu
24.04 ma ọ bụ `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` na
Rocky Linux 9. Ha abụọ na-awụnye ọrụ ahụ n'okpuru
`/usr/share/ansible/roles/wordpress_enterprise`; nye controller Ansible a kwadoro
ma wụnye `requirements.yml` iche. Enwere ike ịwụnye archive ahụ
site na `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz`.
Ngwugwu nke sistemụ nwere isi mmalite ọrụ na akwụkwọ nkọwa ma anaghị agba skriptị ntinye n'ọrụ
ọ bụla n'oge nwụnye. CI na-awụnye, na-enyocha ma na-ewepụ ụdị abụọ ahụ.

## Nchekwa na ikikere

Hụ [SECURITY.md](../../../SECURITY.md) na [ikikere MIT](../../../LICENSE). Metadata ngwugwu, atụmatụ nkwado ikpo okwu, na nnyocha ntọhapụ ga-anọgide na-adakọrịta na ọrụ e wepụtara.
