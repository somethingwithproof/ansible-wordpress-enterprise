<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** [English](../../../README.md) · **ไทย** · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Português (BR)](../pt-BR/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)
- **Africa:** [Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)
- **Asia:** [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [עברית](../he/README.md) · [मराठी](../mr/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · **ไทย** · [اردو](../ur/README.md) · [Bahasa Melayu](../ms/README.md) · [Filipino](../fil/README.md)

</details>
<!-- translations:end -->

# Ansible WordPress Enterprise

[![CI](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_ansible-wordpress-enterprise&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_ansible-wordpress-enterprise)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/ansible-wordpress-enterprise)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/releases)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/ansible-wordpress-enterprise/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/ansible-wordpress-enterprise)

role ของ Ansible สำหรับกำหนดค่าโฮสต์ WordPress ร่วมกับ PHP เว็บเซิร์ฟเวอร์ และฐานข้อมูลภายในเครื่องหรือภายนอก การตรวจสอบแพลตฟอร์มและข้อมูลนำเข้าจะทำงานก่อนเข้าสู่ขั้นตอนการดีพลอย ขณะที่การแบ่งขอบเขตของงานช่วยให้สามารถตรวจสอบการติดตั้ง การกำหนดค่า และการทวนสอบแยกจากกันได้

## ข้อกำหนดการดีพลอยที่รองรับ

[meta/platform_support.yml](../../../meta/platform_support.yml) เป็นแหล่งอ้างอิงหลักของนโยบายการรองรับ เมทริกซ์การทดสอบ Molecule เวอร์ชันเสถียรครอบคลุม Ubuntu 24.04/PHP 8.3 และ Ubuntu 26.04/PHP 8.5 ร่วมกับ Nginx, Debian 13/PHP 8.4 ร่วมกับ Nginx และ Rocky Linux 9 และ 10/PHP 8.3 ร่วมกับ Apache โดยทุกเส้นทางผ่านการทดสอบทั้งผ่าน HTTP และ HTTPS คู่ระบบปฏิบัติการ/PHP เหล่านี้คือคู่ที่ผ่านการทดสอบแล้ว การเขียนทับค่าใน inventory เป็นคู่ที่ไม่ได้ผ่านการทดสอบจะล้มเหลวก่อนมีการเปลี่ยนแปลงแพ็กเกจ ชื่อแทน (alias) ในตระกูล EL ใช้นโยบายร่วมกัน แต่หลักฐานการทำงานจริงมาจากการทดสอบบนคอนเทนเนอร์ Rocky Linux

คอนโทรลเลอร์ Python 3.12 ใช้ Ansible 14.6 ขึ้นไปในสาย 14.x ร่วมกับ ansible-core 2.21.6 ขึ้นไปในสาย 2.21 ส่วนคอนโทรลเลอร์ Python 3.13 และ 3.14 ใช้ Ansible 15.x ร่วมกับ ansible-core 2.22.x ไฟล์ล็อกรายการแพ็กเกจแบบมีแฮช (hashed requirements lock) จะเลือกคู่เวอร์ชันให้เหมาะกับตัวแปลภาษาของคอนโทรลเลอร์ ข้อกำหนดตัวแปลภาษาของโหนดที่ถูกจัดการ (managed node) จะแยกต่างหาก โปรดตรวจสอบนโยบายก่อนเลือกเวอร์ชัน แพลตฟอร์มรุ่นเก่าและเวอร์ชัน PHP ที่รองรับเฉพาะฝั่งต้นน้ำ (upstream) จะไม่ได้รับการรองรับโดยอัตโนมัติ

## ความพร้อมใช้งานของฟีเจอร์

ลำดับงานหลักถูกกำหนดไว้ใน [tasks/main.yml](../../../tasks/main.yml) กลุ่มฟีเจอร์ด้านการมอนิเตอร์ การสำรองข้อมูล Fail2ban ความปลอดภัย แคชชิ่ง และไฟร์วอลล์ ยังมีข้อกำหนดเทมเพลตที่ขาดหายไปซึ่งบันทึกไว้ใน [tests/unit/missing_templates.yml](../../../tests/unit/missing_templates.yml) แฟล็กของกลุ่มเหล่านี้ถูกปิดไว้เป็นค่าเริ่มต้น และการตรวจสอบความถูกต้องจะปฏิเสธการเปิดใช้งานกลุ่มที่ยังไม่สมบูรณ์ ไม่ควรนำชื่องานและตัวแปรตัวอย่างมาอ้างอิงว่าเป็นฟีเจอร์ที่พร้อมใช้งานจริง

TLS ข้อมูลรับรองฐานข้อมูล ค่าความลับของ WordPress ที่ถูกสร้างขึ้น กลไกป้องกันพาธ และการจัดการเฉพาะระบบปฏิบัติการจำเป็นต้องมีการกำหนดค่าและการตรวจสอบระหว่างทำงานตามที่ระบุในเอกสาร ไม่มีการรับประกันการสลับระบบอัตโนมัติ (automatic failover), SLA ความพร้อมใช้งานระดับคลาวด์ หรือความพร้อมสำหรับสภาพแวดล้อมการผลิตทุกกรณีในที่นี้

## เริ่มต้นใช้งานอย่างรวดเร็ว

ติดตั้ง role จากซอร์สในรีโพซิทอรีพร้อมคอลเลกชันที่ต้องพึ่งพา:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git
ansible-galaxy collection install -r requirements.yml
```

รันคำสั่งติดตั้งคอลเลกชันจากโค้ดที่ checkout มา ตรวจสอบ [defaults/main.yml](../../../defaults/main.yml) และ[ตัวอย่าง](../../../examples/README.md) ก่อนทำการดีพลอย และใช้จุดเข้าใช้งานที่รองรับแทนการเรียกขั้นตอนงานภายในโดยตรง

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

จัดเตรียมค่าความลับที่อ้างอิงผ่าน Ansible Vault หรือระบบจัดการความลับที่มีอยู่ ตั้งค่าใบรับรองและการแปลงชื่อโฮสต์ (hostname resolution) สำหรับโฮสต์เป้าหมายก่อนรันการดีพลอย และคงสถานะปิดใช้งานสำหรับกลุ่มฟีเจอร์ที่ยังไม่สมบูรณ์

## การพัฒนาและการทดสอบ

[Makefile](../../../Makefile), [CONTRIBUTING.md](../../../CONTRIBUTING.md) และ [TESTING.md](../../../TESTING.md) กำหนดการติดตั้งดีเพนเดนซีแบบมีแฮช การตรวจสอบ lint ยูนิตเทสต์ และข้อกำหนดการทดสอบแบบใช้แล้วทิ้งด้วย Docker/Molecule ทั้งนี้ ยูนิตเทสต์และ lint ไม่ได้เป็นเครื่องรับประกันว่าการดีพลอยจะสำเร็จ

```bash
make lint
```

ดูคู่มือการทดสอบสำหรับสถานการณ์ทดสอบเสถียร `default` และ `tls` รวมถึงข้อกำหนดเบื้องต้น งานด้านการติดตั้ง อัปเกรด ทำความสะอาด และกู้คืนบนโฮสต์จะเปลี่ยนแปลงสถานะของเครื่องที่เลือก จึงควรใช้ inventory ทดสอบที่แยกต่างหากในการตรวจสอบ

## การกำหนดเวอร์ชันและแพ็กเกจรีลีส

การออกรีลีสของโปรเจกต์ใช้เลขเวอร์ชัน SemVer แบบเต็มในไฟล์ `VERSION` โดยแยกอิสระจากเวอร์ชัน Ansible ขั้นต่ำใน `meta/main.yml` ให้พุชแท็ก `v2.22.1` ที่ตรงกันบนบรานช์ main เพื่อทริกเกอร์เวิร์กโฟลว์ Release หรือสั่งรันด้วยตนเองจาก main หลังจากสร้างแท็กที่ตรงกันแล้ว เวิร์กโฟลว์จะตรวจสอบว่าแท็กที่มีอยู่ชี้ไปยังซอร์สโค้ดที่ตรวจสอบไว้ รันชุดทดสอบ CI เต็มรูปแบบ (รวมถึงสถานการณ์ทดสอบ Molecule ทั้ง 4 ชุด) และเผยแพร่ไฟล์เก็บถาวรของ role ที่เข้ากันได้กับ Galaxy, แพ็กเกจ Debian, RPM, `release.json` และ `SHA256SUMS` การเผยแพร่จะใช้แท็กที่มีอยู่และผ่านการตรวจสอบแล้วนั้นโดยไม่เขียนทับเป้าหมายเริ่มต้นของ release API เพื่อให้การอัปเดตเวิร์กโฟลว์บน main ในภายหลังไม่จำเป็นต้องใช้สิทธิ์การเขียนเวิร์กโฟลว์ที่กว้างขึ้น หากไม่มีแท็กหรือแท็กไม่ตรงกัน เวิร์กโฟลว์จะล้มเหลวก่อนเริ่มการทดสอบ

ตรวจสอบไฟล์ที่ดาวน์โหลดด้วย `sha256sum --check SHA256SUMS` ติดตั้งแพ็กเกจเนทีฟด้วย `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` บน Ubuntu 24.04 หรือ `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` บน Rocky Linux 9 แพ็กเกจทั้งสองจะติดตั้ง role ไว้ที่ `/usr/share/ansible/roles/wordpress_enterprise` โดยต้องเตรียมคอนโทรลเลอร์ Ansible ที่รองรับและติดตั้ง `requirements.yml` แยกต่างหาก สามารถติดตั้งไฟล์เก็บถาวรได้ด้วย `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz` แพ็กเกจเนทีฟประกอบด้วยซอร์สโค้ดของ role และเอกสารประกอบเท่านั้น และจะไม่รันสคริปต์ดีพลอยใด ๆ ระหว่างการติดตั้ง ทั้งนี้ CI จะทำการติดตั้ง ตรวจสอบ และถอนการติดตั้งแพ็กเกจทั้งสองรูปแบบ

## ความปลอดภัยและสัญญาอนุญาต

ดูรายละเอียดเพิ่มเติมได้ที่ [SECURITY.md](../../../SECURITY.md) และ[สัญญาอนุญาต MIT](../../../LICENSE) ข้อมูลเมตาของแพ็กเกจ นโยบายการรองรับแพลตฟอร์ม และการตรวจสอบรีลีสต้องสอดคล้องกับ role ที่เผยแพร่อยู่เสมอ
