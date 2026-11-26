<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · **العربية** · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · **العربية** · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
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

دور Ansible لتهيئة مضيفات WordPress مع PHP وخادم ويب وقاعدة بيانات محلية أو خارجية. تُنفَّذ عمليات التحقق من المنصة والمدخلات قبل مراحل النشر، بينما تضمن حدود المهام إمكانية مراجعة التثبيت والتهيئة والتحقق بصورة منفصلة.

## عقد النشر المدعوم

يمثّل [meta/platform_support.yml](../../../meta/platform_support.yml) المرجع الرسمي لسياسة الدعم. تغطي مصفوفة Molecule المستقرة كلاً من Ubuntu 24.04/PHP 8.3 وUbuntu 26.04/PHP 8.5 مع Nginx، وDebian 13/PHP 8.4 مع Nginx، وRocky Linux 9 و10/PHP 8.3 مع Apache. ويُختبر كل مسار عبر HTTP وHTTPS. هذه هي أزواج نظام التشغيل وPHP المختبرة؛ وأي تجاوزات في المخزون (inventory) لأزواج غير مختبرة تفشل قبل إجراء أي تغييرات على الحزم. تتشارك بدائل EL السياسة نفسها، غير أن أدلة وقت التشغيل مستمدة من حاويات Rocky Linux.

تستخدم عقد التحكم العاملة بـ Python 3.12 إصدار Ansible 14.6 أو أحدث ضمن السلسلة 14.x مع ansible-core 2.21.6 أو أحدث ضمن السلسلة 2.21. بينما تستخدم عقد التحكم العاملة بـ Python 3.13 و3.14 إصدار Ansible 15.x مع ansible-core 2.22.x. يختار ملف قفل المتطلبات المزوّد بالتجزئة الزوج المناسب لمفسّر عقدة التحكم. وتُعدّ متطلبات مفسّر العقد المُدارة منفصلة. راجع السياسة قبل اختيار الإصدارات؛ إذ لا يُعتمد تلقائياً دعم المنصات الأقدم أو إصدارات PHP المدعومة من المصدر الأصلي فقط.

## نضج الميزات

يُعرَّف تسلسل المهام الأساسي في [tasks/main.yml](../../../tasks/main.yml). وتحتوي مجموعات المراقبة والنسخ الاحتياطي وFail2ban والأمان والتخزين المؤقت وجدار الحماية على عقود قوالب مفقودة مسجّلة في [tests/unit/missing_templates.yml](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/tests/unit/missing_templates.yml). تبقى رايات تفعيلها معطّلة افتراضياً، ويرفض التحقق تفعيل المجموعات غير المكتملة. يجب عدم تقديم أسماء المهام أو متغيرات الأمثلة على أنها تنفيذات عاملة لتلك الميزات.

تتطلب تهيئة TLS وبيانات اعتماد قاعدة البيانات وأسرار WordPress المُنشأة وآليات حماية المسارات والمعالجة الخاصة بكل نظام تشغيل التهيئةَ الموثّقة وفحوصات وقت التشغيل. لا يُدّعى هنا وجود تجاوز فشل تلقائي، أو اتفاقية مستوى خدمة (SLA) للتوافر على مستوى السحابة، أو جاهزية شاملة للإنتاج.

## البدء السريع

ثبّت الدور من مصدر مستودعه وتبعيات مجموعاته:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git,HEAD,wordpress_enterprise
ansible-galaxy collection install -r requirements.yml
```

نفّذ أمر المجموعة من هذه النسخة المستخرجة. وراجع [defaults/main.yml](../../../defaults/main.yml) و[الأمثلة](../../../examples/README.md) قبل النشر. استخدم نقطة الدخول المدعومة بدلاً من استدعاء مراحل المهام الداخلية مباشرةً.

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

زوّد الأسرار المشار إليها عبر Ansible Vault أو مدير أسرار قائم. وهيّئ الشهادات وتحليل أسماء المضيفات للمضيف المستهدف قبل تشغيل النشر. وأبقِ مجموعات الميزات غير المكتملة معطّلة.

## التطوير والاختبار

يحدّد كل من [Makefile](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/Makefile) و[CONTRIBUTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/CONTRIBUTING.md) و[TESTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/TESTING.md) إعداد التبعيات المزوّدة بالتجزئة، وفحوصات التدقيق للشفرة (lint)، واختبارات الوحدات، وعقود Docker/Molecule المؤقتة. ولا تثبت اختبارات الوحدات وفحوصات التدقيق نجاح عملية النشر.

```bash
make lint
```

ارجع إلى دليل الاختبار لمعرفة السيناريوهين المستقرين `default` و`tls` ومتطلباتهما المسبقة. تُعدّل مهام تثبيت المضيف وترقيته وتنظيفه واستعادته الأجهزةَ المحددة؛ لذا استخدم مخزونات اختبار معزولة لأغراض التحقق.

## الإصدارات وحزم الإطلاق

تستخدم إصدارات المشروع رقم إصدار SemVer الكامل الموجود في `VERSION`، بصورة مستقلة عن الحد الأدنى لإصدار Ansible المحدّد في `meta/main.yml`. ادفع وسماً مطابقاً مثل `v2.22.1` على الفرع main لتشغيل سير عمل الإطلاق (Release)، أو شغّله يدوياً من الفرع main بعد إنشاء الوسم المطابق. يتحقق سير العمل من أن الوسم الموجود يشير إلى الشفرة المصدرية التي جرى فحصها، ويشغّل حزمة التكامل المستمر (CI) الكاملة (بما في ذلك جميع سيناريوهات Molecule الأربعة)، ثم ينشر أرشيف دور متوافقاً مع Galaxy وحزمة Debian وحزمة RPM وملفي `release.json` و`SHA256SUMS`. يعتمد النشر على ذلك الوسم الموجود والمتحقَّق منه دون تجاوز الهدف الافتراضي لواجهة برمجة تطبيقات الإطلاقات، بحيث لا يتطلب أي تحديث لاحق لسير العمل على main صلاحيات أوسع لكتابة سير العمل. ويفشل التشغيل قبل الاختبار في حال كان الوسم مفقوداً أو غير مطابق.

تحقق من التنزيلات باستخدام `sha256sum --check SHA256SUMS`. ثبّت الحزم الأصلية باستخدام `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` على Ubuntu 24.04 أو `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` على Rocky Linux 9. يثبّت كلاهما الدور تحت المسار `/usr/share/ansible/roles/wordpress_enterprise`؛ وفّر عقدة تحكم Ansible مدعومة وثبّت `requirements.yml` بشكل منفصل. ويمكن تثبيت الأرشيف باستخدام `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz,,wordpress_enterprise`. تحتوي الحزم الأصلية على مصادر الدور وتوثيقه ولا تشغّل أي نصوص نشر برمجية أثناء التثبيت. ويقوم التكامل المستمر (CI) بتثبيت كلا التنسيقين والتحقق منهما وإزالتهما.

## الأمان والترخيص

راجع [SECURITY.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/SECURITY.md) و[رخصة MIT](../../../LICENSE). يجب أن تظل البيانات الوصفية للحزمة وسياسة دعم المنصات والتحقق من الإطلاقات متوافقة مع الدور المُشحون.
