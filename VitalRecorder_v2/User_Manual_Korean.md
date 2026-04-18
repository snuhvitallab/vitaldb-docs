# VitalRecorder 사용자 매뉴얼 (Korean)

VitalRecorder는 Windows, Raspberry Pi, Ubuntu에서 실행되는 실시간 생체신호 기록 프로그램입니다. 80종 이상의 의료기기에서 데이터를 수집하여 `.vital` 파일 형식으로 저장합니다.

---

## 목차

1. [설치](#설치)
2. [빠른 시작](#빠른-시작)
3. [사용자 인터페이스](#사용자-인터페이스)
4. [장비 추가](#장비-추가)
5. [연결 방식](#연결-방식)
6. [포트 필터링](#포트-필터링)
7. [녹화](#녹화)
8. [서버 업로드](#서버-업로드)
9. [설정 파일 (vr.conf)](#설정-파일-vrconf)
10. [명령줄 옵션](#명령줄-옵션)
11. [지원 장비](#지원-장비)
12. [문제 해결](#문제-해결)

---

## 설치

### Windows

Microsoft Store에서 다운로드하여 설치합니다:
- Store URL: https://apps.microsoft.com/detail/9MVBQL8R0TFL

또는 릴리스 페이지에서 MSI 설치 파일이나 MSIX 패키지를 다운로드하여 설치합니다.

### Raspberry Pi / Ubuntu

릴리스 페이지에서 플랫폼별 바이너리(`pivr64` 또는 `ubuntu64`)를 다운로드하여 직접 실행합니다.

---

## 빠른 시작

1. VitalRecorder를 실행합니다.
2. **장비 추가** 버튼을 클릭하여 의료 장비를 추가합니다.
3. 장비 유형을 선택합니다 (예: `Medtronic : BIS`, `Philips : Intellivue`).
4. 연결 포트를 선택합니다 (COM 포트, IP 주소, 또는 포트 번호).
5. **확인**을 클릭합니다. VitalRecorder가 장비와 통신을 시작합니다.
6. **녹화**를 클릭하여 데이터 기록을 시작합니다.

---

## 사용자 인터페이스

VitalRecorder는 탭 기반 인터페이스를 사용합니다. 각 탭은 "방" 또는 "침상"을 나타내며, 하나의 탭에 여러 장비를 연결할 수 있습니다.

- **트랙**: 각 장비는 하나 이상의 트랙을 생성합니다 (예: HR, SpO2, BIS). 트랙은 파형 또는 숫자로 표시됩니다.
- **이벤트**: 녹화 중 이벤트 마커를 추가할 수 있습니다.
- **모니터**: 설정 가능한 모니터 패널에서 선택한 파라미터를 큰 글씨로 표시합니다.

### 침상명

각 탭에 **침상명**을 지정할 수 있습니다. 침상명의 용도:
- 서버에 데이터를 업로드할 때 방을 구분합니다.
- HL7 게이트웨이 장비에서 다중 침상 데이터를 분리합니다.

---

## 장비 추가

**장비 추가**에서 장비 그룹을 선택합니다:

| 그룹 | 예시 |
|------|------|
| VitalDB 장비 | SNUADC, SNUADCM, BUTTON, VitalBOLUS |
| 아날로그-디지털 변환기 | DataQ DI-149, DI-155, DI-245, DI-1100, DI-1120 |
| 환자 감시 장치 | Philips Intellivue, GE Solar/Dash/Bx50, Nihon Kohden, Mindray HL7, MEKICS |
| 다기능 모니터 | Masimo Radical-7/Root, Sentec SDM |
| 마취기 | Draeger Primus/Zeus/Fabius, GE Datex-Ohmeda Aisys/Avance |
| 인공호흡기 | Maquet SERVO-i/s/U, Hamilton MR1/C2/C6/T1 |
| 약물 주입 펌프 | Fresenius Agilia/Primea/PCBM, BBraun SpaceCom/HL7, Daiwha, Pion |
| 뇌 모니터 | Medtronic BIS/VISTA/INVOS, Fresenius Conox, OBELAB NirsitON |
| 근이완 모니터 | TwitchView, TOFScan, TOFcuff |
| 수액 가온기 | Belmont FMS 2000 |
| 심박출량 모니터 | Edwards Hemosphere/Vigilance/EV1000/Vigileo, Getinge PulsioFlex |
| 태아 감시 장치 | GE Corometrics 250cx |

---

## 연결 방식

### RS-232 (시리얼 / COM 포트)

대부분의 장비는 물리적 COM 포트 또는 USB-to-Serial 어댑터를 통한 RS-232 시리얼 통신을 사용합니다.

- COM 포트 번호를 선택합니다 (예: `COM3`).
- 전송 속도 및 기타 시리얼 파라미터는 장비 유형에 따라 자동 설정됩니다.
- 연결 전에 USB-to-Serial 드라이버를 설치하십시오.

### TCP (네트워크)

네트워크 연결 장비용입니다. VitalRecorder는 TCP **클라이언트** 또는 **서버** 역할을 할 수 있습니다.

- **클라이언트 모드**: 장비의 IP 주소와 포트를 `IP:PORT` 형식으로 입력합니다 (예: `192.168.1.100:9001`).
- **서버 모드**: 포트 번호만 입력합니다 (예: `2575`). VitalRecorder가 수신 대기하며 장비의 연결을 기다립니다.

HL7 장비(Mindray HL7, Nihon Kohden HL7GW, BBraun HL7)는 일반적으로 MLLP 프레이밍을 사용하는 서버 모드를 사용합니다.

### UDP (네트워크)

일부 장비는 UDP로 데이터를 브로드캐스트합니다.

- 수신할 포트 번호를 입력합니다.

### BLE (Bluetooth Low Energy)

Movesense 등 무선 센서용입니다.

- Windows 10 이상 및 Bluetooth 4.0 어댑터가 필요합니다.
- 장비가 페어링 모드여야 합니다.

---

## 포트 필터링

TCP/UDP 장비 연결 시, 포트 문자열에 필터를 추가하여 연결이나 메시지를 선택적으로 수신할 수 있습니다. 구분자 기반 프레임 통신(HL7 등)에서만 동작합니다.

### 형식

```
포트#키워드@IP주소
```

포트를 제외한 모든 부분은 선택 사항입니다.

### 키워드 필터 (`#`)

수신 메시지 내에서 키워드 문자열을 검색하여 필터링합니다. 키워드가 포함되지 않은 메시지는 무시됩니다.

```
2575#BED-001
```

포트 2575에서 수신 대기하며, `BED-001`이 포함된 메시지만 처리합니다. 단일 HL7 게이트웨이(예: DoseLink, Mindray Gateway)가 하나의 연결로 여러 침상의 데이터를 전송할 때 유용합니다.

#### 다중 키워드

- **AND 조건**: 키워드 사이에 공백을 넣으면 모든 키워드가 포함된 메시지만 처리합니다.
  ```
  2575#BED-001 Propofol
  ```
- **OR 조건**: `#`을 여러 번 사용하면 어느 하나의 키워드라도 포함된 메시지를 처리합니다.
  ```
  2575#BED-001#BED-002
  ```

### IP 필터 (`@`)

수신 TCP 연결의 소스 IP 주소로 필터링합니다. 다른 IP에서의 연결은 TCP accept 단계에서 거부됩니다. IP 필터는 UDP 및 TCP 서버 모드에서만 동작합니다.

```
2575@192.168.100.22
```

포트 2575에서 수신 대기하며, `192.168.100.22`에서의 연결만 허용합니다.

#### 접미사 매칭

점(`.`) 단위로 구분된 접미사 매칭을 지원합니다. 전체 IP 주소를 입력할 필요 없이 뒷부분만 지정할 수 있습니다.

```
2575@.100.22
```

이 설정은 `xxx.xxx.100.22` 형태의 모든 IP에서의 연결을 허용합니다.

### 조합 사용

```
2575#BED-001@192.168.100.22
```

포트 2575에서 수신 대기하며, `192.168.100.22`에서의 연결만 허용하고, `BED-001`이 포함된 메시지만 처리합니다.

### 사용 예

- **BBraun DoseLink**: DoseLink의 Endpoint Filtering이 활성화된 경우, `#`을 사용하여 펌프 시리얼 번호나 침상 식별자로 필터링합니다.
- **Mindray HL7 Gateway**: 하나의 게이트웨이 포트를 공유하는 여러 침상을 침상명 키워드로 분리할 수 있습니다.
- **여러 DoseLink 서버**: `@`를 사용하여 어떤 DoseLink 서버가 어떤 VitalRecorder 탭에 연결될지 구분합니다.

### 다중 침상 HL7 게이트웨이 라우팅

하나의 HL7 게이트웨이(Mindray eGateway, BBraun DoseLink, Nihon Kohden HL7GW)가 여러 침상 데이터를 단일 TCP 연결로 전송하는 경우, VitalRecorder는 각 프레임을 자동으로 올바른 탭으로 라우팅합니다.

1. **하나의 탭만 TCP 포트를 점유**(primary)하고, 같은 포트·같은 장비 타입의 나머지 탭은 자동으로 passive subscriber로 전환됩니다. 이전 버전에서 재시작 시 수동 "Add device"를 요구했던 Windows `SO_REUSEADDR` 경쟁 문제가 원천적으로 해결됩니다.

2. **침상명 기반 라우팅 (권장)** — 각 탭의 Bed Name을 게이트웨이가 보내는 식별자와 동일하게 설정하면 필터 설정 없이 자동 매칭됩니다:
   - **Mindray**: `PV1-3` 침상 ID (예: `SU-1`, `BED-001`)
   - **Nihon Kohden**: `deviceId` JSON 필드 또는 12바이트 MFER prefix
   - **BBraun**: `MDC_ATTR_LOCATION` OBX 값의 `~` 구분자로 분리된 non-empty 토큰 중 아무거나 (예: `Forskning`, `Bord4`, `Anilab`)

3. **키워드 필터 라우팅 (대체)** — 탭 이름을 게이트웨이 식별자와 다르게 짓고 싶을 때는 위의 `포트#키워드` 문법을 사용합니다.

4. **자동 탭 생성** — 매칭되는 탭이 없고 프레임에 침상 식별자가 있으면 해당 이름으로 새 탭이 자동 생성됩니다.

5. **재시작 자동 복구** — VitalRecorder를 재시작하면 약 15초 이내에 모든 탭이 primary/subscriber 관계를 자동으로 재수립합니다. "Add device"나 "Recording" 버튼을 수동으로 누를 필요가 없습니다.

BBraun DoseLink의 경우 하나의 HL7 프레임이 하나의 rack(=한 침상)을 나타내며, rack 안의 여러 펌프는 VMD 블록으로 프레임 안에 포함되어 같은 탭의 별도 트랙(PUMP1, PUMP2, ...)으로 기록됩니다.

---

## 녹화

### 자동 녹화

기본적으로 VitalRecorder는 실행 시 자동으로 녹화를 시작합니다 (`RECORD_WHEN_START` 설정).

### 파일 형식

녹화는 트랙 기반의 압축 바이너리 형식인 `.vital` 파일로 저장됩니다.

### 저장 디렉터리

설정에서 저장 디렉터리를 지정합니다. 기본값은 사용자의 문서 폴더입니다.

### 파일명 템플릿

파일명은 템플릿으로 생성됩니다. 기본값: `%r_%y%m%d_%h%i%s`

| 코드 | 의미 |
|------|------|
| `%r` | 방/침상명 |
| `%y` | 연도 (4자리) |
| `%m` | 월 (2자리) |
| `%d` | 일 (2자리) |
| `%h` | 시 (2자리) |
| `%i` | 분 (2자리) |
| `%s` | 초 (2자리) |

---

## 서버 업로드

VitalRecorder는 WebSocket을 통해 VitalServer 인스턴스에 실시간으로 데이터를 업로드할 수 있습니다.

### 설정

| 설정 | 설명 |
|------|------|
| `SERVER_IP` | VitalServer IP 주소 또는 호스트명 |
| `SEND_WEB` | 서버 업로드 활성화/비활성화 (`1` 또는 `0`) |
| `CLOUD_UPLOAD` | 클라우드 업로드 활성화/비활성화 (`1` 또는 `0`) |
| `VRCODE` | 이 VitalRecorder 인스턴스의 고유 식별자 |

### 업로드 내용

- VitalRecorder 인스턴스의 **버전, OS, 아키텍처**.
- **설정** 및 **지원 장비 유형 목록** (부팅 후 첫 업로드 성공 시 1회 전송).
- **방 데이터**: 각 탭의 침상명, 장비 목록, 트랙 값, 파형.

데이터는 업로드 전 zlib으로 압축됩니다.

### HL7 모드

`HL7` 설정이 활성화되면 VitalRecorder는 JSON 대신 HL7 형식으로 방 데이터를 전송합니다.

---

## 설정 파일 (vr.conf)

VitalRecorder는 모든 설정을 `vr.conf`라는 단일 설정 파일에 저장합니다. 이 파일은 INI와 유사한 형식을 사용하며, 헤드리스 배포나 일괄 설정에 활용할 수 있습니다.

### 파일 위치

| 플랫폼 | 경로 |
|--------|------|
| Windows | `%APPDATA%\VitalRecorder\vr.conf` |
| Linux | `./vr.conf` > `~/vr.conf` > `/boot/vr.conf` (순서대로 검색) |

- 인코딩: UTF-8
- `--conf <경로>`로 대체 설정 파일을 지정할 수 있습니다.

### 파일 구조

```ini
# 전역 설정 (섹션 시작 전)
KEY=VALUE

# 침상(탭) 정의
[BED/침상명]

# 이 침상에 속하는 장비
[DEV/장비명]
type=장비유형
port=포트설정

# 이 침상에 속하는 필터
[FILT/필터모듈명]
```

**규칙:**
- 한 줄에 하나의 `KEY=VALUE` 쌍.
- 섹션 헤더는 `[`로 시작합니다.
- 빈 줄은 무시됩니다.
- `[DEV/...]`와 `[FILT/...]` 섹션은 앞의 `[BED/...]`에 속합니다.
- 하나의 `[BED/...]`에 여러 장비와 필터를 포함할 수 있습니다.

### 전역 설정

#### 일반

| 키 | 기본값 | 설명 |
|----|--------|------|
| `SAVEDIR` | (시스템 기본값) | 녹화 파일 저장 디렉터리 |
| `VRCODE` | (자동 생성) | VitalRecorder 고유 식별 코드 |
| `FILENAME_TEMPLATE` | `%r_%y%m%d_%h%i%s` | 녹화 파일명 템플릿 |

#### 녹화

| 키 | 기본값 | 설명 |
|----|--------|------|
| `RECORD_WHEN_START` | 1 | 실행 시 자동 녹화 (0: 끔, 1: 켬) |
| `CUT_FILE` | 1 | 환자 경계에서 파일 분할 (0: 끔, 1: 켬) |
| `CUT_HOURLY` | 0 | 매시간 파일 분할 (0: 끔, 1: 켬) |
| `CUT_BY` | (없음) | 파일 분할 트리거 신호 (예: `spo2`, `hr`, `any`) |
| `PT_WAITING_TIME` | 5 | 환자 대기 시간 (분) |

#### 서버

| 키 | 기본값 | 설명 |
|----|--------|------|
| `SERVER_IP` | (없음) | VitalDB 서버 주소 (IP:port) |
| `UPLOAD_SERVER_IP` | (없음) | 파일 업로드 서버 주소 |
| `MONITOR_SERVER_IP` | (없음) | 웹 모니터링 서버 주소 |
| `SEND_WEB` | 1 | 웹 서버로 데이터 전송 (0: 끔, 1: 켬) |
| `CLOUD_UPLOAD` | 0 | 클라우드 업로드 활성화 (0: 끔, 1: 켬) |

#### 창

| 키 | 기본값 | 설명 |
|----|--------|------|
| `START_MAXIMIZED` | 1 | 최대화 상태로 시작 |
| `START_MINIMIZED` | 0 | 최소화 상태로 시작 |
| `OPTION_MIN_TO_TRAY` | 0 | 시스템 트레이로 최소화 |
| `OPTION_ALWAYS_ON_TOP` | 0 | 항상 위에 표시 |
| `PLAY_SOUND` | 1 | 알람 소리 재생 |

#### 이벤트 프리셋

`EVT_TEXT_0`부터 `EVT_TEXT_29`까지 최대 30개의 이벤트 프리셋 라벨을 정의할 수 있습니다.

```ini
EVT_TEXT_0=Induction
EVT_TEXT_1=Intubation
EVT_TEXT_2=Incision
```

### 침상 섹션

침상(탭)을 정의합니다. 하나의 설정 파일에 여러 침상을 정의할 수 있습니다.

```ini
[BED/OR1]
```

- 침상명은 `BED/` 뒤에 옵니다 (예: `OR1`, `ICU_BED3`).
- 생략하면 VRCODE 또는 PC 호스트명으로 자동 생성됩니다.

### 장비 섹션

장비는 `[BED/...]` 섹션 아래에 추가합니다.

```ini
[DEV/장비명]
type=장비유형
port=포트설정
```

| 키 | 필수 | 설명 |
|----|------|------|
| `type` | 예 | 장비 유형 (예: `BIS`, `Intellivue`, `Solar8000`) |
| `port` | 예 | 연결 포트 (아래 포트 형식 참조) |
| `company` | 아니오 | 제조사 (예: `Nihon Kohden`) |
| `readonly` | 아니오 | 읽기 전용 모드 (0: 끔, 1: 켬) |

#### 포트 형식

| 형식 | 예시 | 설명 |
|------|------|------|
| COM 포트 | `COM1`, `COM3` | Windows 시리얼 포트 |
| TCP/IP | `192.168.1.100:4343` | 네트워크 장비 (IP:port) |
| 포트 번호 | `4343` | TCP 서버 모드 (localhost) |
| RPi 시리얼 | `F1`-`F4` | Raspberry Pi AMA 포트 |
| RPi USB | `LU`, `LU1`-`LU4` | USB 왼쪽 위 |
| RPi USB | `RU`, `RU1`-`RU4` | USB 오른쪽 위 |

#### 설정 파일에서의 포트 필터링

포트 값에 키워드 및 IP 필터를 사용할 수 있습니다 ([포트 필터링](#포트-필터링)과 동일한 문법):

```
port=포트#키워드1 키워드2#키워드3@IP접미사
```

#### ADC 장비 설정

ADC(아날로그-디지털 변환기) 장비에는 채널별 추가 설정이 있습니다:

| 키 | 설명 |
|----|------|
| `srate` | 샘플링 레이트 (Hz) |
| `parname1`, `parname2`, ... | 각 채널의 파라미터명 |
| `gain1`, `gain2`, ... | 각 채널의 전압-물리단위 변환 게인 |

```ini
[DEV/SNUADC]
type=SNUADC
port=COM3
srate=500
parname1=ECG
gain1=1.0
parname2=ART
gain2=100.0
```

### 필터 섹션

실시간 신호 처리 필터를 추가합니다. 필터 정의는 필터 서버에서 로드됩니다.

```ini
[FILT/필터모듈명]
```

- 모듈명은 서버에 등록된 필터의 `modname`과 일치해야 합니다.
- 추가 설정은 불필요합니다 (필터 파라미터는 서버에서 제공).

### 설정 예시

#### 단일 환자 감시 장치

```ini
SAVEDIR=D:\VitalData

[BED/OR1]

[DEV/Solar8000]
type=Solar8000
port=COM1
```

#### 다중 장비

```ini
SAVEDIR=D:\VitalData
VRCODE=OR1_PC

[BED/OR1]

[DEV/Intellivue]
type=Intellivue
port=192.168.1.100:4343

[DEV/BIS]
type=BIS
port=COM3

[DEV/Primus]
type=Primus
port=COM4
```

#### 다중 침상

```ini
SAVEDIR=D:\VitalData

[BED/OR1]

[DEV/Solar8000]
type=Solar8000
port=COM1

[BED/OR2]

[DEV/Philips]
type=Intellivue
port=192.168.1.101:4343
```

#### 디버그 / 테스트

```ini
SAVEDIR=C:\Users\lucid\Desktop

[BED/test]

[DEV/NK EGA]
type=EGA
company=Nihon Kohden
port=9001
```

#### 필터 포함

```ini
[BED/OR1]

[DEV/Solar8000]
type=Solar8000
port=COM1

[FILT/pleth_spi]
```

---

## 명령줄 옵션

```
vital.exe [옵션] [파일명]
```

| 옵션 | 설명 |
|------|------|
| `--version`, `-v` | 버전 번호 표시 |
| `--devtypes`, `-d` | 지원 장비 유형 전체 목록 표시 |
| `--console`, `-c` | 콘솔 모드 실행 (GUI 없음) |
| `--debug [conf]` | 디버그 모드 실행 (콘솔 모드 포함, 선택적 설정 파일 지정) |
| `--conf <경로>` | 설정 파일 경로 지정 |
| `--upgrade`, `-u` | 최신 버전으로 업그레이드 |
| `-u1.18.0` | 특정 버전으로 업그레이드 |
| `--help`, `-h` | 도움말 표시 |
| `파일명.vital` | `.vital` 파일을 열어 재생 |

### 콘솔 모드

콘솔 모드(`--console` 또는 `-c`)는 GUI 없이 VitalRecorder를 실행합니다. Raspberry Pi나 Ubuntu 서버에서 헤드리스 배포에 유용합니다. 장비는 저장된 설정에서 로드됩니다.

### 디버그 모드

디버그 모드(`--debug`)는 콘솔 모드를 포함하며, 장비 열기/닫기, 프레임 포워딩 등 상세 로그를 표준 출력으로 출력합니다. 디버그 모드에서는 실제 `.vital` 파일을 생성하지 않습니다.

```bash
# 기본 설정으로 디버그 모드 실행
vital.exe --debug

# 특정 설정 파일로 디버그 모드 실행
vital.exe --debug test_mindray.conf
```

---

## 지원 장비

지원 장비의 전체 목록과 연결 정보, 파라미터에 대해서는 [Supported Devices](../VitalRecorder/Supported_Devices.md)를 참조하십시오.

### 주요 장비 요약

| 장비 | 연결 | 포트 설정 |
|------|------|----------|
| Philips Intellivue | RS-232 | COM 포트, 115200 baud |
| GE Solar 8000 | RS-232 | COM 포트, 9600 baud |
| Nihon Kohden (시리얼) | RS-232 | COM 포트, 9600 baud |
| Nihon Kohden (HL7GW) | TCP 서버 | 포트 9001 |
| Nihon Kohden (EGA) | UDP | 포트 번호 |
| Mindray (HL7) | TCP 서버 | 포트 10000 |
| Draeger (Medibus) | RS-232 | COM 포트, 9600 baud (8N2) |
| GE Datex-Ohmeda | RS-232 | COM 포트, 19200 baud (7E1) |
| Medtronic BIS | RS-232 | COM 포트, 57600 baud |
| BBraun SpaceCom | RS-232 | COM 포트, 9600 baud |
| BBraun HL7 (DoseLink) | TCP 서버 | 포트 2575 |
| Masimo Radical-7 | RS-232 | COM 포트, 9600 baud |
| Edwards Hemosphere | RS-232 | COM 포트, 9600 baud |
| Hamilton 인공호흡기 | RS-232 | COM 포트, 38400 baud |

---

## 문제 해결

### 장비가 연결되지 않는 경우

1. **RS-232**: 올바른 COM 포트가 선택되었는지 확인합니다. 장치 관리자에서 포트 번호를 확인하십시오. USB-to-Serial 드라이버가 설치되어 있는지 확인합니다.
2. **TCP 서버 모드**: 방화벽이 지정된 포트의 수신 연결을 허용하는지 확인합니다.
3. **TCP 클라이언트 모드**: 장비 IP 주소에 접근 가능한지 확인합니다 (`ping` 테스트).

### 데이터가 표시되지 않는 경우

- 일부 장비는 장비 측에서 별도 설정이 필요합니다 (예: Draeger 서비스 메뉴에서 RS-232 출력 활성화, Philips Intellivue에서 MIB 출력 활성화).
- 전송 속도 및 시리얼 파라미터가 장비 설정과 일치하는지 확인합니다.
- `--debug` 모드를 사용하여 통신을 확인합니다.

### 동일 포트의 다중 장비

하나의 게이트웨이 포트를 공유하는 HL7 장비의 경우, [포트 필터링](#포트-필터링) 기능의 `#` 키워드를 사용하여 침상을 분리합니다.

### BBraun HL7 다중 펌프

BBraun DoseLink는 단일 TCP 연결로 여러 펌프의 데이터를 전송합니다. VitalRecorder는 OBX-18(장비 인스턴스 식별자)의 시리얼 번호를 사용하여 각 펌프를 자동으로 구분하고 PUMP1부터 PUMP8까지 매핑합니다.

펌프가 올바르게 분리되지 않는 경우:
- `--debug` 모드를 사용하여 로그를 확인합니다.
- 원시 HL7 메시지의 OBX-18 값을 확인합니다.
- DoseLink Endpoint Filtering을 사용하는 경우, 필요시 `#` 키워드 필터를 사용합니다.

### 서버 업로드가 동작하지 않는 경우

- `SERVER_IP`가 올바르게 설정되었는지 확인합니다.
- `SEND_WEB`이 `1`로 설정되어 있는지 확인합니다.
- 서버와의 네트워크 연결을 확인합니다.
- 설정 및 장비 유형 목록은 부팅 후 첫 업로드 성공 시 전송됩니다. 활성 장비 없이 VitalRecorder가 부팅되면 장비 연결 시까지 초기 업로드가 지연될 수 있습니다.
