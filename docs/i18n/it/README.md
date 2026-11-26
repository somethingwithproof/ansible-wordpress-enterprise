<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · **Italiano** · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · **Italiano** · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
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

Un ruolo Ansible per configurare host WordPress con PHP, un server web e un database locale o esterno. La validazione della piattaforma e degli input viene eseguita prima delle fasi di deployment, mentre i confini tra i task mantengono installazione, configurazione e verifica esaminabili separatamente.

## Contratto di deployment supportato

[meta/platform_support.yml](../../../meta/platform_support.yml) è il riferimento autorevole per la policy di supporto. La matrice stabile di Molecule copre Ubuntu 24.04/PHP 8.3 e Ubuntu 26.04/PHP 8.5 con Nginx, Debian 13/PHP 8.4 con Nginx e Rocky Linux 9 e 10/PHP 8.3 con Apache. Ogni percorso è testato su HTTP e HTTPS. Queste sono le coppie OS/PHP testate; gli override di inventario verso coppie non testate falliscono prima di qualsiasi modifica ai pacchetti. Gli alias EL condividono la policy, ma l'evidenza a runtime proviene dai container Rocky Linux.

I controller Python 3.12 utilizzano Ansible 14.6 o versione successiva nella linea 14.x con ansible-core 2.21.6 o versione successiva nella linea 2.21. I controller Python 3.13 e 3.14 utilizzano Ansible 15.x con ansible-core 2.22.x. Il lock dei requisiti con hash seleziona la coppia per l'interprete del controller. I requisiti dell'interprete per i nodi gestiti sono separati. Consulta la policy prima di scegliere le versioni; le piattaforme più datate e le versioni PHP semplicemente supportate upstream non vengono adottate automaticamente.

## Maturità delle funzionalità

La sequenza dei task principali è definita in [tasks/main.yml](../../../tasks/main.yml). I gruppi di monitoraggio, backup, Fail2ban, sicurezza, caching e firewall presentano contratti di template mancanti registrati in [tests/unit/missing_templates.yml](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/tests/unit/missing_templates.yml). I relativi flag rimangono disattivati per impostazione predefinita e la validazione rifiuta l'abilitazione di gruppi incompleti. I nomi dei task e le variabili di esempio non devono essere presentati come implementazioni funzionanti di tali funzionalità.

TLS, credenziali del database, segreti WordPress generati, controlli di sicurezza sui percorsi (path guard) e gestione specifica del sistema operativo richiedono la configurazione documentata e le verifiche a runtime. Qui non viene rivendicato alcun failover automatico, SLA di disponibilità su scala cloud né idoneità universale alla produzione.

## Avvio rapido

Installa il ruolo dal sorgente del repository e le sue dipendenze di collection:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git,HEAD,wordpress_enterprise
ansible-galaxy collection install -r requirements.yml
```

Esegui il comando della collection da questo checkout. Esamina [defaults/main.yml](../../../defaults/main.yml) e gli [esempi](../../../examples/README.md) prima del deployment. Usa il punto di ingresso supportato anziché richiamare direttamente le fasi interne dei task.

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

Fornisci i segreti referenziati tramite Ansible Vault o un secret manager esistente. Configura i certificati e la risoluzione del nome host per l'host di destinazione prima di eseguire un deployment. Mantieni disabilitati i gruppi di funzionalità incompleti.

## Sviluppo e test

Il [Makefile](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/Makefile), [CONTRIBUTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/CONTRIBUTING.md) e [TESTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/TESTING.md) definiscono la configurazione delle dipendenze con hash, i controlli lint, i test unitari e i contratti effimeri Docker/Molecule. I test unitari e il lint non garantiscono un deployment riuscito.

```bash
make lint
```

Consulta la guida ai test per gli scenari stabili `default` e `tls` e i relativi prerequisiti. I task di installazione, aggiornamento, pulizia e ripristino dell'host modificano le macchine selezionate; utilizza inventari di test isolati per la validazione.

## Versioning e pacchetti di rilascio

I rilasci del progetto utilizzano la versione SemVer completa in `VERSION`, indipendentemente
dalla versione minima di Ansible indicata in `meta/main.yml`. Esegui il push di un tag corrispondente `v2.22.1` su main
per attivare Release, oppure eseguilo manualmente da main dopo aver creato il tag corrispondente.
Il workflow verifica che il tag esistente punti al codice sorgente controllato, esegue l'intera suite
CI (inclusi tutti e quattro gli scenari Molecule) e pubblica un archivio del ruolo compatibile con Galaxy,
un pacchetto Debian, un RPM, `release.json` e `SHA256SUMS`.
La pubblicazione utilizza quel tag esistente verificato senza sovrascrivere il target predefinito
dell'API di rilascio, così un successivo aggiornamento del workflow su main non richiede credenziali
più ampie di scrittura sui workflow. Un tag mancante o non corrispondente fallisce prima dei test.

Verifica i download con `sha256sum --check SHA256SUMS`. Installa i pacchetti nativi
con `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` su Ubuntu
24.04 oppure `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` su
Rocky Linux 9. Entrambi installano il ruolo in
`/usr/share/ansible/roles/wordpress_enterprise`; predisponi un controller Ansible
supportato e installa separatamente `requirements.yml`. L'archivio può essere
installato con `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz,,wordpress_enterprise`.
I pacchetti nativi contengono i sorgenti del ruolo e la documentazione e non eseguono alcuno script
di deployment durante l'installazione. La CI installa, verifica e rimuove entrambi i formati.

## Sicurezza e licenza

Vedi [SECURITY.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/SECURITY.md) e la [licenza MIT](../../../LICENSE). I metadati del pacchetto, la policy di supporto della piattaforma e la validazione del rilascio devono rimanere allineati con il ruolo distribuito.
