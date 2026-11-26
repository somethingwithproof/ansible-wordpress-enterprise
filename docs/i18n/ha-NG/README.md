<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · **Hausa** · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
- **Africa:** [Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · **Hausa** · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)
- **Asia:** [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [עברית](../he/README.md) · [मराठी](../mr/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [Bahasa Melayu](../ms/README.md) · [Filipino](../fil/README.md)

</details>
<!-- translations:end -->

# Ansible WordPress Enterprise

[![CI](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_ansible-wordpress-enterprise&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_ansible-wordpress-enterprise)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/ansible-wordpress-enterprise)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/releases)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/ansible-wordpress-enterprise/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/ansible-wordpress-enterprise)

Aikin Ansible ne don saita na'urorin WordPress tare da PHP, uwar garken yanar gizo, da rumbun adana bayanai na gida ko na waje. Tantancewar dandamali da shigarwa suna gudana kafin matakan turawa, yayin da iyakokin ayyuka ke kiyaye girkawa, saitawa, da tabbatarwa a rabe don sauƙin dubawa.

## Yarjejeniyar turawa da ake goyon baya

[meta/platform_support.yml](../../../meta/platform_support.yml) ne babban tushen manufar goyon baya. Tsarin gwajin Molecule mai ƙarfi ya ƙunshi Ubuntu 24.04/PHP 8.3 da Ubuntu 26.04/PHP 8.5 tare da Nginx, Debian 13/PHP 8.4 tare da Nginx, da kuma Rocky Linux 9 da 10/PHP 8.3 tare da Apache. Ana gwada kowace hanya ta HTTP da HTTPS. Waɗannan su ne nau'ikan haɗin OS/PHP da aka gwada; canje-canjen inventory zuwa haɗin da ba a gwada ba suna kasawa kafin a canza fakiti. Sunayen madadin EL suna raba manufar guda, amma shaidar aikin zahiri tana fitowa ne daga kwantenonin Rocky Linux.

Masu sarrafawa (controllers) na Python 3.12 suna amfani da Ansible 14.6 ko sabo a layin 14.x tare da ansible-core 2.21.6 ko sabo a layin 2.21. Masu sarrafawa na Python 3.13 da 3.14 suna amfani da Ansible 15.x tare da ansible-core 2.22.x. Fayil ɗin kulle buƙatu mai hash yana zaɓar haɗin da ya dace da mai fassarar (interpreter) mai sarrafawa. Buƙatun mai fassarar na'urar da ake sarrafawa daban suke. Duba manufar kafin zaɓar sigogi; ba a karɓar tsofaffin dandamali ko sigogin PHP da ke samun goyon bayan tushe kaɗai kai tsaye ba.

## Balagar fasaloli

An bayyana jerin manyan ayyuka a cikin [tasks/main.yml](../../../tasks/main.yml). Rukunonin sa ido, ajiyar baya, Fail2ban, tsaro, adanar wucin gadi (caching), da firewall suna da yarjejeniyoyin samfuri da suka ɓata waɗanda aka rubuta a [tests/unit/missing_templates.yml](../../../tests/unit/missing_templates.yml). Alamomin kunnawa nasu suna kashe a matsayin tsoho kuma tantancewa tana ƙin kunna rukunonin da ba su cika ba. Kada a gabatar da sunayen ayyuka da misalan masu canji a matsayin aiwatarwa masu aiki na waɗannan fasalolin.

TLS, takardun shaidar rumbun adana bayanai, sirrikan WordPress da aka samar, masu tsaron hanya, da sarrafawa ta musamman ga OS suna buƙatar saitin da aka rubuta da kuma binciken lokacin aiki. Ba a da'awar sauyawa ta atomatik yayin gazawa (failover), yarjejeniyar samuwar sabis ta girgije (SLA), ko shiryawa gaba ɗaya don aikin zahiri a nan.

## Fara aiki da sauri

Girka aikin (role) daga tushen ma'ajiyarsa da abubuwan dogaro na tarinsa:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git,HEAD,wordpress_enterprise
ansible-galaxy collection install -r requirements.yml
```

Gudanar da umarnin tarin daga wannan kwafin ma'ajiyar. Duba [defaults/main.yml](../../../defaults/main.yml) da [misalai](../../../examples/README.md) kafin turawa. Yi amfani da hanyar shigar da ake goyon baya maimakon kiran matakan ayyukan cikin gida kai tsaye.

```yaml
- hosts: wordpress_test_hosts
  become: true
  vars:
    wordpress_web_server: nginx
    wordpress_site_url: "http://wordpress.example.com"
    wordpress_server_name: wordpress.example.com
    wordpress_admin_password: "{{ vault_wordpress_admin_password }}"
    wordpress_db_password: "{{ vault_wordpress_db_password }}"
    wordpress_db_root_password: "{{ vault_wordpress_db_root_password }}"
  roles:
    - wordpress_enterprise
```

Samar da sirrikan da aka ambata ta hanyar Ansible Vault ko manajan sirri da ke akwai. Saita takardun shaida da fassarar sunan na'ura (hostname resolution) don na'urar da aka yi niyya kafin gudanar da turawa. Bar rukunonin fasalolin da ba su cika ba a kashe.

## Haɓakawa da gwaji

[Makefile](../../../Makefile), [CONTRIBUTING.md](../../../CONTRIBUTING.md), da [TESTING.md](../../../TESTING.md) suna bayyana saitin abubuwan dogaro mai hash, binciken lint, gwaje-gwajen sashe (unit tests), da yarjejeniyoyin Docker/Molecule masu zubarwa. Gwaje-gwajen sashe da lint ba sa tabbatar da nasarar turawa.

```bash
make lint
```

Yi amfani da jagorar gwaji don yanayin gwaji masu ƙarfi na `default` da `tls` da buƙatunsu na farko. Ayyukan girkawa, haɓakawa, tsaftacewa, da maidowa suna canza na'urorin da aka zaɓa; yi amfani da keɓantattun jerin na'urorin gwaji (inventories) don tantancewa.

## Sanya sigar lamba da fakitin saki

Sakin aikin yana amfani da cikakkiyar sigar SemVer da ke cikin `VERSION`, ba tare da dogara da
mafi ƙarancin sigar Ansible a cikin `meta/main.yml` ba. Tura alamar (tag) mai dacewa ta `v2.22.1` a kan main
don tayar da saki (Release), ko ka gudanar da shi da hannu daga main bayan ƙirƙirar alamar da ta dace.
Tsarin aikin yana tabbatar da cewa alamar da ke akwai tana nuna tushen da aka bincika, yana gudanar da cikakken jerin gwaje-gwajen CI
(gami da duk yanayin gwajin Molecule guda huɗu), sannan yana wallafa kundin ajiyar role mai dacewa da Galaxy,
fakitin Debian, RPM, `release.json` da `SHA256SUMS`.
Wallafawa tana amfani da wannan alamar da aka tabbatar ba tare da maye gurbin tsohon makasudin API na saki ba,
don haka sabuntawar tsarin aiki a nan gaba a kan main ba ya buƙatar ƙarin izinin rubuta tsarin aiki.
Alamar da ta ɓata ko ba ta dace ba tana kasawa kafin gwaji.

Tabbatar da abubuwan da aka sauke da `sha256sum --check SHA256SUMS`. Girka fakiti na asali
da `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` a kan Ubuntu
24.04 ko `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` a kan
Rocky Linux 9. Dukansu biyu suna girka aikin a ƙarƙashin
`/usr/share/ansible/roles/wordpress_enterprise`; ka samar da mai sarrafa Ansible da ake goyon baya
kuma ka girka `requirements.yml` daban. Ana iya girka kundin ajiyar
da `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz,,wordpress_enterprise`.
Fakiti na asali suna ɗauke da tushen aikin da takardu kuma ba sa gudanar da wani rubutun turawa
yayin girkawa. CI yana girkawa, bincikawa da cire duka nau'ikan biyu.

## Tsaro da lasisi

Duba [SECURITY.md](../../../SECURITY.md) da [lasisin MIT](../../../LICENSE). Bayanan metadata na fakiti, manufar goyon bayan dandamali, da tantancewar saki dole su ci gaba da kasancewa a daidai da aikin da aka tura.
