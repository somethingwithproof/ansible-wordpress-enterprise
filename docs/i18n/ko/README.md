<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · **한국어** · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · **한국어** · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
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

PHP, 웹 서버, 그리고 로컬 또는 외부 데이터베이스로 WordPress 호스트를 구성하기 위한 Ansible 역할입니다. 플랫폼 및 입력값 검증은 배포 단계 이전에 실행되며, 작업 경계를 통해 설치, 구성, 검증 단계를 각각 독립적으로 검토할 수 있습니다.

## 지원되는 배포 계약

[meta/platform_support.yml](../../../meta/platform_support.yml)이 지원 정책의 기준 파일입니다. 안정화된 Molecule 매트릭스는 Nginx를 사용하는 Ubuntu 24.04/PHP 8.3 및 Ubuntu 26.04/PHP 8.5, Nginx를 사용하는 Debian 13/PHP 8.4, 그리고 Apache를 사용하는 Rocky Linux 9 및 10/PHP 8.3을 포괄합니다. 모든 경로는 HTTP 및 HTTPS로 테스트됩니다. 이들은 테스트가 완료된 OS/PHP 조합이며, 테스트되지 않은 조합으로 인벤토리를 재정의하면 패키지가 변경되기 전에 실패합니다. EL 별칭도 동일한 정책을 공유하지만, 런타임 검증 근거는 Rocky Linux 컨테이너에서 확보합니다.

Python 3.12 컨트롤러는 14.x 계열의 Ansible 14.6 이상과 2.21 계열의 ansible-core 2.21.6 이상을 사용합니다. Python 3.13 및 3.14 컨트롤러는 Ansible 15.x와 ansible-core 2.22.x를 사용합니다. 해시된 요구 사항 잠금 파일이 컨트롤러 인터프리터에 맞는 조합을 선택합니다. 관리 노드의 인터프리터 요구 사항은 별개입니다. 버전을 선택하기 전에 지원 정책을 확인하세요. 구형 플랫폼이나 단순히 업스트림에서 지원되는 PHP 버전은 자동으로 채택되지 않습니다.

## 기능 성숙도

핵심 작업 순서는 [tasks/main.yml](../../../tasks/main.yml)에 정의되어 있습니다. 모니터링, 백업, Fail2ban, 보안, 캐싱, 방화벽 그룹에는 누락된 템플릿 계약이 있으며 이는 [tests/unit/missing_templates.yml](../../../tests/unit/missing_templates.yml)에 기록되어 있습니다. 해당 플래그는 기본값이 비활성화 상태이며, 미완성 그룹을 활성화하면 검증 단계에서 거부됩니다. 작업 이름이나 예제 변수가 해당 기능의 완성된 구현인 것처럼 제시되어서는 안 됩니다.

TLS, 데이터베이스 자격 증명, 생성된 WordPress 시크릿, 경로 보호 장치, 그리고 OS별 처리는 문서화된 구성과 런타임 검증이 필요합니다. 여기서는 자동 장애 조치, 클라우드 전역 가용성 SLA 또는 범용 프로덕션 준비 완료를 보장하지 않습니다.

## 빠른 시작

저장소 소스에서 역할과 컬렉션 의존성을 설치합니다:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git,HEAD,wordpress_enterprise
ansible-galaxy collection install -r requirements.yml
```

이 체크아웃에서 컬렉션 설치 명령을 실행하세요. 배포 전에 [defaults/main.yml](../../../defaults/main.yml)과 [예제](../../../examples/README.md)를 검토하세요. 내부 작업 단계를 직접 호출하지 말고 지원되는 진입점을 사용하세요.

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

참조되는 시크릿은 Ansible Vault 또는 기존 시크릿 관리자를 통해 제공하세요. 배포를 실행하기 전에 대상 호스트의 인증서와 호스트 이름 확인을 구성하세요. 미완성 기능 그룹은 비활성화 상태로 유지하세요.

## 개발 및 테스트

[Makefile](../../../Makefile), [CONTRIBUTING.md](../../../CONTRIBUTING.md), [TESTING.md](../../../TESTING.md)에는 해시된 의존성 설정, 린트 검사, 단위 테스트, 그리고 일회성 Docker/Molecule 계약이 정의되어 있습니다. 단위 테스트와 린트 검사가 성공적인 배포를 보장하지는 않습니다.

```bash
make lint
```

안정화된 `default` 및 `tls` 시나리오와 사전 요구 사항은 테스트 가이드를 참고하세요. 호스트 설치, 업그레이드, 정리, 복원 작업은 선택한 머신의 상태를 변경하므로 검증에는 격리된 테스트 인벤토리를 사용하세요.

## 버전 관리 및 릴리스 패키지

프로젝트 릴리스는 `meta/main.yml`의 최소 Ansible 버전과는 독립적으로 `VERSION`에 지정된 전체 SemVer 버전을 사용합니다. main 브랜치에 일치하는 `v2.22.1` 태그를 푸시하여 Release를 트리거하거나, 일치하는 태그를 생성한 뒤 main에서 수동으로 실행하세요. 워크플로는 기존 태그가 검사 대상 소스를 가리키는지 확인하고, 전체 CI 스위트(4개의 Molecule 시나리오 모두 포함)를 실행한 다음, Galaxy 호환 역할 아카이브, Debian 패키지, RPM, `release.json` 및 `SHA256SUMS`를 게시합니다. 게시는 릴리스 API의 기본 대상을 덮어쓰지 않고 검증된 기존 태그를 사용하므로, 이후 main에서 워크플로를 업데이트하더라도 더 넓은 워크플로 쓰기 권한이 필요하지 않습니다. 태그가 누락되었거나 일치하지 않으면 테스트 전에 실패합니다.

다운로드한 파일은 `sha256sum --check SHA256SUMS`로 검증하세요. 네이티브 패키지는 Ubuntu 24.04에서 `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb`로, Rocky Linux 9에서는 `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm`으로 설치할 수 있습니다. 두 패키지 모두 역할을 `/usr/share/ansible/roles/wordpress_enterprise` 경로에 설치합니다. 지원되는 Ansible 컨트롤러를 준비하고 `requirements.yml`은 별도로 설치하세요. 아카이브는 `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz,,wordpress_enterprise`로 설치할 수 있습니다. 네이티브 패키지에는 역할 소스와 문서만 포함되며 설치 중에 배포 스크립트를 실행하지 않습니다. CI는 두 형식을 모두 설치, 확인 및 제거합니다.

## 보안 및 라이선스

[SECURITY.md](../../../SECURITY.md)와 [MIT 라이선스](../../../LICENSE)를 참고하세요. 패키지 메타데이터, 플랫폼 지원 정책 및 릴리스 검증은 배포되는 역할과 일관되게 유지되어야 합니다.
