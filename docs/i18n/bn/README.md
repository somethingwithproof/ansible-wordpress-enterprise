<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · **বাংলা** · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
- **Africa:** [Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)
- **Asia:** **বাংলা** · [فارسی](../fa/README.md) · [עברית](../he/README.md) · [मराठी](../mr/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [Bahasa Melayu](../ms/README.md) · [Filipino](../fil/README.md)

</details>
<!-- translations:end -->

# Ansible WordPress Enterprise

[![CI](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_ansible-wordpress-enterprise&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_ansible-wordpress-enterprise)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/ansible-wordpress-enterprise)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/releases)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/ansible-wordpress-enterprise/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/ansible-wordpress-enterprise)

PHP, একটি ওয়েব সার্ভার এবং একটি লোকাল বা বাহ্যিক ডেটাবেসসহ WordPress হোস্ট কনফিগার করার জন্য একটি Ansible রোল। ডিপ্লয়মেন্ট ধাপগুলোর আগে প্ল্যাটফর্ম এবং ইনপুট যাচাইকরণ চালানো হয়, আর টাস্কের সীমানাগুলো ইনস্টলেশন, কনফিগারেশন ও যাচাইকরণকে আলাদাভাবে পর্যালোচনাযোগ্য রাখে।

## সমর্থিত ডিপ্লয়মেন্ট চুক্তি

[meta/platform_support.yml](../../../meta/platform_support.yml) হলো সমর্থন-নীতির মূল কর্তৃপক্ষ। স্থিতিশীল Molecule ম্যাট্রিক্সের আওতায় রয়েছে Nginx-সহ Ubuntu 24.04/PHP 8.3 এবং Ubuntu 26.04/PHP 8.5, Nginx-সহ Debian 13/PHP 8.4, এবং Apache-সহ Rocky Linux 9 ও 10/PHP 8.3। প্রতিটি পথ HTTP এবং HTTPS উভয়ের মাধ্যমে পরীক্ষা করা হয়। এগুলোই পরীক্ষিত OS/PHP জোড়া; অপরীক্ষিত জোড়ার জন্য ইনভেন্টরি ওভাররাইড প্যাকেজ পরিবর্তনের আগেই ব্যর্থ হয়। EL উপনামগুলো একই নীতি অনুসরণ করে, তবে রানটাইম প্রমাণ Rocky Linux কন্টেইনার থেকে আসে।

Python 3.12 কন্ট্রোলারগুলোতে 14.x ধারায় Ansible 14.6 বা পরবর্তী সংস্করণের সাথে 2.21 ধারায় ansible-core 2.21.6 বা পরবর্তী সংস্করণ ব্যবহৃত হয়। Python 3.13 এবং 3.14 কন্ট্রোলারগুলোতে ansible-core 2.22.x-সহ Ansible 15.x ব্যবহৃত হয়। হ্যাশকৃত requirements লক কন্ট্রোলার ইন্টারপ্রেটারের জন্য উপযুক্ত জোড়াটি নির্বাচন করে। ম্যানেজড-নোড ইন্টারপ্রেটারের আবশ্যকতাগুলো আলাদা। সংস্করণ নির্বাচনের আগে নীতিটি দেখে নিন; পুরোনো প্ল্যাটফর্ম এবং কেবল আপস্ট্রিম-সমর্থিত PHP সংস্করণগুলো স্বয়ংক্রিয়ভাবে গৃহীত হয় না।

## ফিচারের পরিপক্বতা

মূল টাস্কের ক্রম [tasks/main.yml](../../../tasks/main.yml)-এ সংজ্ঞায়িত করা আছে। মনিটরিং, ব্যাকআপ, Fail2ban, নিরাপত্তা, ক্যাশিং এবং ফায়ারওয়াল গ্রুপগুলোর অনুপস্থিত টেমপ্লেট চুক্তিগুলো [tests/unit/missing_templates.yml](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/tests/unit/missing_templates.yml)-এ নথিভুক্ত আছে। এগুলোর ফ্ল্যাগ ডিফল্টভাবে বন্ধ থাকে এবং যাচাইকরণ প্রক্রিয়া অসম্পূর্ণ গ্রুপগুলো চালু করতে বাধা দেয়। টাস্কের নাম এবং উদাহরণ ভেরিয়েবলগুলোকে সেই ফিচারগুলোর কার্যকর বাস্তবায়ন হিসেবে উপস্থাপন করা যাবে না।

TLS, ডেটাবেস ক্রেডেনশিয়াল, জেনারেট করা WordPress সিক্রেট, পাথ গার্ড এবং OS-নির্দিষ্ট পরিচালনার জন্য নথিভুক্ত কনফিগারেশন ও রানটাইম যাচাইকরণ প্রয়োজন। এখানে কোনো স্বয়ংক্রিয় ফেইলওভার, ক্লাউড-ব্যাপী প্রাপ্যতা SLA বা সর্বজনীন প্রোডাকশন-প্রস্তুতির দাবি করা হয়নি।

## দ্রুত শুরু

রিপোজিটরি উৎস থেকে রোলটি এবং এর কালেকশন ডিপেন্ডেন্সিগুলো ইনস্টল করুন:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git,HEAD,wordpress_enterprise
ansible-galaxy collection install -r requirements.yml
```

এই চেকআউট থেকে কালেকশন কমান্ডটি চালান। ডিপ্লয়মেন্টের আগে [defaults/main.yml](../../../defaults/main.yml) এবং [উদাহরণসমূহ](../../../examples/README.md) পর্যালোচনা করুন। অভ্যন্তরীণ টাস্ক ধাপগুলো সরাসরি কল করার পরিবর্তে সমর্থিত এন্ট্রি পয়েন্ট ব্যবহার করুন।

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

উল্লিখিত সিক্রেটগুলো Ansible Vault অথবা কোনো বিদ্যমান সিক্রেট ম্যানেজারের মাধ্যমে সরবরাহ করুন। ডিপ্লয়মেন্ট চালানোর আগে লক্ষ্য হোস্টের জন্য সার্টিফিকেট এবং হোস্টনেম রেজোলিউশন কনফিগার করুন। অসম্পূর্ণ ফিচার গ্রুপগুলো নিষ্ক্রিয় রাখুন।

## ডেভেলপমেন্ট ও টেস্টিং

[Makefile](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/Makefile), [CONTRIBUTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/CONTRIBUTING.md), এবং [TESTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/TESTING.md) হ্যাশকৃত ডিপেন্ডেন্সি সেটআপ, লিন্ট পরীক্ষা, ইউনিট টেস্ট এবং ডিসপোজেবল Docker/Molecule চুক্তিগুলো সংজ্ঞায়িত করে। ইউনিট টেস্ট এবং লিন্ট সফল ডিপ্লয়মেন্টের নিশ্চয়তা দেয় না।

```bash
make lint
```

স্থিতিশীল `default` এবং `tls` সিনারিও এবং সেগুলোর পূর্বশর্তগুলোর জন্য টেস্টিং গাইড ব্যবহার করুন। হোস্ট ইনস্টলেশন, আপগ্রেড, ক্লিনআপ এবং রিস্টোর টাস্কগুলো নির্বাচিত মেশিনগুলোতে পরিবর্তন ঘটায়; যাচাইকরণের জন্য বিচ্ছিন্ন টেস্ট ইনভেন্টরি ব্যবহার করুন।

## সংস্করণ নির্ধারণ এবং রিলিজ প্যাকেজ

প্রকল্পের রিলিজগুলো `meta/main.yml`-এর ন্যূনতম Ansible সংস্করণ থেকে স্বতন্ত্রভাবে `VERSION`-এ থাকা সম্পূর্ণ SemVer সংস্করণ ব্যবহার করে। Release ট্রিগার করতে main ব্রাঞ্চে একটি মানানসই `v2.22.1` ট্যাগ পুশ করুন, অথবা মানানসই ট্যাগ তৈরি করার পর main থেকে ম্যানুয়ালি এটি চালান। ওয়ার্কফ্লোটি যাচাই করে যে বিদ্যমান ট্যাগটি পরীক্ষিত উৎসের দিকে নির্দেশ করছে কি না, সম্পূর্ণ CI স্যুট চালায় (চারটি Molecule সিনারিওসহ), এবং একটি Galaxy-সামঞ্জস্যপূর্ণ রোল আর্কাইভ, Debian প্যাকেজ, RPM, `release.json` এবং `SHA256SUMS` প্রকাশ করে। প্রকাশনা প্রক্রিয়াটি রিলিজ API-এর ডিফল্ট টার্গেট ওভাররাইড না করে সেই যাচাইকৃত বিদ্যমান ট্যাগটিই ব্যবহার করে, ফলে পরবর্তীতে main-এ ওয়ার্কফ্লো আপডেটের জন্য বিস্তৃত workflow-write ক্রেডেনশিয়ালের প্রয়োজন হয় না। অনুপস্থিত বা অমিল ট্যাগ পরীক্ষার আগেই ব্যর্থ হয়।

`sha256sum --check SHA256SUMS` ব্যবহার করে ডাউনলোডগুলো যাচাই করুন। Ubuntu 24.04-এ `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` অথবা Rocky Linux 9-এ `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` দিয়ে নেটিভ প্যাকেজগুলো ইনস্টল করুন। উভয়ই রোলটি `/usr/share/ansible/roles/wordpress_enterprise`-এর অধীনে ইনস্টল করে; একটি সমর্থিত Ansible কন্ট্রোলার সরবরাহ করুন এবং `requirements.yml` আলাদাভাবে ইনস্টল করুন। আর্কাইভটি `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz,,wordpress_enterprise` দিয়ে ইনস্টল করা যাবে। নেটিভ প্যাকেজগুলোতে রোলের সোর্স ও ডকুমেন্টেশন থাকে এবং ইনস্টলেশনের সময় কোনো ডিপ্লয়মেন্ট স্ক্রিপ্ট চালানো হয় না। CI উভয় ফরম্যাট ইনস্টল, পরীক্ষা এবং অপসারণ করে।

## নিরাপত্তা এবং লাইসেন্স

[SECURITY.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/SECURITY.md) এবং [MIT লাইসেন্স](../../../LICENSE) দেখুন। প্যাকেজের মেটাডেটা, প্ল্যাটফর্ম সমর্থন নীতি এবং রিলিজ যাচাইকরণ অবশ্যই সরবরাহকৃত রোলের সাথে সামঞ্জস্যপূর্ণ থাকতে হবে।
