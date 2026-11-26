<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · **اردو** · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
- **Africa:** [Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)
- **Asia:** [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [עברית](../he/README.md) · [मराठी](../mr/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · **اردو** · [Bahasa Melayu](../ms/README.md) · [Filipino](../fil/README.md)

</details>
<!-- translations:end -->

# Ansible WordPress Enterprise

[![CI](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_ansible-wordpress-enterprise&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_ansible-wordpress-enterprise)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/ansible-wordpress-enterprise)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/releases)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/ansible-wordpress-enterprise/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/ansible-wordpress-enterprise)

PHP، ویب سرور، اور مقامی یا بیرونی ڈیٹا بیس کے ساتھ WordPress ہوسٹس کو کنفیگر کرنے کے لیے ایک Ansible رول۔ تعیناتی کے مراحل سے پہلے پلیٹ فارم اور ان پٹ کی توثیق چلائی جاتی ہے، جبکہ ٹاسک کی حدود انسٹالیشن، کنفیگریشن اور تصدیق کو الگ الگ قابلِ جائزہ رکھتی ہیں۔

## سپورٹ شدہ تعیناتی کا معاہدہ

[meta/platform_support.yml](../../../meta/platform_support.yml) سپورٹ پالیسی کا حتمی ماخذ ہے۔ مستحکم Molecule میٹرکس میں Nginx کے ساتھ Ubuntu 24.04/PHP 8.3 اور Ubuntu 26.04/PHP 8.5، Nginx کے ساتھ Debian 13/PHP 8.4، اور Apache کے ساتھ Rocky Linux 9 اور 10/PHP 8.3 شامل ہیں۔ ہر راستے کو HTTP اور HTTPS دونوں پر جانچا جاتا ہے۔ یہ ٹیسٹ شدہ OS/PHP جوڑے ہیں؛ غیر ٹیسٹ شدہ جوڑوں کے لیے انوینٹری اوور رائیڈز پیکیج میں تبدیلیوں سے پہلے ہی ناکام ہو جاتے ہیں۔ EL ایلیئسز (aliases) یہی پالیسی مشترک رکھتے ہیں، لیکن رن ٹائم شواہد Rocky Linux کنٹینرز سے حاصل ہوتے ہیں۔

Python 3.12 کنٹرولرز 14.x لائن میں Ansible 14.6 یا اس سے جدید ورژن کے ساتھ 2.21 لائن میں ansible-core 2.21.6 یا اس سے جدید ورژن استعمال کرتے ہیں۔ Python 3.13 اور 3.14 کنٹرولرز ansible-core 2.22.x کے ساتھ Ansible 15.x استعمال کرتے ہیں۔ ہیش شدہ requirements لاک کنٹرولر انٹرپریٹر کے لیے موزوں جوڑا منتخب کرتا ہے۔ مینیجڈ نوڈ انٹرپریٹر کے تقاضے الگ ہیں۔ ورژن منتخب کرنے سے پہلے پالیسی ملاحظہ کریں؛ پرانے پلیٹ فارمز اور محض اپ اسٹریم کی جانب سے سپورٹ شدہ PHP ورژنز خودکار طور پر نہیں اپنائے جاتے۔

## فیچر کی پختگی

بنیادی ٹاسک کی ترتیب [tasks/main.yml](../../../tasks/main.yml) میں بیان کی گئی ہے۔ مانیٹرنگ، بیک اپ، Fail2ban، سیکیورٹی، کیشنگ، اور فائر وال گروپس کے نامکمل ٹیمپلیٹ معاہدے [tests/unit/missing_templates.yml](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/tests/unit/missing_templates.yml) میں درج ہیں۔ ان کے فلیگز بطورِ ڈیفالٹ بند رہتے ہیں اور توثیق نامکمل گروپس کو فعال کرنے سے روک دیتی ہے۔ ٹاسک کے ناموں اور مثالی متغیرات (example variables) کو ان فیچرز کے فعال نفاذ کے طور پر پیش نہیں کیا جانا چاہیے۔

TLS، ڈیٹا بیس کریڈنشلز، تیار کردہ WordPress سیکرٹس، پاتھ گارڈز، اور OS سے مخصوص ہینڈلنگ کے لیے دستاویزی کنفیگریشن اور رن ٹائم چیکس ضروری ہیں۔ یہاں کسی خودکار فیل اوور، کلاؤڈ سطح پر دستیابی کے SLA، یا عالمگیر پروڈکشن تیاری کا دعویٰ نہیں کیا گیا ہے۔

## فوری آغاز

رول کو اس کے ریپوزیٹری سورس سے اور اس کی کلیکشن ڈیپینڈنسیز کو انسٹال کریں:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git,HEAD,wordpress_enterprise
ansible-galaxy collection install -r requirements.yml
```

کلیکشن کمانڈ اس چیک آؤٹ سے چلائیں۔ تعیناتی سے پہلے [defaults/main.yml](../../../defaults/main.yml) اور [مثالیں](../../../examples/README.md) کا جائزہ لیں۔ اندرونی ٹاسک مراحل کو براہِ راست کال کرنے کے بجائے سپورٹ شدہ انٹری پوائنٹ استعمال کریں۔

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

حوالہ دیے گئے سیکرٹس کو Ansible Vault یا کسی موجودہ سیکرٹ مینیجر کے ذریعے فراہم کریں۔ تعیناتی چلانے سے پہلے ٹارگٹ ہوسٹ کے لیے سرٹیفکیٹس اور ہوسٹ نیم ریزولوشن کنفیگر کریں۔ نامکمل فیچر گروپس کو غیر فعال رکھیں۔

## ڈیولپمنٹ اور ٹیسٹنگ

[Makefile](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/Makefile)، [CONTRIBUTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/CONTRIBUTING.md)، اور [TESTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/TESTING.md) ہیش شدہ ڈیپینڈنسی سیٹ اپ، لنٹ چیکس، یونٹ ٹیسٹس، اور عارضی Docker/Molecule معاہدوں کی وضاحت کرتے ہیں۔ یونٹ ٹیسٹس اور لنٹ کامیاب تعیناتی کی تصدیق نہیں کرتے۔

```bash
make lint
```

مستحکم `default` اور `tls` منظرناموں اور ان کی پیشگی شرائط کے لیے ٹیسٹنگ گائیڈ استعمال کریں۔ ہوسٹ انسٹالیشن، اپ گریڈ، کلین اپ، اور ریسٹور ٹاسکس منتخب مشینوں میں تبدیلیاں کرتے ہیں؛ توثیق کے لیے الگ تھلگ ٹیسٹ انوینٹریز استعمال کریں۔

## ورژننگ اور ریلیز پیکیجز

پروجیکٹ ریلیزز `meta/main.yml` کے کم از کم Ansible ورژن سے آزادانہ طور پر `VERSION` میں موجود مکمل SemVer ورژن استعمال کرتی ہیں۔ ریلیز کو ٹرگر کرنے کے لیے main برانچ پر مماثل `v2.22.1` ٹیگ پش کریں، یا مماثل ٹیگ بنانے کے بعد اسے main سے دستی طور پر چلائیں۔ ورک فلو تصدیق کرتا ہے کہ موجودہ ٹیگ چیک شدہ سورس کی طرف اشارہ کرتا ہے، مکمل CI سوٹ (بشمول چاروں Molecule منظرنامے) چلاتا ہے، اور Galaxy سے ہم آہنگ رول آرکائیو، Debian پیکیج، RPM، `release.json` اور `SHA256SUMS` شائع کرتا ہے۔ اشاعت ریلیز API کے ڈیفالٹ ٹارگٹ کو اوور رائیڈ کیے بغیر اسی تصدیق شدہ موجودہ ٹیگ کو استعمال کرتی ہے، چنانچہ main پر بعد کی کسی ورک فلو اپ ڈیٹ کے لیے وسیع تر workflow-write کریڈنشلز کی ضرورت نہیں پڑتی۔ غائب یا غیر مماثل ٹیگ ٹیسٹنگ سے پہلے ہی ناکام ہو جاتا ہے۔

ڈاؤن لوڈز کی تصدیق `sha256sum --check SHA256SUMS` سے کریں۔ مقامی پیکیجز کو Ubuntu 24.04 پر `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` یا Rocky Linux 9 پر `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` کے ذریعے انسٹال کریں۔ دونوں رول کو `/usr/share/ansible/roles/wordpress_enterprise` کے تحت انسٹال کرتے ہیں؛ ایک سپورٹ شدہ Ansible کنٹرولر فراہم کریں اور `requirements.yml` کو الگ سے انسٹال کریں۔ آرکائیو کو `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz,,wordpress_enterprise` سے انسٹال کیا جا سکتا ہے۔ مقامی پیکیجز میں رول کے سورسز اور دستاویزات شامل ہوتی ہیں اور انسٹالیشن کے دوران کوئی تعیناتی اسکرپٹ نہیں چلاتے۔ CI دونوں فارمیٹس کو انسٹال، چیک اور ریموو کرتا ہے۔

## سیکیورٹی اور لائسنس

[SECURITY.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/SECURITY.md) اور [MIT لائسنس](../../../LICENSE) ملاحظہ کریں۔ پیکیج میٹا ڈیٹا، پلیٹ فارم سپورٹ پالیسی، اور ریلیز توثیق کا فراہم کردہ رول کے ساتھ ہم آہنگ رہنا ضروری ہے۔
