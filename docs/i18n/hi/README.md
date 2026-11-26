<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · **हिन्दी**

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · **हिन्दी** · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
- **Africa:** [Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)
- **Asia:** [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [עברית](../he/README.md) · [मराठी](../mr/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [Bahasa Melayu](../ms/README.md) · [Filipino](../fil/README.md)

</details>
<!-- translations:end -->

# Ansible WordPress Enterprise

[![CI](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_ansible-wordpress-enterprise&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_ansible-wordpress-enterprise)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/ansible-wordpress-enterprise)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/releases)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/ansible-wordpress-enterprise/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/ansible-wordpress-enterprise)

PHP, वेब सर्वर और स्थानीय या बाहरी डेटाबेस के साथ WordPress होस्ट को कॉन्फ़िगर करने के लिए एक Ansible रोल। प्लेटफ़ॉर्म और इनपुट सत्यापन परिनियोजन चरणों से पहले चलते हैं, जबकि कार्य सीमाएँ इंस्टॉलेशन, कॉन्फ़िगरेशन और सत्यापन को अलग-अलग समीक्षा योग्य बनाए रखती हैं।

## समर्थित परिनियोजन अनुबंध

[meta/platform_support.yml](../../../meta/platform_support.yml) समर्थन-नीति का आधिकारिक स्रोत है। स्थिर Molecule मैट्रिक्स में Nginx के साथ Ubuntu 24.04/PHP 8.3 और Ubuntu 26.04/PHP 8.5, Nginx के साथ Debian 13/PHP 8.4, तथा Apache के साथ Rocky Linux 9 और 10/PHP 8.3 शामिल हैं। प्रत्येक पाथ का परीक्षण HTTP और HTTPS दोनों पर किया जाता है। ये परीक्षित OS/PHP जोड़े हैं; अपरीक्षित जोड़ों के लिए इन्वेंटरी ओवरराइड पैकेज परिवर्तन से पहले ही विफल हो जाते हैं। EL उपनाम इस नीति को साझा करते हैं, लेकिन रनटाइम प्रमाण Rocky Linux कंटेनरों से प्राप्त होता है।

Python 3.12 कंट्रोलर 14.x शृंखला में Ansible 14.6 या उसके बाद के संस्करण के साथ 2.21 शृंखला में ansible-core 2.21.6 या उसके बाद के संस्करण का उपयोग करते हैं। Python 3.13 और 3.14 कंट्रोलर ansible-core 2.22.x के साथ Ansible 15.x का उपयोग करते हैं। हैश्ड रिक्वायरमेंट्स लॉक कंट्रोलर इंटरप्रेटर के लिए उपयुक्त जोड़ा चुनता है। प्रबंधित-नोड इंटरप्रेटर की आवश्यकताएँ अलग हैं। संस्करण चुनने से पहले नीति देखें; पुराने प्लेटफ़ॉर्म और केवल अपस्ट्रीम द्वारा समर्थित PHP संस्करण स्वतः स्वीकार नहीं किए जाते हैं।

## फ़ीचर परिपक्वता

मुख्य कार्य अनुक्रम [tasks/main.yml](../../../tasks/main.yml) में परिभाषित है। मॉनिटरिंग, बैकअप, Fail2ban, सुरक्षा, कैशिंग और फ़ायरवॉल समूहों के अनुपलब्ध टेम्पलेट अनुबंध [tests/unit/missing_templates.yml](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/tests/unit/missing_templates.yml) में दर्ज हैं। उनके फ़्लैग डिफ़ॉल्ट रूप से बंद रहते हैं और सत्यापन अधूरे समूहों को सक्षम करने को अस्वीकार कर देता है। कार्य नामों और उदाहरण वेरिएबल को उन फ़ीचर के कार्यशील कार्यान्वयन के रूप में प्रस्तुत नहीं किया जाना चाहिए।

TLS, डेटाबेस क्रेडेंशियल, जनरेट किए गए WordPress सीक्रेट्स, पाथ गार्ड और OS-विशिष्ट हैंडलिंग के लिए प्रलेखित कॉन्फ़िगरेशन और रनटाइम जाँच की आवश्यकता होती है। यहाँ किसी स्वचालित फ़ेलओवर, क्लाउड-व्यापी उपलब्धता SLA या सार्वभौमिक प्रोडक्शन-तैयारी का दावा नहीं किया गया है।

## त्वरित शुरुआत

रोल को इसके रिपॉजिटरी स्रोत और इसकी कलेक्शन निर्भरताओं के साथ इंस्टॉल करें:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git,HEAD,wordpress_enterprise
ansible-galaxy collection install -r requirements.yml
```

इस चेकआउट से कलेक्शन कमांड चलाएँ। परिनियोजन से पहले [defaults/main.yml](../../../defaults/main.yml) और [उदाहरणों](../../../examples/README.md) की समीक्षा करें। आंतरिक कार्य चरणों को सीधे कॉल करने के बजाय समर्थित एंट्री पॉइंट का उपयोग करें।

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

संदर्भित सीक्रेट्स को Ansible Vault या किसी मौजूदा सीक्रेट मैनेजर के माध्यम से प्रदान करें। परिनियोजन चलाने से पहले लक्ष्य होस्ट के लिए प्रमाणपत्र और होस्टनाम रिज़ॉल्यूशन कॉन्फ़िगर करें। अधूरे फ़ीचर समूहों को अक्षम रखें।

## विकास और परीक्षण

[Makefile](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/Makefile), [CONTRIBUTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/CONTRIBUTING.md), और [TESTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/TESTING.md) हैश्ड निर्भरता सेटअप, लिंट जाँच, यूनिट परीक्षण और डिस्पोज़ेबल Docker/Molecule अनुबंधों को परिभाषित करते हैं। यूनिट परीक्षण और लिंट सफल परिनियोजन को सिद्ध नहीं करते हैं।

```bash
make lint
```

स्थिर `default` और `tls` परिदृश्यों तथा उनकी पूर्व-आवश्यकताओं के लिए परीक्षण मार्गदर्शिका का उपयोग करें। होस्ट इंस्टॉलेशन, अपग्रेड, क्लीनअप और रिस्टोर कार्य चयनित मशीनों में बदलाव करते हैं; सत्यापन के लिए अलग परीक्षण इन्वेंटरी का उपयोग करें।

## वर्ज़निंग और रिलीज़ पैकेज

प्रोजेक्ट रिलीज़ `meta/main.yml` के न्यूनतम Ansible संस्करण से स्वतंत्र रूप से, `VERSION` में दिए गए पूर्ण SemVer संस्करण का उपयोग करती हैं। Release को ट्रिगर करने के लिए main पर एक मेल खाने वाला `v2.22.1` टैग पुश करें, या मेल खाने वाला टैग बनाने के बाद इसे main से मैन्युअल रूप से चलाएँ। यह वर्कफ़्लो सत्यापित करता है कि मौजूदा टैग जाँचे गए स्रोत की ओर इंगित करता है, पूर्ण CI सूट (सभी चार Molecule परिदृश्यों सहित) चलाता है, और Galaxy-संगत रोल आर्काइव, Debian पैकेज, RPM, `release.json` तथा `SHA256SUMS` प्रकाशित करता है। प्रकाशन रिलीज़ API के डिफ़ॉल्ट लक्ष्य को ओवरराइड किए बिना उस सत्यापित मौजूदा टैग का उपयोग करता है, जिससे main पर बाद के वर्कफ़्लो अपडेट के लिए व्यापक workflow-write क्रेडेंशियल की आवश्यकता नहीं पड़ती। अनुपस्थित या बेमेल टैग परीक्षण से पहले ही विफल हो जाता है।

डाउनलोड को `sha256sum --check SHA256SUMS` के साथ सत्यापित करें। Ubuntu 24.04 पर `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` या Rocky Linux 9 पर `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` के साथ नेटिव पैकेज इंस्टॉल करें। दोनों ही रोल को `/usr/share/ansible/roles/wordpress_enterprise` के अंतर्गत इंस्टॉल करते हैं; एक समर्थित Ansible कंट्रोलर उपलब्ध कराएँ और `requirements.yml` को अलग से इंस्टॉल करें। आर्काइव को `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz,,wordpress_enterprise` के साथ इंस्टॉल किया जा सकता है। नेटिव पैकेज में रोल स्रोत और दस्तावेज़ होते हैं तथा इंस्टॉलेशन के दौरान वे कोई परिनियोजन स्क्रिप्ट नहीं चलाते। CI दोनों प्रारूपों को इंस्टॉल, जाँच और रिमूव करता है।

## सुरक्षा और लाइसेंस

[SECURITY.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/SECURITY.md) और [MIT लाइसेंस](../../../LICENSE) देखें। पैकेज मेटाडेटा, प्लेटफ़ॉर्म समर्थन नीति और रिलीज़ सत्यापन को वितरित रोल के साथ संरेखित रहना चाहिए।
