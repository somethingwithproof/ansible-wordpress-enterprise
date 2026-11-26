<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · **Afrikaans** · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
- **Africa:** **Afrikaans** · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)
- **Asia:** [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [עברית](../he/README.md) · [मराठी](../mr/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [Bahasa Melayu](../ms/README.md) · [Filipino](../fil/README.md)

</details>
<!-- translations:end -->

# Ansible WordPress Enterprise

[![CI](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_ansible-wordpress-enterprise&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_ansible-wordpress-enterprise)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/ansible-wordpress-enterprise)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/releases)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/ansible-wordpress-enterprise/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/ansible-wordpress-enterprise)

'n Ansible-rol vir die konfigurasie van WordPress-gashere met PHP, 'n webbediener en 'n plaaslike of eksterne databasis. Platform- en invoervalidering loop voor ontplooiingsfases, terwyl taakgrense installasie, konfigurasie en verifikasie afsonderlik hersienbaar hou.

## Ondersteunde ontplooiingskontrak

[meta/platform_support.yml](../../../meta/platform_support.yml) is die gesaghebbende bron vir die ondersteuningsbeleid. Die stabiele Molecule-matriks dek Ubuntu 24.04/PHP 8.3 en Ubuntu 26.04/PHP 8.5 met Nginx, Debian 13/PHP 8.4 met Nginx, en Rocky Linux 9 en 10/PHP 8.3 met Apache. Elke pad word oor HTTP en HTTPS getoets. Dit is die getoetste bedryfstelsel-/PHP-pare; inventarisoorheersings na ongetoetste pare misluk voor pakketveranderinge. EL-aliasse deel die beleid, maar looptydbewyse kom van Rocky Linux-houers.

Python 3.12-beheerders gebruik Ansible 14.6 of nuwer in die 14.x-reeks met ansible-core 2.21.6 of nuwer in die 2.21-reeks. Python 3.13- en 3.14-beheerders gebruik Ansible 15.x met ansible-core 2.22.x. Die gehashte vereisteslot kies die paar vir die beheerder-vertolker. Bestuurde nodus-vertolkervereistes is afsonderlik. Raadpleeg die beleid voordat weergawes gekies word; ouer platforms en PHP-weergawes wat bloot stroomop ondersteun word, word nie outomaties aanvaar nie.

## Funksievolwassenheid

Die kerntaakvolgorde word in [tasks/main.yml](../../../tasks/main.yml) gedefinieer. Monitering-, rugsteun-, Fail2ban-, sekuriteit-, kasgeheue- en brandmuurgroepe het ontbrekende sjabloonkontrakte wat in [tests/unit/missing_templates.yml](../../../tests/unit/missing_templates.yml) aangeteken is. Hul vlae bly by verstek afgeskakel en validering verwerp die aktivering van onvolledige groepe. Taakname en voorbeeldveranderlikes mag nie as werkende implementerings van daardie funksies voorgestel word nie.

TLS, databasis-aanmeldbewyse, gegenereerde WordPress-geheime, padwagte en bedryfstelselspesifieke hantering vereis die gedokumenteerde konfigurasie en looptydkontroles. Geen outomatiese foutoorskakeling, wolk-wye beskikbaarheids-SLA of universele produksiegereedheid word hier beweer nie.

## Vinnige begin

Installeer die rol vanuit sy bewaarplekbron en sy versamelingsafhanklikhede:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git
ansible-galaxy collection install -r requirements.yml
```

Voer die versamelingsopdrag vanuit hierdie werkskopie uit. Hersien [defaults/main.yml](../../../defaults/main.yml) en [voorbeelde](../../../examples/README.md) voor ontplooiing. Gebruik die ondersteunde toegangspunt eerder as om interne taakfases direk op te roep.

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

Verskaf die verwysde geheime deur middel van Ansible Vault of 'n bestaande geheimbestuurder. Konfigureer sertifikate en gasheernaam-oplossing vir die teikengasheer voordat 'n ontplooiing uitgevoer word. Hou onvolledige funksiegroepe gedeaktiveer.

## Ontwikkeling en toetsing

Die [Makefile](../../../Makefile), [CONTRIBUTING.md](../../../CONTRIBUTING.md) en [TESTING.md](../../../TESTING.md) definieer die gehashte afhanklikheidsopstelling, lint-kontroles, eenheidstoetse en weggooibare Docker/Molecule-kontrakte. Eenheidstoetse en lint bewys nie 'n suksesvolle ontplooiing nie.

```bash
make lint
```

Gebruik die toetsgids vir die stabiele `default`- en `tls`-scenario's en hul voorvereistes. Gasheerinstallasie-, opgraderings-, opruimings- en hersteltake verander die geselekteerde masjiene; gebruik geïsoleerde toetsinventarisse vir validering.

## Weergawebestuur en vrystellingspakkette

Projekvrystellings gebruik die volledige SemVer-weergawe in `VERSION`, onafhanklik
van `meta/main.yml` se minimum Ansible-weergawe. Stoot 'n ooreenstemmende `v2.22.1`-etiket
op main om Release te aktiveer, of voer dit handmatig vanaf main uit nadat die
ooreenstemmende etiket geskep is. Die werkvloei valideer dat die bestaande etiket na die
gekontroleerde bronkode wys, voer die volledige CI-toetsstel uit (insluitend al vier
Molecule-scenario's), en publiseer 'n Galaxy-versoenbare rolargief, Debian-pakket, RPM,
`release.json` en `SHA256SUMS`. Publikasie gebruik daardie geverifieerde bestaande etiket
sonder om die vrystellings-API se verstekteiken te oorheers, sodat 'n latere
werkvloei-opdatering op main nie breër werkvloei-skryfbewyse vereis nie. 'n Ontbrekende
of nie-ooreenstemmende etiket misluk voor toetsing.

Verifieer aflaaie met `sha256sum --check SHA256SUMS`. Installeer inheemse pakkette
met `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` op Ubuntu 24.04
of `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` op Rocky Linux 9.
Albei installeer die rol onder `/usr/share/ansible/roles/wordpress_enterprise`; verskaf
'n ondersteunde Ansible-beheerder en installeer `requirements.yml` afsonderlik. Die argief
kan geïnstalleer word met `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz`.
Inheemse pakkette bevat rolbronkode en dokumentasie en voer geen ontplooiingskripte tydens
installasie uit nie. CI installeer, kontroleer en verwyder albei formate.

## Sekuriteit en lisensie

Sien [SECURITY.md](../../../SECURITY.md) en die [MIT-lisensie](../../../LICENSE). Pakketmetadata, platformondersteuningsbeleid en vrystellingsvalidering moet in ooreenstemming bly met die verskafte rol.
