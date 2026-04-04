# VitalRecorder 지원 장비 목록

VitalRecorder에서 지원하는 장비의 전체 목록입니다.
연결 인터페이스, 통신 설정, 수집 파라미터를 포함합니다.

---

## 목차

1. [VitalDB 전용 장비](#1-vitaldb-전용-장비)
2. [아날로그-디지털 변환기 (ADC)](#2-아날로그-디지털-변환기-adc)
3. [환자 모니터](#3-환자-모니터)
4. [다기능 모니터](#4-다기능-모니터)
5. [마취기](#5-마취기)
6. [기계환기기 (인공호흡기)](#6-기계환기기-인공호흡기)
7. [약물 주입 펌프](#7-약물-주입-펌프)
8. [뇌 모니터](#8-뇌-모니터)
9. [신경근 모니터](#9-신경근-모니터)
10. [수액 주입기](#10-수액-주입기)
11. [심장 모니터](#11-심장-모니터)
12. [태아 모니터](#12-태아-모니터)
13. [연구용 장비](#13-연구용-장비)

---

## 연결 방식 범례

| 기호 | 설명 |
|------|------|
| RS-232 | 직렬 포트 (COM 포트 / USB-Serial 변환기) |
| TCP | 네트워크 TCP 소켓 |
| UDP | 네트워크 UDP 소켓 |
| BLE | Bluetooth Low Energy |

---

## 1. VitalDB 전용 장비

| 장비명 | 제조사 | 인터페이스 | 주요 파라미터 |
|--------|--------|-----------|--------------|
| SNUADC | VitalDB | RS-232, 57600 baud | 8채널 아날로그 입력 (12-bit, 500 Hz) |
| SNUADCM | VitalDB | RS-232, 57600 baud | 다채널 ADC (SNUADC 확장형) |
| BUTTON | VitalDB | RS-232, 57600 baud | 이벤트 버튼 입력 |
| VitalBOLUS | VitalDB | RS-232 | 볼루스(일시투여) 이벤트 기록 |

---

## 2. 아날로그-디지털 변환기 (ADC)

DataQ Instruments 의 USB ADC 장비를 지원합니다.
USB로 연결되며, 드라이버 설치 후 VirtualCOM 포트로 인식됩니다.

| 장비명 | 제조사 | 채널 수 | 분해능 | 최대 샘플링 | 비고 |
|--------|--------|--------|--------|------------|------|
| DI-149 | DataQ | 8채널 | 10-bit | 1,000 Hz | 저가형 기본 모델 |
| DI-155 | DataQ | 4채널 | 14-bit | 10,000 Hz | 고분해능 |
| DI-245 | DataQ | 2채널 | 14-bit | 2,000 Hz | 아이솔레이션 지원 |
| DI-1100 | DataQ | 4채널 | 12-bit | 10,000 Hz | |
| DI-1120 | DataQ | 4채널 | 14-bit | 10,000 Hz | 고분해능 확장형 |

---

## 3. 환자 모니터

### Philips

| 장비명 | 인터페이스 | 통신 설정 | 주요 파라미터 |
|--------|-----------|----------|--------------|
| Intellivue (MX/MP 시리즈) | RS-232 | 115200 baud | ECG, PLETH, ABP, CVP, CO2, RESP, SpO2, NIBP, Temp |
| VueLink | RS-232 | 115200 baud | Intellivue와 동일 (외부 VueLink 모듈 경유) |

> **연결 방법**: 장비 후면의 MIB/RS-232 포트 또는 VueLink 모듈에 RS-232 케이블 연결.
> Intellivue의 경우 장비 메뉴에서 MIB 출력을 활성화해야 합니다.

### GE Healthcare

| 장비명 | 인터페이스 | 통신 설정 | 주요 파라미터 |
|--------|-----------|----------|--------------|
| Solar 8000 / Solar 8000M | RS-232 | 9600 baud | ECG, NIBP, SpO2, Temp, Resp, IBP |
| Dash 2500 / 4000 | RS-232 | 9600 baud | ECG, NIBP, SpO2, Temp, Resp, IBP |
| Bx50 | RS-232 | 9600 baud | ECG, NIBP, SpO2, Temp, IBP |
| B105M / B125M | RS-232 | 9600 baud | ECG, NIBP, SpO2, Temp, IBP |
| GE Canvas | RS-232 | 9600 baud | ECG, NIBP, SpO2, Temp, IBP |
| MPS (Dash 2500) | RS-232 | 9600 baud | ECG, PLETH 파형, NIBP, SpO2 |

### Draeger

| 장비명 | 인터페이스 | 통신 설정 | 주요 파라미터 |
|--------|-----------|----------|--------------|
| Infinity (Delta/Kappa/Gamma) | RS-232 | 19200 baud | ECG, NIBP, SpO2, Temp, IBP, CO2 |

### Nihon Kohden

| 장비명 | 인터페이스 | 통신 설정 | 주요 파라미터 |
|--------|-----------|----------|--------------|
| BSM 시리즈 (Serial) | RS-232 | 9600 baud | ECG, NIBP, SpO2, Temp, IBP |
| BSM 시리즈 (EGA) | UDP | 네트워크 | 파형 + 수치 데이터 |
| BSM 시리즈 (ADT) | TCP | 9007 포트 | 환자 정보 (입퇴원) |
| BSM 시리즈 (HL7 GW) | TCP | 9001 포트 | HL7 v2 게이트웨이 |
| BSM 시리즈 (HL7 GN) | TCP | 7999 포트 | HL7 v2 확장 게이트웨이 |

### MEKICS

| 장비명 | 인터페이스 | 통신 설정 | 주요 파라미터 |
|--------|-----------|----------|--------------|
| MEKICS 환자모니터 | TCP | 6002 포트 | ECG, Resp, SpO2, IBP, ETCO2, 마취가스 |

---

## 4. 다기능 모니터

| 장비명 | 제조사 | 인터페이스 | 통신 설정 | 주요 파라미터 |
|--------|--------|-----------|----------|--------------|
| Radical-7 | Masimo | RS-232 | 9600 baud | SpO2, PR, PVI, PI, SpHb, SpMet |
| Root (NIBP 포함) | Masimo | RS-232 | 19200 baud | SpO2, PR, NIBP, PVI, SpHb, SpCO |
| SDM (SenTec) | Sentec | RS-232 | 115200 baud | SpO2, PCO2, PO2, PR, PI (경피 측정) |

---

## 5. 마취기

| 장비명 | 제조사 | 인터페이스 | 통신 설정 | 주요 파라미터 |
|--------|--------|-----------|----------|--------------|
| Primus / Zeus / Fabius | Draeger | RS-232 | 9600 baud (8,2) | AWP, AWF, FiO2, EtCO2, MAC, TV, MV |
| Primus IE / Perseus (Medibus X) | Draeger | RS-232 | 19200 baud (8,2) | AWP, AWF, FiO2, EtCO2, MAC, TV, MV (확장) |
| Aisys / Avance / Aestiva | GE Datex-Ohmeda | RS-232 | 19200 baud (7,1) | Paw, Pplat, EtCO2, TV, MV, FiO2 |
| Flowi | Maquet | RS-232 | — | 유량 측정 |

> **주의**: Draeger Primus/Zeus는 Medibus 프로토콜을 사용합니다.
> 장비의 Service 메뉴에서 RS-232 출력을 활성화하고, Communication 설정을 Medibus로 맞춰야 합니다.

---

## 6. 기계환기기 (인공호흡기)

| 장비명 | 제조사 | 인터페이스 | 통신 설정 | 주요 파라미터 |
|--------|--------|-----------|----------|--------------|
| SERVO-i / SERVO-s | Maquet | RS-232 | 9600 baud | Paw, PEEP, TV, MV, RR, FiO2 |
| SERVO-U | Maquet | RS-232 | 19200 baud | Paw, PEEP, TV, MV, RR, FiO2 (확장) |
| MR1 / C2 / C6 / T1 | Hamilton Medical | RS-232 | 38400 baud (STX/ETX) | Paw, PEEP, Pplat, TV, MV, RR, FiO2, CO2 |

---

## 7. 약물 주입 펌프

| 장비명 | 제조사 | 인터페이스 | 통신 설정 | 주요 파라미터 |
|--------|--------|-----------|----------|--------------|
| Agilia / Link+ | Fresenius Kabi | RS-232 | 115200 baud | 주입량, 주입속도, 알람 상태 |
| Primea (Orchestra) | Fresenius Kabi | RS-232 | 19200 baud | 주입량, 주입속도, 알람 상태 |
| PCBM | Fresenius Kabi | RS-232 | 19200 baud (7,2) | 다모듈 펌프 상태 (ENQ/ACK 프로토콜) |
| SpaceCom | BBraun | RS-232 | 9600 baud | 주입량, 주입속도, 약물명 |
| DS-5000 | Daiwha | RS-232 | 57600 baud | 주입량, 주입속도 |
| Pion | Bionet | RS-232 | 115200 baud | 주입량, 주입속도 |
| Link 4 | — | RS-232 | — | 링크 채널 4개 펌프 상태 |

---

## 8. 뇌 모니터

### EEG / 마취 심도

| 장비명 | 제조사 | 인터페이스 | 통신 설정 | 주요 파라미터 |
|--------|--------|-----------|----------|--------------|
| BISx (BIS 단채널) | Medtronic | RS-232 | 57600 baud | BIS, EMG, SQI, SR, EEG 파형 |
| A2000 (BIS 256Hz) | Medtronic | RS-232 | 57600 baud | BIS, EMG, SQI, SR, EEG 파형 (고해상도) |
| VISTA (BIS 4채널) | Medtronic | RS-232 | 57600 baud | BIS×4, EMG, SQI, SR, EEG 파형 (4채널) |
| Conox | Fresenius Kabi | RS-232 | 9600 baud | qCON, qNOX, EEG 지수 |

### 진통 모니터

| 장비명 | 제조사 | 인터페이스 | 통신 설정 | 주요 파라미터 |
|--------|--------|-----------|----------|--------------|
| ANIMonitor | MDMS | RS-232 | — | ANI (자율신경 진통 지수) |
| ANIMonitor 2 | MDMS | RS-232 | 115200 baud | ANI, HRV 지수 |

### 뇌 산소포화도 / 혈역학

| 장비명 | 제조사 | 인터페이스 | 통신 설정 | 주요 파라미터 |
|--------|--------|-----------|----------|--------------|
| INVOS 5100C | Medtronic | RS-232 | — | rSO2 (좌/우 뇌 산소포화도) |
| NirsitON | OBELAB | RS-232 | 115200 baud | RSO2, HbO2, HbR, CCO, NIRS 파형 |
| PLEM100 | Inbody | RS-232 | 230400 baud | 체임피던스 기반 뇌혈역학 지수 |
| CAIS | — | RS-232 | — | 뇌 자율신경 지수 (연구용) |

---

## 9. 신경근 모니터

| 장비명 | 제조사 | 인터페이스 | 통신 설정 | 주요 파라미터 |
|--------|--------|-----------|----------|--------------|
| TwitchView | BlinkDC | RS-232 | 19200 baud | TOF 비율, T1~T4, PTC |
| TOFScan | IDMed | RS-232 | 19200 baud | TOF 비율, T1~T4, PTC |
| TOFcuff | RGB Medical | RS-232 | 38400 baud | TOF 비율, T1~T4 (자동 커프 방식) |

---

## 10. 수액 주입기

| 장비명 | 제조사 | 인터페이스 | 통신 설정 | 주요 파라미터 |
|--------|--------|-----------|----------|--------------|
| FMS 2000 | Belmont Instrument | RS-232 | 19200 baud | 주입속도, 주입온도, 총 주입량, 알람 |

---

## 11. 심장 모니터

### Edwards Lifesciences

| 장비명 | 인터페이스 | 통신 설정 | 주요 파라미터 |
|--------|-----------|----------|--------------|
| Vigilance II / Vigilance C | RS-232 | 9600 baud (STX/ETX) | CO, CI, SvO2, SVO2, HR, Temp |
| Hemosphere | RS-232 | 9600 baud (STX/ETX) | CO, CI, SV, SVR, DO2, CCO |
| EV1000 | RS-232 | 9600 baud (STX/ETX) | CO, CI, SV, SVV, PPV, SVR |
| ClearSight (비침습) | RS-232 | 9600 baud (STX/ETX) | CO, CI, SV, SVV, MAP, HR (비침습) |
| Vigileo (FloTrac) | RS-232 | 9600 baud (STX/ETX) | CO, CI, SV, SVV, SVR |

### 기타 심장 모니터

| 장비명 | 제조사 | 인터페이스 | 통신 설정 | 주요 파라미터 |
|--------|--------|-----------|----------|--------------|
| PulsioFlex (PiCCO) | Getinge | RS-232 | 19200 baud (8,2) | CO, CI, SV, SVV, PPV, SVRI, EVLWI |
| CardioQ | Deltex | RS-232 | 57600 baud | CO, SV, FTc, MA, PV, FLOW 파형 |
| LiDCOrapid | LiDCO | RS-232 | 57600 baud (STX/ETX) | CO, CI, SV, SVV, MAP, HR |
| AirTom | Bilab | RS-232 | 115200 baud | CO, CI, SV, SVV, SBP, DBP, MAP, SpO2 |
| HemoVista | Bilab | RS-232 | 115200 baud | AirTom과 동일 (HemoVista 기종) |
| CW10 | Edgecare | RS-232 | 115200 baud (MLLP/HL7) | VTIc, VTIf, HRc, HRf, FTcc, FTcf, eSVc, eSVf, eSVVc, eSVVf, BFc, BFf, BFc+f, DPTT, B-line |
| Movesense | Movesense | Bluetooth LE | — | ECG, 가속도, 심박수 (웨어러블) |

#### Edgecare CW10 파라미터 상세

| 파라미터 | 단위 | 설명 |
|---------|------|------|
| VTIc | cm | Velocity Time Integral — 경동맥 |
| VTIf | cm | Velocity Time Integral — 대퇴동맥 |
| HRc | bpm | 심박수 — 경동맥 기반 |
| HRf | bpm | 심박수 — 대퇴동맥 기반 |
| FTcc | ms | 보정 혈류 시간 — 경동맥 |
| FTcf | ms | 보정 혈류 시간 — 대퇴동맥 |
| eSVc | mL/beat | 일회박출량 — 경동맥 |
| eSVf | mL/beat | 일회박출량 — 대퇴동맥 |
| eSVVc | % | 일회박출량 변이 — 경동맥 |
| eSVVf | % | 일회박출량 변이 — 대퇴동맥 |
| BFc | L/min | 혈류량 — 경동맥 |
| BFf | L/min | 혈류량 — 대퇴동맥 |
| BFc+f | L/min | 총 혈류량 (경동맥 + 대퇴동맥) |
| DPTT | ms | 맥파 전달 시간 차이 |
| B-line | EA | B-라인 수 (폐부종 지표) |

---

## 12. 태아 모니터

| 장비명 | 제조사 | 인터페이스 | 통신 설정 | 주요 파라미터 |
|--------|--------|-----------|----------|--------------|
| Corometrics 250cx | GE Healthcare | RS-232 | 9600 baud | FHR (태아 심박수), MHR (모성 심박수), TOCO |

---

## 13. 연구용 장비

| 장비명 | 제조사 | 인터페이스 | 설명 |
|--------|--------|-----------|------|
| IAP (Serial) | VitalDB | RS-232 | 침습적 동맥압 연구용 파형 수집 |
| IAP (Radical7) | VitalDB | RS-232 | Masimo Radical7 연동 IAP 수집 |
| IAP (TCP) | VitalDB | TCP | 네트워크 기반 IAP 수집 |
| IAP (Official) | VitalDB | — | 공식 IAP 프로토콜 |
| AU | — | RS-232 | 범용 직렬 입력 |
| Laxtha | Laxtha | RS-232 | EEG/EMG/ECG 다채널 생체신호 |
| SKNA | — | RS-232 | 피부 교감신경 활동 (SKNA) |
| SNUPATCH | VitalDB | — | 패치형 생체신호 센서 |
| SNUECG | VitalDB | — | 연구용 ECG 수집 모듈 |
| SNUEEG | VitalDB | — | 연구용 EEG 수집 모듈 |

---

## 연결 설정 빠른 참조

### RS-232 (COM 포트) 연결 시 공통 사항

- USB-to-Serial 변환기 사용 시 해당 드라이버를 먼저 설치하세요.
- VitalRecorder의 장비 추가 화면에서 COM 포트 번호를 선택합니다.
- 장비별 baud rate는 위 표를 참고하며, 나머지 설정(data bit, parity, stop bit)은 장비 페이지에서 확인하세요.

### 네트워크 (TCP/UDP) 연결 시 공통 사항

- VitalRecorder가 실행되는 PC와 장비가 같은 네트워크에 있어야 합니다.
- 장비의 IP 주소와 포트 번호를 VitalRecorder 설정에 입력합니다.
- 방화벽 예외 설정이 필요할 수 있습니다.

### Port Name 필터링 (TCP/UDP Framed 통신 전용)

Port Name에 `#`과 `@`를 사용하여 수신 데이터를 필터링할 수 있습니다. 이 기능은 구분자에 의해 프레임이 나뉘는 Framed 통신(HL7 등 TCP 일부, UDP)에서만 동작하며, 바이너리 프로토콜이나 RS-232 시리얼 통신에서는 동작하지 않습니다.

**형식**: `포트명#검색어@IP주소`

- **`#` (키워드 필터)**: `#` 뒤의 검색어가 포함된 프레임만 수신합니다.
  - 띄어쓰기로 구분된 키워드는 **AND** 조건입니다 (모든 키워드가 포함되어야 통과).
  - `#`을 여러 번 사용하면 **OR** 조건입니다 (하나의 그룹만 매칭되면 통과).
- **`@` (IP 필터, UDP/TCP Server 전용)**: `@` 뒤의 IP 주소에서 수신된 데이터만 처리합니다. UDP와 TCP Server 모드에서만 동작하며, RS-232 시리얼 등에서는 무시됩니다. 숫자와 `.`만 허용됩니다. `.` 단위 postfix matching을 지원하므로 IP 주소의 뒷부분만 입력해도 됩니다 (예: `@10.1`은 `192.168.10.1`과 매칭되지만 `192.168.110.1`과는 매칭되지 않음).

**예시**:

| Port Name | 의미 |
|---|---|
| `7001#PV1` | 7001 포트, "PV1" 포함된 프레임만 수신 |
| `7001#PV1 ICU` | 7001 포트, "PV1" **AND** "ICU" 모두 포함된 프레임만 수신 |
| `7001#PV1#MSH` | 7001 포트, "PV1" **OR** "MSH" 포함된 프레임 수신 |
| `7001#PV1 ICU#MSH` | 7001 포트, ("PV1" AND "ICU") **OR** "MSH" |
| `7001@192.168.0.1` | 7001 포트, 192.168.0.1에서 온 데이터만 처리 |
| `7001@10.1` | 7001 포트, x.x.10.1에서 온 데이터만 처리 (postfix matching) |
| `7001#PV1@192.168.0.1` | 키워드 필터와 IP 필터 동시 사용 |

### Bluetooth LE (BLE) 연결 시 공통 사항

- Windows 10 이상, Bluetooth 4.0 이상의 어댑터가 필요합니다.
- 장비를 페어링 모드로 설정 후 VitalRecorder에서 검색합니다.

### 콘솔 모드 및 디버깅

VitalRecorder는 GUI 없이 콘솔 모드로 실행할 수 있습니다. 커맨드라인 옵션:

| 옵션 | 설명 |
|---|---|
| `--console`, `-c` | GUI 없이 콘솔 모드로 실행 (정상 녹화) |
| `--debug [conf]` | 콘솔 + 디버그 모드 (vital 파일 생성 안함, 뒤에 vr.conf 경로 지정 가능) |
| `--conf <path>` | 지정된 vr.conf 파일 사용 |
| `--help`, `-h` | 사용법 출력 |

**사용 예시**:

```bash
# 콘솔 모드로 실행 (GUI 없이 녹화)
Vital.exe --console

# 콘솔 모드로 특정 설정 파일 사용
Vital.exe --console --conf custom.conf

# 디버그 모드 (기본 vr.conf 사용)
Vital.exe --debug

# 디버그 모드 + 테스트용 설정 파일
Vital.exe --debug test_mindray.conf
```

디버그 모드에서는 다음 정보가 출력되며, vital 파일은 생성되지 않습니다:

| 출력 | 의미 |
|---|---|
| `[+tab] BED-001` | 탭 생성 |
| `[+dev] HL7 -> BED-001` | 장비 추가 |
| `[+trk] HR -> BED-001` | 트랙 추가 |
| `[fwd] HL7 -> HL7` | 프레임 포워딩 |
| `[BED-001] HL7/HR = 72.00` | 데이터 수신 |
