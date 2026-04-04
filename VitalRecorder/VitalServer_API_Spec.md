# VitalServer JSON API Specification

Third-party Patient Monitor에서 VitalServer로 데이터를 전송하기 위한 기술 스펙

## 1. 통신 방식

| 항목 | 값 |
|------|-----|
| Protocol | WebSocket (RFC 6455) |
| Port | 443 (WSS) 또는 80 (WS) |
| Path | `/` |
| Data Format | JSON (UTF-8) |
| Compression | gzip (선택) |

## 2. 연결 절차

1. WebSocket Handshake
2. 연결 성공 후 주기적으로 데이터 전송 (1~5초 간격 권장)
3. Ping/Pong으로 연결 유지

## 3. JSON 메시지 구조

```json
{
  "ver": "1.0.0",
  "vrcode": "DEVICE_ID",
  "os": "custom",
  "rooms": [
    {
      "devs": [...],
      "trks": [...],
      "evts": [...]
    }
  ]
}
```

## 4. 장치 정보 (devs)

```json
{
  "type": "Patient Monitor",
  "name": "Monitor-001",
  "status": "run",
  "port": "192.168.1.100:5000"
}
```

| 필드 | 타입 | 설명 |
|------|------|------|
| type | string | 장비 종류 |
| name | string | 장비 식별자 |
| status | string | `run`, `stop`, `disconnected` |
| port | string | 연결 정보 |

## 5. 트랙 데이터 (trks)

### 5.1 Numeric (숫자값)

```json
{
  "name": "HR",
  "type": "num",
  "dname": "Monitor-001",
  "montype": "ECG_HR",
  "unit": "bpm",
  "recs": [
    {"dt": 1738656000.123, "val": 72.0},
    {"dt": 1738656001.123, "val": 73.0}
  ]
}
```

### 5.2 Waveform (파형)

```json
{
  "name": "ECG_II",
  "type": "wav",
  "dname": "Monitor-001",
  "montype": "ECG_WAV",
  "srate": 250,
  "mindisp": -1.5,
  "maxdisp": 1.5,
  "unit": "mV",
  "recs": [
    {"dt": 1738656000.0, "vals": [0.1, 0.2, 0.15, ...]}
  ]
}
```

### 5.3 String (문자열)

```json
{
  "name": "Agent1",
  "type": "str",
  "dname": "Vaporizer",
  "montype": "AGENT1_NAME",
  "recs": [
    {"dt": 1738656000.0, "val": "Sevoflurane"}
  ]
}
```

## 6. 필수/선택 필드

| 필드 | 타입 | 필수 | 설명 |
|------|------|:----:|------|
| name | string | O | 트랙 이름 |
| type | string | O | `num`, `wav`, `str` |
| dname | string | - | 장비 이름 |
| montype | string | - | 모니터 타입 코드 |
| srate | float | wav일 때 O | 샘플링 레이트 (Hz) |
| mindisp | float | - | 표시 최소값 |
| maxdisp | float | - | 표시 최대값 |
| unit | string | - | 단위 |
| color | string | - | 색상 (#RRGGBB) |
| recs | array | O | 레코드 배열 |

## 7. 레코드 형식

| 타입 | 필드 | 설명 |
|------|------|------|
| num | dt | Unix timestamp (초, 소수점 포함) |
| num | val | float 값 |
| wav | dt | 파형 시작 시각 |
| wav | vals | float 배열 |
| str | dt | 시각 |
| str | val | 문자열 값 |

## 8. montype 코드 목록

### Waveform
| 코드 | 설명 |
|------|------|
| ECG_WAV | ECG 파형 |
| PLETH_WAV | SpO2 파형 |
| RESP_WAV | 호흡 파형 |
| CO2_WAV | CO2 파형 |
| AWP_WAV | 기도압 파형 |
| IABP_WAV | 동맥압 파형 |
| CVP_WAV | CVP 파형 |
| EEG_WAV | EEG 파형 |
| ICP_WAV | ICP 파형 |
| PAP_WAV | PA 파형 |

### Numeric
| 코드 | 설명 |
|------|------|
| ECG_HR | 심박수 |
| PLETH_SPO2 | SpO2 |
| RESP_RR | 호흡수 |
| CO2_CONC | EtCO2 |
| NIBP_SBP | NIBP 수축기압 |
| NIBP_DBP | NIBP 이완기압 |
| NIBP_MBP | NIBP 평균압 |
| IABP_SBP | ABP 수축기압 |
| IABP_DBP | ABP 이완기압 |
| IABP_MBP | ABP 평균압 |
| BT | 체온 |
| EEG_BIS | BIS |
| TV | 일회호흡량 |
| MV | 분당환기량 |
| PIP | 최고기도압 |
| PEEP | PEEP |

### String
| 코드 | 설명 |
|------|------|
| AGENT1_NAME | 마취가스 1 이름 |
| AGENT1_CONC | 마취가스 1 농도 |
| DRUG1_NAME | 약물 1 이름 |
| DRUG1_CE | 약물 1 효과처 농도 |

## 9. 이벤트 (evts)

```json
{
  "dt": 1738656000.0,
  "val": "Induction Start"
}
```

## 10. 예제 (전체)

```json
{
  "ver": "1.0.0",
  "vrcode": "PM_001",
  "os": "custom",
  "rooms": [{
    "devs": [
      {"type": "Patient Monitor", "name": "Bedside-1", "status": "run", "port": "COM3"}
    ],
    "trks": [
      {
        "name": "HR",
        "type": "num",
        "dname": "Bedside-1",
        "montype": "ECG_HR",
        "unit": "bpm",
        "recs": [{"dt": 1738656000.0, "val": 72}]
      },
      {
        "name": "ECG_II",
        "type": "wav",
        "dname": "Bedside-1",
        "montype": "ECG_WAV",
        "srate": 250,
        "mindisp": -1.5,
        "maxdisp": 1.5,
        "unit": "mV",
        "recs": [{"dt": 1738656000.0, "vals": [0.1, 0.2, 0.15, 0.3]}]
      }
    ],
    "evts": []
  }]
}
```

## 11. 주의사항

1. **시간 형식**: Unix timestamp (초 단위, 밀리초는 소수점)
2. **파형 데이터**: 1초 이하 단위로 분할 전송 권장
3. **srate 제한**: 100Hz 초과 시 서버에서 다운샘플링됨
4. **인코딩**: 모든 문자열은 UTF-8
5. **NaN 처리**: 유효하지 않은 값은 전송하지 않거나 null 사용
