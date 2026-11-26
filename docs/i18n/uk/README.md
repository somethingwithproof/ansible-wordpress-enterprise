<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · **Українська** · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · **Українська** · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
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

Роль Ansible для налаштування хостів WordPress із PHP, вебсервером та локальною або зовнішньою базою даних. Перевірка платформи та вхідних параметрів виконується до етапів розгортання, а чіткі межі між завданнями дають змогу окремо переглядати встановлення, налаштування та перевірку.

## Контракт підтримуваного розгортання

[meta/platform_support.yml](../../../meta/platform_support.yml) є основним джерелом політики підтримки. Стабільна матриця Molecule охоплює Ubuntu 24.04/PHP 8.3 та Ubuntu 26.04/PHP 8.5 із Nginx, Debian 13/PHP 8.4 із Nginx, а також Rocky Linux 9 і 10/PHP 8.3 з Apache. Кожен варіант перевіряється через HTTP та HTTPS. Це протестовані пари ОС/PHP; перевизначення в інвентарі на непротестовані пари завершуються помилкою ще до зміни пакетів. Псевдоніми EL підпорядковуються тій самій політиці, проте результати виконання отримано в контейнерах Rocky Linux.

Контролери з Python 3.12 використовують Ansible 14.6 або новішої версії в лінійці 14.x разом із ansible-core 2.21.6 або новішої версії в лінійці 2.21. Контролери з Python 3.13 і 3.14 використовують Ansible 15.x з ansible-core 2.22.x. Файл блокування залежностей із хешами вибирає відповідну пару для інтерпретатора контролера. Вимоги до інтерпретатора керованого вузла визначаються окремо. Ознайомтеся з політикою перед вибором версій; старіші платформи та версії PHP, які підтримуються лише в апстрімі, не додаються автоматично.

## Зрілість функціональності

Основну послідовність завдань визначено в [tasks/main.yml](../../../tasks/main.yml). Групи моніторингу, резервного копіювання, Fail2ban, безпеки, кешування та брандмауера мають відсутні контракти шаблонів, зафіксовані в [tests/unit/missing_templates.yml](../../../tests/unit/missing_templates.yml). Їхні прапорці за замовчуванням вимкнено, а валідація відхиляє ввімкнення незавершених груп. Назви завдань і приклади змінних не слід сприймати як робочі реалізації цих функцій.

TLS, облікові дані бази даних, згенеровані секрети WordPress, перевірки шляхів і специфічна для ОС обробка потребують задокументованої конфігурації та перевірок під час виконання. Тут не надається жодних гарантій автоматичного аварійного перемикання, хмарної угоди SLA щодо доступності чи універсальної готовності до промислової експлуатації.

## Швидкий старт

Встановіть роль із її репозиторію та залежності її колекцій:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git,HEAD,wordpress_enterprise
ansible-galaxy collection install -r requirements.yml
```

Виконайте команду для колекцій із цієї локальної копії репозиторію. Перед розгортанням перегляньте [defaults/main.yml](../../../defaults/main.yml) та [приклади](../../../examples/README.md). Використовуйте підтримувану точку входу замість прямого виклику внутрішніх етапів завдань.

```yaml
- hosts: wordpress_test_hosts
  become: true
  vars:
    wordpress_web_server: nginx
    wordpress_site_url: "http://wordpress.example.com"
    wordpress_server_name: wordpress.example.com
    wordpress_admin_password: "{{ vault_wordpress_admin_password }}"
    wordpress_db_password: "{{ vault_wordpress_db_password }}"
    wordpress_db_root_password: "{{ vault_wordpress_db_root_password }}"
  roles:
    - wordpress_enterprise
```

Передавайте зазначені секрети через Ansible Vault або наявний менеджер секретів. Перед запуском розгортання налаштуйте сертифікати та розпізнавання імені хоста для цільового сервера. Залишайте незавершені групи функцій вимкненими.

## Розробка та тестування

[Makefile](../../../Makefile), [CONTRIBUTING.md](../../../CONTRIBUTING.md) і [TESTING.md](../../../TESTING.md) визначають налаштування залежностей із хешами, перевірки лінтером, модульні тести та одноразові контракти Docker/Molecule. Модульні тести та лінтинг не гарантують успішного розгортання.

```bash
make lint
```

Скористайтеся посібником із тестування для стабільних сценаріїв `default` і `tls` та їхніх передумов. Завдання встановлення, оновлення, очищення та відновлення хоста змінюють стан вибраних машин; для перевірки використовуйте ізольовані тестові інвентарі.

## Версіонування та пакети релізів

Релізи проєкту використовують повну версію SemVer із файлу `VERSION`, незалежно від мінімальної версії Ansible у `meta/main.yml`. Надішліть відповідний тег `v2.22.1` у гілку main, щоб запустити робочий процес Release, або запустіть його вручну з main після створення відповідного тегу. Робочий процес перевіряє, що наявний тег указує на перевірений вихідний код, виконує повний набір CI (включно з усіма чотирма сценаріями Molecule) та публікує сумісний із Galaxy архів ролі, пакет Debian, RPM, `release.json` і `SHA256SUMS`. Публікація використовує цей перевірений наявний тег без перевизначення цілі за замовчуванням у API релізів, тому подальше оновлення робочого процесу в main не вимагає ширших прав запису для робочих процесів. Відсутній або невідповідний тег призводить до помилки ще до початку тестування.

Перевірте завантажені файли командою `sha256sum --check SHA256SUMS`. Встановіть системні пакети за допомогою `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` на Ubuntu 24.04 або `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` на Rocky Linux 9. Обидва встановлюють роль у каталог `/usr/share/ansible/roles/wordpress_enterprise`; забезпечте підтримуваний контролер Ansible та встановіть `requirements.yml` окремо. Архів можна встановити командою `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz,,wordpress_enterprise`. Системні пакети містять вихідний код ролі та документацію і не запускають жодних скриптів розгортання під час встановлення. CI встановлює, перевіряє та видаляє обидва формати.

## Безпека та ліцензія

Див. [SECURITY.md](../../../SECURITY.md) і [ліцензію MIT](../../../LICENSE). Метадані пакета, політика підтримки платформ і перевірка релізів повинні залишатися узгодженими з роллю, що постачається.
