<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · **Tiếng Việt** · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · **Tiếng Việt** · [Bahasa Indonesia](../id/README.md)
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

Một vai trò Ansible dùng để cấu hình các máy chủ WordPress với PHP, máy chủ web và cơ sở dữ liệu cục bộ hoặc bên ngoài. Bước kiểm tra hợp lệ nền tảng và dữ liệu đầu vào chạy trước các giai đoạn triển khai, trong khi ranh giới tác vụ giúp quá trình cài đặt, cấu hình và xác minh có thể được rà soát tách biệt.

## Cam kết hỗ trợ triển khai

[meta/platform_support.yml](../../../meta/platform_support.yml) là nguồn quy định chính thức về chính sách hỗ trợ. Ma trận Molecule ổn định bao gồm Ubuntu 24.04/PHP 8.3 và Ubuntu 26.04/PHP 8.5 với Nginx, Debian 13/PHP 8.4 với Nginx, và Rocky Linux 9 và 10/PHP 8.3 với Apache. Mọi đường dẫn triển khai đều được kiểm thử qua HTTP và HTTPS. Đây là các cặp hệ điều hành/PHP đã được kiểm thử; việc ghi đè trong inventory sang các cặp chưa được kiểm thử sẽ thất bại trước khi có thay đổi về gói phần mềm. Các tên gọi tương đương của EL dùng chung chính sách này, nhưng bằng chứng chạy thực tế đến từ các container Rocky Linux.

Các máy điều khiển dùng Python 3.12 sử dụng Ansible 14.6 trở lên thuộc nhánh 14.x cùng với ansible-core 2.21.6 trở lên thuộc nhánh 2.21. Các máy điều khiển dùng Python 3.13 và 3.14 sử dụng Ansible 15.x cùng với ansible-core 2.22.x. Tệp khóa phụ thuộc có mã băm sẽ chọn cặp phiên bản phù hợp cho trình thông dịch của máy điều khiển. Yêu cầu về trình thông dịch trên nút được quản lý là riêng biệt. Hãy tham khảo chính sách trước khi chọn phiên bản; các nền tảng cũ hơn và những phiên bản PHP chỉ mới được hỗ trợ từ thượng nguồn không tự động được áp dụng.

## Mức độ hoàn thiện tính năng

Chuỗi tác vụ cốt lõi được định nghĩa trong [tasks/main.yml](../../../tasks/main.yml). Các nhóm giám sát, sao lưu, Fail2ban, bảo mật, bộ nhớ đệm và tường lửa có các hợp đồng mẫu cấu hình bị thiếu được ghi nhận trong [tests/unit/missing_templates.yml](../../../tests/unit/missing_templates.yml). Các cờ kích hoạt của chúng mặc định bị tắt và bước kiểm tra hợp lệ sẽ từ chối khi bật các nhóm chưa hoàn thiện. Tên tác vụ và các biến ví dụ không được xem là các bản triển khai hoạt động hoàn chỉnh của những tính năng đó.

TLS, thông tin xác thực cơ sở dữ liệu, các khóa bí mật WordPress được tạo tự động, cơ chế bảo vệ đường dẫn và xử lý đặc thù theo hệ điều hành đòi hỏi cấu hình đúng tài liệu và kiểm tra trong quá trình chạy. Không có tuyên bố nào về chuyển đổi dự phòng tự động, cam kết mức độ sẵn sàng (SLA) trên toàn nền tảng đám mây hay tính sẵn sàng phổ quát cho môi trường sản xuất được đưa ra ở đây.

## Bắt đầu nhanh

Cài đặt vai trò từ mã nguồn kho lưu trữ và các bộ sưu tập phụ thuộc của nó:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git
ansible-galaxy collection install -r requirements.yml
```

Chạy lệnh cài đặt bộ sưu tập từ bản sao mã nguồn này. Hãy rà soát [defaults/main.yml](../../../defaults/main.yml) và [các ví dụ](../../../examples/README.md) trước khi triển khai. Sử dụng điểm vào được hỗ trợ thay vì gọi trực tiếp các giai đoạn tác vụ nội bộ.

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

Cung cấp các bí mật được tham chiếu thông qua Ansible Vault hoặc trình quản lý bí mật hiện có. Cấu hình chứng chỉ và phân giải tên máy chủ cho máy đích trước khi chạy triển khai. Giữ trạng thái tắt đối với các nhóm tính năng chưa hoàn thiện.

## Phát triển và kiểm thử

[Makefile](../../../Makefile), [CONTRIBUTING.md](../../../CONTRIBUTING.md) và [TESTING.md](../../../TESTING.md) định nghĩa thiết lập phụ thuộc có mã băm, kiểm tra lint, kiểm thử đơn vị và các kịch bản Docker/Molecule dùng một lần. Kiểm thử đơn vị và lint không đảm bảo một bản triển khai sẽ thành công.

```bash
make lint
```

Tham khảo hướng dẫn kiểm thử cho hai kịch bản ổn định `default` và `tls` cùng các điều kiện tiên quyết của chúng. Các tác vụ cài đặt, nâng cấp, dọn dẹp và khôi phục trên máy chủ sẽ thay đổi trạng thái của các máy được chọn; hãy sử dụng inventory thử nghiệm cô lập để xác minh.

## Quản lý phiên bản và gói phát hành

Các bản phát hành của dự án sử dụng phiên bản SemVer đầy đủ trong `VERSION`, độc lập với phiên bản Ansible tối thiểu trong `meta/main.yml`. Đẩy một thẻ `v2.22.1` tương ứng trên nhánh main để kích hoạt quy trình Release, hoặc chạy thủ công từ nhánh main sau khi tạo thẻ tương ứng. Quy trình sẽ xác minh thẻ hiện có trỏ đúng đến mã nguồn được kiểm tra, chạy toàn bộ bộ kiểm thử CI (bao gồm cả bốn kịch bản Molecule), và xuất bản tệp lưu trữ vai trò tương thích Galaxy, gói Debian, gói RPM, `release.json` và `SHA256SUMS`. Việc xuất bản sử dụng thẻ hiện có đã được xác minh đó mà không ghi đè đích mặc định của API phát hành, nhờ vậy các bản cập nhật quy trình sau này trên nhánh main không yêu cầu quyền ghi quy trình rộng hơn. Thẻ bị thiếu hoặc không khớp sẽ gây lỗi trước khi kiểm thử.

Xác minh các tệp tải xuống bằng `sha256sum --check SHA256SUMS`. Cài đặt gói gốc bằng `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` trên Ubuntu 24.04 hoặc `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` trên Rocky Linux 9. Cả hai đều cài đặt vai trò vào `/usr/share/ansible/roles/wordpress_enterprise`; hãy cung cấp máy điều khiển Ansible được hỗ trợ và cài đặt riêng `requirements.yml`. Tệp lưu trữ có thể được cài đặt bằng `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz`. Các gói gốc chứa mã nguồn vai trò cùng tài liệu và không chạy bất kỳ kịch bản triển khai nào trong quá trình cài đặt. CI sẽ cài đặt, kiểm tra và gỡ bỏ cả hai định dạng.

## Bảo mật và giấy phép

Xem [SECURITY.md](../../../SECURITY.md) và [giấy phép MIT](../../../LICENSE). Siêu dữ liệu gói, chính sách hỗ trợ nền tảng và bước xác minh phát hành phải luôn đồng nhất với vai trò được phân phối.
