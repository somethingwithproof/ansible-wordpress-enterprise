<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · **Nederlands** · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · **Nederlands** · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
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

Een Ansible-rol voor het configureren van WordPress-hosts met PHP, een webserver en een lokale of externe database. Platform- en invoervalidatie worden uitgevoerd vóór de uitrolfasen, terwijl taakgrenzen installatie, configuratie en verificatie afzonderlijk controleerbaar houden.

## Ondersteund uitrolcontract

[meta/platform_support.yml](../../../meta/platform_support.yml) is de gezaghebbende bron voor het ondersteuningsbeleid. De stabiele Molecule-matrix omvat Ubuntu 24.04/PHP 8.3 en Ubuntu 26.04/PHP 8.5 met Nginx, Debian 13/PHP 8.4 met Nginx, en Rocky Linux 9 en 10/PHP 8.3 met Apache. Elk pad wordt getest over HTTP en HTTPS. Dit zijn de geteste OS/PHP-combinaties; inventory-overschrijvingen naar ongeteste combinaties falen vóór pakketwijzigingen. EL-aliassen delen het beleid, maar runtime-bewijs komt van Rocky Linux-containers.

Controllers met Python 3.12 gebruiken Ansible 14.6 of nieuwer binnen de 14.x-lijn met ansible-core 2.21.6 of nieuwer binnen de 2.21-lijn. Controllers met Python 3.13 en 3.14 gebruiken Ansible 15.x met ansible-core 2.22.x. Het gehashte requirements-lockbestand selecteert het juiste paar voor de controller-interpreter. De interpretervereisten voor beheerde nodes staan hier los van. Raadpleeg het beleid voordat je versies kiest; oudere platformen en PHP-versies die uitsluitend upstream worden ondersteund worden niet automatisch overgenomen.

## Volwassenheid van functies

De kerntaakvolgorde is gedefinieerd in [tasks/main.yml](../../../tasks/main.yml). De groepen voor monitoring, back-up, Fail2ban, beveiliging, caching en firewall hebben ontbrekende sjablooncontracten die zijn vastgelegd in [tests/unit/missing_templates.yml](../../../tests/unit/missing_templates.yml). Hun vlaggen staan standaard uit en de validatie weigert het inschakelen van onvolledige groepen. Taaknamen en voorbeeldvariabelen mogen niet worden gepresenteerd als werkende implementaties van die functies.

TLS, databasegegevens, gegenereerde WordPress-geheimen, padbeveiligingen en OS-specifieke afhandeling vereisen de gedocumenteerde configuratie en runtime-controles. Er wordt hier geen automatische failover, cloudbrede beschikbaarheids-SLA of universele claim van productiegeschiktheid gedaan.

## Snelstart

Installeer de rol vanuit de repositorybron en de bijbehorende collectieafhankelijkheden:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git
ansible-galaxy collection install -r requirements.yml
```

Voer het collectiecommando uit vanuit deze checkout. Controleer [defaults/main.yml](../../../defaults/main.yml) en [voorbeelden](../../../examples/README.md) vóór de uitrol. Gebruik het ondersteunde startpunt in plaats van interne taakfasen rechtstreeks aan te roepen.

```yaml
- hosts: wordpress_test_hosts
  become: true
  vars:
    wordpress_web_server: nginx
    wordpress_site_url: "https://wordpress.example.com"
    wordpress_server_name: wordpress.example.com
    wordpress_admin_password: "{{ vault_wordpress_admin_password }}"
    wordpress_db_password: "{{ vault_wordpress_db_password }}"
    wordpress_db_root_password: "{{ vault_wordpress_db_root_password }}"
  roles:
    - ansible-wordpress-enterprise
```

Lever de genoemde geheimen aan via Ansible Vault of een bestaande secret manager. Configureer certificaten en hostnaamresolutie voor de doelhost voordat je een uitrol uitvoert. Houd onvolledige functiegroepen uitgeschakeld.

## Ontwikkeling en testen

De [Makefile](../../../Makefile), [CONTRIBUTING.md](../../../CONTRIBUTING.md) en [TESTING.md](../../../TESTING.md) definiëren de gehashte afhankelijkheidsconfiguratie, lintcontroles, unittests en wegwerpbare Docker/Molecule-contracten. Unittests en lint bewijzen geen succesvolle uitrol.

```bash
make lint
```

Raadpleeg de testhandleiding voor de stabiele `default`- en `tls`-scenario's en hun vereisten. Taken voor hostinstallatie, upgrade, opschoning en herstel wijzigen de geselecteerde machines; gebruik geïsoleerde testinventarissen voor validatie.

## Versiebeheer en releasepakketten

Projectreleases gebruiken de volledige SemVer-versie in `VERSION`, onafhankelijk van de minimale Ansible-versie in `meta/main.yml`. Push een overeenkomende `v2.22.1`-tag op main om Release te starten, of voer de workflow handmatig uit vanaf main nadat de overeenkomende tag is aangemaakt. De workflow valideert dat de bestaande tag verwijst naar de gecontroleerde broncode, voert de volledige CI-suite uit (inclusief alle vier de Molecule-scenario's) en publiceert een Galaxy-compatibel rolarchief, Debian-pakket, RPM, `release.json` en `SHA256SUMS`. Bij het publiceren wordt die geverifieerde bestaande tag gebruikt zonder het standaarddoel van de release-API te overschrijven, zodat een latere workflow-update op main geen bredere workflow-schrijfrechten vereist. Een ontbrekende of afwijkende tag faalt vóór het testen.

Verifieer downloads met `sha256sum --check SHA256SUMS`. Installeer native pakketten met `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` op Ubuntu 24.04 of `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` op Rocky Linux 9. Beide installeren de rol onder `/usr/share/ansible/roles/wordpress_enterprise`; zorg voor een ondersteunde Ansible-controller en installeer `requirements.yml` afzonderlijk. Het archief kan worden geïnstalleerd met `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz`. Native pakketten bevatten rolbroncode en documentatie en voeren tijdens de installatie geen uitrolscripts uit. CI installeert, controleert en verwijdert beide formaten.

## Beveiliging en licentie

Zie [SECURITY.md](../../../SECURITY.md) en de [MIT-licentie](../../../LICENSE). Pakketmetadata, het beleid voor platformondersteuning en releasevalidatie moeten in lijn blijven met de meegeleverde rol.
