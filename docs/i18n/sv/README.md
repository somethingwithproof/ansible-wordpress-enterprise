<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · **Svenska** · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · **Svenska** · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
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

En Ansible-roll för att konfigurera WordPress-värdar med PHP, en webbserver och en lokal eller extern databas. Plattforms- och indatavalidering körs före driftsättningsfaserna, medan uppgiftsgränser håller installation, konfiguration och verifiering separat granskningsbara.

## Kontrakt för driftsättning som stöds

[meta/platform_support.yml](../../../meta/platform_support.yml) är auktoriteten för stödpolicyn. Den stabila Molecule-matrisen omfattar Ubuntu 24.04/PHP 8.3 och Ubuntu 26.04/PHP 8.5 med Nginx, Debian 13/PHP 8.4 med Nginx samt Rocky Linux 9 och 10/PHP 8.3 med Apache. Varje kombination testas över HTTP och HTTPS. Dessa är de testade OS/PHP-paren; åsidosättningar i inventeringen till otestade par misslyckas före paketändringar. EL-alias delar policyn, men körtidsbevis kommer från Rocky Linux-containrar.

Kontrollnoder med Python 3.12 använder Ansible 14.6 eller senare i 14.x-serien med ansible-core 2.21.6 eller senare i 2.21-serien. Kontrollnoder med Python 3.13 och 3.14 använder Ansible 15.x med ansible-core 2.22.x. Den hashade kravfilen väljer rätt par för kontrollnodens tolk. Tolkkraven för hanterade noder är separata. Läs policyn innan du väljer versioner; äldre plattformar och PHP-versioner som enbart stöds uppströms antas inte automatiskt.

## Funktionsmognad

Den centrala uppgiftssekvensen definieras i [tasks/main.yml](../../../tasks/main.yml). Grupperna för övervakning, säkerhetskopiering, Fail2ban, säkerhet, cachning och brandvägg saknar mallkontrakt som är dokumenterade i [tests/unit/missing_templates.yml](../../../tests/unit/missing_templates.yml). Deras flaggor är avstängda som standard och valideringen avvisar aktivering av ofullständiga grupper. Uppgiftsnamn och exempelvariabler får inte framställas som fungerande implementeringar av dessa funktioner.

TLS, databasautentiseringsuppgifter, genererade WordPress-hemligheter, sökvägsskydd och OS-specifik hantering kräver den dokumenterade konfigurationen och körtidskontrollerna. Ingen automatisk redundansväxling, molnövergripande tillgänglighets-SLA eller generell garanti om produktionsmognad görs gällande här.

## Snabbstart

Installera rollen från dess kodarkiv och dess samlingsberoenden:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git
ansible-galaxy collection install -r requirements.yml
```

Kör samlingskommandot från denna utcheckning. Granska [defaults/main.yml](../../../defaults/main.yml) och [exempel](../../../examples/README.md) före driftsättning. Använd den startpunkt som stöds i stället för att anropa interna uppgiftsfaser direkt.

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

Tillhandahåll de refererade hemligheterna via Ansible Vault eller en befintlig hemlighetshanterare. Konfigurera certifikat och värdnamnsuppslagning för målvärden innan du kör en driftsättning. Håll ofullständiga funktionsgrupper inaktiverade.

## Utveckling och testning

[Makefile](../../../Makefile), [CONTRIBUTING.md](../../../CONTRIBUTING.md) och [TESTING.md](../../../TESTING.md) definierar den hashade beroendekonfigurationen, lint-kontroller, enhetstester och tillfälliga Docker/Molecule-kontrakt. Enhetstester och lint-kontroller bevisar inte en lyckad driftsättning.

```bash
make lint
```

Använd testguiden för de stabila scenarierna `default` och `tls` och deras förutsättningar. Uppgifter för värdinstallation, uppgradering, rensning och återställning ändrar de valda maskinerna; använd isolerade testinventeringar för validering.

## Versionshantering och utgåvepaket

Projektets utgåvor använder den fullständiga SemVer-versionen i `VERSION`, oberoende av den lägsta Ansible-versionen i `meta/main.yml`. Pusha en matchande `v2.22.1`-tagg på main för att utlösa Release, eller kör den manuellt från main efter att den matchande taggen skapats. Arbetsflödet validerar att den befintliga taggen pekar på den utcheckade källkoden, kör hela CI-sviten (inklusive alla fyra Molecule-scenarier) och publicerar ett Galaxy-kompatibelt rollarkiv, ett Debian-paket, en RPM, `release.json` och `SHA256SUMS`. Publiceringen använder den verifierade befintliga taggen utan att åsidosätta release-API:ets standardmål, så en senare arbetsflödesuppdatering på main kräver inte utökade skrivrättigheter för arbetsflöden. En saknad eller felaktig tagg gör att körningen avbryts före testning.

Verifiera nedladdningar med `sha256sum --check SHA256SUMS`. Installera systempaket med `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` på Ubuntu 24.04 eller `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` på Rocky Linux 9. Båda installerar rollen under `/usr/share/ansible/roles/wordpress_enterprise`; tillhandahåll en Ansible-kontrollnod som stöds och installera `requirements.yml` separat. Arkivet kan installeras med `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz`. Systempaketen innehåller rollens källkod och dokumentation och kör inga driftsättningsskript vid installationen. CI installerar, kontrollerar och tar bort båda formaten.

## Säkerhet och licens

Se [SECURITY.md](../../../SECURITY.md) och [MIT-licensen](../../../LICENSE). Paketmetadata, plattformsstödspolicy och utgåvevalidering måste överensstämma med den levererade rollen.
