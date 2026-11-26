<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · **Português (BR)** · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · **Português (BR)** · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
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

Uma role Ansible para configurar hosts WordPress com PHP, um servidor web e um banco de dados local ou externo. A validação de plataforma e de entradas é executada antes das fases de implantação, enquanto os limites entre tarefas mantêm a instalação, a configuração e a verificação revisáveis separadamente.

## Contrato de implantação suportado

[meta/platform_support.yml](../../../meta/platform_support.yml) é a referência oficial da política de suporte. A matriz estável do Molecule cobre Ubuntu 24.04/PHP 8.3 e Ubuntu 26.04/PHP 8.5 com Nginx, Debian 13/PHP 8.4 com Nginx e Rocky Linux 9 e 10/PHP 8.3 com Apache. Cada caminho é exercitado em HTTP e HTTPS. Esses são os pares SO/PHP testados; substituições de inventário para pares não testados falham antes de alterações em pacotes. Aliases do EL compartilham a política, mas as evidências de execução vêm de contêineres Rocky Linux.

Controladores com Python 3.12 usam Ansible 14.6 ou posterior na linha 14.x com ansible-core 2.21.6 ou posterior na linha 2.21. Controladores com Python 3.13 e 3.14 usam Ansible 15.x com ansible-core 2.22.x. O arquivo lock de requisitos com hashes seleciona o par para o interpretador do controlador. Os requisitos de interpretador dos nós gerenciados são separados. Consulte a política antes de selecionar versões; plataformas mais antigas e versões do PHP suportadas apenas pelo upstream não são adotadas automaticamente.

## Maturidade dos recursos

A sequência principal de tarefas é definida em [tasks/main.yml](../../../tasks/main.yml). Os grupos de monitoramento, backup, Fail2ban, segurança, cache e firewall possuem contratos de template ausentes registrados em [tests/unit/missing_templates.yml](../../../tests/unit/missing_templates.yml). Suas flags permanecem desativadas por padrão e a validação rejeita a ativação de grupos incompletos. Nomes de tarefas e variáveis de exemplo não devem ser apresentados como implementações funcionais desses recursos.

TLS, credenciais de banco de dados, segredos gerados do WordPress, proteções de caminho e tratamento específico de SO exigem a configuração documentada e verificações em tempo de execução. Não há garantia de failover automático, SLA de disponibilidade em nuvem nem prontidão universal para produção.

## Início rápido

Instale a role a partir do repositório de origem e suas dependências de coleção:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git
ansible-galaxy collection install -r requirements.yml
```

Execute o comando de coleção a partir deste checkout. Revise [defaults/main.yml](../../../defaults/main.yml) e os [exemplos](../../../examples/README.md) antes da implantação. Use o ponto de entrada suportado em vez de chamar fases internas de tarefas diretamente.

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

Forneça os segredos referenciados por meio do Ansible Vault ou de um gerenciador de segredos existente. Configure certificados e resolução de nomes de host para o host de destino antes de executar uma implantação. Mantenha os grupos de recursos incompletos desativados.

## Desenvolvimento e testes

O [Makefile](../../../Makefile), o [CONTRIBUTING.md](../../../CONTRIBUTING.md) e o [TESTING.md](../../../TESTING.md) definem a configuração de dependências com hash, verificações de lint, testes unitários e contratos descartáveis de Docker/Molecule. Testes unitários e lint não garantem uma implantação bem-sucedida.

```bash
make lint
```

Use o guia de testes para os cenários estáveis `default` e `tls` e seus pré-requisitos. As tarefas de instalação, atualização, limpeza e restauração de host modificam as máquinas selecionadas; use inventários de teste isolados para validação.

## Versionamento e pacotes de lançamento

Os lançamentos do projeto usam a versão SemVer completa em `VERSION`, independentemente
da versão mínima do Ansible em `meta/main.yml`. Envie uma tag correspondente `v2.22.1` na branch main
para acionar o workflow de Release ou execute-o manualmente a partir da main após criar a tag correspondente.
O workflow valida que a tag existente aponta para o código verificado, executa a suíte completa
de CI (incluindo todos os quatro cenários do Molecule) e publica um arquivo de role compatível
com o Galaxy, pacote Debian, RPM, `release.json` e `SHA256SUMS`.
A publicação usa essa tag existente verificada sem sobrescrever o destino padrão da API
de release, de modo que uma atualização posterior do workflow na main não exija credenciais
mais amplas de escrita em workflows. Uma tag ausente ou incompatível falha antes dos testes.

Verifique os downloads com `sha256sum --check SHA256SUMS`. Instale os pacotes nativos
com `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` no Ubuntu
24.04 ou `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` no
Rocky Linux 9. Ambos instalam a role em
`/usr/share/ansible/roles/wordpress_enterprise`; forneça um controlador Ansible
suportado e instale `requirements.yml` separadamente. O arquivo compactado pode ser
instalado com `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz`.
Os pacotes nativos contêm o código-fonte e a documentação da role e não executam scripts
de implantação durante a instalação. O CI instala, verifica e remove ambos os formatos.

## Segurança e licença

Consulte [SECURITY.md](../../../SECURITY.md) e a [licença MIT](../../../LICENSE). Os metadados do pacote, a política de suporte a plataformas e a validação de lançamentos devem permanecer alinhados com a role distribuída.
