<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · **मराठी** · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
- **Africa:** [Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)
- **Asia:** [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [עברית](../he/README.md) · **मराठी** · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [Bahasa Melayu](../ms/README.md) · [Filipino](../fil/README.md)

</details>
<!-- translations:end -->

# Ansible WordPress Enterprise

[![CI](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_ansible-wordpress-enterprise&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_ansible-wordpress-enterprise)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/ansible-wordpress-enterprise)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/releases)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/ansible-wordpress-enterprise/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/ansible-wordpress-enterprise)

PHP, वेब सर्व्हर आणि स्थानिक किंवा बाह्य डेटाबेससह WordPress होस्ट्स कॉन्फिगर करण्यासाठी एक Ansible रोल. प्लॅटफॉर्म आणि इनपुट पडताळणी डिप्लॉयमेंट टप्प्यांपूर्वी चालते, तर टास्क मर्यादा इन्स्टॉलेशन, कॉन्फिगरेशन आणि पडताळणी स्वतंत्रपणे पुनरावलोकनायोग्य ठेवतात.

## समर्थित डिप्लॉयमेंट करार

[meta/platform_support.yml](../../../meta/platform_support.yml) हे समर्थन-धोरणाचे अधिकृत संदर्भस्थान आहे. स्थिर Molecule मॅट्रिक्समध्ये Nginx सह Ubuntu 24.04/PHP 8.3 आणि Ubuntu 26.04/PHP 8.5, Nginx सह Debian 13/PHP 8.4, तसेच Apache सह Rocky Linux 9 आणि 10/PHP 8.3 यांचा समावेश आहे. प्रत्येक मार्गाची चाचणी HTTP आणि HTTPS वर केली जाते. या चाचणी केलेल्या OS/PHP जोड्या आहेत; चाचणी न केलेल्या जोड्यांसाठी इन्व्हेंटरी ओव्हरराइड्स पॅकेज बदलांपूर्वीच अयशस्वी होतात. EL अ‍ॅलिअसेस हेच धोरण वापरतात, परंतु रनटाइम पुरावे Rocky Linux कंटेनर्समधून येतात.

Python 3.12 कंट्रोलर्स 14.x श्रेणीतील Ansible 14.6 किंवा त्यानंतरची आवृत्ती आणि 2.21 श्रेणीतील ansible-core 2.21.6 किंवा त्यानंतरची आवृत्ती वापरतात. Python 3.13 आणि 3.14 कंट्रोलर्स ansible-core 2.22.x सह Ansible 15.x वापरतात. हॅश केलेले requirements लॉक कंट्रोलर इंटरप्रिटरसाठी योग्य जोडी निवडते. व्यवस्थापित-नोड (managed-node) इंटरप्रिटर आवश्यकता स्वतंत्र आहेत. आवृत्त्या निवडण्यापूर्वी धोरण पहा; जुने प्लॅटफॉर्म आणि केवळ अपस्ट्रीम-समर्थित PHP आवृत्त्या आपोआप स्वीकारल्या जात नाहीत.

## वैशिष्ट्यांची परिपक्वता

मुख्य टास्क क्रम [tasks/main.yml](../../../tasks/main.yml) मध्ये परिभाषित केला आहे. मॉनिटरिंग, बॅकअप, Fail2ban, सुरक्षा, कॅशिंग आणि फायरवॉल गटांचे गहाळ टेम्प्लेट करार [tests/unit/missing_templates.yml](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/tests/unit/missing_templates.yml) मध्ये नोंदवलेले आहेत. त्यांचे फ्लॅग्स डीफॉल्टनुसार बंद राहतात, आणि सक्षम केलेला अपूर्ण गट मागील टप्पे चालल्यानंतर त्याची टास्क्स चालतात तेव्हाच थांबतो. टास्क नावे आणि उदाहरण व्हेरिएबल्स त्या वैशिष्ट्यांच्या कार्यरत अंमलबजावणी म्हणून सादर करू नयेत.

TLS, डेटाबेस क्रेडेंशियल्स, तयार केलेले WordPress सिक्रेट्स, पाथ गार्ड्स आणि OS-विशिष्ट हाताळणीसाठी दस्तऐवजीकरण केलेले कॉन्फिगरेशन आणि रनटाइम तपासण्या आवश्यक आहेत. येथे कोणताही स्वयंचलित फेलओव्हर, क्लाउड-व्यापी उपलब्धता SLA किंवा सार्वत्रिक प्रोडक्शन-सज्जतेचा दावा केला जात नाही.

## झटपट सुरुवात

रिपॉझिटरी स्रोतावरून हा रोल आणि त्याची कलेक्शन अवलंबने (dependencies) इन्स्टॉल करा:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git,HEAD,wordpress_enterprise
ansible-galaxy collection install -r requirements.yml
```

या चेकआउटमधून कलेक्शन कमांड चालवा. डिप्लॉयमेंटपूर्वी [defaults/main.yml](../../../defaults/main.yml) आणि [उदाहरणे](../../../examples/README.md) यांचे पुनरावलोकन करा. अंतर्गत टास्क टप्पे थेट कॉल करण्याऐवजी समर्थित एंट्री पॉइंट वापरा.

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

संदर्भित सिक्रेट्स Ansible Vault किंवा विद्यमान सिक्रेट मॅनेजरद्वारे प्रदान करा. डिप्लॉयमेंट चालवण्यापूर्वी लक्ष्य होस्टसाठी प्रमाणपत्रे आणि होस्टनेम रिझोल्यूशन कॉन्फिगर करा. अपूर्ण वैशिष्ट्य गट अक्षम ठेवा.

## विकास आणि चाचणी

[Makefile](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/Makefile), [CONTRIBUTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/CONTRIBUTING.md), आणि [TESTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/TESTING.md) मध्ये हॅश केलेला अवलंबन सेटअप, लिंट तपासण्या, युनिट चाचण्या आणि तात्पुरते Docker/Molecule करार परिभाषित केले आहेत. युनिट चाचण्या आणि लिंट यशस्वी डिप्लॉयमेंट सिद्ध करत नाहीत.

```bash
make lint
```

स्थिर `default` आणि `tls` सिनॅरिओज आणि त्यांच्या पूर्वअटींसाठी चाचणी मार्गदर्शिका वापरा. होस्ट इन्स्टॉलेशन, अपग्रेड, क्लीनअप आणि रिस्टोअर टास्क्स निवडलेल्या मशीन्समध्ये बदल करतात; पडताळणीसाठी स्वतंत्र चाचणी इन्व्हेंटरी वापरा.

## आवृत्तीकरण आणि रिलीज पॅकेजेस

प्रकल्प रिलीज `meta/main.yml` च्या किमान Ansible आवृत्तीपासून स्वतंत्रपणे `VERSION` मधील संपूर्ण SemVer आवृत्ती वापरतात. Release कार्यान्वित करण्यासाठी main वर जुळणारा `v2.22.1` टॅग पुश करा किंवा जुळणारा टॅग तयार केल्यानंतर main वरून ते मॅन्युअली चालवा. हा वर्कफ्लो विद्यमान टॅग तपासलेल्या स्रोताकडे निर्देश करतो याची पडताळणी करतो, संपूर्ण CI संच (सर्व चार Molecule सिनॅरिओजसह) चालवतो आणि Galaxy-सुसंगत रोल आर्काइव्ह, Debian पॅकेज, RPM, `release.json` तसेच `SHA256SUMS` प्रकाशित करतो. प्रकाशन रिलीज API च्या डीफॉल्ट लक्ष्याला ओव्हरराइड न करता त्या पडताळलेल्या विद्यमान टॅगचा वापर करते, ज्यामुळे main वरील नंतरच्या वर्कफ्लो अपडेटसाठी अधिक व्यापक workflow-write क्रेडेंशियल्सची आवश्यकता पडत नाही. गहाळ किंवा न जुळणारा टॅग चाचणीपूर्वीच अयशस्वी होतो.

`sha256sum --check SHA256SUMS` वापरून डाउनलोडची पडताळणी करा. Ubuntu 24.04 वर `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` किंवा Rocky Linux 9 वर `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` वापरून नेटिव्ह पॅकेजेस इन्स्टॉल करा. दोन्ही `/usr/share/ansible/roles/wordpress_enterprise` अंतर्गत रोल इन्स्टॉल करतात; समर्थित Ansible कंट्रोलर उपलब्ध करून द्या आणि `requirements.yml` स्वतंत्रपणे इन्स्टॉल करा. आर्काइव्ह `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz,,wordpress_enterprise` वापरून इन्स्टॉल करता येते. नेटिव्ह पॅकेजेसमध्ये रोल स्रोत आणि दस्तऐवजीकरण असते आणि इन्स्टॉलेशन दरम्यान कोणतीही डिप्लॉयमेंट स्क्रिप्ट चालवली जात नाही. CI दोन्ही फॉरमॅट्स इन्स्टॉल करते, तपासते आणि काढून टाकते.

## सुरक्षा आणि परवाना

[SECURITY.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/SECURITY.md) आणि [MIT परवाना](../../../LICENSE) पहा. पॅकेज मेटाडेटा, प्लॅटफॉर्म समर्थन धोरण आणि रिलीज पडताळणी वितरित केलेल्या रोलशी सुसंगत राहणे आवश्यक आहे.
