<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · **አማርኛ** · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
- **Africa:** [Afrikaans](../af-ZA/README.md) · **አማርኛ** · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)
- **Asia:** [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [עברית](../he/README.md) · [मराठी](../mr/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [Bahasa Melayu](../ms/README.md) · [Filipino](../fil/README.md)

</details>
<!-- translations:end -->

# Ansible WordPress Enterprise

[![CI](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_ansible-wordpress-enterprise&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_ansible-wordpress-enterprise)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/ansible-wordpress-enterprise)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/releases)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/ansible-wordpress-enterprise/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/ansible-wordpress-enterprise)

የWordPress አስተናጋጆችን በPHP፣ በድር አገልጋይ እና በአካባቢያዊ ወይም ውጫዊ የውሂብ ጎታ ለማዋቀር የሚያገለግል የAnsible ሚና። የመድረክ እና የግቤት ማረጋገጫ ከማሰማራት ደረጃዎች በፊት ይከናወናል፣ የተግባር ወሰኖች ደግሞ መጫንን፣ ማዋቀርን እና ማረጋገጥን በተናጠል ለመገምገም ያስችላሉ።

## የሚደገፍ የማሰማራት ውል

[meta/platform_support.yml](../../../meta/platform_support.yml) የድጋፍ ፖሊሲው ዋና ምንጭ ነው። የተረጋጋው የMolecule ማትሪክስ Ubuntu 24.04/PHP 8.3 እና Ubuntu 26.04/PHP 8.5ን ከNginx ጋር፣ Debian 13/PHP 8.4ን ከNginx ጋር፣ እንዲሁም Rocky Linux 9 እና 10/PHP 8.3ን ከApache ጋር ይሸፍናል። እያንዳንዱ መንገድ በHTTP እና በHTTPS ይፈተሻል። እነዚህ የተፈተሹ የሥርዓተ ክወና/PHP ጥንዶች ናቸው፤ ወደ ያልተፈተሹ ጥንዶች የሚደረጉ የኢንቬንቶሪ ተለዋጮች የጥቅል ለውጦች ከመደረጋቸው በፊት ይከሽፋሉ። የEL ተለዋጭ ስሞች ፖሊሲውን ይጋራሉ፣ ነገር ግን የአሂድ ጊዜ ማስረጃው ከRocky Linux ኮንቴይነሮች ይመጣል።

የPython 3.12 ተቆጣጣሪዎች በ14.x መስመር ውስጥ Ansible 14.6 ወይም ከዚያ በላይን በ2.21 መስመር ውስጥ ካለው ansible-core 2.21.6 ወይም ከዚያ በላይ ጋር ይጠቀማሉ። የPython 3.13 እና 3.14 ተቆጣጣሪዎች Ansible 15.xን ከansible-core 2.22.x ጋር ይጠቀማሉ። ሃሽ የተደረገው የመስፈርቶች መቆለፊያ ለተቆጣጣሪው ተርጓሚ ጥንዱን ይመርጣል። የሚተዳደሩ ኖዶች የተርጓሚ መስፈርቶች የተለዩ ናቸው። ሥሪቶችን ከመምረጥዎ በፊት ፖሊሲውን ያማክሩ፤ የቆዩ መድረኮች እና በዋናው ምንጭ ብቻ የሚደገፉ የPHP ሥሪቶች በራስ-ሰር ተቀባይነት አያገኙም።

## የባህሪ ብስለት

ዋናው የተግባራት ቅደም ተከተል በ[tasks/main.yml](../../../tasks/main.yml) ውስጥ ተገልጿል። የክትትል፣ የመጠባበቂያ ቅጂ፣ የFail2ban፣ የደህንነት፣ የመሸጎጫ እና የፋየርዎል ቡድኖች በ[tests/unit/missing_templates.yml](../../../tests/unit/missing_templates.yml) ውስጥ የተመዘገቡ የጎደሉ የአብነት ውሎች አሏቸው። መቀየሪያዎቻቸው በነባሪነት ጠፍተው ይቆያሉ እንዲሁም ማረጋገጫው ያልተሟሉ ቡድኖችን ማንቃትን አይቀበልም። የተግባር ስሞች እና የምሳሌ ተለዋዋጮች የእነዚያ ባህሪያት የሚሠሩ አተገባበሮች ተደርገው መቅረብ የለባቸውም።

TLS፣ የውሂብ ጎታ ማረጋገጫዎች፣ የተመነጩ የWordPress ምስጢሮች፣ የዱካ ጥበቃዎች እና ለሥርዓተ ክወና የተለዩ አያያዞች የተመዘገበውን ውቅር እና የአሂድ ጊዜ ፍተሻዎችን ይፈልጋሉ። እዚህ ምንም ዓይነት ራስ-ሰር መተካካት፣ ደመና-አቀፍ የተደራሽነት SLA ወይም ሁለንተናዊ ለምርት ዝግጁነት አይገለጽም።

## ፈጣን ጅማሬ

ሚናውን ከማከማቻ ምንጩ እና ከስብስብ ጥገኞቹ ጋር ይጫኑ፦

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git,HEAD,wordpress_enterprise
ansible-galaxy collection install -r requirements.yml
```

የስብስብ ትዕዛዙን ከዚህ ቅጂ ያስኪዱ። ከማሰማራትዎ በፊት [defaults/main.yml](../../../defaults/main.yml) እና [ምሳሌዎች](../../../examples/README.md)ን ይገምግሙ። የውስጥ የተግባር ደረጃዎችን በቀጥታ ከመጥራት ይልቅ የሚደገፈውን የመግቢያ ነጥብ ይጠቀሙ።

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

የተጠቀሱትን ምስጢሮች በAnsible Vault ወይም ባለው የምስጢር አስተዳዳሪ በኩል ያቅርቡ። ማሰማራት ከማስኬድዎ በፊት ለታለመው አስተናጋጅ የምስክር ወረቀቶችን እና የአስተናጋጅ ስም መፍቻን ያዋቅሩ። ያልተሟሉ የባህሪ ቡድኖችን እንደተሰናከሉ ይተዉ።

## ልማት እና ሙከራ

[Makefile](../../../Makefile)፣ [CONTRIBUTING.md](../../../CONTRIBUTING.md) እና [TESTING.md](../../../TESTING.md) ሃሽ የተደረገውን የጥገኝነት አወቃቀር፣ የlint ፍተሻዎችን፣ የአሃድ ሙከራዎችን እና ጊዜያዊ የDocker/Molecule ውሎችን ይገልጻሉ። የአሃድ ሙከራዎች እና lint የተሳካ ማሰማራትን አያረጋግጡም።

```bash
make lint
```

ለተረጋጉት `default` እና `tls` ሁኔታዎች እና ቅድመ ሁኔታዎቻቸው የሙከራ መመሪያውን ይጠቀሙ። የአስተናጋጅ መጫን፣ ማሻሻል፣ ማጽዳት እና ወደ ቀድሞው መመለስ ተግባራት የተመረጡትን ማሽኖች ይለውጣሉ፤ ለማረጋገጫ የተገለሉ የሙከራ ኢንቬንቶሪዎችን ይጠቀሙ።

## ሥሪት አሰጣጥ እና የልቀት ጥቅሎች

የፕሮጀክት ልቀቶች ከ`meta/main.yml` ዝቅተኛው የAnsible ሥሪት ተለይተው በ`VERSION` ውስጥ ያለውን ሙሉ የSemVer ሥሪት ይጠቀማሉ። ልቀቱን ለማስጀመር የሚዛመድ `v2.22.1` መለያ ወደ main ይግፉ፣ ወይም የሚዛመደውን መለያ ከፈጠሩ በኋላ ከmain በእጅ ያስኪዱት። የሥራ ፍሰቱ ያለው መለያ ወደ ተፈተሸው ምንጭ እንደሚያመለክት ያረጋግጣል፣ ሙሉውን የCI ስብስብ (ሁሉንም አራቱን የMolecule ሁኔታዎች ጨምሮ) ያስኪዳል፣ እንዲሁም ከGalaxy ጋር የሚጣጣም የሚና ማህደር፣ የDebian ጥቅል፣ RPM፣ `release.json` እና `SHA256SUMS` ያትማል። ማተም የልቀት APIን ነባሪ ዒላማ ሳይሽር ያንን የተረጋገጠ ነባር መለያ ይጠቀማል፣ ስለዚህ በኋላ በmain ላይ የሚደረግ የሥራ ፍሰት ዝማኔ ሰፊ የሥራ ፍሰት መጻፊያ ፈቃዶችን አይፈልግም። የጎደለ ወይም የማይዛመድ መለያ ከሙከራ በፊት ይከሽፋል።

ውርዶችን በ`sha256sum --check SHA256SUMS` ያረጋግጡ። ነባር ጥቅሎችን በUbuntu 24.04 ላይ በ`sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` ወይም በRocky Linux 9 ላይ በ`sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` ይጫኑ። ሁለቱም ሚናውን በ`/usr/share/ansible/roles/wordpress_enterprise` ሥር ይጭናሉ፤ የሚደገፍ የAnsible ተቆጣጣሪ ያቅርቡ እና `requirements.yml`ን በተናጠል ይጫኑ። ማህደሩ በ`ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz,,wordpress_enterprise` ሊጫን ይችላል። ነባር ጥቅሎች የሚና ምንጮችን እና ሰነዶችን ይይዛሉ እንዲሁም በመጫን ጊዜ ምንም የማሰማራት ስክሪፕቶችን አያስኪዱም። CI ሁለቱንም ቅርጸቶች ይጭናል፣ ይፈትሻል እና ያስወግዳል።

## ደህንነት እና ፈቃድ

[SECURITY.md](../../../SECURITY.md) እና [የMIT ፈቃድ](../../../LICENSE)ን ይመልከቱ። የጥቅል ሜታዳታ፣ የመድረክ ድጋፍ ፖሊሲ እና የልቀት ማረጋገጫ ከሚሰራጨው ሚና ጋር የተጣጣሙ መሆን አለባቸው።
