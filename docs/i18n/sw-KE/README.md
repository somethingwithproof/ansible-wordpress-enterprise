<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · **Kiswahili** · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
- **Africa:** [Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · **Kiswahili** · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)
- **Asia:** [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [עברית](../he/README.md) · [मराठी](../mr/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [Bahasa Melayu](../ms/README.md) · [Filipino](../fil/README.md)

</details>
<!-- translations:end -->

# Ansible WordPress Enterprise

[![CI](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_ansible-wordpress-enterprise&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_ansible-wordpress-enterprise)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/ansible-wordpress-enterprise)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/releases)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/ansible-wordpress-enterprise/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/ansible-wordpress-enterprise)

Role ya Ansible ya kusanidi mashine za WordPress zenye PHP, seva ya wavuti, na hifadhidata ya ndani au ya nje. Uthibitishaji wa jukwaa na data za ingizo hufanyika kabla ya hatua za utekelezaji, huku mipaka ya kazi ikiwezesha usakinishaji, usanidi, na uthibitishaji kukaguliwa kando.

## Mkataba wa utekelezaji unaotumika

[meta/platform_support.yml](../../../meta/platform_support.yml) ndiyo mamlaka ya sera ya usaidizi. Jedwali thabiti la Molecule linajumuisha Ubuntu 24.04/PHP 8.3 na Ubuntu 26.04/PHP 8.5 na Nginx, Debian 13/PHP 8.4 na Nginx, na Rocky Linux 9 na 10/PHP 8.3 na Apache. Kila njia hujaribiwa kupitia HTTP na HTTPS. Hizi ndizo jozi za mfumo endeshi/PHP zilizothibitishwa; mabadiliko ya orodha ya mashine kwa jozi ambazo hazijajaribiwa hushindwa kabla ya mabadiliko ya vifurushi. Majina mengine ya EL hutumia sera hiyo hiyo, lakini ushahidi wa uendeshaji unatoka kwa kontena za Rocky Linux.

Vidhibiti vya Python 3.12 hutumia Ansible 14.6 au toleo jipya zaidi katika mfululizo wa 14.x pamoja na ansible-core 2.21.6 au toleo jipya zaidi katika mfululizo wa 2.21. Vidhibiti vya Python 3.13 na 3.14 hutumia Ansible 15.x pamoja na ansible-core 2.22.x. Faili ya kufuli ya mahitaji yenye hashi huchagua jozi inayofaa kwa mkalimani wa kidhibiti. Mahitaji ya mkalimani wa mashine zinazosimamiwa ni tofauti. Rejelea sera kabla ya kuchagua matoleo; majukwaa ya zamani na matoleo ya PHP yanayotumika tu na chanzo kikuu hayakubaliwi kiotomatiki.

## Ukomavu wa vipengele

Mlolongo mkuu wa kazi umefafanuliwa katika [tasks/main.yml](../../../tasks/main.yml). Vikundi vya ufuatiliaji, nakala rudufu, Fail2ban, usalama, akiba ya muda (caching), na firewall vina mikataba ya violezo inayokosekana iliyorekodiwa katika [tests/unit/missing_templates.yml](../../../tests/unit/missing_templates.yml). Bendera zake hubaki zimezimwa kwa chaguo-msingi na uthibitishaji hukataa kuwasha vikundi visivyokamilika. Majina ya kazi na vigeu vya mifano havipaswi kuwasilishwa kama utekelezaji unaofanya kazi wa vipengele hivyo.

TLS, vitambulisho vya hifadhidata, siri za WordPress zinazozalishwa, ulinzi wa njia za faili, na ushughulikiaji mahususi wa mfumo endeshi huhitaji usanidi ulioandikwa na ukaguzi wakati wa uendeshaji. Hakuna uhamishaji wa kiotomatiki wakati wa hitilafu, SLA ya upatikanaji wa wingu zima, wala dai la utayari wa uzalishaji kwa mazingira yote linalotolewa hapa.

## Kuanza haraka

Sakinisha role kutoka chanzo cha hazina yake pamoja na vitegemezi vyake vya mkusanyiko:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git
ansible-galaxy collection install -r requirements.yml
```

Endesha amri ya mkusanyiko kutoka nakala hii ya hazina. Kagua [defaults/main.yml](../../../defaults/main.yml) na [mifano](../../../examples/README.md) kabla ya utekelezaji. Tumia njia ya kuingilia inayotumika badala ya kuita hatua za kazi za ndani moja kwa moja.

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

Weka siri zilizorejelewa kupitia Ansible Vault au kidhibiti cha siri kilichopo. Sanidi vyeti na utatuzi wa jina la mashine lengwa kabla ya kuendesha utekelezaji. Acha vikundi vya vipengele visivyokamilika vimezimwa.

## Uendelezaji na majaribio

[Makefile](../../../Makefile), [CONTRIBUTING.md](../../../CONTRIBUTING.md), na [TESTING.md](../../../TESTING.md) hufafanua usanidi wa vitegemezi vyenye hashi, ukaguzi wa lint, majaribio ya vitengo, na mikataba ya muda ya Docker/Molecule. Majaribio ya vitengo na lint havithibitishi utekelezaji wenye mafanikio.

```bash
make lint
```

Tumia mwongozo wa majaribio kwa matukio thabiti ya `default` na `tls` pamoja na mahitaji yake ya awali. Kazi za usakinishaji, usasishaji, usafishaji, na urejeshaji hubadilisha mashine zilizochaguliwa; tumia orodha za majaribio zilizotengwa kwa uthibitishaji.

## Matoleo na vifurushi vya uchapishaji

Matoleo ya mradi hutumia toleo kamili la SemVer katika `VERSION`, bila kutegemea toleo la chini la Ansible katika `meta/main.yml`. Sukuma lebo inayolingana ya `v2.22.1` kwenye tawi la main ili kuanzisha Release, au uendeshe mtiririko huo kwa mkono kutoka main baada ya kuunda lebo inayolingana. Mtiririko wa kazi huthibitisha kuwa lebo iliyopo inaelekeza kwenye msimbo uliokaguliwa, huendesha seti kamili ya CI (ikiwa ni pamoja na matukio yote manne ya Molecule), na huchapisha kumbukumbu ya role inayolingana na Galaxy, kifurushi cha Debian, RPM, `release.json` na `SHA256SUMS`. Uchapishaji hutumia lebo hiyo iliyothibitishwa bila kubatilisha lengo chaguo-msingi la API ya uchapishaji, hivyo sasisho la baadaye la mtiririko wa kazi kwenye main halihitaji ruhusa pana zaidi za uandishi wa mtiririko wa kazi. Lebo inayokosekana au isiyolingana hushindwa kabla ya majaribio.

Thibitisha faili zilizopakuliwa kwa `sha256sum --check SHA256SUMS`. Sakinisha vifurushi asili kwa `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` kwenye Ubuntu 24.04 au `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` kwenye Rocky Linux 9. Vyote viwili husakinisha role katika `/usr/share/ansible/roles/wordpress_enterprise`; tumia kidhibiti cha Ansible kinachotumika na usakinishe `requirements.yml` kando. Kumbukumbu inaweza kusakinishwa kwa `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz`. Vifurushi asili vina msimbo chanzo wa role na nyaraka na haviendeshi hati zozote za utekelezaji wakati wa usakinishaji. CI husakinisha, hukagua na kuondoa miundo yote miwili.

## Usalama na leseni

Tazama [SECURITY.md](../../../SECURITY.md) na [leseni ya MIT](../../../LICENSE). Metadata ya kifurushi, sera ya usaidizi wa jukwaa, na uthibitishaji wa toleo lazima vibaki vinawiana na role iliyochapishwa.
