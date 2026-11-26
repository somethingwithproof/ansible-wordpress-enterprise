<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · **العربية (المغرب)** · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
- **Africa:** [Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · **العربية (المغرب)** · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)
- **Asia:** [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [עברית](../he/README.md) · [मराठी](../mr/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [Bahasa Melayu](../ms/README.md) · [Filipino](../fil/README.md)

</details>
<!-- translations:end -->

# Ansible WordPress Enterprise

[![CI](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_ansible-wordpress-enterprise&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_ansible-wordpress-enterprise)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/ansible-wordpress-enterprise)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/releases)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/ansible-wordpress-enterprise/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/ansible-wordpress-enterprise)

دور Ansible باش تضبط مضيفي WordPress مع PHP، وسيرفر ويب، وقاعدة بيانات محلية ولا خارجية. التحقق من المنصة والمدخلات كيخدم قبل مراحل النشر، بينما حدود المهام كتخلي التثبيت، والإعداد، والتحقق قابلين للمراجعة كل واحد بوحدو.

## عقد النشر المدعوم

الملف [meta/platform_support.yml](../../../meta/platform_support.yml) هو المرجع الرسمي لسياسة الدعم. مصفوفة Molecule المستقرة كتغطي Ubuntu 24.04/PHP 8.3 وUbuntu 26.04/PHP 8.5 مع Nginx، وDebian 13/PHP 8.4 مع Nginx، وRocky Linux 9 و10/PHP 8.3 مع Apache. كل مسار كيتجرب عبر HTTP وHTTPS. هادو هما ثنائيات OS/PHP المجربة؛ أي تجاوزات فالـ inventory لثنائيات ما مجرباش كتفشل قبل ما توقع أي تغييرات فالحزم. الأسماء البديلة ديال EL كتشارك نفس السياسة، ولكن الأدلة ديال وقت التشغيل جاية من حاويات Rocky Linux.

متحكمات (controllers) ديال Python 3.12 كيستعملو Ansible 14.6 أو أحدث فسلسلة 14.x مع ansible-core 2.21.6 أو أحدث فسلسلة 2.21. متحكمات Python 3.13 و3.14 كيستعملو Ansible 15.x مع ansible-core 2.22.x. ملف قفل المتطلبات المجزأ (hashed requirements lock) كيختار الثنائي المناسب لمفسر المتحكم. متطلبات المفسر ديال العقدة المدارة (managed-node) منفصلة. راجع السياسة قبل ما تختار الإصدارات؛ المنصات القديمة وإصدارات PHP اللي مدعومة غير من المنبع (upstream) ما كيتعتمدوش تلقائياً.

## نضج الميزات

تسلسل المهام الأساسي محدد فـ [tasks/main.yml](../../../tasks/main.yml). المجموعات ديال المراقبة، والنسخ الاحتياطي، وFail2ban، والأمان، والتخزين المؤقت (caching)، والجدار الناري (firewall) عندهم عقود قوالب ناقصة مسجلة فـ [tests/unit/missing_templates.yml](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/tests/unit/missing_templates.yml). الخيارات (flags) ديالهم كتبقى طافية افتراضياً، وأي مجموعة ما كاملاش مفعّلة كتوقف غير ملي كيتشغّلو المهام ديالها، من بعد ما كيكونو المراحل السابقة دازو. سميات المهام ومتغيرات الأمثلة ما خاصش يتقدمو بحال إلا كانو تطبيقات خدامة ديال هاد الميزات.

إعدادات TLS، وبيانات الولوج لقاعدة البيانات، وأسرار WordPress المولدة، وحمايات المسارات، والتعامل الخاص بكل نظام تشغيل كيطلبو الإعدادات الموثقة وفحوصات وقت التشغيل. ما كاين حتى ادعاء هنا بتحويل تلقائي عند الفشل (failover)، أو اتفاقية مستوى خدمة (SLA) للتوفر على مستوى السحابة، أو جاهزية شاملة للإنتاج.

## البداية السريعة

ثبت الدور من المصدر ديالو فالمستودع ومعاه التبعيات ديال المجموعات:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git,HEAD,wordpress_enterprise
ansible-galaxy collection install -r requirements.yml
```

شغل أمر المجموعة من هاد النسخة المحلية. راجع [defaults/main.yml](../../../defaults/main.yml) و[الأمثلة](../../../examples/README.md) قبل النشر. استعمل نقطة الدخول المدعومة عوض ما تستدعي مراحل المهام الداخلية مباشرة.

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

وفر الأسرار المشار ليها عبر Ansible Vault ولا شي مدير أسرار موجود عندك. ضبط الشهادات وحل أسماء المضيفين (hostname resolution) للمضيف المستهدف قبل ما تطلق النشر. خلي مجموعات الميزات اللي ما كاملاش معطلة.

## التطوير والاختبار

الملفات [Makefile](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/Makefile) و[CONTRIBUTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/CONTRIBUTING.md) و[TESTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/TESTING.md) كيحددو إعداد التبعيات المجزأة، وفحوصات الـ lint، واختبارات الوحدة، وعقود Docker/Molecule المؤقتة. اختبارات الوحدة والـ lint بوحدهم ما كيضمنوش نجاح النشر.

```bash
make lint
```

استعمل دليل الاختبار على قبل سيناريوهات `default` و`tls` المستقرة والمتطلبات المسبقة ديالهم. مهام تثبيت المضيف، والتحديث، والتنظيف، والاسترجاع كتغير الآلات المختارة؛ خاصك تستعمل قوائم جرد (inventories) تجريبية معزولة باش تتحقق.

## الإصدارات وحزم الإطلاق

إصدارات المشروع كتستعمل رقم SemVer الكامل اللي كاين فـ `VERSION`، بشكل مستقل على أدنى إصدار Ansible اللي كاين فـ `meta/main.yml`. دفع وسم (tag) مطابق بحال `v2.22.1` على فرع main باش تطلق مسار Release، ولا شغلو يدوياً من main من بعد ما تصاوب الوسم المطابق. مسار العمل كيتحقق بلي الوسم الموجود كيشير للكود اللي تفحص، كيشغل مجموعة اختبارات CI كاملة (بما فيها سيناريوهات Molecule الأربعة كاملين)، وكينشر أرشيف دور متوافق مع Galaxy، وحزمة Debian، وRPM، و`release.json` و`SHA256SUMS`. النشر كيستعمل داك الوسم الموجود المتحقق منو بلا ما يتجاوز الهدف الافتراضي ديال API الإطلاق، باش أي تحديث لاحق لمسار العمل على main ما يحتاجش صلاحيات أوسع لكتابة مسارات العمل. إلى كان الوسم ناقص ولا ما مطابقش، العملية كتفشل قبل الاختبار.

تحقق من التحميلات بـ `sha256sum --check SHA256SUMS`. تقدر تثبت الحزم الأصلية بـ `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` على Ubuntu 24.04 ولا بـ `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` على Rocky Linux 9. بجوجهم كيثبتو الدور تحت `/usr/share/ansible/roles/wordpress_enterprise`؛ خاصك توفر متحكم Ansible مدعوم وتثبت `requirements.yml` بوحدو. الأرشيف تقدر تثبتو بـ `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz,,wordpress_enterprise`. الحزم الأصلية فيهم مصادر الدور والوثائق وما كيشغلو حتى سكريبت ديال النشر وقت التثبيت. نظام CI كيثبت، وكيتحقق، وكيزول الصيغتين بجوج.

## الأمان والرخصة

شوف [SECURITY.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/SECURITY.md) و[رخصة MIT](../../../LICENSE). البيانات الوصفية ديال الحزمة، وسياسة دعم المنصات، والتحقق من الإطلاق خاصهم يبقاو متوافقين مع الدور اللي كيتوزع.
