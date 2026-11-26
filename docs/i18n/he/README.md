<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · **עברית** · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
- **Africa:** [Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)
- **Asia:** [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · **עברית** · [मराठी](../mr/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [Bahasa Melayu](../ms/README.md) · [Filipino](../fil/README.md)

</details>
<!-- translations:end -->

# Ansible WordPress Enterprise

[![CI](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_ansible-wordpress-enterprise&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_ansible-wordpress-enterprise)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/ansible-wordpress-enterprise)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/releases)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/ansible-wordpress-enterprise/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/ansible-wordpress-enterprise)

תפקיד Ansible להגדרת מארחי WordPress עם PHP, שרת אינטרנט ומסד נתונים מקומי או חיצוני. אימות הפלטפורמה והקלט רץ לפני שלבי הפריסה, בעוד שגבולות המשימות מאפשרים לסקור בנפרד את ההתקנה, התצורה והאימות.

## חוזה הפריסה הנתמך

[meta/platform_support.yml](../../../meta/platform_support.yml) הוא המקור הקובע למדיניות התמיכה. מטריצת Molecule היציבה מכסה את Ubuntu 24.04/PHP 8.3 ו-Ubuntu 26.04/PHP 8.5 עם Nginx, את Debian 13/PHP 8.4 עם Nginx, ואת Rocky Linux 9 ו-10/PHP 8.3 עם Apache. כל נתיב נבדק מעל HTTP ו-HTTPS. אלו הם צמדי מערכת ההפעלה וה-PHP שנבדקו; דריסות במלאי (inventory) לצמדים שלא נבדקו נכשלות לפני שינויי חבילות. כינויי EL חולקים את המדיניות, אך ראיות זמן הריצה מגיעות ממכולות Rocky Linux.

בקרים עם Python 3.12 משתמשים ב-Ansible 14.6 ומעלה בענף 14.x יחד עם ansible-core 2.21.6 ומעלה בענף 2.21. בקרים עם Python 3.13 ו-3.14 משתמשים ב-Ansible 15.x יחד עם ansible-core 2.22.x. קובץ נעילת הדרישות המגובב (hashed) בוחר את הצמד המתאים למפרש של הבקר. דרישות המפרש של הצמתים המנוהלים הן נפרדות. עיינו במדיניות לפני בחירת גרסאות; פלטפורמות ישנות יותר וגרסאות PHP הנתמכות רק ב-upstream אינן מאומצות באופן אוטומטי.

## בשלות התכונות

רצף המשימות המרכזי מוגדר ב-[tasks/main.yml](../../../tasks/main.yml). לקבוצות הניטור, הגיבוי, Fail2ban, האבטחה, המטמון וחומת האש יש חוזי תבניות חסרים המתועדים ב-[tests/unit/missing_templates.yml](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/tests/unit/missing_templates.yml). הדגלים שלהן נותרים כבויים כברירת מחדל, וקבוצה לא שלמה שהופעלה נעצרת רק כאשר משימותיה רצות, לאחר שהשלבים הקודמים כבר רצו. אין להציג שמות משימות ומשתני דוגמה כמימושים פעילים של תכונות אלו.

TLS, פרטי התחברות למסד הנתונים, סודות WordPress שנוצרו, הגנות נתיבים וטיפול ייעודי למערכת ההפעלה מחייבים את התצורה המתועדת ובדיקות זמן ריצה. לא נטענות כאן יכולת מעבר אוטומטי לגיבוי (failover), הבטחת זמינות (SLA) כלל-עננית או מוכנות אוניברסלית לייצור.

## התחלה מהירה

התקינו את התפקיד ממקור המאגר שלו ואת תלויות האוספים שלו:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git,HEAD,wordpress_enterprise
ansible-galaxy collection install -r requirements.yml
```

הריצו את פקודת האוסף מעותק העבודה הנוכחי. עיינו ב-[defaults/main.yml](../../../defaults/main.yml) וב[דוגמאות](../../../examples/README.md) לפני הפריסה. השתמשו בנקודת הכניסה הנתמכת במקום לקרוא ישירות לשלבי משימות פנימיים.

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

ספקו את הסודות הנדרשים באמצעות Ansible Vault או מנהל סודות קיים. הגדירו תעודות ופתרון שמות מארחים (hostname resolution) עבור מארח היעד לפני הרצת פריסה. השאירו קבוצות תכונות לא שלמות מושבתות.

## פיתוח ובדיקות

[Makefile](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/Makefile), [CONTRIBUTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/CONTRIBUTING.md) ו-[TESTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/TESTING.md) מגדירים את התקנת התלויות המגובבות, בדיקות ה-lint, בדיקות היחידה וחוזי ה-Docker/Molecule החד-פעמיים. בדיקות יחידה ו-lint אינם מוכיחים פריסה מוצלחת.

```bash
make lint
```

היעזרו במדריך הבדיקות עבור התרחישים היציבים `default` ו-`tls` והדרישות המקדימות שלהם. משימות התקנה, שדרוג, ניקוי ושחזור במארח משנות את המכונות שנבחרו; השתמשו במלאי בדיקה מבודד לצורך אימות.

## ניהול גרסאות וחבילות שחרור

שחרורי הפרויקט משתמשים בגרסת SemVer המלאה בקובץ `VERSION`, ללא תלות בגרסת ה-Ansible המינימלית שב-`meta/main.yml`. דחפו תג `v2.22.1` תואם בענף main כדי להפעיל את Release, או הריצו אותו ידנית מתוך main לאחר יצירת התג התואם. התהליך מאמת שהתג הקיים מצביע על קוד המקור הנבדק, מריץ את חבילת ה-CI המלאה (כולל כל ארבעת תרחישי Molecule), ומפרסם ארכיון תפקיד תואם Galaxy, חבילת Debian, חבילת RPM, `release.json` ו-`SHA256SUMS`. הפרסום משתמש בתג הקיים והמאומת מבלי לדרוס את יעד ברירת המחדל של ה-API לשחרורים, כך שעדכון מאוחר יותר של התהליך בענף main אינו דורש הרשאות כתיבה רחבות יותר לתהליכי עבודה. תג חסר או לא תואם נכשל עוד לפני הבדיקות.

אמתו את ההורדות באמצעות `sha256sum --check SHA256SUMS`. התקינו חבילות מקומיות באמצעות `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` על Ubuntu 24.04 או באמצעות `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` על Rocky Linux 9. שתי החבילות מתקינות את התפקיד תחת `/usr/share/ansible/roles/wordpress_enterprise`; יש לספק בקר Ansible נתמך ולהתקין את `requirements.yml` בנפרד. ניתן להתקין את הארכיון באמצעות `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz,,wordpress_enterprise`. החבילות המקומיות מכילות את מקורות התפקיד והתיעוד ואינן מריצות סקריפטי פריסה במהלך ההתקנה. ה-CI מתקין, בודק ומסיר את שני הפורמטים.

## אבטחה ורישיון

ראו [SECURITY.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/SECURITY.md) ואת [רישיון MIT](../../../LICENSE). המטא-דאטה של החבילה, מדיניות התמיכה בפלטפורמות ואימות השחרור חייבים להישאר מסונכרנים עם התפקיד המופץ.
