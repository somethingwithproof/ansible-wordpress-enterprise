<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · **Русский** · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · **Русский** · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
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

Роль Ansible для настройки хостов WordPress с PHP, веб-сервером и локальной или внешней базой данных. Проверка платформы и входных данных выполняется до этапов развёртывания, а чёткое разделение задач позволяет независимо проверять установку, настройку и верификацию.

## Контракт поддерживаемого развёртывания

Источником политики поддержки является [meta/platform_support.yml](../../../meta/platform_support.yml). Стабильная матрица Molecule охватывает Ubuntu 24.04/PHP 8.3 и Ubuntu 26.04/PHP 8.5 с Nginx, Debian 13/PHP 8.4 с Nginx, а также Rocky Linux 9 и 10/PHP 8.3 с Apache. Каждый вариант проверяется по протоколам HTTP и HTTPS. Это протестированные пары ОС/PHP; переопределения в инвентаре на непротестированные пары завершаются ошибкой до внесения изменений в пакеты. Псевдонимы EL разделяют эту политику, но подтверждение работы в среде выполнения получено на контейнерах Rocky Linux.

Управляющие узлы с Python 3.12 используют Ansible 14.6 или новее в ветке 14.x совместно с ansible-core 2.21.6 или новее в ветке 2.21. Управляющие узлы с Python 3.13 и 3.14 используют Ansible 15.x с ansible-core 2.22.x. Файл блокировки зависимостей с хешами выбирает нужную пару для интерпретатора управляющего узла. Требования к интерпретатору управляемых узлов задаются отдельно. Ознакомьтесь с политикой перед выбором версий; более старые платформы и версии PHP, поддерживаемые только в upstream, не включаются автоматически.

## Зрелость функциональности

Основная последовательность задач определена в [tasks/main.yml](../../../tasks/main.yml). Группы мониторинга, резервного копирования, Fail2ban, безопасности, кэширования и межсетевого экрана имеют отсутствующие контракты шаблонов, зафиксированные в [tests/unit/missing_templates.yml](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/tests/unit/missing_templates.yml). Их флаги по умолчанию отключены, а включённая незавершённая группа останавливается только при выполнении её задач, после того как уже выполнились предыдущие фазы. Имена задач и примеры переменных не следует рассматривать как рабочие реализации этих функций.

TLS, учётные данные базы данных, сгенерированные секреты WordPress, проверки путей и обработка особенностей ОС требуют документированной конфигурации и проверок во время выполнения. Автоматическое аварийное переключение, SLA доступности на уровне облака или универсальная готовность к промышленной эксплуатации здесь не гарантируются.

## Быстрый старт

Установите роль из источника репозитория и её зависимости коллекций:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git,HEAD,wordpress_enterprise
ansible-galaxy collection install -r requirements.yml
```

Выполните команду установки коллекций из этой локальной копии репозитория. Перед развёртыванием ознакомьтесь с [defaults/main.yml](../../../defaults/main.yml) и [примерами](../../../examples/README.md). Используйте поддерживаемую точку входа вместо прямого вызова внутренних фаз задач.

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

Передавайте указанные секреты через Ansible Vault или используемый менеджер секретов. Перед запуском развёртывания настройте сертификаты и разрешение имён хостов для целевого узла. Оставляйте незавершённые группы функций отключёнными.

## Разработка и тестирование

[Makefile](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/Makefile), [CONTRIBUTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/CONTRIBUTING.md) и [TESTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/TESTING.md) описывают настройку зависимостей с проверкой хешей, проверки линтером, модульные тесты и контракты для одноразовых сред Docker/Molecule. Модульные тесты и линтер сами по себе не подтверждают успешное развёртывание.

```bash
make lint
```

Обратитесь к руководству по тестированию для работы со стабильными сценариями `default` и `tls` и их предварительными требованиями. Задачи установки, обновления, очистки и восстановления хоста изменяют состояние выбранных машин; для проверки используйте изолированные тестовые инвентари.

## Версионирование и релизные пакеты

Релизы проекта используют полную версию SemVer из `VERSION` независимо от минимальной версии Ansible в `meta/main.yml`. Отправьте соответствующий тег `v2.22.1` в ветку main для запуска рабочего процесса Release или запустите его вручную из main после создания соответствующего тега. Рабочий процесс проверяет, что существующий тег указывает на проверяемый исходный код, запускает полный набор CI (включая все четыре сценария Molecule) и публикует архив роли, совместимый с Galaxy, пакет Debian, пакет RPM, `release.json` и `SHA256SUMS`. Публикация использует этот проверенный существующий тег без переопределения целевой ссылки API релизов по умолчанию, поэтому последующее обновление рабочего процесса в main не требует расширенных прав записи в рабочие процессы. Отсутствующий или несовпадающий тег приводит к ошибке ещё до начала тестирования.

Проверяйте загруженные файлы с помощью `sha256sum --check SHA256SUMS`. Установите нативные пакеты командой `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` на Ubuntu 24.04 или `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` на Rocky Linux 9. Оба пакета устанавливают роль в `/usr/share/ansible/roles/wordpress_enterprise`; предоставьте поддерживаемый управляющий узел Ansible и установите зависимости из `requirements.yml` отдельно. Архив можно установить с помощью `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz,,wordpress_enterprise`. Нативные пакеты содержат исходные файлы роли и документацию и не выполняют никаких скриптов развёртывания при установке. CI устанавливает, проверяет и удаляет оба формата.

## Безопасность и лицензия

См. [SECURITY.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/SECURITY.md) и [лицензию MIT](../../../LICENSE). Метаданные пакета, политика поддержки платформ и проверки релизов должны оставаться согласованными с поставляемой ролью.
