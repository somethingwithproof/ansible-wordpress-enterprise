<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · **Español** · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · **Español** · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
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

Un rol de Ansible para configurar hosts de WordPress con PHP, un servidor web y una base de datos local o externa. La validación de plataforma y de entradas se ejecuta antes de las fases de despliegue, mientras que los límites entre tareas mantienen la instalación, la configuración y la verificación revisables por separado.

## Contrato de despliegue compatible

[meta/platform_support.yml](../../../meta/platform_support.yml) es la fuente de referencia para la política de soporte. La matriz estable de Molecule cubre Ubuntu 24.04/PHP 8.3 y Ubuntu 26.04/PHP 8.5 con Nginx, Debian 13/PHP 8.4 con Nginx, y Rocky Linux 9 y 10/PHP 8.3 con Apache. Cada ruta se valida sobre HTTP y HTTPS. Estos son los pares SO/PHP probados; las sobrescrituras de inventario hacia pares no probados fallan antes de aplicar cambios en paquetes. Los alias de EL comparten la política, pero la evidencia en tiempo de ejecución proviene de contenedores de Rocky Linux.

Los controladores con Python 3.12 utilizan Ansible 14.6 o posterior en la rama 14.x con ansible-core 2.21.6 o posterior en la rama 2.21. Los controladores con Python 3.13 y 3.14 utilizan Ansible 15.x con ansible-core 2.22.x. El archivo de bloqueo de requisitos con hashes selecciona el par correspondiente al intérprete del controlador. Los requisitos del intérprete en nodos gestionados son independientes. Consulte la política antes de elegir versiones; las plataformas antiguas y las versiones de PHP con mero soporte upstream no se adoptan automáticamente.

## Madurez de funcionalidades

La secuencia principal de tareas está definida en [tasks/main.yml](../../../tasks/main.yml). Los grupos de monitorización, copias de seguridad, Fail2ban, seguridad, almacenamiento en caché y firewall tienen contratos de plantilla faltantes registrados en [tests/unit/missing_templates.yml](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/tests/unit/missing_templates.yml). Sus indicadores permanecen desactivados de forma predeterminada y la validación rechaza habilitar grupos incompletos. Los nombres de tareas y las variables de ejemplo no deben presentarse como implementaciones funcionales de esas capacidades.

TLS, las credenciales de base de datos, los secretos generados de WordPress, las protecciones de rutas y el manejo específico por sistema operativo requieren la configuración y las comprobaciones en tiempo de ejecución documentadas. Aquí no se ofrece conmutación por error automática, ningún SLA de disponibilidad en la nube ni una afirmación universal de preparación para producción.

## Inicio rápido

Instale el rol desde el origen de su repositorio y sus dependencias de colección:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git,HEAD,wordpress_enterprise
ansible-galaxy collection install -r requirements.yml
```

Ejecute el comando de colección desde esta copia local. Revise [defaults/main.yml](../../../defaults/main.yml) y los [ejemplos](../../../examples/README.md) antes del despliegue. Use el punto de entrada compatible en lugar de invocar directamente fases internas de tareas.

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

Proporcione los secretos referenciados mediante Ansible Vault o un gestor de secretos existente. Configure los certificados y la resolución de nombres de host para el host de destino antes de ejecutar un despliegue. Mantenga desactivados los grupos de funcionalidades incompletos.

## Desarrollo y pruebas

[Makefile](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/Makefile), [CONTRIBUTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/CONTRIBUTING.md) y [TESTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/TESTING.md) definen la configuración de dependencias con hashes, las comprobaciones de lint, las pruebas unitarias y los contratos desechables de Docker/Molecule. Las pruebas unitarias y el análisis de lint no garantizan un despliegue exitoso.

```bash
make lint
```

Consulte la guía de pruebas para los escenarios estables `default` y `tls` y sus requisitos previos. Las tareas de instalación, actualización, limpieza y restauración en hosts modifican las máquinas seleccionadas; use inventarios de pruebas aislados para la validación.

## Versionado y paquetes de lanzamiento

Los lanzamientos del proyecto utilizan la versión SemVer completa definida en `VERSION`, de forma independiente
de la versión mínima de Ansible en `meta/main.yml`. Publique una etiqueta `v2.22.1` coincidente en main
para activar Release, o ejecútelo manualmente desde main después de crear la etiqueta coincidente.
El flujo de trabajo valida que la etiqueta existente apunte al código fuente verificado, ejecuta la suite completa de CI
(incluidos los cuatro escenarios de Molecule) y publica un archivo de rol compatible con Galaxy,
un paquete Debian, un RPM, `release.json` y `SHA256SUMS`.
La publicación utiliza esa etiqueta existente verificada sin sobrescribir el destino predeterminado de la API de
lanzamientos, de modo que una actualización posterior del flujo de trabajo en main no requiera credenciales más amplias
de escritura de flujos de trabajo. Una etiqueta faltante o no coincidente falla antes de las pruebas.

Verifique las descargas con `sha256sum --check SHA256SUMS`. Instale los paquetes nativos
con `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` en Ubuntu
24.04 o `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` en
Rocky Linux 9. Ambos instalan el rol en
`/usr/share/ansible/roles/wordpress_enterprise`; proporcione un controlador de Ansible
compatible e instale `requirements.yml` por separado. El archivo comprimido puede
instalarse con `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz,,wordpress_enterprise`.
Los paquetes nativos contienen el código fuente del rol y la documentación, y no ejecutan scripts de despliegue
durante la instalación. CI instala, comprueba y elimina ambos formatos.

## Seguridad y licencia

Consulte [SECURITY.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/SECURITY.md) y la [licencia MIT](../../../LICENSE). Los metadatos del paquete, la política de soporte de plataformas y la validación de lanzamientos deben permanecer alineados con el rol distribuido.
