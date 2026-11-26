<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · **Yorùbá** · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
- **Africa:** [Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [isiXhosa](../xh-ZA/README.md) · **Yorùbá** · [isiZulu](../zu-ZA/README.md)
- **Asia:** [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [עברית](../he/README.md) · [मराठी](../mr/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [Bahasa Melayu](../ms/README.md) · [Filipino](../fil/README.md)

</details>
<!-- translations:end -->

# Ansible WordPress Enterprise

[![CI](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_ansible-wordpress-enterprise&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_ansible-wordpress-enterprise)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/ansible-wordpress-enterprise)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/releases)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/ansible-wordpress-enterprise/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/ansible-wordpress-enterprise)

Ipa Ansible kan fún ṣíṣètò àwọn ẹ̀rọ olùgbàlejò WordPress pẹ̀lú PHP, ẹ̀rọ-ìpèsè wẹ́ẹ̀bù, àti ibi-ìpamọ́ dátà abẹ́lé tàbí ti ìta. Ìjẹ́rìísí pẹpẹ àti ìtẹ̀wọlé máa ń ṣiṣẹ́ ṣáájú àwọn ìpele ìgbékalẹ̀, nígbà tí àwọn ààlà iṣẹ́ ń jẹ́ kí ìfisílẹ̀, ìṣètò, àti ìjẹ́rìísí ṣeé ṣàyẹ̀wò lọ́tọ̀ọ̀tọ̀.

## Àdéhùn ìgbékalẹ̀ tí a ṣètìlẹ́yìn fún

[meta/platform_support.yml](../../../meta/platform_support.yml) ni orísun àṣẹ fún ìlànà àtìlẹ́yìn. Àtẹ Molecule tí ó dúró ṣinṣin bo Ubuntu 24.04/PHP 8.3 àti Ubuntu 26.04/PHP 8.5 pẹ̀lú Nginx, Debian 13/PHP 8.4 pẹ̀lú Nginx, àti Rocky Linux 9 àti 10/PHP 8.3 pẹ̀lú Apache. Gbogbo ọ̀nà ni a dán wò lórí HTTP àti HTTPS. Àwọn wọ̀nyí ni àwọn àpapọ̀ OS/PHP tí a ti dán wò; àwọn àyípadà àkójọ-ẹ̀rọ sí àwọn àpapọ̀ tí a kò tíì dán wò yóò kùnà ṣáájú àwọn àyípadà àpò. Àwọn orúkọ-ìtọ́kasí EL pín ìlànà náà, ṣùgbọ́n ẹ̀rí ìṣiṣẹ́ wá láti àwọn àpótí-ẹ̀rọ Rocky Linux.

Àwọn olùṣàkóso Python 3.12 ń lo Ansible 14.6 tàbí ẹ̀yà tuntun nínú ìlà 14.x pẹ̀lú ansible-core 2.21.6 tàbí ẹ̀yà tuntun nínú ìlà 2.21. Àwọn olùṣàkóso Python 3.13 àti 3.14 ń lo Ansible 15.x pẹ̀lú ansible-core 2.22.x. Ìtìpa àwọn ohun-ìbéèrè tí a ṣe haṣì rẹ̀ ni ó ń yan àpapọ̀ náà fún olùtúmọ̀ olùṣàkóso. Àwọn ohun-ìbéèrè olùtúmọ̀ fún ẹ̀rọ tí a ń ṣàkóso wà lọ́tọ̀. Wo ìlànà náà kí o tó yan àwọn ẹ̀yà; àwọn pẹpẹ àtijọ́ àti àwọn ẹ̀yà PHP tí orísun-òkè nìkan ń ṣètìlẹ́yìn fún kì í ṣe gbígba lọ́gán láìṣe àyẹ̀wò.

## Ìpele ìdàgbà àwọn ẹ̀yà-iṣẹ́

A ṣàlàyé ìtòlẹ́sẹẹsẹ iṣẹ́ pàtàkì nínú [tasks/main.yml](../../../tasks/main.yml). Àwọn ẹgbẹ́ àbójútó, àdàkọ ààbò, Fail2ban, ààbò, ìfipamọ́ kíákíá, àti ògiri-iná ní àwọn àdéhùn àwòkọ́ṣe tí ó sọnù tí a ṣàkọsílẹ̀ nínú [tests/unit/missing_templates.yml](../../../tests/unit/missing_templates.yml). Àwọn àsíá wọn wà ní ìpa ní ìbẹ̀rẹ̀, ìjẹ́rìísí sì ń kọ̀ láti tan àwọn ẹgbẹ́ tí kò pé. A kò gbọ́dọ̀ fi àwọn orúkọ iṣẹ́ àti àwọn àpẹẹrẹ oníyípadà hàn gẹ́gẹ́ bí ìmúṣẹ tí ń ṣiṣẹ́ fún àwọn ẹ̀yà-iṣẹ́ wọ̀nyẹn.

TLS, àwọn ẹ̀rí ìwọlé ibi-ìpamọ́ dátà, àwọn àṣírí WordPress tí a ṣẹ̀dá, àwọn ìṣọ́ ọ̀nà, àti ìṣàkóso pàtó fún OS nílò ìṣètò tí a kọ sílẹ̀ àti àwọn ìṣàyẹ̀wò nígbà ìṣiṣẹ́. Kò sí ìpèsè ìyípadà-àìdáwọ́dúró aládàáṣe, SLA wíwà-ní-ìmúrasílẹ̀ káàkiri àwọsánmà, tàbí ẹ̀tọ́ ìmúrasílẹ̀ fún ìṣẹ̀dá gidi ní gbogbo ibi tí a sọ níbí.

## Ìbẹ̀rẹ̀ kíákíá

Fi ipa náà sórí ẹ̀rọ láti orísun ibi-ìpamọ́ rẹ̀ àti àwọn ìgbẹ́kẹ̀lé àkójọpọ̀ rẹ̀:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git,HEAD,wordpress_enterprise
ansible-galaxy collection install -r requirements.yml
```

Ṣiṣẹ́ àṣẹ àkójọpọ̀ náà láti inú àdàkọ ìṣiṣẹ́ yìí. Ṣàyẹ̀wò [defaults/main.yml](../../../defaults/main.yml) àti [àwọn àpẹẹrẹ](../../../examples/README.md) ṣáájú ìgbékalẹ̀. Lo ojú-ọ̀nà ìbẹ̀rẹ̀ tí a ṣètìlẹ́yìn fún dípò pípè àwọn ìpele iṣẹ́ abẹ́lé tààrà.

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

Pèsè àwọn àṣírí tí a tọ́ka sí nípasẹ̀ Ansible Vault tàbí olùṣàkóso àṣírí tí ó wà tẹ́lẹ̀. Ṣètò àwọn ìwé-ẹ̀rí àti ìtúmọ̀ orúkọ-ẹ̀rọ fún ẹ̀rọ olùgbàlejò ìfojúsùn ṣáájú ṣíṣiṣẹ́ ìgbékalẹ̀. Pa àwọn ẹgbẹ́ ẹ̀yà-iṣẹ́ tí kò pé mọ́ ní ìpa.

## Ìdàgbàsókè àti ìdánwò

[Makefile](../../../Makefile), [CONTRIBUTING.md](../../../CONTRIBUTING.md), àti [TESTING.md](../../../TESTING.md) ṣàlàyé ìṣètò ìgbẹ́kẹ̀lé tí a ṣe haṣì rẹ̀, àwọn ìṣàyẹ̀wò lint, àwọn ìdánwò ẹyọkan, àti àwọn àdéhùn Docker/Molecule tí a lè dà nù lẹ́yìn ìlò. Àwọn ìdánwò ẹyọkan àti lint kò fìdí ìgbékalẹ̀ àṣeyọrí múlẹ̀.

```bash
make lint
```

Lo ìtọ́sọ́nà ìdánwò fún àwọn ìṣẹ̀lẹ̀ `default` àti `tls` tí ó dúró ṣinṣin àti àwọn ohun-ìbéèrè wọn ṣáájú. Àwọn iṣẹ́ ìfisílẹ̀ ẹ̀rọ olùgbàlejò, ìgbéga, ìwẹ̀nùmọ́, àti ìdápadà máa ń yí àwọn ẹ̀rọ tí a yàn padà; lo àwọn àkójọ-ẹ̀rọ ìdánwò tí a yà sọ́tọ̀ fún ìjẹ́rìísí.

## Ìṣètò ẹ̀yà àti àwọn àpò ìtújáde

Àwọn ìtújáde iṣẹ́ àkànṣe ń lo ẹ̀yà SemVer pípé nínú `VERSION`, lọ́tọ̀ sí ẹ̀yà Ansible tó kéré jùlọ nínú `meta/main.yml`. Tì àmì `v2.22.1` tí ó bá a mu lọ sí main láti mú Release ṣiṣẹ́, tàbí ṣiṣẹ́ rẹ̀ pẹ̀lú ọwọ́ láti main lẹ́yìn ṣíṣẹ̀dá àmì tí ó bá a mu. Ìṣàn-iṣẹ́ náà ń jẹ́rìísí pé àmì tí ó wà tẹ́lẹ̀ tọ́ka sí orísun tí a ṣàyẹ̀wò, ó ń ṣiṣẹ́ gbogbo àkójọ CI (pẹ̀lú gbogbo ìṣẹ̀lẹ̀ Molecule mẹ́rẹ̀ẹ̀rin), ó sì ń tẹ àpò-ìpamọ́ ipa tí ó bá Galaxy mu, àpò Debian, RPM, `release.json`, àti `SHA256SUMS` jáde. Ìtẹ̀jáde ń lo àmì tí ó wà tẹ́lẹ̀ tí a ti jẹ́rìísí láìyí ìfojúsùn àkọ́kọ́ ti API ìtújáde padà, nítorí náà àtúnṣe ìṣàn-iṣẹ́ tí ó tẹ̀lé e lórí main kò nílò àwọn ẹ̀rí ìwọlé kíkọ ìṣàn-iṣẹ́ tí ó gbòòrò sí i. Àmì tí ó sọnù tàbí tí kò bá mu yóò kùnà ṣáájú ìdánwò.

Jẹ́rìísí àwọn ìgbàsílẹ̀ pẹ̀lú `sha256sum --check SHA256SUMS`. Fi àwọn àpò abínibí sórí ẹ̀rọ pẹ̀lú `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` lórí Ubuntu 24.04 tàbí `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` lórí Rocky Linux 9. Àwọn méjèèjì ń fi ipa náà sílẹ̀ lábẹ́ `/usr/share/ansible/roles/wordpress_enterprise`; pèsè olùṣàkóso Ansible tí a ṣètìlẹ́yìn fún kí o sì fi `requirements.yml` sórí ẹ̀rọ lọ́tọ̀. A lè fi àpò-ìpamọ́ náà sórí ẹ̀rọ pẹ̀lú `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz,,wordpress_enterprise`. Àwọn àpò abínibí ní àwọn orísun ipa àti ìwé-àkọsílẹ̀ nínú, wọn kò sì ṣiṣẹ́ ìwé-àṣẹ ìgbékalẹ̀ kankan nígbà ìfisílẹ̀. CI ń fi àwọn ọ̀nà méjèèjì sórí ẹ̀rọ, ó ń ṣàyẹ̀wò wọn, ó sì ń yọ wọ́n kúrò.

## Ààbò àti ìwé-àṣẹ

Wo [SECURITY.md](../../../SECURITY.md) àti [ìwé-àṣẹ MIT](../../../LICENSE). Àwọn dátà-àpèjúwe àpò, ìlànà àtìlẹ́yìn pẹpẹ, àti ìjẹ́rìísí ìtújáde gbọ́dọ̀ bá ipa tí a fi ránṣẹ́ mu nígbà gbogbo.
