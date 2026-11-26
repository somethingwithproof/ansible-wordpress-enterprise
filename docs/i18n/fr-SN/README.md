<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · **Français (Sénégal)** · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
- **Africa:** [Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [Français (Maroc)](../fr-MA/README.md) · **Français (Sénégal)** · [Hausa](../ha-NG/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)
- **Asia:** [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [עברית](../he/README.md) · [मराठी](../mr/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [Bahasa Melayu](../ms/README.md) · [Filipino](../fil/README.md)

</details>
<!-- translations:end -->

# Ansible WordPress Enterprise

[![CI](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_ansible-wordpress-enterprise&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_ansible-wordpress-enterprise)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/ansible-wordpress-enterprise)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/releases)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/ansible-wordpress-enterprise/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/ansible-wordpress-enterprise)

Un rôle Ansible pour configurer des hôtes WordPress avec PHP, un serveur web et une base de données locale ou externe. La validation de la plateforme et des paramètres s'exécute avant les phases de déploiement, tandis que le découpage des tâches permet d'examiner séparément l'installation, la configuration et la vérification.

## Contrat de déploiement pris en charge

[meta/platform_support.yml](../../../meta/platform_support.yml) fait foi en matière de politique de prise en charge. La matrice Molecule stable couvre Ubuntu 24.04/PHP 8.3 et Ubuntu 26.04/PHP 8.5 avec Nginx, Debian 13/PHP 8.4 avec Nginx, ainsi que Rocky Linux 9 et 10/PHP 8.3 avec Apache. Chaque parcours est testé en HTTP et en HTTPS. Il s'agit des couples OS/PHP testés ; les surcharges d'inventaire visant des couples non testés échouent avant toute modification des paquets. Les alias EL partagent la même politique, mais les preuves d'exécution proviennent de conteneurs Rocky Linux.

Les contrôleurs Python 3.12 utilisent Ansible 14.6 ou une version ultérieure de la branche 14.x avec ansible-core 2.21.6 ou une version ultérieure de la branche 2.21. Les contrôleurs Python 3.13 et 3.14 utilisent Ansible 15.x avec ansible-core 2.22.x. Le fichier de verrouillage des dépendances avec empreintes sélectionne le couple adapté à l'interpréteur du contrôleur. Les exigences relatives à l'interpréteur des nœuds gérés sont distinctes. Consultez la politique avant de choisir les versions ; les plateformes plus anciennes et les versions de PHP uniquement prises en charge en amont ne sont pas automatiquement adoptées.

## Maturité des fonctionnalités

La séquence principale des tâches est définie dans [tasks/main.yml](../../../tasks/main.yml). Les groupes de supervision, sauvegarde, Fail2ban, sécurité, mise en cache et pare-feu présentent des contrats de modèles manquants consignés dans [tests/unit/missing_templates.yml](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/tests/unit/missing_templates.yml). Leurs indicateurs restent désactivés par défaut, et un groupe incomplet activé ne s'arrête que lorsque ses tâches s'exécutent, après l'exécution des phases précédentes. Les noms de tâches et les exemples de variables ne doivent pas être présentés comme des implémentations fonctionnelles de ces fonctionnalités.

TLS, les identifiants de base de données, les secrets WordPress générés, les garde-fous de chemins et les traitements spécifiques au système d'exploitation nécessitent la configuration et les vérifications d'exécution documentées. Aucun basculement automatique, aucun SLA de disponibilité à l'échelle du cloud ni aucune garantie universelle de mise en production ne sont revendiqués ici.

## Démarrage rapide

Installez le rôle depuis la source de son dépôt ainsi que ses dépendances de collections :

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git,HEAD,wordpress_enterprise
ansible-galaxy collection install -r requirements.yml
```

Exécutez la commande de collection depuis cette copie locale. Passez en revue [defaults/main.yml](../../../defaults/main.yml) et les [exemples](../../../examples/README.md) avant le déploiement. Utilisez le point d'entrée pris en charge plutôt que d'appeler directement les phases de tâches internes.

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

Fournissez les secrets référencés via Ansible Vault ou un gestionnaire de secrets existant. Configurez les certificats et la résolution de noms d'hôtes pour la machine cible avant de lancer un déploiement. Laissez les groupes de fonctionnalités incomplets désactivés.

## Développement et tests

Le [Makefile](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/Makefile), [CONTRIBUTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/CONTRIBUTING.md) et [TESTING.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/TESTING.md) définissent la configuration des dépendances vérifiées par empreinte, les vérifications de lint, les tests unitaires ainsi que les contrats Docker/Molecule jetables. Les tests unitaires et le lint ne garantissent pas un déploiement réussi.

```bash
make lint
```

Consultez le guide de test pour les scénarios stables `default` et `tls` ainsi que leurs prérequis. Les tâches d'installation, de mise à niveau, de nettoyage et de restauration d'hôtes modifient les machines sélectionnées ; utilisez des inventaires de test isolés pour la validation.

## Gestion des versions et paquets de publication

Les versions publiées du projet utilisent la version SemVer complète indiquée dans `VERSION`, indépendamment de la version minimale d'Ansible figurant dans `meta/main.yml`. Poussez un tag `v2.22.1` correspondant sur main pour déclencher la publication, ou exécutez le workflow manuellement depuis main après avoir créé le tag correspondant. Le workflow vérifie que le tag existant pointe vers les sources contrôlées, exécute la suite CI complète (y compris les quatre scénarios Molecule) et publie une archive de rôle compatible Galaxy, un paquet Debian, un RPM, `release.json` et `SHA256SUMS`. La publication utilise ce tag existant vérifié sans remplacer la cible par défaut de l'API de publication, afin qu'une mise à jour ultérieure du workflow sur main ne nécessite pas d'autorisations plus étendues en écriture sur les workflows. Un tag manquant ou non concordant provoque un échec avant l'exécution des tests.

Vérifiez les téléchargements avec `sha256sum --check SHA256SUMS`. Installez les paquets natifs avec `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` sur Ubuntu 24.04 ou `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` sur Rocky Linux 9. Les deux installent le rôle sous `/usr/share/ansible/roles/wordpress_enterprise` ; fournissez un contrôleur Ansible pris en charge et installez `requirements.yml` séparément. L'archive peut être installée avec `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz,,wordpress_enterprise`. Les paquets natifs contiennent les sources du rôle ainsi que la documentation et n'exécutent aucun script de déploiement lors de l'installation. La CI installe, vérifie et supprime les deux formats.

## Sécurité et licence

Consultez [SECURITY.md](https://github.com/somethingwithproof/ansible-wordpress-enterprise/blob/main/SECURITY.md) et la [licence MIT](../../../LICENSE). Les métadonnées du paquet, la politique de prise en charge des plateformes et la validation des publications doivent rester alignées avec le rôle distribué.
