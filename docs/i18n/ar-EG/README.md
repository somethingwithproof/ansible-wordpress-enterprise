<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · **العربية (مصر)** · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
- **Africa:** [Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · **العربية (مصر)** · [العربية (المغرب)](../ar-MA/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)
- **Asia:** [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [עברית](../he/README.md) · [मराठी](../mr/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [Bahasa Melayu](../ms/README.md) · [Filipino](../fil/README.md)

</details>
<!-- translations:end -->

# Ansible WordPress Enterprise

[![CI](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_ansible-wordpress-enterprise&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_ansible-wordpress-enterprise)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/ansible-wordpress-enterprise)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/releases)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/ansible-wordpress-enterprise/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/ansible-wordpress-enterprise)

دور (role) لـ Ansible علشان تهيّأ سيرفرات WordPress مع PHP، وسيرفر ويب، وقاعدة بيانات محلية أو خارجية. التحقق من المنصة والمدخلات بيشتغل قبل مراحل النشر، وحدود المهام بتخلّي التثبيت والإعدادات والتحقق قابلين للمراجعة كل واحد لوحده.

## عقد النشر المدعوم

الملف [meta/platform_support.yml](../../../meta/platform_support.yml) هو المرجع الأساسي لسياسة الدعم. مصفوفة Molecule المستقرة بتغطي Ubuntu 24.04/PHP 8.3 وUbuntu 26.04/PHP 8.5 مع Nginx، وDebian 13/PHP 8.4 مع Nginx، وRocky Linux 9 و10/PHP 8.3 مع Apache. كل مسار بيتجرّب على HTTP وHTTPS. دي أزواج أنظمة التشغيل وPHP اللي تم اختبارها؛ أي تعديل في الـ inventory لأزواج غير مختبرة بيفشل قبل ما يحصل أي تغيير في الحزم. أسماء EL البديلة بتتشارك نفس السياسة، لكن أدلة التشغيل الفعلية جاية من حاويات Rocky Linux.

أجهزة الـ controller اللي عليها Python 3.12 بتستخدم Ansible 14.6 أو أحدث في سلسلة 14.x مع ansible-core 2.21.6 أو أحدث في سلسلة 2.21. أما أجهزة الـ controller اللي عليها Python 3.13 و3.14 فبتستخدم Ansible 15.x مع ansible-core 2.22.x. ملف قفل المتطلبات بالـ hash بيختار الزوج المناسب لمفسّر الـ controller. متطلبات مفسّر العُقد المُدارة (managed nodes) منفصلة. راجع السياسة قبل ما تختار الإصدارات؛ المنصات الأقدم وإصدارات PHP المدعومة من المصدر الأصلي بس مش بتُعتمد بشكل تلقائي.

## نضج الميزات

تسلسل المهام الأساسي متعرّف في [tasks/main.yml](../../../tasks/main.yml). مجموعات المراقبة، والنسخ الاحتياطي، وFail2ban، والأمان، والـ caching، والـ firewall عندها عقود قوالب ناقصة متسجّلة في [tests/unit/missing_templates.yml](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/tests/unit/missing_templates.yml). الإعدادات (flags) بتاعتها بتفضل مقفولة افتراضيًا، وأي مجموعة غير مكتملة متفعّلة بتقف بس لما مهامها تشتغل، بعد ما المراحل اللي قبلها تكون اشتغلت. ما ينفعش تقديم أسماء المهام أو متغيرات الأمثلة على إنها تنفيذ شغال للميزات دي.

الـ TLS، وبيانات اعتماد قاعدة البيانات، وأسرار WordPress المولّدة، وحمايات المسارات، والتعامل الخاص بكل نظام تشغيل محتاجين الإعدادات الموثّقة وفحوصات وقت التشغيل. مفيش هنا أي ادعاء بوجود failover تلقائي، أو اتفاقية مستوى خدمة (SLA) للتوافر على مستوى السحابة، أو جاهزية إنتاجية شاملة.

## البداية السريعة

ثبّت الدور من مصدر المستودع بتاعه ومن التبعيات بتاعة الـ collections الخاصة بيه:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git,HEAD,wordpress_enterprise
ansible-galaxy collection install -r requirements.yml
```

شغّل أمر الـ collection من النسخة دي. راجع [defaults/main.yml](../../../defaults/main.yml) و[الأمثلة](../../../examples/README.md) قبل النشر. استخدم نقطة الدخول المدعومة بدل ما تنادي مراحل المهام الداخلية بشكل مباشر.

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

وفّر الأسرار المذكورة عن طريق Ansible Vault أو مدير أسرار موجود عندك. اضبط الشهادات وتحليل أسماء النطاقات (hostname resolution) للسيرفر المستهدف قبل ما تشغّل النشر. وسيب مجموعات الميزات غير المكتملة مقفولة.

## التطوير والاختبار

الملفات [Makefile](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/Makefile) و[CONTRIBUTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/CONTRIBUTING.md) و[TESTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/TESTING.md) بتحدد إعداد التبعيات بالـ hash، وفحوصات الـ lint، واختبارات الوحدة (unit tests)، وعقود Docker/Molecule المؤقتة. اختبارات الوحدة والـ lint لوحدهم مش بيثبتوا نجاح النشر.

```bash
make lint
```

استخدم دليل الاختبار علشان تشوف سيناريوهات `default` و`tls` المستقرة ومتطلباتها المسبقة. مهام التثبيت والترقية والتنظيف والاستعادة على السيرفر بتغيّر الأجهزة المختارة؛ علشان كده استخدم inventories تجريبية معزولة للتحقق.

## إدارة الإصدارات وحزم الإطلاق

إصدارات المشروع بتستخدم رقم SemVer الكامل الموجود في `VERSION`، بشكل مستقل عن الحد الأدنى لإصدار Ansible الموجود في `meta/main.yml`. ارفع تاج مطابق زي `v2.22.1` على فرع main علشان تشغّل سير عمل Release، أو شغّله يدويًا من main بعد ما تعمل التاج المطابق. سير العمل بيتأكد إن التاج الموجود بيشاور على الكود اللي بيتفحص، وبيشغّل مجموعة الـ CI كاملة (بما فيها الأربع سيناريوهات بتوع Molecule)، وبينشر أرشيف للدور متوافق مع Galaxy، وحزمة Debian، وحزمة RPM، وملفات `release.json` و`SHA256SUMS`. النشر بيستخدم التاج المتحقَّق منه ده من غير ما يغيّر الهدف الافتراضي لـ API الإصدارات، فبالتالي أي تحديث لاحق لسير العمل على main مش بيحتاج صلاحيات أوسع للكتابة على الـ workflows. لو التاج ناقص أو غير مطابق العملية بتفشل قبل الاختبار.

تقدر تتحقق من التنزيلات باستخدام `sha256sum --check SHA256SUMS`. وثبّت الحزم الأصلية باستخدام `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` على Ubuntu 24.04 أو `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` على Rocky Linux 9. الاتنين بيثبّتوا الدور تحت `/usr/share/ansible/roles/wordpress_enterprise`؛ لازم توفّر Ansible controller مدعوم وتثبّت `requirements.yml` بشكل منفصل. وتقدر تثبّت الأرشيف باستخدام `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz,,wordpress_enterprise`. الحزم الأصلية فيها ملفات مصدر الدور والتوثيق بس ومش بتشغّل أي سكربتات نشر أثناء التثبيت. الـ CI بيثبّت الصيغتين وبيتحقق منهم وبيمسحهم.

## الأمان والرخصة

راجع [SECURITY.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/SECURITY.md) و[رخصة MIT](../../../LICENSE). لازم البيانات الوصفية للحزمة، وسياسة دعم المنصات، والتحقق من الإصدار يفضلوا متوافقين مع الدور المنشور.
