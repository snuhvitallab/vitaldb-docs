# VitalRecorder 설정 파일 (vr.conf) 가이드

VitalRecorder는 `vr.conf` 파일을 통해 장비, 베드, 필터 등의 설정을 관리합니다.
이 문서는 설정 파일의 구조와 작성 방법을 설명합니다.

---

## 목차

1. [파일 위치](#1-파일-위치)
2. [파일 구조](#2-파일-구조)
3. [전역 설정](#3-전역-설정)
4. [베드 섹션](#4-베드-섹션)
5. [장비 섹션](#5-장비-섹션)
6. [필터 섹션](#6-필터-섹션)
7. [명령줄 옵션](#7-명령줄-옵션)
8. [설정 예시](#8-설정-예시)

---

## 1. 파일 위치

| 플랫폼 | 경로 |
|---------|------|
| Windows | `%APPDATA%\VitalRecorder\vr.conf` |
| Linux | `./vr.conf` → `~/vr.conf` → `/boot/vr.conf` (순서대로 탐색) |

- 인코딩: UTF-8
- 명령줄에서 `--conf <경로>` 옵션으로 다른 설정 파일을 지정할 수 있습니다.

---

## 2. 파일 구조

INI 형식을 따르며, 전역 설정과 섹션으로 구성됩니다.

```ini
# 전역 설정 (파일 최상단)
KEY=VALUE

# 베드 (탭) 정의
[BED/베드이름]

# 해당 베드에 속한 장비
[DEV/장비이름]
type=장비타입
port=포트

# 해당 베드에 속한 필터
[FILT/필터모듈이름]
```

**규칙:**
- 한 줄에 하나의 `KEY=VALUE` 쌍
- 섹션 헤더는 `[` 로 시작
- 빈 줄은 무시됨
- `[BED/...]` 아래에 `[DEV/...]`, `[FILT/...]` 섹션이 속함
- 하나의 `[BED/...]` 에 여러 장비와 필터를 추가할 수 있음

---

## 3. 전역 설정

`[BED/...]` 섹션 이전에 작성하는 설정입니다.

### 기본 설정

| 키 | 기본값 | 설명 |
|----|--------|------|
| `SAVEDIR` | (시스템 기본) | 녹화 파일 저장 디렉토리 |
| `VRCODE` | (자동 발급) | VitalRecorder 식별 코드 |
| `DEBUG` | 0 | 디버그 모드 (0: 끔, 1: 켬) |
| `FILENAME_TEMPLATE` | `%r_%y%m%d_%h%i%s` | 녹화 파일명 템플릿 |

### 녹화 설정

| 키 | 기본값 | 설명 |
|----|--------|------|
| `RECORD_WHEN_START` | 1 | 시작 시 자동 녹화 (0: 끔, 1: 켬) |
| `CUT_FILE` | 1 | 환자 경계에서 파일 분할 (0: 끔, 1: 켬) |
| `CUT_HOURLY` | 0 | 매시간 파일 분할 (0: 끔, 1: 켬) |
| `CUT_BY` | (없음) | 파일 분할 기준 신호 (예: `spo2`, `hr`, `any`) |
| `PT_WAITING_TIME` | 5 | 환자 대기 시간 (분) |

### 서버 설정

| 키 | 기본값 | 설명 |
|----|--------|------|
| `SERVER_IP` | (없음) | VitalDB 서버 주소 (IP:포트) |
| `UPLOAD_SERVER_IP` | (없음) | 파일 업로드 서버 주소 |
| `MONITOR_SERVER_IP` | (없음) | 웹 모니터링 서버 주소 |
| `SEND_WEB` | 1 | 웹 서버로 데이터 전송 (0: 끔, 1: 켬) |
| `CLOUD_UPLOAD` | 0 | 클라우드 업로드 (0: 끔, 1: 켬) |

### 창 설정

| 키 | 기본값 | 설명 |
|----|--------|------|
| `START_MAXIMIZED` | 1 | 최대화 상태로 시작 |
| `START_MINIMIZED` | 0 | 최소화 상태로 시작 |
| `OPTION_MIN_TO_TRAY` | 0 | 최소화 시 트레이로 이동 |
| `OPTION_ALWAYS_ON_TOP` | 0 | 항상 위에 표시 |
| `PLAY_SOUND` | 1 | 알람 소리 재생 |

### 이벤트 프리셋

`EVT_TEXT_0` ~ `EVT_TEXT_29` 로 최대 30개의 이벤트 프리셋 텍스트를 지정할 수 있습니다.

```ini
EVT_TEXT_0=Induction
EVT_TEXT_1=Intubation
EVT_TEXT_2=Incision
```

---

## 4. 베드 섹션

베드(탭)를 정의합니다. 하나의 설정 파일에 여러 베드를 정의할 수 있습니다.

```ini
[BED/OR1]
```

- 베드 이름은 `BED/` 뒤에 지정 (예: `OR1`, `ICU_BED3`)
- 지정하지 않으면 VRCODE 또는 PC 호스트명을 사용하여 자동 생성

---

## 5. 장비 섹션

`[BED/...]` 아래에 장비를 추가합니다.

### 기본 설정

```ini
[DEV/장비이름]
type=장비타입
port=포트
```

| 키 | 필수 | 설명 |
|----|------|------|
| `type` | O | 장비 타입 (예: `BIS`, `Intellivue`, `Solar8000`) |
| `port` | O | 연결 포트 (아래 포트 형식 참조) |
| `company` | | 제조사 (예: `Nihon Kohden`) |
| `readonly` | | 읽기 전용 모드 (0: 끔, 1: 켬) |

### 포트 형식

| 형식 | 예시 | 설명 |
|------|------|------|
| COM 포트 | `COM1`, `COM3` | Windows 시리얼 포트 |
| TCP/IP | `192.168.1.100:4343` | 네트워크 장비 (IP:포트) |
| 포트 번호 | `4343` | localhost TCP 포트 |
| RPi 시리얼 | `F1`~`F4` | Raspberry Pi AMA 포트 |
| RPi USB | `LU`, `LU1`~`LU4` | USB Left Upper |
| RPi USB | `RU`, `RU1`~`RU4` | USB Right Upper |

### 포트 필터링

포트 값에 키워드/IP 필터를 추가할 수 있습니다.

```
port=포트#키워드1 키워드2#키워드3@IP접미사
```

| 구분자 | 설명 |
|--------|------|
| `#` | 키워드 OR 그룹 구분 |
| (공백) | 같은 `#` 그룹 내 AND 조건 |
| `@` | IP 주소 접미사 필터 |

예시:
- `COM1#BIS` — COM1에서 "BIS" 키워드 포함 프레임만 수신
- `4343#HR SpO2#BP` — "HR AND SpO2" 또는 "BP" 포함 프레임
- `4343@10.1` — IP가 10.1로 끝나는 연결만

### ADC 장비 추가 설정

ADC (아날로그-디지털 변환기) 장비일 경우 채널별 설정을 추가합니다.

| 키 | 설명 |
|----|------|
| `srate` | 샘플링 레이트 (Hz) |
| `parname1`, `parname2`, ... | 각 채널의 파라미터 이름 |
| `gain1`, `gain2`, ... | 각 채널의 전압→물리단위 변환 계수 |

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

---

## 6. 필터 섹션

실시간 신호 처리 필터를 추가합니다. 필터 목록은 필터 서버에서 자동으로 로드됩니다.

```ini
[FILT/필터모듈이름]
```

- 모듈 이름은 서버에 등록된 필터의 `modname` 값입니다.
- 추가 설정은 필요하지 않습니다 (필터 정의는 서버에서 제공).

---

## 7. 명령줄 옵션

```
vr --conf <경로>         설정 파일 경로 지정
vr --console             GUI 없이 콘솔 모드로 실행
vr --debug               콘솔 + 디버그 모드
vr --debug test.conf     디버그 모드로 지정 설정 파일 사용
vr --version             버전 정보 출력
vr --devtypes            지원 장비 타입 목록 출력
vr --help                도움말 출력
```

---

## 8. 설정 예시

### 기본 구성: 환자 모니터 1대

```ini
SAVEDIR=D:\VitalData

[BED/OR1]

[DEV/Solar8000]
type=Solar8000
port=COM1
```

### 여러 장비 구성

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

### 다중 베드 구성

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

### 디버그/테스트용

```ini
SAVEDIR=C:\Users\lucid\Desktop
DEBUG=1

[BED/test]

[DEV/NK EGA]
type=EGA
company=Nihon Kohden
port=9001
```

### 필터 포함 구성

```ini
[BED/OR1]

[DEV/Solar8000]
type=Solar8000
port=COM1

[FILT/pleth_spi]
```
