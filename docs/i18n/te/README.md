<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · **తెలుగు** · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
- **Africa:** [Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)
- **Asia:** [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [עברית](../he/README.md) · [मराठी](../mr/README.md) · [தமிழ்](../ta/README.md) · **తెలుగు** · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [Bahasa Melayu](../ms/README.md) · [Filipino](../fil/README.md)

</details>
<!-- translations:end -->

# Ansible WordPress Enterprise

[![CI](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_ansible-wordpress-enterprise&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_ansible-wordpress-enterprise)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/ansible-wordpress-enterprise)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/releases)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/ansible-wordpress-enterprise/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/ansible-wordpress-enterprise)

PHP, వెబ్ సర్వర్ మరియు లోకల్ లేదా ఎక్స్‌టర్నల్ డేటాబేస్‌తో WordPress హోస్ట్‌లను కాన్ఫిగర్ చేయడానికి ఉపయోగపడే Ansible రోల్. డిప్లాయ్‌మెంట్ దశలకు ముందే ప్లాట్‌ఫారమ్ మరియు ఇన్‌పుట్ ధృవీకరణ అమలవుతుంది, అలాగే టాస్క్ సరిహద్దులు ఇన్‌స్టాలేషన్, కాన్ఫిగరేషన్ మరియు ధృవీకరణను విడివిడిగా సమీక్షించడానికి వీలుగా ఉంచుతాయి.

## మద్దతు ఉన్న డిప్లాయ్‌మెంట్ ఒప్పందం

[meta/platform_support.yml](../../../meta/platform_support.yml) మద్దతు పాలసీకి అధికారిక మూలం. స్థిరమైన Molecule మ్యాట్రిక్స్ Nginxతో Ubuntu 24.04/PHP 8.3 మరియు Ubuntu 26.04/PHP 8.5, Nginxతో Debian 13/PHP 8.4, మరియు Apacheతో Rocky Linux 9 మరియు 10/PHP 8.3లను కవర్ చేస్తుంది. ప్రతి మార్గాన్ని HTTP మరియు HTTPS ద్వారా పరీక్షిస్తారు. ఇవి పరీక్షించబడిన OS/PHP జతలు; పరీక్షించబడని జతలకు ఇన్వెంటరీ ఓవర్‌రైడ్‌లు ప్యాకేజీ మార్పులకు ముందే విఫలమవుతాయి. EL అలియాస్‌లు ఇదే పాలసీని పంచుకుంటాయి, కానీ రన్‌టైమ్ ఆధారాలు Rocky Linux కంటైనర్ల నుండి వస్తాయి.

Python 3.12 కంట్రోలర్లు 14.x శ్రేణిలో Ansible 14.6 లేదా తదుపరి వెర్షన్‌ను, 2.21 శ్రేణిలో ansible-core 2.21.6 లేదా తదుపరి వెర్షన్‌తో ఉపయోగిస్తాయి. Python 3.13 మరియు 3.14 కంట్రోలర్లు ansible-core 2.22.xతో Ansible 15.xను ఉపయోగిస్తాయి. హ్యాష్ చేయబడిన రిక్వైర్‌మెంట్స్ లాక్ కంట్రోలర్ ఇంటర్‌ప్రెటర్ కోసం తగిన జతను ఎంచుకుంటుంది. మేనేజ్డ్-నోడ్ ఇంటర్‌ప్రెటర్ అవసరాలు వేరుగా ఉంటాయి. వెర్షన్లను ఎంచుకునే ముందు పాలసీని పరిశీలించండి; పాత ప్లాట్‌ఫారమ్‌లు మరియు కేవలం అప్‌స్ట్రీమ్-మద్దతు ఉన్న PHP వెర్షన్లు స్వయంచాలకంగా స్వీకరించబడవు.

## ఫీచర్ పరిపక్వత

ప్రధాన టాస్క్ క్రమం [tasks/main.yml](../../../tasks/main.yml)లో నిర్వచించబడింది. మానిటరింగ్, బ్యాకప్, Fail2ban, సెక్యూరిటీ, క్యాషింగ్ మరియు ఫైర్‌వాల్ గ్రూపులకు లోపించిన టెంప్లేట్ ఒప్పందాలు [tests/unit/missing_templates.yml](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/tests/unit/missing_templates.yml)లో నమోదు చేయబడ్డాయి. వాటి ఫ్లాగ్‌లు డిఫాల్ట్‌గా ఆఫ్‌లో ఉంటాయి, మరియు ఎనేబుల్ చేసిన అసంపూర్ణ గ్రూపు మునుపటి దశలు నడిచిన తర్వాత దాని టాస్క్‌లు నడిచినప్పుడే ఆగిపోతుంది. టాస్క్ పేర్లు మరియు ఉదాహరణ వేరియబుల్స్ ఆ ఫీచర్ల పనిచేసే అమలుగా పరిగణించకూడదు.

TLS, డేటాబేస్ క్రెడెన్షియల్స్, జనరేట్ చేయబడిన WordPress సీక్రెట్స్, పాత్ గార్డ్‌లు మరియు OS-నిర్దిష్ట నిర్వహణకు డాక్యుమెంట్ చేయబడిన కాన్ఫిగరేషన్ మరియు రన్‌టైమ్ తనిఖీలు అవసరం. ఇక్కడ ఆటోమేటిక్ ఫెయిల్‌ఓవర్, క్లౌడ్-వ్యాప్త లభ్యత SLA లేదా సార్వత్రిక ప్రొడక్షన్-సంసిద్ధత హామీ ఏదీ ఇవ్వబడదు.

## త్వరిత ప్రారంభం

ఈ రోల్‌ను దాని రిపోజిటరీ మూలం నుండి మరియు దాని కలెక్షన్ డిపెండెన్సీలను ఇన్‌స్టాల్ చేయండి:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git,HEAD,wordpress_enterprise
ansible-galaxy collection install -r requirements.yml
```

ఈ చెక్‌అవుట్ నుండి కలెక్షన్ కమాండ్‌ను అమలు చేయండి. డిప్లాయ్‌మెంట్‌కు ముందు [defaults/main.yml](../../../defaults/main.yml) మరియు [ఉదాహరణలు](../../../examples/README.md)ను సమీక్షించండి. అంతర్గత టాస్క్ దశలను నేరుగా కాల్ చేయకుండా మద్దతు ఉన్న ఎంట్రీ పాయింట్‌ను ఉపయోగించండి.

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

ప్రస్తావించిన సీక్రెట్‌లను Ansible Vault లేదా ఇప్పటికే ఉన్న సీక్రెట్ మేనేజర్ ద్వారా అందించండి. డిప్లాయ్‌మెంట్‌ను అమలు చేయడానికి ముందు లక్ష్య హోస్ట్ కోసం సర్టిఫికేట్లు మరియు హోస్ట్‌నేమ్ రిజల్యూషన్‌ను కాన్ఫిగర్ చేయండి. అసంపూర్ణ ఫీచర్ గ్రూపులను డిజేబుల్‌లో ఉంచండి.

## అభివృద్ధి మరియు పరీక్ష

[Makefile](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/Makefile), [CONTRIBUTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/CONTRIBUTING.md), మరియు [TESTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/TESTING.md) హ్యాష్ చేయబడిన డిపెండెన్సీ సెటప్, లింట్ తనిఖీలు, యూనిట్ పరీక్షలు మరియు డిస్పోజబుల్ Docker/Molecule ఒప్పందాలను నిర్వచిస్తాయి. యూనిట్ పరీక్షలు మరియు లింట్ విజయవంతమైన డిప్లాయ్‌మెంట్‌ను నిర్ధారించవు.

```bash
make lint
```

స్థిరమైన `default` మరియు `tls` సినారియోలు మరియు వాటి ముందస్తు అవసరాల కోసం పరీక్ష మార్గదర్శినిని ఉపయోగించండి. హోస్ట్ ఇన్‌స్టాలేషన్, అప్‌గ్రేడ్, క్లీనప్ మరియు రిస్టోర్ టాస్క్‌లు ఎంచుకున్న మెషీన్లలో మార్పులు చేస్తాయి; ధృవీకరణ కోసం వేరుచేసిన టెస్ట్ ఇన్వెంటరీలను ఉపయోగించండి.

## వెర్షనింగ్ మరియు రిలీజ్ ప్యాకేజీలు

ప్రాజెక్ట్ రిలీజ్‌లు `meta/main.yml` యొక్క కనీస Ansible వెర్షన్‌తో సంబంధం లేకుండా
`VERSION`లోని పూర్తి SemVer వెర్షన్‌ను ఉపయోగిస్తాయి. Releaseను ట్రిగ్గర్ చేయడానికి mainలో
సరిపోలే `v2.22.1` ట్యాగ్‌ను పుష్ చేయండి, లేదా సరిపోలే ట్యాగ్‌ను సృష్టించిన తర్వాత main నుండి దానిని మాన్యువల్‌గా అమలు చేయండి.
ఈ వర్క్‌ఫ్లో ఇప్పటికే ఉన్న ట్యాగ్ తనిఖీ చేయబడిన సోర్స్‌ను సూచిస్తుందని ధృవీకరిస్తుంది, పూర్తి CI
సూట్‌ను (మొత్తం నాలుగు Molecule సినారియోలతో సహా) అమలు చేస్తుంది మరియు Galaxy-అనుకూల
రోల్ ఆర్కైవ్, Debian ప్యాకేజీ, RPM, `release.json` మరియు `SHA256SUMS`లను ప్రచురిస్తుంది.
ప్రచురణ రిలీజ్ API యొక్క డిఫాల్ట్ టార్గెట్‌ను ఓవర్‌రైడ్ చేయకుండా ఆ ధృవీకరించబడిన ఇప్పటికే ఉన్న ట్యాగ్‌ను
ఉపయోగిస్తుంది, కాబట్టి mainలో తదుపరి వర్క్‌ఫ్లో అప్‌డేట్‌కు విస్తృత workflow-write క్రెడెన్షియల్స్ అవసరం లేదు.
ట్యాగ్ లేకపోయినా లేదా సరిపోలకపోయినా పరీక్షకు ముందే విఫలమవుతుంది.

`sha256sum --check SHA256SUMS`తో డౌన్‌లోడ్‌లను ధృవీకరించండి. Ubuntu 24.04లో
`sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb`తో లేదా Rocky Linux 9లో
`sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm`తో నేటివ్ ప్యాకేజీలను
ఇన్‌స్టాల్ చేయండి. రెండూ రోల్‌ను `/usr/share/ansible/roles/wordpress_enterprise` క్రింద
ఇన్‌స్టాల్ చేస్తాయి; మద్దతు ఉన్న Ansible కంట్రోలర్‌ను అందించి `requirements.yml`ను విడిగా
ఇన్‌స్టాల్ చేయండి. ఆర్కైవ్‌ను `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz,,wordpress_enterprise`తో
ఇన్‌స్టాల్ చేయవచ్చు. నేటివ్ ప్యాకేజీలు రోల్ సోర్స్‌లు మరియు డాక్యుమెంటేషన్‌ను కలిగి ఉంటాయి మరియు
ఇన్‌స్టాలేషన్ సమయంలో ఎటువంటి డిప్లాయ్‌మెంట్ స్క్రిప్ట్‌లను అమలు చేయవు. CI రెండు ఫార్మాట్‌లను ఇన్‌స్టాల్ చేస్తుంది, తనిఖీ చేస్తుంది మరియు తొలగిస్తుంది.

## భద్రత మరియు లైసెన్స్

[SECURITY.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/SECURITY.md) మరియు [MIT లైసెన్స్](../../../LICENSE) చూడండి. ప్యాకేజీ మెటాడేటా, ప్లాట్‌ఫారమ్ మద్దతు పాలసీ మరియు రిలీజ్ ధృవీకరణ షిప్ చేయబడిన రోల్‌తో సమన్వయంగా ఉండాలి.
