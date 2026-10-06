# PiVR 설치 가이드 (Raspberry Pi 이미지)

PiVR은 미리 만들어진 microSD 카드 이미지로 Vital Recorder를 실행하는 Raspberry Pi입니다. 이미지에는 Vital Recorder, 네트워크 감시 기능, 웹 관리자 페이지(**PiVR Control Panel**)가 들어 있습니다. 이 문서는 이미지를 카드에 기록하는 방법, 첫 부팅, 관리자 페이지 설정을 다룹니다.

- 케이블과 장비 쪽 설정: [Hardware Connection Guide](connection-guide/devices/README.md)
- `vr.conf` 항목: [Configuration Guide](Configuration_Guide.md)

> ⚠️ 이미지에는 기본 계정 정보가 들어 있습니다. 이미지 파일과 관리자 기본 비밀번호를 기관 밖으로 공유하지 마십시오.

---

## 목차

1. [준비물](#준비물)
2. [이미지 파일 확인](#1-이미지-파일-확인)
3. [microSD 카드에 이미지 기록](#2-microsd-카드에-이미지-기록)
4. [첫 부팅](#3-첫-부팅)
5. [관리자 페이지 접속](#4-관리자-페이지-접속)
6. [초기 설정 순서](#5-초기-설정-순서)
7. [관리자 페이지 화면별 설명](#관리자-페이지-화면별-설명)
8. [문제 해결](#문제-해결)

---

## 준비물

| 항목 | 설명 |
|------|------|
| Raspberry Pi | Raspberry Pi 4 Model B, Raspberry Pi 5, Raspberry Pi Zero 2 W |
| microSD 카드 | 32 GB, 고내구성(High Endurance) 제품 (예: SanDisk High Endurance). 녹화 중에는 카드에 계속 기록합니다. |
| 전원 어댑터 | 모델에 맞는 정격 전원 (Raspberry Pi 4는 5 V 3 A) |
| USB Wi-Fi 동글 | Realtek RTL8821CU. 병원 Wi-Fi 연결에 쓰며, 핫스팟을 쓰려면 반드시 필요합니다. |
| 시리얼 인터페이스 | FTDI FT4232H USB-시리얼 HAT (시리얼 연결 장비용) |
| 노트북과 랜선 | 관리자 페이지 접속용. Raspberry Pi Zero 2 W에는 이더넷 포트가 없으므로 USB 이더넷 어댑터를 사용합니다. |
| 이미지 파일 | `pivr-<버전>-<날짜>.img.xz`와 SHA-256 체크섬. VitalLab에서 제공합니다. |

---

## 1. 이미지 파일 확인

내려받은 파일의 SHA-256 값을 이미지와 함께 받은 값(`.sha256` 파일 또는 `SHA256SUMS.txt`)과 비교합니다. `.img.xz` 파일과 압축을 푼 `.img` 파일은 값이 다릅니다.

```bash
# macOS
shasum -a 256 pivr-<버전>-<날짜>.img.xz

# Linux
sha256sum pivr-<버전>-<날짜>.img.xz
```

```powershell
# Windows
certutil -hashfile pivr-<버전>-<날짜>.img.xz SHA256
```

값이 다르면 파일을 다시 내려받습니다.

---

## 2. microSD 카드에 이미지 기록

> ⚠️ 이미지를 기록하면 카드 전체가 지워집니다. PiVR에서 쓰던 카드라면 Wi-Fi 설정, `vr.conf`, 로그, 녹화 파일이 있는 데이터 파티션도 함께 지워집니다. 녹화 파일을 먼저 복사해 두십시오.

Raspberry Pi Imager와 balenaEtcher는 `.img.xz` 파일을 그대로 넣으면 됩니다. 압축을 풀 필요가 없습니다.

### Raspberry Pi Imager

1. 사용하는 Raspberry Pi 모델을 선택합니다.
2. **운영체제(Operating System)** 에서 **Use custom** 을 선택하고 `.img.xz` 파일을 고릅니다.
3. **저장소(Storage)** 에서 microSD 카드를 선택합니다.
4. Imager가 OS 사용자 지정(호스트 이름, 사용자, Wi-Fi)을 물으면 적용하지 않습니다. 이미지에 자체 설정이 있고, Wi-Fi는 관리자 페이지에서 설정합니다.
5. 기록을 시작하고 검증이 끝날 때까지 기다립니다.

### balenaEtcher

1. **Flash from file** → `.img.xz` 파일을 선택합니다.
2. **Select target** → microSD 카드를 선택합니다.
3. **Flash!** 를 누르고 검증이 끝날 때까지 기다립니다.

### 명령줄 (macOS / Linux)

압축을 먼저 푼 뒤 `.img` 파일을 기록합니다. 디스크 이름을 반드시 확인하십시오. 다른 디스크에 기록하면 그 디스크의 내용이 지워집니다.

```bash
xz -dk pivr-<버전>-<날짜>.img.xz

# macOS (카드 확인: diskutil list)
diskutil unmountDisk /dev/diskN
sudo dd if=pivr-<버전>-<날짜>.img of=/dev/rdiskN bs=4m status=progress

# Linux (카드 확인: lsblk)
sudo dd if=pivr-<버전>-<날짜>.img of=/dev/sdX bs=4M status=progress conv=fsync
```

---

## 3. 첫 부팅

1. 카드를 꽂고 USB Wi-Fi 동글을 연결한 뒤 전원을 켭니다.
2. 첫 부팅 때 카드의 남은 공간으로 데이터 파티션(`/data`)을 만들고 스스로 1회 재부팅합니다.
3. 이 과정 중에 전원이 꺼져도 괜찮습니다. 다음 부팅 때 이어서 진행합니다.

첫 부팅 이후 Wi-Fi 설정, `vr.conf`, 로그, 녹화 파일은 `/data`에 저장되며 재부팅해도 유지됩니다.

---

## 4. 관리자 페이지 접속

1. 노트북과 Pi의 이더넷 포트를 랜선으로 연결합니다.
2. 노트북 유선 네트워크 어댑터를 IP 자동 받기로 설정합니다. Pi가 `192.168.137.50`~`192.168.137.100` 범위의 주소를 할당합니다. 주소를 받지 못하면 IP `192.168.137.10`, 서브넷 마스크 `255.255.255.0`으로 직접 설정합니다.
3. 웹 브라우저에서 `http://192.168.137.2`에 접속합니다.
4. 주황색 **First-time setup in progress** 배너가 보이면 기다립니다. 배너가 초록색으로 바뀌고 **Setup complete — Rebooting shortly...** 가 표시되면 재부팅을 기다린 뒤 페이지를 새로 고칩니다.
5. 관리자 비밀번호로 로그인합니다. 기본 비밀번호는 VitalLab이 이미지와 함께 안내합니다. 로그인 후 **System** 화면에서 변경합니다.

**화면 이동:** 왼쪽 위 ☰ 버튼을 누르면 전체 화면 목록이 나옵니다. 키보드 좌우 화살표 키(터치 화면에서는 좌우로 밀기)로 이전/다음 화면으로 이동합니다. 설정이 있는 화면은 오른쪽 위 **Save** 버튼으로 저장하며, 적용 전에 확인 창이 뜹니다.

---

## 5. 초기 설정 순서

| # | 화면 | 작업 |
|---|------|------|
| 1 | System | **Sync time** 누르기 ([System](#system) 참고) |
| 2 | System | 관리자 비밀번호 변경 |
| 3 | Information | 병원망이 MAC 등록제이면 Wi-Fi MAC 주소 확인 |
| 4 | General | VR Name, 파일 분할 방식, Vitalserver 주소 입력 |
| 5 | Network | 병원 Wi-Fi 설정 입력 |
| 6 | Devices | 연결한 장비 추가 |
| 7 | Logs | Vital Recorder가 데이터를 받는지 확인 |

---

## 관리자 페이지 화면별 설명

### General

| 항목 | `vr.conf` | 설명 |
|------|-----------|------|
| VR Name | `[BED/<이름>]` | 녹화 파일과 서버에서 쓰는 침상명. 설정된 이름이 없으면 Pi 시리얼 번호의 마지막 8자리가 표시됩니다. |
| Cut file by: **case** | `CUT_FILE=1`, `CUT_HOURLY=0` | 환자 단위로 파일 분할 |
| after *N* min | `PT_WAITING_TIME=N` | 환자 대기 시간(분). **case** 선택 시 표시, 기본값 5 |
| Cut file by: **hour** | `CUT_FILE=0`, `CUT_HOURLY=1` | 1시간 단위로 파일 분할 |
| Vitalserver Address | `SERVER_IP` | **Optional Settings** 안에 있습니다. `host:port` 형식이며 앞에 `http://` 또는 `https://`를 붙일 수 있습니다. 예: `192.168.10.20:5000`, `https://vitalserver.example.com:443` |

**Save** 를 누르면 `vr.conf`에 저장하고 Vital Recorder를 재시작합니다.

Vitalserver 주소가 형식에 맞지 않으면(포트 누락, 공백 포함, 포트가 1~65535 범위 밖, http/https 외의 스킴) 저장되지 않고 이전 값이 그대로 남으며, 오류 메시지는 표시되지 않습니다. 저장 후 페이지를 새로 고쳐 값을 확인하십시오.

### Devices

왼쪽에 설정된 장비 목록이 표시됩니다. **Add Device** 를 누르면 장비 목록이 분류별로 나오며 검색할 수 있습니다. 이 목록은 설치된 Vital Recorder에서 가져오므로 해당 버전이 지원하는 장비와 일치합니다.

| 항목 | `vr.conf` | 설명 |
|------|-----------|------|
| Name | `[DEV/<이름>]` | 장비 이름. 기본값은 장비 종류 이름입니다. |
| Type | `type` | 장비 종류 |
| Port | `port` | `LU`, `RU`, `LL`, `RL`(`1`~`4` 포함), `F1`~`F4`, `C1`~`C4`, `ACM0`, `4202`, `6002`, 그 밖의 값(예: `IP:port`)은 **Other**. [Configuration Guide](Configuration_Guide.md#port-formats)의 Port Formats 참고 |
| Y cable | `readonly=1` | 수신 전용. 다른 시스템과 Y 케이블로 신호를 나눠 받을 때 사용합니다. |

장비별 추가 옵션:

| 장비 종류 | 옵션 |
|-----------|------|
| SNUADC, SNUADCM, DI-149, DI-155, DI-1100, DI-1120 | Sampling Frequency, Voltage to Physical Unit 프리셋(GE Tram Rec 4A), 채널별 파라미터 이름과 gain |
| Intellivue, VueLink | 파형 선택. ART, CVP 같은 일반 파형은 선택하지 않아도 추가됩니다. ECG 3개 또는 ECG 외 8개까지 안정적으로 받을 수 있습니다. |
| Bx50, B1x5M | 파형 선택, **Do not request numeric data** (`waveonly=1`). S5 프로토콜은 전체 600 samples/s까지 받을 수 있습니다. |
| ADT | Bed name. Port는 **Other** 로 지정되며 주소를 입력합니다. |
| EGA, HL7GW | Port는 **Other** 로 지정되며 주소를 입력합니다. Y cable 옵션 없음 |
| Demo | Port 없음 |

**Save** 를 누르면 `vr.conf`에 저장하고 Vital Recorder를 재시작합니다. 장비를 지우려면 해당 장비 화면에서 **Delete** 를 누른 뒤 **Save** 를 누릅니다.

> ⚠️ Devices 화면을 저장하면 모든 `[DEV/...]` 절을 이 화면의 항목만으로 다시 씁니다. **Advanced** 화면에서 직접 추가했지만 이 화면에 없는 장비 옵션(예: `auto_wavs=0`)은 지워집니다. 저장 후 **Advanced** 화면을 확인하십시오.

### Network

**Wireless** — 병원 Wi-Fi 연결입니다. USB Wi-Fi 동글이 연결되어 있으면 동글을, 없으면 내장 Wi-Fi를 사용합니다.

| 항목 | 설명 |
|------|------|
| SSID | 네트워크 이름 |
| PW | Wi-Fi 비밀번호 |
| Hidden Network | SSID를 숨긴 네트워크이면 체크 |
| User | WPA2-Enterprise(PEAP / MSCHAPv2) 사용자 ID. 비밀번호만 쓰는 네트워크(WPA2-Personal)는 비워 둡니다. |

**Static IP Settings** — 모두 비워 두면 IP를 자동으로 받습니다(DHCP). 고정 IP를 쓰려면 IP, Netmask, Gateway를 입력합니다. IP를 입력하면 Gateway가 `x.x.x.1`로 채워지므로, 병원망의 게이트웨이가 다르면 고칩니다. Primary/Secondary DNS는 선택 항목이며 비워 두면 `1.1.1.1`, `8.8.8.8`을 사용합니다. 고정 IP는 Wi-Fi SSID를 함께 입력해야 적용됩니다.

**Hotspot** — 내장 Wi-Fi로 Wi-Fi 접속점을 만듭니다. PiVR에 무선으로 연결하는 장비용입니다.

| 항목 | 설명 |
|------|------|
| Hotspot On/Off | USB Wi-Fi 동글이 연결되어 있을 때만 사용할 수 있습니다(없으면 스위치가 비활성). |
| SSID | 핫스팟 이름. General 화면에서 VR Name을 입력하면 `vital_<이름>`으로 채워집니다. |
| PW | 핫스팟 비밀번호(WPA2). 비워 두면 개방형 네트워크가 됩니다. |

핫스팟은 2.4 GHz 1번 채널을 사용합니다. 핫스팟 네트워크에서 PiVR의 주소는 `192.168.137.1`이며, 접속한 장비에 주소를 할당합니다.

**Save** 를 누르면 설정을 적용하고 Wi-Fi에 다시 연결합니다. 랜선으로 접속한 관리자 페이지는 그대로 유지됩니다.

### System

| 버튼 | 동작 |
|------|------|
| VR → Restart | Vital Recorder 재시작 |
| OS → Reboot | Pi 재부팅 |
| OS → Sync time | Pi 시계를 노트북 시계에 맞춥니다. 옆 칸에 시간 차이(초)가 표시됩니다. |
| Password → Save | 관리자 비밀번호 변경(현재 비밀번호, 새 비밀번호, 새 비밀번호 확인) |

> ⚠️ **첫 부팅 후 Sync time을 반드시 누르십시오.** Pi에는 배터리로 유지되는 시계가 없습니다. 새 카드는 이미지에 저장된 날짜에서 시작하며, 시계를 맞추기 전까지 녹화 파일 이름과 시간이 그 날짜로 기록됩니다. 버튼을 누르기 전에 노트북 시계가 맞는지 확인하십시오.

- Pi 전원이 꺼져 있는 동안은 시계가 멈춥니다. 장시간 정전 뒤에는 **Sync time** 을 다시 누릅니다.
- 시계가 바뀌면 Vital Recorder가 1회 재시작합니다(약 11초 녹화 공백).
- NTP가 켜진 이미지는 네트워크에서 NTP를 허용하면 시계를 자동으로 맞춥니다. NTP를 막는 네트워크에서는 **Sync time** 을 사용합니다.

### Information

| 항목 | 설명 |
|------|------|
| VR code | 설치된 Vital Recorder가 표시하는 코드 |
| Serial | Raspberry Pi 시리얼 번호 |
| eth0 | 이더넷 MAC 주소 |
| wlan0 | 내장 Wi-Fi MAC 주소 |
| wlan1 | USB Wi-Fi 동글 MAC 주소 |

이미지는 Wi-Fi MAC 주소를 무작위로 바꾸지 않으므로 MAC 등록제 병원망에 이 값을 등록할 수 있습니다. 병원 Wi-Fi에 연결되는 인터페이스의 주소를 등록합니다(USB Wi-Fi 동글을 쓰면 `wlan1`).

`wlan0`이 비어 있을 수 있습니다. USB Wi-Fi 동글이 연결되어 있고 핫스팟이 꺼져 있으면 부팅 약 1분 뒤 내장 Wi-Fi를 끕니다.

### Logs

시스템 로그를 보여 줍니다. 드롭다운에 로그 파일이 마지막 수정 시각으로 표시됩니다. 현재 로그는 마지막 30줄을 보여 주며 2초마다 갱신됩니다. 새로 고침 버튼은 파일 목록을 다시 불러옵니다.

### Advanced

`vr.conf`를 텍스트로 직접 편집합니다. 다른 화면에 없는 항목을 설정할 때 사용합니다([Configuration Guide](Configuration_Guide.md) 참고). **Save** 를 누르면 파일을 저장하고 Vital Recorder를 재시작합니다. General 또는 Devices 화면을 저장하면 그 화면이 관리하는 부분을 다시 씁니다.

---

## 문제 해결

| 증상 | 확인할 것 |
|------|-----------|
| `http://192.168.137.2`에 접속되지 않음 | 랜선이 Pi의 이더넷 포트에 꽂혀 있는지, 노트북 유선 어댑터가 자동 받기 또는 `192.168.137.10` / `255.255.255.0`인지 확인합니다. 새 카드라면 첫 부팅 재부팅이 끝날 때까지 기다립니다. |
| 첫 부팅 배너에 `ERROR`로 시작하는 메시지 | 이미지를 다시 기록하거나 다른 카드를 사용합니다. |
| "Incorrect password" | 이미지와 함께 안내받은 기본 비밀번호 또는 System 화면에서 바꾼 비밀번호를 입력합니다. 비밀번호를 잊었으면 VitalLab에 문의합니다. |
| Vitalserver 주소가 이전 값으로 돌아감 | 입력 형식이 잘못되었습니다. `host:port` 형식으로 입력합니다. |
| 고정 IP가 적용되지 않음 | IP와 Gateway를 모두 입력하고 Wi-Fi SSID도 함께 입력합니다. |
| Hotspot 스위치가 비활성 | USB Wi-Fi 동글이 인식되지 않았습니다. 동글을 연결하고 재부팅합니다. |
| 녹화 파일 이름의 날짜가 틀림 | System 화면에서 **Sync time** 을 누릅니다. |
| Wi-Fi가 연결되지 않거나, 연결되어도 통신이 안 됨 | 병원망이 MAC 등록제일 수 있습니다. Information 화면의 MAC 주소를 등록합니다. |
