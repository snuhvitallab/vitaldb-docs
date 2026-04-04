# VitalServer HL7 v2 Protocol Specification

HL7 v2 protocol specification for VitalRecorder to transmit real-time vital data to the demo.vitaldb.net server.
The server also follows this specification when providing data in the same format to clients for the open dataset service.

---

## 1. Communication

| Item | Value |
|------|-------|
| Protocol | WebSocket (RFC 6455) over TLS |
| Port | 443 (WSS) |
| Path | `/socket.io/?EIO=3&transport=websocket` |
| Application Layer | Engine.IO v3 / Socket.IO |
| Data Format | HL7 v2.6 (UTF-8) |
| Compression | gzip (zlib) |

---

## 2. Connection Procedure

### 2.1 WebSocket Connection and Socket.IO Handshake

```
Client -> Server  [WS Upgrade]
Client -> Server  "40"                        <- engine.io MESSAGE(4) + socket.io CONNECT(0)
Server -> Client  [confirmation frame]
Client -> Server  42["join_vr","<vrcode>"]    <- socket.io EVENT: join room
```

`vrcode` is the unique identifier for the VitalRecorder device (e.g., `VR_ABC123`).

### 2.2 Data Transmission Loop (1-second interval)

```
Client -> Server  451-["send_data",{"_placeholder":true,"num":0}]   <- text frame, binary attachment announcement
Client -> Server  [binary frame] = 0x04 + gzip(HL7_payload)         <- binary frame
```

- First frame: `451-[...]` format to announce a binary attachment
  - `4` = engine.io MESSAGE, `5` = socket.io BINARY_EVENT, `1-` = 1 binary attachment
- Second frame: `0x04` (1-byte attachment header) + gzip-compressed HL7 text payload

### 2.3 Ping/Pong (Keep-alive)

```
Server -> Client  "2"    <- engine.io PING
Client -> Server  "3"    <- engine.io PONG
```

### 2.4 Server-to-Client Commands

The server can send commands in socket.io EVENT (`42[...]`) format:

| Command | Parameter | Description |
|---------|-----------|-------------|
| `update` | -- | Software update |
| `restart` | -- | Restart |
| `dt` | `<unix_timestamp>` | Time synchronization |
| `del_bed` | `"<bedname>"` | Delete bed |
| `new_bed` | `"<bedname>"` | Add bed |
| `edit_bed` | `"{...}"` (JSON string) | Modify bed settings |

---

## 3. HL7 v2 Message Structure

Each transmission payload is a concatenation of one or more HL7 messages (one per bed, sent consecutively).

### 3.1 Segment Delimiters

| Delimiter | Value | Description |
|-----------|-------|-------------|
| Segment terminator | `\r` (0x0D) | HL7 standard CR |
| Field | `\|` | Field separator |
| Component | `^` | Component separator |
| Repetition | `~` | Repeat separator |
| Escape | `\\` | Escape character |
| Sub-component | `&` | Sub-component separator |

### 3.2 Full Message Structure

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

## 4. Segment Details

### 4.1 MSH (Message Header)

| Field | Example | Description |
|-------|---------|-------------|
| MSH-3 | `VitalRecorder` | Sending application |
| MSH-4 | `VR_ABC123` | Sending device vrcode |
| MSH-7 | `20250323143000` | Message creation time (YYYYMMDDHHmmss) |
| MSH-9 | `ORU^R01` | Message type: Observation result |
| MSH-10 | `12345` | Message sequence number (monotonically increasing) |
| MSH-11 | `P` | Processing ID: Production |
| MSH-12 | `2.6` | HL7 version |

### 4.2 PID (Patient Identification)

| Field | Example | Description |
|-------|---------|-------------|
| PID-3 | `PT-001` | Patient ID (empty string if unavailable) |

### 4.3 PV1 (Patient Visit)

| Field | Example | Description |
|-------|---------|-------------|
| PV1-2 | `I` | Patient Class: Inpatient |
| PV1-3 | `OR-1` | Bed/room name |

### 4.4 OBR (Observation Request)

| Field | Example | Description |
|-------|---------|-------------|
| OBR-1 | `1` | Set ID |
| OBR-4 | `VITAL_SIGNS` | Observation identifier |
| OBR-7 | `20250323143000` | Observation start time |
| OBR-8 | `20250323143001` | Observation end time |

### 4.5 OBX (Observation Result)

```
OBX|<set_id>|<value_type>|<observation_id>||<observation_value>|<units>|<refrange>||||R
```

| Field | Position | Description |
|-------|----------|-------------|
| OBX-1 | Set ID | Sequential from 1 |
| OBX-2 | Value Type | `NM` (numeric), `NA` (numeric array/waveform), `ST` (string) |
| OBX-3 | Observation ID | `<code>^<device>/<track>[@<srate>]` |
| OBX-5 | Observation Value | Value (see type-specific formats) |
| OBX-6 | Units | Unit string (e.g., `bpm`, `mmHg`, `mV`) |
| OBX-7 | Reference Range | `<mindisp>^<maxdisp>` (display range; empty if not applicable) |
| OBX-11 | Observation Status | `R` (Result) |

---

## 5. OBX-3 Observation Identifier Format

```
<montype>^<device>/<track>[@<srate>]
```

| Part | Example | Description |
|------|---------|-------------|
| `<montype>` | `ECG_HR`, `ECG_WAV` | Monitor type code (see list below) |
| `<device>` | `BeneView` | Device name |
| `<track>` | `HR`, `ECG_II` | Track name |
| `@<srate>` | `@250` | Appended to waveforms (NA) only: sampling rate (Hz) |

**Examples:**
```
ECG_HR^BeneView/HR
ECG_WAV^BeneView/ECG_II@250
AWP_WAV^Ventilator/Paw@25
```

---

## 6. OBX-5 Observation Value Format

### 6.1 Numeric (NM)

Single float value:
```
72.5
```

### 6.2 Waveform (NA)

`^`-separated float sample array. Invalid samples (NaN) are represented as empty strings:
```
0.12^0.15^0.09^^0.11^0.20
```

- Waveform data contains sequential samples for the OBR-7 (from) to OBR-8 (to) interval
- Maximum transmission window per message is 60 seconds
- Tracks with srate > 100 Hz are downsampled to 100 Hz
- Airway pressure (AWP) and CO2 waveforms are downsampled to a fixed 25 Hz

### 6.3 String Event (ST)

```
OBX|<idx>|ST|EVENT^^||Induction Start||||||R
```

- OBX-3: `EVENT^^` (fixed)
- Up to 3 most recent events are appended at the end of the message

---

## 7. montype Code List

### Waveform (OBX-2 = NA)

| Code | Description | Default srate |
|------|-------------|---------------|
| `ECG_WAV` | ECG waveform | up to 100 Hz |
| `PLETH_WAV` | SpO2 pleth waveform | up to 100 Hz |
| `RESP_WAV` | Respiration waveform | up to 100 Hz |
| `CO2_WAV` | CO2 waveform | 25 Hz (fixed) |
| `AWP_WAV` | Airway pressure waveform | 25 Hz (fixed) |
| `IABP_WAV` | Arterial BP waveform | up to 100 Hz |
| `CVP_WAV` | CVP waveform | up to 100 Hz |
| `EEG_WAV` | EEG waveform | up to 100 Hz |
| `ICP_WAV` | ICP waveform | up to 100 Hz |
| `PAP_WAV` | PA waveform | up to 100 Hz |

### Numeric (OBX-2 = NM)

| Code | Description | Unit |
|------|-------------|------|
| `ECG_HR` | Heart rate | bpm |
| `PLETH_SPO2` | SpO2 | % |
| `RESP_RR` | Respiratory rate | /min |
| `CO2_CONC` | EtCO2 | mmHg |
| `NIBP_SBP` | NIBP systolic pressure | mmHg |
| `NIBP_DBP` | NIBP diastolic pressure | mmHg |
| `NIBP_MBP` | NIBP mean pressure | mmHg |
| `IABP_SBP` | ABP systolic pressure | mmHg |
| `IABP_DBP` | ABP diastolic pressure | mmHg |
| `IABP_MBP` | ABP mean pressure | mmHg |
| `BT` | Body temperature | C |
| `EEG_BIS` | BIS | |
| `TV` | Tidal volume | mL |
| `MV` | Minute ventilation | L/min |
| `PIP` | Peak inspiratory pressure | cmH2O |
| `PEEP` | PEEP | cmH2O |

---

## 8. Full Examples

### 8.1 Numeric Tracks Only

```
MSH|^~\&|VitalRecorder|VR_ABC123|||20250323143001||ORU^R01|42|P|2.6\r
PID|||PT-2025-001\r
PV1||I|OR-3\r
OBR|1|||VITAL_SIGNS|||20250323143000|20250323143001\r
OBX|1|NM|ECG_HR^BeneView/HR||72|bpm|40^200||||R\r
OBX|2|NM|PLETH_SPO2^BeneView/SpO2||98|%|80^100||||R\r
OBX|3|NM|NIBP_SBP^BeneView/NIBP_SBP||118|mmHg|40^260||||R\r
OBX|4|NM|NIBP_DBP^BeneView/NIBP_DBP||74|mmHg|20^200||||R\r
OBX|5|NM|BT^BeneView/BT||36.7|C|30^42||||R\r
```

### 8.2 With Waveforms (ECG 250 -> 100 Hz downsampled)

```
MSH|^~\&|VitalRecorder|VR_ABC123|||20250323143001||ORU^R01|43|P|2.6\r
PID|||PT-2025-001\r
PV1||I|OR-3\r
OBR|1|||VITAL_SIGNS|||20250323143000|20250323143001\r
OBX|1|NA|ECG_WAV^BeneView/ECG_II@100||0.12^0.15^0.09^0.11^...(100 samples)...|mV|-1.5^1.5||||R\r
OBX|2|NA|AWP_WAV^Ventilator/Paw@25||12.1^12.3^12.0^11.9^...(25 samples)...|cmH2O|0^60||||R\r
OBX|3|NM|ECG_HR^BeneView/HR||72|bpm|40^200||||R\r
OBX|4|ST|EVENT^^||Induction Start||||||R\r
```

### 8.3 Multi-Bed Message (full payload)

Bed-specific messages are concatenated with segments separated by CR (`\r`):

```
MSH|...|OR-1|...\r PID|...\r PV1|...|OR-1\r OBR|...\r OBX|...\r
MSH|...|OR-2|...\r PID|...\r PV1|...|OR-2\r OBR|...\r OBX|...\r
```

---

## 9. Notes

| Item | Details |
|------|---------|
| Time format | `YYYYMMDDHHmmss` (local time, second precision) |
| Waveform NaN | Invalid sample values are empty strings (nothing between `^` delimiters) |
| Waveform srate | Tracks exceeding 100 Hz are automatically downsampled to 100 Hz |
| Transmission window | Up to 60 seconds of data per message |
| Transmission interval | 1 second (SEND_WEB_INTERVAL_SECS) |
| Encoding | All strings UTF-8 |
| Ref Range | If mindisp == maxdisp, OBX-7 is left empty |
| No data | If a track has no data in the transmission window, the OBX row is omitted |
| No OBX | If a bed has no OBX rows, its entire message is not sent |
