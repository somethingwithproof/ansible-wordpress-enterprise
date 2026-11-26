<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · **isiZulu** · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
- **Africa:** [Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · **isiZulu**
- **Asia:** [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [עברית](../he/README.md) · [मराठी](../mr/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [Bahasa Melayu](../ms/README.md) · [Filipino](../fil/README.md)

</details>
<!-- translations:end -->

# Ansible WordPress Enterprise

[![CI](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_ansible-wordpress-enterprise&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_ansible-wordpress-enterprise)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/ansible-wordpress-enterprise)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/releases)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/ansible-wordpress-enterprise/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/ansible-wordpress-enterprise)

Indima (role) ye-Ansible yokulungiselela imishini ye-WordPress nge-PHP, iseva yewebhu, kanye nesizindalwazi sendawo noma sangaphandle. Ukuqinisekiswa kwepulatifomu nokokufakiwe kusebenza ngaphambi kwezigaba zokuthunyelwa, kuyilapho imikhawulo yemisebenzi igcina ukufakwa, ukulungiselelwa, nokuqinisekiswa kubuyekezeka ngokwehlukana.

## Inkontileka yokuthunyelwa esekelwayo

I-[meta/platform_support.yml](../../../meta/platform_support.yml) ingumthombo osemthethweni wenqubomgomo yokusekelwa. Uhlaka oluzinzile lwe-Molecule luhlanganisa i-Ubuntu 24.04/PHP 8.3 ne-Ubuntu 26.04/PHP 8.5 nge-Nginx, i-Debian 13/PHP 8.4 nge-Nginx, kanye ne-Rocky Linux 9 no-10/PHP 8.3 nge-Apache. Yonke indlela ihlolwa nge-HTTP ne-HTTPS. Lawa ngamapheya e-OS/PHP ahloliwe; ukuguqulwa kwe-inventory kuya kumapheya angahloliwe kwehluleka ngaphambi koshintsho lwamaphakheji. Amagama afanayo e-EL abelana ngenqubomgomo, kodwa ubufakazi bokusebenza buvela kuma-container e-Rocky Linux.

Ama-controller e-Python 3.12 asebenzisa i-Ansible 14.6 noma entsha emgqeni we-14.x kanye ne-ansible-core 2.21.6 noma entsha emgqeni we-2.21. Ama-controller e-Python 3.13 no-3.14 asebenzisa i-Ansible 15.x kanye ne-ansible-core 2.22.x. Ukukhiya kwezidingo okune-hash kukhetha ipheya efanele umhumushi we-controller. Izidingo zomhumushi womshini ophethwe zihlukile. Bheka inqubomgomo ngaphambi kokukhetha izinhlobo zenguqulo; amapulatifomu amadala nezinhlobo ze-PHP ezisekelwa kuphela ngabakhi bazo (upstream) azamukelwa ngokuzenzakalelayo.

## Ukukhula kwezici

Ukulandelana okuyisisekelo kwemisebenzi kuchazwe ku-[tasks/main.yml](../../../tasks/main.yml). Amaqembu okuqapha (monitoring), okwenza ikhophi eyisipele, i-Fail2ban, ukuvikeleka, i-caching, kanye ne-firewall anezinkontileka zamathemphulethi ezishodayo ezirekhodwe ku-[tests/unit/missing_templates.yml](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/tests/unit/missing_templates.yml). Amafulegi awo ahlala evaliwe ngokuzenzakalelayo, futhi iqembu elingaphelele elivuliwe lima kuphela uma imisebenzi yalo isebenza, ngemva kokuba izigaba zangaphambili sezenzekile. Amagama emisebenzi nezibonelo zokuguquguqukayo (variables) akufanele kwethulwe njengokusebenza okuphelele kwalezo zici.

I-TLS, imininingwane yokungena yesizindalwazi, izimfihlo ze-WordPress ezikhiqiziwe, izivikeli zendlela, nokuphathwa okuqondene ne-OS kudinga izilungiselelo ezibhaliwe nokuhlolwa kokusebenza. Akukho ukuguqukela kokunye ngokuzenzakalelayo (failover), i-SLA yokutholakala kwefu lonke, noma isiqinisekiso sokulungela ukukhiqiza kuyo yonke indawo esenziwa lapha.

## Ukuqala ngokushesha

Faka indima (role) kusuka kumthombo wayo wenqolobane kanye nezidingo zayo zeqoqo:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git,HEAD,wordpress_enterprise
ansible-galaxy collection install -r requirements.yml
```

Sebenzisa umyalo weqoqo usuka kule khophi yekhodi. Buyekeza i-[defaults/main.yml](../../../defaults/main.yml) kanye [nezibonelo](../../../examples/README.md) ngaphambi kokuthumela. Sebenzisa indawo yokungena esekelwayo esikhundleni sokubiza izigaba zemisebenzi yangaphakathi ngqo.

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

Nikeza izimfihlo okukhulunywe ngazo nge-Ansible Vault noma ngomphathi wezimfihlo okhona. Lungiselela izitifiketi nokuxazululwa kwegama lomshini (hostname) kumshini oqondiswe kuwo ngaphambi kokwenza ukuthunyelwa. Gcina amaqembu ezici ezingaphelele evaliwe.

## Ukuthuthukiswa nokuhlola

I-[Makefile](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/Makefile), i-[CONTRIBUTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/CONTRIBUTING.md), kanye ne-[TESTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/TESTING.md) kuchaza ukusethwa kwezidingo okune-hash, ukuhlolwa kwe-lint, ukuhlolwa kweyunithi, kanye nezinkontileka ze-Docker/Molecule ezilahlwayo. Ukuhlolwa kweyunithi ne-lint akuqinisekisi ukuthunyelwa okuphumelelayo.

```bash
make lint
```

Sebenzisa umhlahlandlela wokuhlola ngezimo ezizinzile ze-`default` ne-`tls` kanye nezidingo zazo zangaphambili. Imisebenzi yokufaka kumshini, ukuthuthukisa inguqulo, ukuhlanza, nokubuyisela iguqula imishini ekhethiwe; sebenzisa ama-inventory okuhlola ahlukanisiwe ukuze uqinisekise.

## Ukuhlelwa kwezinguqulo namaphakheji okukhishwa

Ukukhishwa kwephrojekthi kusebenzisa inguqulo ephelele ye-SemVer eku-`VERSION`, ngokuzimela
enguqulweni encane ye-Ansible eku-`meta/main.yml`. Thumela ithegi efanayo ye-`v2.22.1` egatsheni elithi main
ukuze uqalise u-Release, noma uyiqalise ngesandla kusuka ku-main ngemuva kokudala ithegi efanayo.
Uhlelo lomsebenzi luqinisekisa ukuthi ithegi ekhona ikhomba kumthombo ohloliwe, lusebenzise lonke uhlelo lwe-CI
(kuhlanganise nazo zonke izimo ezine ze-Molecule), bese lushicilela ifayela eliqoqelwe lendima elihambisana ne-Galaxy,
iphakheji ye-Debian, i-RPM, i-`release.json` kanye ne-`SHA256SUMS`.
Ukushicilela kusebenzisa leyo thegi ekhona eqinisekisiwe ngaphandle kokushintsha umgomo ozenzakalelayo we-API
yokukhishwa, ukuze ukubuyekezwa kohlelo lomsebenzi okulandelayo ku-main kungadingi izimvume ezibanzi
zokubhala uhlelo lomsebenzi. Ithegi engekho noma engafani yehluleka ngaphambi kokuhlolwa.

Qinisekisa okulandiwe nge-`sha256sum --check SHA256SUMS`. Faka amaphakheji omdabu
nge-`sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` ku-Ubuntu
24.04 noma nge-`sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` ku-Rocky Linux 9.
Womabili afaka indima ngaphansi kwe-`/usr/share/ansible/roles/wordpress_enterprise`;
nikeza i-controller ye-Ansible esekelwayo bese ufaka i-`requirements.yml` ngokwehlukana. Ifayela eliqoqelwe lingafakwa
nge-`ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz,,wordpress_enterprise`.
Amaphakheji omdabu aqukethe imithombo yendima nemibhalo futhi awasebenzisi imibhalo yokuthunyelwa
ngesikhathi sokufakwa. I-CI ifaka, ihlole futhi isuse zombili izinhlobo.

## Ukuvikeleka nelayisense

Bheka i-[SECURITY.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/SECURITY.md) kanye [nelayisense ye-MIT](../../../LICENSE). Imethadatha yephakheji, inqubomgomo yokusekelwa kwepulatifomu, nokuqinisekiswa kokukhishwa kufanele kuhlale kuhambisana nendima ethunyelwayo.
