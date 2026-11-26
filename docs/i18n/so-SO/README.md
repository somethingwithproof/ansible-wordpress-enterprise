<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · **Soomaali** · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
- **Africa:** [Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [Kinyarwanda](../rw-RW/README.md) · **Soomaali** · [Kiswahili](../sw-KE/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)
- **Asia:** [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [עברית](../he/README.md) · [मराठी](../mr/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [Bahasa Melayu](../ms/README.md) · [Filipino](../fil/README.md)

</details>
<!-- translations:end -->

# Ansible WordPress Enterprise

[![CI](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_ansible-wordpress-enterprise&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_ansible-wordpress-enterprise)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/ansible-wordpress-enterprise)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/releases)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/ansible-wordpress-enterprise/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/ansible-wordpress-enterprise)

Door Ansible ah oo loogu talagalay habaynta martigeliyeyaasha WordPress iyadoo la adeegsanayo PHP, server web, iyo kayd-xogeed maxalli ah ama dibadda ah. Xaqiijinta madasha iyo gelinta xogtu waxay dhacaan ka hor marxaladaha gaynta, halka xuduudaha hawshu ay ka dhigayaan rakibidda, habaynta, iyo xaqiijinta kuwo si gooni-gooni ah dib loogu eegi karo.

## Heshiiska gaynta ee la taageero

[meta/platform_support.yml](../../../meta/platform_support.yml) waa tixraaca rasmiga ah ee siyaasadda taageerada. Shaxda deggan ee Molecule waxay dabooshaa Ubuntu 24.04/PHP 8.3 iyo Ubuntu 26.04/PHP 8.5 oo leh Nginx, Debian 13/PHP 8.4 oo leh Nginx, iyo Rocky Linux 9 iyo 10/PHP 8.3 oo leh Apache. Marin kasta waxaa lagu tijaabiyaa HTTP iyo HTTPS. Kuwani waa lammaanaha OS/PHP ee la tijaabiyay; beddelka liiska martigeliyeyaasha (inventory) ee u weecda lammaane aan la tijaabin wuxuu fashilmaa ka hor inta aan wax isbeddel xirmo ah la samayn. Magacyada kale ee EL way wadaagaan siyaasadda, laakiin caddaynta wakhtiga-shaqadu waxay ka timaaddaa koonteenarrada Rocky Linux.

Koontaroolayaasha Python 3.12 waxay adeegsadaan Ansible 14.6 ama ka dambeeya ee taxanaha 14.x iyagoo wata ansible-core 2.21.6 ama ka dambeeya ee taxanaha 2.21. Koontaroolayaasha Python 3.13 iyo 3.14 waxay adeegsadaan Ansible 15.x oo wata ansible-core 2.22.x. Qufulka shuruudaha ee hash-ka leh wuxuu u doortaa lammaanaha ku habboon turjumaanka koontaroolaha. Shuruudaha turjumaanka ee noodhka la maamulo waa kuwo gooni ah. La tasho siyaasadda ka hor inta aanad dooran noocyada; madallada duugga ah iyo noocyada PHP ee ay kaliya taageeraan mashruucyada sare si toos ah looma qaato.

## Bisaylka sifooyinka

Isku-xigxiga hawlaha aasaasiga ah waxaa lagu qeexay [tasks/main.yml](../../../tasks/main.yml). Kooxaha kormeerka, nuqul-kaydinta, Fail2ban, amniga, kaydinta degdegga ah (caching), iyo derbiga-dabka waxay leeyihiin heshiisyo qaab-dhismeed oo maqan kuwaas oo ku diiwaangashan [tests/unit/missing_templates.yml](../../../tests/unit/missing_templates.yml). Calamadoodu waxay ahaanayaan kuwo dansan si caadi ah, xaqiijintuna way diiddaa in la shido kooxaha aan dhammaystirnayn. Magacyada hawlaha iyo doorsoomayaasha tusaalaha looma soo bandhigi karo inay yihiin hirgelin shaqaynaysa ee sifooyinkaas.

TLS, aqoonsiyada kaydka xogta, siraha WordPress ee la soo saaray, ilaalinta marinnada, iyo maaraynta u gaarka ah nidaamka hawlgalka waxay u baahan yihiin habaynta la diiwaangeliyay iyo hubinta wakhtiga-shaqada. Wax u-wareegid toos ah marka fashil dhaco (failover), heshiis helitaan heer-daruur ah (SLA), ama sheegasho diyaarsanaan wax-soo-saar oo caalami ah laguma samaynayo halkan.

## Bilow degdeg ah

Ka rakib doorka isha kaydkiisa iyo ku-tiirsanaanta ururintiisa:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git
ansible-galaxy collection install -r requirements.yml
```

Ka socodsii amarka ururinta nuqulkan kaydka. Dib u eeg [defaults/main.yml](../../../defaults/main.yml) iyo [tusaalooyinka](../../../examples/README.md) ka hor gaynta. Isticmaal barta gelitaanka ee la taageero halkii aad si toos ah ugu yeedhi lahayd marxaladaha hawlaha gudaha.

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

Ku bixi siraha la tixraacay iyadoo loo marayo Ansible Vault ama maamule sir ah oo jira. Habeey shahaadooyinka iyo furitaanka magaca martigeliyaha (hostname resolution) ee martigeliyaha la bartilmaameedsanayo ka hor inta aanad socodsiin gaynta. Hayso kooxaha sifooyinka aan dhammaystirnayn iyagoo dansan.

## Horumarinta iyo tijaabinta

[Makefile](../../../Makefile), [CONTRIBUTING.md](../../../CONTRIBUTING.md), iyo [TESTING.md](../../../TESTING.md) waxay qeexaan dejinta ku-tiirsanaanta ee hash-ka leh, hubinta lint, tijaabooyinka cutubyada (unit tests), iyo heshiisyada Docker/Molecule ee la tuuri karo. Tijaabooyinka cutubyada iyo lint ma caddeynayaan in gayntu guulaysatay.

```bash
make lint
```

U isticmaal hagaha tijaabinta xaaladaha deggan ee `default` iyo `tls` iyo shuruudahooda horudhaca ah. Hawlaha rakibidda martigeliyaha, cusboonaysiinta, nadiifinta, iyo soo-celintu waxay wax ka beddelaan mashiinnada la doortay; u isticmaal liisaska martigeliyeyaasha tijaabada ee go'doonsan xaqiijinta.

## Noocyada iyo xirmooyinka sii-daynta

Sii-daynta mashruucu waxay adeegsataa nooca SemVer ee buuxa ee ku jira `VERSION`, iyadoo ka madax-bannaan nooca ugu yar ee Ansible ee ku jira `meta/main.yml`. Ku riix sumadda u dhiganta `v2.22.1` laanta main si aad u kiciso Release, ama gacanta uga socodsii main ka dib markaad abuurto sumadda u dhiganta. Socodka shaqadu wuxuu xaqiijiyaa in sumadda jirta ay tilmaamayso koodhka isha ee la hubiyay, wuxuu socodsiiyaa xirmada CI oo dhammaystiran (oo ay ku jiraan dhammaan afarta xaaladood ee Molecule), wuxuuna daabacaa kayd door ah oo la jaanqaada Galaxy, xirmo Debian ah, RPM, `release.json` iyo `SHA256SUMS`. Daabacaddu waxay isticmaashaa sumaddaas jirta ee la xaqiijiyay iyadoo aan beddelin bartilmaameedka caadiga ah ee API-ga sii-daynta, sidaas darteed cusboonaysiinta dambe ee socodka shaqada ee main uma baahna aqoonsiyo qorista socodka shaqada oo ballaaran. Sumad maqan ama aan iswaafaqsanayn way fashilantaa ka hor tijaabinta.

Ku xaqiiji soo-dejinnada `sha256sum --check SHA256SUMS`. Ku rakib xirmooyinka asalka ah `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` oo ku saabsan Ubuntu 24.04 ama `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` oo ku saabsan Rocky Linux 9. Labaduba waxay doorka ku rakibaan `/usr/share/ansible/roles/wordpress_enterprise`; keen koontaroole Ansible ah oo la taageero oo si gaar ah u rakib `requirements.yml`. Kaydka waxaa lagu rakibi karaa `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz`. Xirmooyinka asalka ahi waxay ka kooban yihiin koodhka isha ee doorka iyo dukumeentiyada mana socodsiiyaan qoraallo gayn inta lagu jiro rakibidda. CI wuxuu rakibaa, hubiyaa, kana saaraa labada qaabba.

## Amniga iyo shatiga

Eeg [SECURITY.md](../../../SECURITY.md) iyo [shatiga MIT](../../../LICENSE). Xogta-hoose ee xirmada, siyaasadda taageerada madasha, iyo xaqiijinta sii-dayntu waa inay la jaanqaadaan doorka la soo saaray.
