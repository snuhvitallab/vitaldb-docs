# VitalServer HL7 v2 Protocol Specification

VitalRecorder가 demo.vitaldb.net 서버로 실시간 바이탈 데이터를 전송하는 HL7 v2 프로토콜 스펙.
오픈 데이터셋 서비스를 위해 서버에서 동일한 형식의 데이터를 클라이언트에 제공할 때도 이 스펙을 따른다.

---

## 1. 통신 방식

| 항목 | 값 |
|------|-----|
| Protocol | WebSocket (RFC 6455) over TLS |
| Port | 443 (WSS) |
| Path | `/socket.io/?EIO=3&transport=websocket` |
| Application Layer | Engine.IO v3 / Socket.IO |
| Data Format | HL7 v2.6 (UTF-8) |
| Compression | gzip (zlib) |

---

## 2. 연결 절차

### 2.1 WebSocket 연결 및 Socket.IO 핸드셰이크

```
Client → Server  [WS Upgrade]
Client → Server  "40"                        ← engine.io MESSAGE(4) + socket.io CONNECT(0)
Server → Client  [확인 프레임]
Client → Server  42["join_vr","<vrcode>"]    ← socket.io EVENT: 방 입장
```

`vrcode`는 VitalRecorder 기기 고유 식별자(예: `VR_ABC123`).

### 2.2 데이터 전송 루프 (1초 주기)

```
Client → Server  451-["send_data",{"_placeholder":true,"num":0}]   ← text 프레임, binary 첨부 예고
Client → Server  [binary 프레임] = 0x04 + gzip(HL7_payload)        ← binary 프레임
```

- 첫 번째 프레임: `451-[...]` 형식으로 binary attachment를 예고
  - `4` = engine.io MESSAGE, `5` = socket.io BINARY_EVENT, `1-` = 1개의 binary 첨부
- 두 번째 프레임: `0x04` (attachment 헤더 1 byte) + gzip 압축된 HL7 텍스트 payload

### 2.3 Ping/Pong (연결 유지)

```
Server → Client  "2"    ← engine.io PING
Client → Server  "3"    ← engine.io PONG
```

### 2.4 서버 → 클라이언트 명령

서버는 socket.io EVENT(`42[...]`) 형식으로 다음 명령을 전송할 수 있다:

| 명령 | 파라미터 | 설명 |
|------|----------|------|
| `update` | — | 소프트웨어 업데이트 |
| `restart` | — | 재시작 |
| `dt` | `<unix_timestamp>` | 시간 동기화 |
| `del_bed` | `"<bedname>"` | 병상 삭제 |
| `new_bed` | `"<bedname>"` | 병상 추가 |
| `edit_bed` | `"{...}"` (JSON 문자열) | 병상 설정 변경 |

---

## 3. HL7 v2 메시지 구조

각 전송 payload는 하나 이상의 HL7 메시지를 이어붙인 텍스트이다 (병상별 메시지 연속 전송).

### 3.1 세그먼트 구분자

| 구분자 | 값 | 설명 |
|--------|-----|------|
| 세그먼트 종료 | `\r` (0x0D) | HL7 표준 CR |
| 필드 | `\|` | Field separator |
| 컴포넌트 | `^` | Component separator |
| 반복 | `~` | Repeat separator |
| 이스케이프 | `\\` | Escape character |
| 서브컴포넌트 | `&` | Sub-component separator |

### 3.2 메시지 전체 구조

```
MSH|^~\&|VitalRecorder|<vrcode>|||<datetime>||ORU^R01|<seq>|P|2.6\r
PID|||<patient_id>\r
PV1||I|<bedname>\r
OBR|1|||VITAL_SIGNS|||<from>|<to>\r
OBX|1|<type>|<code>^<identifier>||<value(s)>|<unit>|<refrange>||||R\r
OBX|2|...\r
...
```

---

## 4. 세그먼트 상세

### 4.1 MSH (Message Header)

| 필드 | 예시 | 설명 |
|------|------|------|
| MSH-3 | `VitalRecorder` | 송신 애플리케이션 |
| MSH-4 | `VR_ABC123` | 송신 기기 vrcode |
| MSH-7 | `20250323143000` | 메시지 생성 시각 (YYYYMMDDHHmmss) |
| MSH-9 | `ORU^R01` | 메시지 타입: 관측 결과 |
| MSH-10 | `12345` | 메시지 일련번호 (단조 증가) |
| MSH-11 | `P` | Processing ID: Production |
| MSH-12 | `2.6` | HL7 버전 |

### 4.2 PID (Patient Identification)

| 필드 | 예시 | 설명 |
|------|------|------|
| PID-3 | `PT-001` | 환자 ID (없으면 빈 문자열) |

### 4.3 PV1 (Patient Visit)

| 필드 | 예시 | 설명 |
|------|------|------|
| PV1-2 | `I` | Patient Class: Inpatient |
| PV1-3 | `OR-1` | 병상/방 이름 |

### 4.4 OBR (Observation Request)

| 필드 | 예시 | 설명 |
|------|------|------|
| OBR-1 | `1` | Set ID |
| OBR-4 | `VITAL_SIGNS` | 관측 식별자 |
| OBR-7 | `20250323143000` | 관측 시작 시각 |
| OBR-8 | `20250323143001` | 관측 종료 시각 |

### 4.5 OBX (Observation Result)

```
OBX|<set_id>|<value_type>|<observation_id>||<observation_value>|<units>|<refrange>||||R
```

| 필드 | 위치 | 설명 |
|------|------|------|
| OBX-1 | Set ID | 1부터 순차 증가 |
| OBX-2 | Value Type | `NM` (숫자), `NA` (숫자 배열/파형), `ST` (문자열) |
| OBX-3 | Observation ID | `<code>^<device>/<track>[@<srate>]` |
| OBX-5 | Observation Value | 값 (타입별 형식 참조) |
| OBX-6 | Units | 단위 문자열 (예: `bpm`, `mmHg`, `mV`) |
| OBX-7 | Reference Range | `<mindisp>^<maxdisp>` (표시 범위, 없으면 빈 값) |
| OBX-11 | Observation Status | `R` (Result) |

---

## 5. OBX-3 Observation Identifier 형식

```
<montype>^<device>/<track>[@<srate>]
```

| 파트 | 예시 | 설명 |
|------|------|------|
| `<montype>` | `ECG_HR`, `ECG_WAV` | 모니터 타입 코드 (아래 목록 참조) |
| `<device>` | `BeneView` | 장비 이름 |
| `<track>` | `HR`, `ECG_II` | 트랙 이름 |
| `@<srate>` | `@250` | 파형(NA)에만 붙음: 샘플링 레이트 (Hz) |

**예시:**
```
ECG_HR^BeneView/HR
ECG_WAV^BeneView/ECG_II@250
AWP_WAV^Ventilator/Paw@25
```

---

## 6. OBX-5 Observation Value 형식

### 6.1 숫자값 (NM)

단일 float 값:
```
72.5
```

### 6.2 파형 (NA)

`^` 로 구분된 float 샘플 배열. 무효 샘플(NaN)은 빈 문자열로 표현:
```
0.12^0.15^0.09^^0.11^0.20
```

- 파형 데이터는 OBR-7(from)~OBR-8(to) 구간의 샘플을 순서대로 포함
- 1회 전송 윈도우는 최대 60초
- srate > 100 Hz인 트랙은 100 Hz로 다운샘플링
- AWP(기도압), CO2 파형은 25 Hz로 고정 다운샘플링

### 6.3 문자열 이벤트 (ST)

```
OBX|<idx>|ST|EVENT^^||Induction Start||||||R
```

- OBX-3: `EVENT^^` (고정)
- 최신 이벤트 최대 3개를 메시지 말미에 추가

---

## 7. montype 코드 목록

### 파형 (OBX-2 = NA)

| 코드 | 설명 | 기본 srate |
|------|------|-----------|
| `ECG_WAV` | ECG 파형 | 최대 100 Hz |
| `PLETH_WAV` | SpO2 Pleth 파형 | 최대 100 Hz |
| `RESP_WAV` | 호흡 파형 | 최대 100 Hz |
| `CO2_WAV` | CO2 파형 | 25 Hz (고정) |
| `AWP_WAV` | 기도압 파형 | 25 Hz (고정) |
| `IABP_WAV` | 동맥압 파형 | 최대 100 Hz |
| `CVP_WAV` | CVP 파형 | 최대 100 Hz |
| `EEG_WAV` | EEG 파형 | 최대 100 Hz |
| `ICP_WAV` | ICP 파형 | 최대 100 Hz |
| `PAP_WAV` | PA 파형 | 최대 100 Hz |

### 숫자값 (OBX-2 = NM)

| 코드 | 설명 | 단위 |
|------|------|------|
| `ECG_HR` | 심박수 | bpm |
| `PLETH_SPO2` | SpO2 | % |
| `RESP_RR` | 호흡수 | /min |
| `CO2_CONC` | EtCO2 | mmHg |
| `NIBP_SBP` | NIBP 수축기압 | mmHg |
| `NIBP_DBP` | NIBP 이완기압 | mmHg |
| `NIBP_MBP` | NIBP 평균압 | mmHg |
| `IABP_SBP` | ABP 수축기압 | mmHg |
| `IABP_DBP` | ABP 이완기압 | mmHg |
| `IABP_MBP` | ABP 평균압 | mmHg |
| `BT` | 체온 | °C |
| `EEG_BIS` | BIS | |
| `TV` | 일회호흡량 | mL |
| `MV` | 분당환기량 | L/min |
| `PIP` | 최고기도압 | cmH₂O |
| `PEEP` | PEEP | cmH₂O |

---

## 8. 완성 예시

### 8.1 숫자 트랙만 포함한 메시지

```
MSH|^~\&|VitalRecorder|VR_ABC123|||20250323143001||ORU^R01|42|P|2.6\r
PID|||PT-2025-001\r
PV1||I|OR-3\r
OBR|1|||VITAL_SIGNS|||20250323143000|20250323143001\r
OBX|1|NM|ECG_HR^BeneView/HR||72|bpm|40^200||||R\r
OBX|2|NM|PLETH_SPO2^BeneView/SpO2||98|%|80^100||||R\r
OBX|3|NM|NIBP_SBP^BeneView/NIBP_SBP||118|mmHg|40^260||||R\r
OBX|4|NM|NIBP_DBP^BeneView/NIBP_DBP||74|mmHg|20^200||||R\r
OBX|5|NM|BT^BeneView/BT||36.7|°C|30^42||||R\r
```

### 8.2 파형 포함한 메시지 (ECG 250→100 Hz 다운샘플링)

```
MSH|^~\&|VitalRecorder|VR_ABC123|||20250323143001||ORU^R01|43|P|2.6\r
PID|||PT-2025-001\r
PV1||I|OR-3\r
OBR|1|||VITAL_SIGNS|||20250323143000|20250323143001\r
OBX|1|NA|ECG_WAV^BeneView/ECG_II@100||0.12^0.15^0.09^0.11^...(100개 샘플)...|mV|-1.5^1.5||||R\r
OBX|2|NA|AWP_WAV^Ventilator/Paw@25||12.1^12.3^12.0^11.9^...(25개 샘플)...|cmH2O|0^60||||R\r
OBX|3|NM|ECG_HR^BeneView/HR||72|bpm|40^200||||R\r
OBX|4|ST|EVENT^^||Induction Start||||||R\r
```

### 8.3 다중 병상 메시지 (payload 전체)

병상별 메시지가 CR(`\r`)로 분리된 세그먼트로 이어붙여짐:

```
MSH|...|OR-1|...\r PID|...\r PV1|...|OR-1\r OBR|...\r OBX|...\r
MSH|...|OR-2|...\r PID|...\r PV1|...|OR-2\r OBR|...\r OBX|...\r
```

---

## 9. 주의사항

| 항목 | 내용 |
|------|------|
| 시간 형식 | `YYYYMMDDHHmmss` (로컬 타임, 초 단위) |
| 파형 NaN | 샘플 값이 유효하지 않으면 빈 문자열 (`^` 사이 값 없음) |
| 파형 srate | 100 Hz 초과 트랙은 100 Hz로 자동 다운샘플링 |
| 전송 윈도우 | 최대 60초 분량의 데이터를 1메시지에 포함 |
| 전송 주기 | 1초 (SEND_WEB_INTERVAL_SECS) |
| 인코딩 | 모든 문자열 UTF-8 |
| Ref Range | mindisp == maxdisp 이면 OBX-7 빈 값 |
| 데이터 없음 | 해당 트랙에 전송 구간 내 데이터가 없으면 OBX 행 자체를 생략 |
| OBX 없으면 | OBX가 하나도 없는 병상의 메시지는 전송하지 않음 |
