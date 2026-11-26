<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · **Polski** · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · **Polski** · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
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

Rola Ansible do konfigurowania hostów WordPress z PHP, serwerem WWW oraz lokalną lub zewnętrzną bazą danych. Walidacja platformy i danych wejściowych uruchamiana jest przed fazami wdrożenia, a podział zadań pozwala na oddzielny przegląd instalacji, konfiguracji i weryfikacji.

## Obsługiwany kontrakt wdrożeniowy

Plik [meta/platform_support.yml](../../../meta/platform_support.yml) jest źródłem polityki wsparcia. Stabilna macierz Molecule obejmuje Ubuntu 24.04/PHP 8.3 oraz Ubuntu 26.04/PHP 8.5 z Nginx, Debian 13/PHP 8.4 z Nginx, a także Rocky Linux 9 i 10/PHP 8.3 z Apache. Każda ścieżka jest testowana przez HTTP i HTTPS. Są to przetestowane pary OS/PHP; nadpisania w inwentarzu wskazujące nieprzetestowane pary kończą się błędem przed wprowadzeniem zmian w pakietach. Aliasy EL współdzielą tę politykę, lecz potwierdzenie działania pochodzi z kontenerów Rocky Linux.

Kontrolery z Pythonem 3.12 używają Ansible 14.6 lub nowszego z linii 14.x wraz z ansible-core 2.21.6 lub nowszym z linii 2.21. Kontrolery z Pythonem 3.13 i 3.14 używają Ansible 15.x z ansible-core 2.22.x. Plik blokady zależności z sumami kontrolnymi dobiera odpowiednią parę dla interpretera kontrolera. Wymagania dotyczące interpretera na węzłach zarządzanych są odrębne. Przed wyborem wersji zapoznaj się z polityką wsparcia; starsze platformy oraz wersje PHP wspierane jedynie przez projekt nadrzędny nie są automatycznie przyjmowane.

## Dojrzałość funkcji

Podstawowa sekwencja zadań jest zdefiniowana w [tasks/main.yml](../../../tasks/main.yml). Grupy monitoringu, kopii zapasowych, Fail2ban, bezpieczeństwa, pamięci podręcznej i zapory sieciowej mają brakujące kontrakty szablonów zapisane w [tests/unit/missing_templates.yml](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/tests/unit/missing_templates.yml). Ich flagi pozostają domyślnie wyłączone, a walidacja odrzuca włączenie niekompletnych grup. Nazw zadań i przykładowych zmiennych nie należy przedstawiać jako działających implementacji tych funkcji.

Obsługa TLS, poświadczeń bazy danych, generowanych sekretów WordPress, zabezpieczeń ścieżek oraz specyfiki systemów operacyjnych wymaga udokumentowanej konfiguracji i weryfikacji w środowisku uruchomieniowym. Nie deklaruje się tu automatycznego przełączania awaryjnego, gwarancji SLA dla całej chmury ani uniwersalnej gotowości produkcyjnej.

## Szybki start

Zainstaluj rolę ze źródła repozytorium oraz wymagane kolekcje:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git,HEAD,wordpress_enterprise
ansible-galaxy collection install -r requirements.yml
```

Uruchom polecenie instalacji kolekcji z tej kopii roboczej. Przed wdrożeniem przejrzyj [defaults/main.yml](../../../defaults/main.yml) oraz [przykłady](../../../examples/README.md). Używaj wspieranego punktu wejścia zamiast bezpośredniego wywoływania wewnętrznych faz zadań.

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

Przekaż wskazane sekrety przez Ansible Vault lub istniejący menedżer sekretów. Przed uruchomieniem wdrożenia skonfiguruj certyfikaty oraz rozwiązywanie nazw dla hosta docelowego. Pozostaw niekompletne grupy funkcji wyłączone.

## Rozwój i testowanie

Pliki [Makefile](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/Makefile), [CONTRIBUTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/CONTRIBUTING.md) i [TESTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/TESTING.md) definiują konfigurację zależności z weryfikacją sum kontrolnych, analizę statyczną (lint), testy jednostkowe oraz kontrakty jednorazowych środowisk Docker/Molecule. Testy jednostkowe i analiza statyczna nie potwierdzają pomyślnego wdrożenia.

```bash
make lint
```

Skorzystaj z przewodnika testowania dla stabilnych scenariuszy `default` i `tls` oraz ich wymagań wstępnych. Zadania instalacji, aktualizacji, czyszczenia i przywracania modyfikują wybrane maszyny; do walidacji używaj odizolowanych inwentarzy testowych.

## Wersjonowanie i pakiety wydań

Wydania projektu korzystają z pełnej wersji SemVer zapisanej w pliku `VERSION`, niezależnie
od minimalnej wersji Ansible określonej w `meta/main.yml`. Wypchnij odpowiadający tag `v2.22.1`
na gałęzi main, aby uruchomić przepływ Release, lub uruchom go ręcznie z gałęzi main po utworzeniu pasującego tagu.
Przepływ pracy sprawdza, czy istniejący tag wskazuje na weryfikowany kod źródłowy, uruchamia pełny zestaw testów CI
(w tym wszystkie cztery scenariusze Molecule), a następnie publikuje archiwum roli zgodne z Galaxy,
pakiet Debiana, pakiet RPM oraz pliki `release.json` i `SHA256SUMS`.
Publikacja wykorzystuje ten zweryfikowany istniejący tag bez nadpisywania domyślnego celu API wydań,
dzięki czemu późniejsza aktualizacja przepływu pracy na gałęzi main nie wymaga szerszych uprawnień
zapisu przepływów pracy. Brakujący lub niezgodny tag kończy się błędem jeszcze przed uruchomieniem testów.

Zweryfikuj pobrane pliki poleceniem `sha256sum --check SHA256SUMS`. Zainstaluj natywne pakiety
za pomocą `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` w Ubuntu
24.04 lub `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` w
Rocky Linux 9. Oba pakiety instalują rolę w katalogu
`/usr/share/ansible/roles/wordpress_enterprise`; zapewnij wspierany kontroler Ansible
i osobno zainstaluj zależności z `requirements.yml`. Archiwum można zainstalować
za pomocą `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz,,wordpress_enterprise`.
Natywne pakiety zawierają kod źródłowy roli i dokumentację oraz nie uruchamiają żadnych
skryptów wdrożeniowych podczas instalacji. CI instaluje, sprawdza i usuwa oba formaty.

## Bezpieczeństwo i licencja

Zobacz [SECURITY.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/SECURITY.md) oraz [licencję MIT](../../../LICENSE). Metadane pakietu, polityka wsparcia platform i walidacja wydań muszą pozostawać spójne z dostarczaną rolą.
