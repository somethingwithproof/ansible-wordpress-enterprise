<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · **Deutsch** · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · **Deutsch** · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
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

Eine Ansible-Rolle zur Konfiguration von WordPress-Hosts mit PHP, einem Webserver sowie einer lokalen oder externen Datenbank. Plattform- und Eingabevalidierungen laufen vor den Bereitstellungsphasen, während klar abgegrenzte Aufgabenbereiche Installation, Konfiguration und Überprüfung getrennt prüfbar halten.

## Unterstützter Bereitstellungsvertrag

[meta/platform_support.yml](../../../meta/platform_support.yml) ist die maßgebliche Quelle für die Support-Richtlinie. Die stabile Molecule-Matrix umfasst Ubuntu 24.04/PHP 8.3 und Ubuntu 26.04/PHP 8.5 mit Nginx, Debian 13/PHP 8.4 mit Nginx sowie Rocky Linux 9 und 10/PHP 8.3 mit Apache. Jeder Pfad wird über HTTP und HTTPS getestet. Dies sind die getesteten OS-/PHP-Kombinationen; Inventory-Überschreibungen auf ungetestete Kombinationen schlagen vor Paketänderungen fehl. EL-Aliase teilen diese Richtlinie, die Laufzeitnachweise stammen jedoch aus Rocky-Linux-Containern.

Controller mit Python 3.12 verwenden Ansible 14.6 oder neuer aus der 14.x-Reihe mit ansible-core 2.21.6 oder neuer aus der 2.21-Reihe. Controller mit Python 3.13 und 3.14 verwenden Ansible 15.x mit ansible-core 2.22.x. Die gehashte Requirements-Lock-Datei wählt das passende Paar für den Controller-Interpreter aus. Die Interpreter-Anforderungen für verwaltete Knoten sind davon getrennt. Konsultieren Sie die Richtlinie vor der Versionsauswahl; ältere Plattformen und lediglich upstream unterstützte PHP-Versionen werden nicht automatisch übernommen.

## Funktionsreife

Die zentrale Aufgabenfolge ist in [tasks/main.yml](../../../tasks/main.yml) definiert. Für die Gruppen Monitoring, Backup, Fail2ban, Sicherheit, Caching und Firewall fehlen Vorlagenverträge, die in [tests/unit/missing_templates.yml](../../../tests/unit/missing_templates.yml) dokumentiert sind. Ihre Flags sind standardmäßig deaktiviert, und die Validierung lehnt das Aktivieren unvollständiger Gruppen ab. Aufgabennamen und Beispielvariablen dürfen nicht als funktionierende Implementierungen dieser Funktionen dargestellt werden.

TLS, Datenbank-Zugangsdaten, generierte WordPress-Secrets, Pfadschutzprüfungen und betriebssystemspezifische Abläufe erfordern die dokumentierte Konfiguration sowie Laufzeitprüfungen. Es wird hier weder automatisches Failover noch ein cloudweites Verfügbarkeits-SLA oder eine allgemeine Produktionsreife zugesichert.

## Schnellstart

Rolle aus ihrer Repository-Quelle sowie deren Collection-Abhängigkeiten installieren:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git,HEAD,wordpress_enterprise
ansible-galaxy collection install -r requirements.yml
```

Führen Sie den Collection-Befehl aus diesem Checkout aus. Prüfen Sie [defaults/main.yml](../../../defaults/main.yml) und die [Beispiele](../../../examples/README.md) vor der Bereitstellung. Nutzen Sie den unterstützten Einstiegspunkt, anstatt interne Aufgabenphasen direkt aufzurufen.

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

Stellen Sie die referenzierten Secrets über Ansible Vault oder einen bestehenden Secret-Manager bereit. Konfigurieren Sie Zertifikate und Hostnamen-Auflösung für den Zielhost, bevor Sie eine Bereitstellung ausführen. Lassen Sie unvollständige Funktionsgruppen deaktiviert.

## Entwicklung und Tests

[Makefile](../../../Makefile), [CONTRIBUTING.md](../../../CONTRIBUTING.md) und [TESTING.md](../../../TESTING.md) definieren die gehashte Abhängigkeitsinstallation, Lint-Prüfungen, Unit-Tests sowie Wegwerf-Verträge für Docker und Molecule. Unit-Tests und Lint belegen keine erfolgreiche Bereitstellung.

```bash
make lint
```

Nutzen Sie den Testleitfaden für die stabilen Szenarien `default` und `tls` sowie deren Voraussetzungen. Aufgaben zur Host-Installation, Aktualisierung, Bereinigung und Wiederherstellung verändern die ausgewählten Maschinen; verwenden Sie zur Validierung isolierte Test-Inventories.

## Versionierung und Release-Pakete

Projekt-Releases verwenden die vollständige SemVer-Version aus `VERSION`, unabhängig von der Mindestversion für Ansible in `meta/main.yml`. Pushen Sie ein passendes Tag `v2.22.1` auf main, um Release auszulösen, oder starten Sie den Workflow nach dem Erstellen des passenden Tags manuell auf main. Der Workflow prüft, dass das vorhandene Tag auf den ausgecheckten Quellcode zeigt, führt die vollständige CI-Suite (einschließlich aller vier Molecule-Szenarien) aus und veröffentlicht ein Galaxy-kompatibles Rollenarchiv, ein Debian-Paket, ein RPM sowie `release.json` und `SHA256SUMS`. Die Veröffentlichung verwendet dieses verifizierte bestehende Tag, ohne das Standardziel der Release-API zu überschreiben, sodass eine spätere Workflow-Aktualisierung auf main keine weitergehenden Schreibberechtigungen für Workflows erfordert. Ein fehlendes oder nicht übereinstimmendes Tag führt bereits vor den Tests zu einem Fehler.

Überprüfen Sie Downloads mit `sha256sum --check SHA256SUMS`. Installieren Sie native Pakete mit `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` unter Ubuntu 24.04 oder mit `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` unter Rocky Linux 9. Beide installieren die Rolle unter `/usr/share/ansible/roles/wordpress_enterprise`; stellen Sie einen unterstützten Ansible-Controller bereit und installieren Sie `requirements.yml` separat. Das Archiv lässt sich mit `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz,,wordpress_enterprise` installieren. Native Pakete enthalten die Quellen und Dokumentation der Rolle und führen bei der Installation keine Bereitstellungsskripte aus. Die CI installiert, prüft und entfernt beide Formate.

## Sicherheit und Lizenz

Siehe [SECURITY.md](../../../SECURITY.md) und die [MIT-Lizenz](../../../LICENSE). Paketmetadaten, Plattform-Support-Richtlinie und Release-Validierung müssen mit der ausgelieferten Rolle abgestimmt bleiben.
