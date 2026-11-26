<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · **فارسی** · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
- **Africa:** [Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)
- **Asia:** [বাংলা](../bn/README.md) · **فارسی** · [עברית](../he/README.md) · [मराठी](../mr/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [Bahasa Melayu](../ms/README.md) · [Filipino](../fil/README.md)

</details>
<!-- translations:end -->

# Ansible WordPress Enterprise

[![CI](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_ansible-wordpress-enterprise&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_ansible-wordpress-enterprise)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/ansible-wordpress-enterprise)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/releases)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/ansible-wordpress-enterprise/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/ansible-wordpress-enterprise)

نقشی از Ansible برای پیکربندی میزبان‌های WordPress به همراه PHP، وب‌سرور و پایگاه داده محلی یا خارجی. اعتبارسنجی پلتفرم و ورودی‌ها پیش از مراحل استقرار اجرا می‌شود، در حالی که مرزهای وظایف باعث می‌شوند نصب، پیکربندی و راستی‌آزمایی به‌صورت جداگانه قابل بررسی باشند.

## قرارداد استقرار پشتیبانی‌شده

فایل [meta/platform_support.yml](../../../meta/platform_support.yml) مرجع اصلی سیاست پشتیبانی است. ماتریس پایدار Molecule شامل Ubuntu 24.04/PHP 8.3 و Ubuntu 26.04/PHP 8.5 با Nginx، Debian 13/PHP 8.4 با Nginx و Rocky Linux 9 و 10/PHP 8.3 با Apache است. هر مسیر روی HTTP و HTTPS آزمایش می‌شود. این‌ها زوج‌های آزمایش‌شده سیستم‌عامل/PHP هستند؛ بازنویسی‌های inventory به زوج‌های آزمایش‌نشده پیش از اعمال تغییرات بسته‌ها با خطا متوقف می‌شوند. نام‌های مستعار EL همین سیاست را به اشتراک می‌گذارند، اما شواهد زمان اجرا از کانتینرهای Rocky Linux به دست می‌آید.

کنترلرهای Python 3.12 از Ansible 14.6 یا جدیدتر در شاخه 14.x به همراه ansible-core 2.21.6 یا جدیدتر در شاخه 2.21 استفاده می‌کنند. کنترلرهای Python 3.13 و 3.14 از Ansible 15.x به همراه ansible-core 2.22.x استفاده می‌کنند. فایل قفل نیازمندی‌های هش‌شده، زوج متناسب با مفسر کنترلر را انتخاب می‌کند. نیازمندی‌های مفسر گره‌های مدیریت‌شده جداگانه هستند. پیش از انتخاب نسخه‌ها به سیاست پشتیبانی مراجعه کنید؛ پلتفرم‌های قدیمی‌تر و نسخه‌های PHP که صرفاً در بالادست پشتیبانی می‌شوند به‌صورت خودکار پذیرفته نمی‌شوند.

## بلوغ قابلیت‌ها

توالی وظایف هسته در [tasks/main.yml](../../../tasks/main.yml) تعریف شده است. گروه‌های پایش، پشتیبان‌گیری، Fail2ban، امنیت، کش‌سازی و فایروال دارای قراردادهای قالب ناقص هستند که در [tests/unit/missing_templates.yml](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/tests/unit/missing_templates.yml) ثبت شده‌اند. پرچم‌های آن‌ها به‌صورت پیش‌فرض خاموش باقی می‌مانند، و یک گروه ناقص فعال‌شده تنها زمانی متوقف می‌شود که پس از اجرای مراحل قبلی، وظایف خودش اجرا شوند. نام وظایف و متغیرهای نمونه نباید به‌عنوان پیاده‌سازی‌های عملیاتی آن قابلیت‌ها تلقی شوند.

TLS، اعتبارنامه‌های پایگاه داده، اسرار تولیدشده WordPress، محافظ‌های مسیر و مدیریت اختصاصی سیستم‌عامل نیازمند پیکربندی مستندشده و بررسی‌های زمان اجرا هستند. در اینجا هیچ ادعایی درباره انتقال خودکار هنگام خطا (failover)، توافق‌نامه سطح دسترس‌پذیری در مقیاس ابر (SLA) یا آمادگی همگانی برای محیط عملیاتی مطرح نمی‌شود.

## شروع سریع

نقش را از منبع مخزن آن به همراه وابستگی‌های مجموعه‌اش نصب کنید:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git,HEAD,wordpress_enterprise
ansible-galaxy collection install -r requirements.yml
```

دستور مجموعه را از همین نسخه محلی اجرا کنید. پیش از استقرار، [defaults/main.yml](../../../defaults/main.yml) و [مثال‌ها](../../../examples/README.md) را بررسی کنید. به‌جای فراخوانی مستقیم مراحل داخلی وظایف، از نقطه ورود پشتیبانی‌شده استفاده کنید.

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

اسرار ارجاع‌شده را از طریق Ansible Vault یا یک مدیر اسرار موجود تأمین کنید. پیش از اجرای استقرار، گواهینامه‌ها و تفکیک نام میزبان را برای میزبان هدف پیکربندی کنید. گروه‌های قابلیت ناقص را غیرفعال نگه دارید.

## توسعه و آزمون

فایل‌های [Makefile](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/Makefile)، [CONTRIBUTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/CONTRIBUTING.md) و [TESTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/TESTING.md) راه‌اندازی وابستگی‌های هش‌شده، بررسی‌های lint، آزمون‌های واحد و قراردادهای یک‌بارمصرف Docker/Molecule را تعریف می‌کنند. آزمون‌های واحد و lint استقرار موفق را اثبات نمی‌کنند.

```bash
make lint
```

برای سناریوهای پایدار `default` و `tls` و پیش‌نیازهای آن‌ها از راهنمای آزمون استفاده کنید. وظایف نصب، ارتقا، پاک‌سازی و بازیابی میزبان، ماشین‌های انتخاب‌شده را تغییر می‌دهند؛ برای اعتبارسنجی از inventoryهای آزمایشی ایزوله استفاده کنید.

## نسخه‌گذاری و بسته‌های انتشار

انتشارهای پروژه از نسخه کامل SemVer در `VERSION` به‌طور مستقل از حداقل نسخه Ansible در `meta/main.yml` استفاده می‌کنند. برای آغاز گردش‌کار Release، یک برچسب منطبق مانند `v2.22.1` را روی شاخه main ارسال کنید یا پس از ایجاد برچسب منطبق، آن را به‌صورت دستی از main اجرا کنید. گردش‌کار تأیید می‌کند که برچسب موجود به منبع بررسی‌شده اشاره دارد، مجموعه کامل CI (شامل هر چهار سناریوی Molecule) را اجرا می‌کند و یک آرشیو نقش سازگار با Galaxy، بسته Debian، بسته RPM، `release.json` و `SHA256SUMS` را منتشر می‌کند. انتشار از همان برچسب موجود و تأییدشده بدون بازنویسی هدف پیش‌فرض API انتشار استفاده می‌کند، بنابراین به‌روزرسانی بعدی گردش‌کار روی main نیازمند مجوزهای گسترده‌تر نوشتن گردش‌کار نیست. نبود برچسب یا عدم تطابق آن پیش از مرحله آزمون باعث شکست می‌شود.

فایل‌های دریافتی را با `sha256sum --check SHA256SUMS` راستی‌آزمایی کنید. بسته‌های بومی را با `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` در Ubuntu 24.04 یا با `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` در Rocky Linux 9 نصب کنید. هر دو، نقش را در مسیر `/usr/share/ansible/roles/wordpress_enterprise` نصب می‌کنند؛ یک کنترلر پشتیبانی‌شده Ansible فراهم کنید و `requirements.yml` را به‌صورت جداگانه نصب کنید. آرشیو را می‌توان با `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz,,wordpress_enterprise` نصب کرد. بسته‌های بومی حاوی کد منبع و مستندات نقش هستند و هنگام نصب هیچ اسکریپت استقراری اجرا نمی‌کنند. CI هر دو قالب را نصب، بررسی و حذف می‌کند.

## امنیت و مجوز

[SECURITY.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/SECURITY.md) و [مجوز MIT](../../../LICENSE) را ببینید. فراداده بسته، سیاست پشتیبانی پلتفرم و اعتبارسنجی انتشار باید با نقش ارائه‌شده هم‌راستا باقی بمانند.
