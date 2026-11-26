<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · **தமிழ்** · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
- **Africa:** [Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)
- **Asia:** [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [עברית](../he/README.md) · [मराठी](../mr/README.md) · **தமிழ்** · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [Bahasa Melayu](../ms/README.md) · [Filipino](../fil/README.md)

</details>
<!-- translations:end -->

# Ansible WordPress Enterprise

[![CI](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_ansible-wordpress-enterprise&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_ansible-wordpress-enterprise)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/ansible-wordpress-enterprise)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/releases)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/ansible-wordpress-enterprise/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/ansible-wordpress-enterprise)

PHP, ஒரு வலைச் சேவையகம், மற்றும் உள்ளூர் அல்லது வெளிப்புறத் தரவுத்தளத்துடன் WordPress ஹோஸ்ட்களைக் கட்டமைப்பதற்கான ஒரு Ansible பாத்திரம். வரிசைப்படுத்தல் கட்டங்களுக்கு முன்பு தள மற்றும் உள்ளீட்டுச் சரிபார்ப்புகள் இயங்கும்; அதே வேளையில் பணி எல்லைகள் நிறுவல், கட்டமைப்பு மற்றும் சரிபார்ப்பு ஆகியவற்றைத் தனித்தனியாக மதிப்பாய்வு செய்யக்கூடியதாக வைத்திருக்கின்றன.

## ஆதரிக்கப்படும் வரிசைப்படுத்தல் ஒப்பந்தம்

[meta/platform_support.yml](../../../meta/platform_support.yml) ஆதரவுக் கொள்கைக்கான அதிகாரப்பூர்வ ஆதாரமாகும். நிலையான Molecule சோதனை அணி Nginx உடன் Ubuntu 24.04/PHP 8.3 மற்றும் Ubuntu 26.04/PHP 8.5, Nginx உடன் Debian 13/PHP 8.4, மற்றும் Apache உடன் Rocky Linux 9 மற்றும் 10/PHP 8.3 ஆகியவற்றை உள்ளடக்கியது. ஒவ்வொரு பாதையும் HTTP மற்றும் HTTPS வழியாகச் சோதிக்கப்படுகிறது. இவை சோதிக்கப்பட்ட OS/PHP இணைகளாகும்; சோதிக்கப்படாத இணைகளுக்குச் சரக்குப் பட்டியலில் செய்யப்படும் மேலெழுதல்கள் தொகுப்பு மாற்றங்களுக்கு முன்பே தோல்வியடையும். EL மாற்றுப்பெயர்கள் இந்தக் கொள்கையைப் பகிர்ந்துகொண்டாலும், இயக்கநேரச் சான்று Rocky Linux கொள்கலன்களிலிருந்து பெறப்படுகிறது.

Python 3.12 கட்டுப்படுத்திகள் 14.x வரிசையில் Ansible 14.6 அல்லது அதற்கு மேற்பட்ட பதிப்பையும், 2.21 வரிசையில் ansible-core 2.21.6 அல்லது அதற்கு மேற்பட்ட பதிப்பையும் பயன்படுத்துகின்றன. Python 3.13 மற்றும் 3.14 கட்டுப்படுத்திகள் ansible-core 2.22.x உடன் Ansible 15.x-ஐப் பயன்படுத்துகின்றன. ஹேஷ் செய்யப்பட்ட தேவைகள் பூட்டு (hashed requirements lock) கட்டுப்படுத்தி மொழிபெயர்ப்பிக்கான இணையைத் தேர்ந்தெடுக்கிறது. நிர்வகிக்கப்படும் முனை மொழிபெயர்ப்பித் தேவைகள் தனித்தனியானவை. பதிப்புகளைத் தேர்ந்தெடுப்பதற்கு முன் கொள்கையைப் பார்க்கவும்; பழைய தளங்களும் மேல்நிலையில் மட்டுமே ஆதரிக்கப்படும் PHP பதிப்புகளும் தானாக ஏற்றுக்கொள்ளப்படாது.

## அம்ச முதிர்ச்சி

முக்கியப் பணி வரிசை [tasks/main.yml](../../../tasks/main.yml)-இல் வரையறுக்கப்பட்டுள்ளது. கண்காணிப்பு, காப்புப்பிரதி, Fail2ban, பாதுகாப்பு, தேக்ககம், மற்றும் ஃபயர்வால் குழுக்களுக்கான விடுபட்ட வார்ப்புரு ஒப்பந்தங்கள் [tests/unit/missing_templates.yml](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/tests/unit/missing_templates.yml)-இல் பதிவு செய்யப்பட்டுள்ளன. அவற்றின் கொடிகள் இயல்புநிலையாக முடக்கப்பட்டிருக்கும், மேலும் முழுமையற்ற குழுக்களை இயக்குவதைச் சரிபார்ப்பு நிராகரிக்கிறது. பணிப் பெயர்களும் எடுத்துக்காட்டு மாறிகளும் அந்த அம்சங்களின் செயல்படும் அமலாக்கங்களாகக் கருதப்படக் கூடாது.

TLS, தரவுத்தள நற்சான்றிதழ்கள், உருவாக்கப்பட்ட WordPress இரகசியங்கள், பாதைப் பாதுகாப்புகள், மற்றும் OS-குறிப்பிட்ட கையாளுதல் ஆகியவற்றிற்கு ஆவணப்படுத்தப்பட்ட கட்டமைப்பு மற்றும் இயக்கநேரச் சரிபார்ப்புகள் தேவை. தானியங்கி தோல்வி மாற்றம் (failover), மேகக்கணி-அளவிலான கிடைக்கும் தன்மை SLA, அல்லது உலகளாவிய தயாரிப்பு-தயார்நிலை ஆகிய எதுவும் இங்கு கோரப்படவில்லை.

## விரைவுத் தொடக்கம்

இந்தப் பாத்திரத்தை அதன் களஞ்சிய மூலத்திலிருந்தும், அதன் தொகுப்புச் சார்புகளையும் நிறுவவும்:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git,HEAD,wordpress_enterprise
ansible-galaxy collection install -r requirements.yml
```

தொகுப்புக் கட்டளையை இந்தச் சரிபார்ப்புப் பிரதியிலிருந்து இயக்கவும். வரிசைப்படுத்தலுக்கு முன்பு [defaults/main.yml](../../../defaults/main.yml) மற்றும் [எடுத்துக்காட்டுகளை](../../../examples/README.md) மதிப்பாய்வு செய்யவும். உள் பணி நிலைகளை நேரடியாக அழைப்பதற்குப் பதிலாக ஆதரிக்கப்படும் நுழைவுப் புள்ளியைப் பயன்படுத்தவும்.

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

குறிப்பிடப்பட்டுள்ள இரகசியங்களை Ansible Vault அல்லது தற்போதுள்ள இரகசிய மேலாளர் மூலம் வழங்கவும். வரிசைப்படுத்தலை இயக்குவதற்கு முன்பு இலக்கு ஹோஸ்ட்டிற்கான சான்றிதழ்களையும் ஹோஸ்ட் பெயர் தீர்வையும் கட்டமைக்கவும். முழுமையற்ற அம்சக் குழுக்களை முடக்கியே வைத்திருக்கவும்.

## மேம்பாடு மற்றும் சோதனை

[Makefile](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/Makefile), [CONTRIBUTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/CONTRIBUTING.md), மற்றும் [TESTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/TESTING.md) ஆகியவை ஹேஷ் செய்யப்பட்ட சார்பு அமைப்பு, லின்ட் சரிபார்ப்புகள், அலகுச் சோதனைகள், மற்றும் தற்காலிக Docker/Molecule ஒப்பந்தங்களை வரையறுக்கின்றன. அலகுச் சோதனைகளும் லின்ட் சரிபார்ப்புகளும் வெற்றிகரமான வரிசைப்படுத்தலை உறுதிப்படுத்தாது.

```bash
make lint
```

நிலையான `default` மற்றும் `tls` சூழ்நிலைகளுக்கும் அவற்றின் முன்நிபந்தனைகளுக்கும் சோதனை வழிகாட்டியைப் பயன்படுத்தவும். ஹோஸ்ட் நிறுவல், மேம்படுத்தல், சுத்திகரிப்பு மற்றும் மீட்டெடுப்புப் பணிகள் தேர்ந்தெடுக்கப்பட்ட கணினிகளில் மாற்றங்களைச் செய்யும்; சரிபார்ப்பிற்குத் தனிமைப்படுத்தப்பட்ட சோதனைச் சரக்குப் பட்டியல்களைப் பயன்படுத்தவும்.

## பதிப்பிடல் மற்றும் வெளியீட்டுத் தொகுப்புகள்

திட்ட வெளியீடுகள் `meta/main.yml`-இன் குறைந்தபட்ச Ansible பதிப்பிலிருந்து சுயாதீனமாக, `VERSION`-இல் உள்ள முழு SemVer பதிப்பைப் பயன்படுத்துகின்றன. வெளியீட்டைத் தூண்ட main கிளையில் பொருந்தும் `v2.22.1` குறிச்சொல்லைத் தள்ளவும், அல்லது பொருந்தும் குறிச்சொல்லை உருவாக்கிய பிறகு main-இலிருந்து கைமுறையாக இயக்கவும். இந்தப் பணிப்பாய்வு, தற்போதுள்ள குறிச்சொல் சரிபார்க்கப்பட்ட மூலக் குறியீட்டைச் சுட்டிக்காட்டுவதை உறுதிசெய்து, முழு CI தொகுப்பையும் (நான்கு Molecule சூழ்நிலைகளையும் உள்ளடக்கி) இயக்கி, Galaxy-இணக்கமான பாத்திரக் காப்பகம், Debian தொகுப்பு, RPM, `release.json` மற்றும் `SHA256SUMS` ஆகியவற்றை வெளியிடுகிறது. வெளியீட்டு API-இன் இயல்புநிலை இலக்கை மேலெழுதாமல் அந்தச் சரிபார்க்கப்பட்ட குறிச்சொல்லையே வெளியீடு பயன்படுத்துகிறது; இதனால் main-இல் பிற்காலத்தில் செய்யப்படும் பணிப்பாய்வுப் புதுப்பிப்புக்குப் பரந்த workflow-write அனுமதிகள் தேவையில்லை. விடுபட்ட அல்லது பொருந்தாத குறிச்சொல் சோதனைக்கு முன்பே தோல்வியடையும்.

பதிவிறக்கங்களை `sha256sum --check SHA256SUMS` மூலம் சரிபார்க்கவும். Ubuntu 24.04-இல் `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` மூலமாகவோ அல்லது Rocky Linux 9-இல் `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` மூலமாகவோ இயல்பான தொகுப்புகளை நிறுவவும். இரண்டும் இந்தப் பாத்திரத்தை `/usr/share/ansible/roles/wordpress_enterprise`-இன் கீழ் நிறுவுகின்றன; ஆதரிக்கப்படும் Ansible கட்டுப்படுத்தியை வழங்கி `requirements.yml`-ஐத் தனியாக நிறுவவும். காப்பகத்தை `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz,,wordpress_enterprise` மூலம் நிறுவலாம். இயல்பான தொகுப்புகள் பாத்திர மூலக் கோப்புகளையும் ஆவணங்களையும் மட்டுமே கொண்டிருக்கின்றன; நிறுவலின்போது எந்த வரிசைப்படுத்தல் ஸ்கிரிப்டுகளையும் இயக்குவதில்லை. CI இரண்டு வடிவங்களையும் நிறுவி, சரிபார்த்து, அகற்றுகிறது.

## பாதுகாப்பு மற்றும் உரிமம்

[SECURITY.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/SECURITY.md) மற்றும் [MIT உரிமத்தைப்](../../../LICENSE) பார்க்கவும். தொகுப்பு மெட்டாடேட்டா, தள ஆதரவுக் கொள்கை மற்றும் வெளியீட்டுச் சரிபார்ப்பு ஆகியவை வழங்கப்படும் பாத்திரத்துடன் சீரமைக்கப்பட்டிருக்க வேண்டும்.
