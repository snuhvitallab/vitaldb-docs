# Vital File Format Specification

## Introduction

- The vital file is a binary file format used by VitalRecorder for saving vital signs and waveforms.
- It is a single gzip-compressed binary file starting with `1F 8B 08 00`.
- It contains a header and a body part.
- Multi-byte variables are encoded using **little-endian** byte order.
- All data structures are aligned on **1-byte boundaries**.
  - Caution: Some compilers use 4-byte alignment implicitly. For Visual Studio, use `#pragma pack(push, 1)` / `#pragma pack(pop)`.

---

## Data Formats

### String

- Strings are encoded in UTF-8.
- A string field consists of a 4-byte length (excluding the length field itself) followed by a character array of the specified length.
- Caution: The string does **not** include a trailing NULL (`\0`) character.

### Time

- Times are stored in **UTC**.
- UTC can be converted to local time using the time zone bias (offset) in the header:
  - `UTC = local_time + tzbias`
- All time values are represented as the number of seconds since `1970-01-01 00:00:00 UTC` in **IEEE 754 double** format.
- This is compatible with Unix timestamps and convenient for arithmetic operations.
- The decimal part represents sub-second precision. Because the Unix timestamp for year 2020 is approximately 1,606,780,800 (requiring 31 bits for the integer part) and IEEE 754 double has 52 bits of fraction, approximately 21 bits remain for sub-second representation, giving roughly **1 microsecond resolution**.

---

## Header

The total length of the header is `10 + headerlen` bytes.

The vital file does not include the number or length of tracks in the header. You must parse the body to discover tracks and records. This is because VitalRecorder cannot know when recording will stop, and tracks can be added at any time during recording.

The header can be extended by increasing `headerlen`. Parsers should use `headerlen` to determine which optional fields are present.

| Name | Type | Length | Description |
|------|------|--------|-------------|
| sign | BYTE[4] | 4 | `"VITA"` |
| format_ver | DWORD | 4 | File format version, currently `3` |
| headerlen | WORD | 2 | Header length after this field, currently `27` |
| tzbias | short | 2 | Time zone bias: the difference, in minutes, between UTC and local time. For example, Korea (UTC+9) uses `-540`. |
| inst_id | DWORD | 4 | Instance ID assigned when the program starts. Used to verify whether multiple vital files were recorded continuously in the same VitalRecorder session. Files with the same `inst_id` can share track IDs. |
| prog_ver | DWORD | 4 | VitalRecorder version |
| dtstart | double | 8 | (optional, headerlen >= 26) File start time as Unix timestamp |
| dtend | double | 8 | (optional, headerlen >= 26) File end time as Unix timestamp |
| packed | BYTE | 1 | (optional, headerlen >= 27) `0` = streaming format (default), `1` = packed storage format |

### Time Zone Conversion Example

```
time_t t = (time_t)(dt - tzbias * 60);  // UTC -> local time in seconds
struct tm *ptm = gmtime(&t);            // seconds -> year, month, day, hour, minute, second
```

### Packed Mode (packed = 1)

When `packed` is set to `1`, the file uses packed storage format with these guarantees:

- **WAV tracks**: All waveform records for each track are merged into a single REC. Gaps between consecutive records are filled with NaN samples (see table below). This allows direct sample access by index: `sample_time = trk_dtstart + sample_index / srate`.
- **NUM/STR tracks**: Records for each track appear consecutively and are sorted by time.
- **Track grouping**: All RECs belonging to the same track are stored consecutively (track by track).
- **TRKINFO fields**: Each TRKINFO includes `reclen`, `dtstart`, and `dtend` for the track.

#### NaN Values by Format Type

| Format | NaN Value | Description |
|--------|-----------|-------------|
| FMT_FLOAT (1) | NaN | IEEE 754 NaN |
| FMT_DOUBLE (2) | NaN | IEEE 754 NaN |
| FMT_CHAR (3) | -128 | signed byte min |
| FMT_BYTE (4) | 255 | unsigned byte max |
| FMT_SHORT (5) | -32768 | signed short min |
| FMT_WORD (6) | 65535 | unsigned short max |
| FMT_LONG (7) | -2147483648 | signed long min |
| FMT_DWORD (8) | 4294967295 | unsigned long max |

---

## Body

The body is a sequence of packets. Since packet lengths are not constant, there is no way to directly index a specific packet without reading sequentially. However, you can skip unwanted packet types using the `datalen` field.

### Packet Structure

| Name | Type | Length | Description |
|------|------|--------|-------------|
| type | BYTE | 1 | Packet type (see below) |
| datalen | DWORD | 4 | Length of `data` (excludes `type` and `datalen` fields). For unknown types, skip `datalen` bytes. |
| data | BYTE[] | datalen | Contents depend on type |

### Packet Types

| Value | Name | Description |
|-------|------|-------------|
| 0 | SAVE_TRKINFO | Track information |
| 1 | SAVE_REC | Data record (waveform, numeric, or string) |
| 6 | SAVE_CMD | Command |
| 9 | SAVE_DEVINFO | Device information |
| 10 | SAVE_RAW | Raw protocol data (for debugging; contains timestamp, port name, direction flag, and raw bytes) |

---

## DEVINFO (type = 9)

Stores device information. Must be saved before the corresponding `devid` is used in any TRKINFO.

- If `devid` is `0`, it indicates VitalRecorder itself (e.g., filter-generated tracks, event markers).
- A new DEVINFO can appear for the same `devid` within a file; the new values overwrite the previous ones.
- `devid` and `trkid` are meaningful only within the same file.
- VitalRecorder assigns the same `devid` to the same device type connected to the same physical port, even across program restarts.

| Name | Type | Length | Description |
|------|------|--------|-------------|
| devid | DWORD | 4 | Device identifier |
| typename | string | 4+len | Device type (e.g., `BIS`, `Intellivue`) |
| devname | string | 4+len | Device name |
| port | string | 4+len | Port information (e.g., `COM1`, `192.168.1.100:4343`). Devices with the same type and port are generally considered the same device. |

---

## TRKINFO (type = 0)

Stores track information. Must appear before the first REC with the corresponding `trkid`. Records with an unknown `trkid` should be ignored.

- Tracks are identified by `trkid`, a 2-byte integer. The numeric value itself has no inherent meaning and may change between program executions.
- Track display order is determined by order of appearance and the `CMD_TRK_ORDER` command, not by `trkid` value.
- A track with `devid = 0` and name `EVENT` is treated specially: it is displayed in the event bar rather than as a separate track.

| Name | Type | Length | Description |
|------|------|--------|-------------|
| trkid | WORD | 2 | Track ID |
| rec_type | BYTE | 1 | `TYPE_WAV = 1`, `TYPE_NUM = 2`, `TYPE_STR = 5` |
| recfmt | BYTE | 1 | Data format (see below) |
| name | string | 4+len | Track name |
| unit | string | 4+len | Unit (e.g., `bpm`, `mmHg`, `mV`) |
| minval | float | 4 | Display minimum value |
| maxval | float | 4 | Display maximum value |
| color | DWORD | 4 | 4-byte ARGB color |
| srate | float | 4 | Sample rate (Hz), used for WAV tracks |
| adc_gain | double | 8 | `measured_value = adc_offset + saved_value * adc_gain` |
| adc_offset | double | 8 | See above |
| montype | BYTE | 1 | Physiologic meaning of the track (see montype table) |
| devid | DWORD | 4 | Device ID that created this track |
| reclen | DWORD | 4 | (optional, packed mode) Total byte length of all REC packets for this track |
| trk_dtstart | double | 8 | (optional, packed mode) Start time of the first record |
| trk_dtend | double | 8 | (optional, packed mode) End time of the last record |

### Record Format (recfmt)

| Value | Name | Size | Description |
|-------|------|------|-------------|
| 0 | FMT_NULL | 0 | For TYPE_STR |
| 1 | FMT_FLOAT | 4 | 32-bit IEEE 754 float |
| 2 | FMT_DOUBLE | 8 | 64-bit IEEE 754 double |
| 3 | FMT_CHAR | 1 | Signed 8-bit integer |
| 4 | FMT_BYTE | 1 | Unsigned 8-bit integer |
| 5 | FMT_SHORT | 2 | Signed 16-bit integer |
| 6 | FMT_WORD | 2 | Unsigned 16-bit integer |
| 7 | FMT_LONG | 4 | Signed 32-bit integer |
| 8 | FMT_DWORD | 4 | Unsigned 32-bit integer |

---

## REC (type = 1)

Stores time-stamped data (measured samples, sample arrays, or strings).

| Name | Type | Length | Description |
|------|------|--------|-------------|
| infolen | WORD | 2 | Length of the record header, currently `10` |
| dt | double | 8 | Measurement timestamp (Unix time, UTC) |
| trkid | WORD | 2 | Track ID |
| values | BYTE[] | datalen - infolen - 2 | Record-type-specific values (see below) |

### WAV Record Values

Samples continuously measured from time `dt`, stored as an array. The sample rate and data type come from the TRKINFO.

| Name | Type | Length | Description |
|------|------|--------|-------------|
| num | DWORD | 4 | Number of samples |
| vals | recfmt[num] | sizeof(recfmt) * num | Sample data |

### NUM Record Values

| Name | Type | Length | Description |
|------|------|--------|-------------|
| val | recfmt | sizeof(recfmt) | Single numeric value |

### STR Record Values

| Name | Type | Length | Description |
|------|------|--------|-------------|
| unused | DWORD | 4 | Not used |
| sval | string | 4+len | String value |

---

## CMD (type = 6)

Command packets. Unknown commands should be skipped using the packet's `datalen`.

| Name | Type | Length | Description |
|------|------|--------|-------------|
| cmd | BYTE | 1 | Command type |

### CMD_TRK_ORDER (cmd = 5)

Defines the display order of tracks.

| Name | Type | Length | Description |
|------|------|--------|-------------|
| cnt | WORD | 2 | Number of tracks |
| trkids | WORD[cnt] | cnt * 2 | Array of track IDs in display order |

### CMD_RESET_EVENTS (cmd = 6)

Removes all event markers prior to this command. No additional data.

---

## Monitor Type Codes (montype)

The `montype` field in TRKINFO specifies the physiologic meaning of the track. This enables applications to identify and display parameters consistently regardless of track naming conventions.

### ECG

| Value | Name | Description |
|-------|------|-------------|
| 1 | ECG_WAV | ECG waveform |
| 2 | ECG_HR | Heart rate |
| 3 | ECG_PVC | PVC count |

### Arterial Blood Pressure (Invasive)

| Value | Name | Description |
|-------|------|-------------|
| 4 | IABP_WAV | ABP waveform |
| 5 | IABP_SBP | ABP systolic |
| 6 | IABP_DBP | ABP diastolic |
| 7 | IABP_MBP | ABP mean |

### Pulse Oximetry (PLETH)

| Value | Name | Description |
|-------|------|-------------|
| 8 | PLETH_WAV | Pleth waveform |
| 9 | PLETH_HR | Pulse rate |
| 10 | PLETH_SPO2 | SpO2 |

### Respiration

| Value | Name | Description |
|-------|------|-------------|
| 11 | RESP_WAV | Respiration waveform |
| 12 | RESP_RR | Respiratory rate |

### CO2

| Value | Name | Description |
|-------|------|-------------|
| 13 | CO2_WAV | CO2 waveform |
| 14 | CO2_RR | CO2 respiratory rate |
| 15 | CO2_CONC | EtCO2 concentration |

### Non-Invasive Blood Pressure

| Value | Name | Description |
|-------|------|-------------|
| 16 | NIBP_SBP | NIBP systolic |
| 17 | NIBP_DBP | NIBP diastolic |
| 18 | NIBP_MBP | NIBP mean |

### Temperature

| Value | Name | Description |
|-------|------|-------------|
| 19 | BT | Body temperature |

### Central Venous Pressure

| Value | Name | Description |
|-------|------|-------------|
| 20 | CVP_WAV | CVP waveform |
| 21 | CVP_CVP | CVP value |

### EEG / Brain Monitoring

| Value | Name | Description |
|-------|------|-------------|
| 22 | EEG_BIS | BIS index |
| 23 | EEG_SEF | Spectral Edge Frequency |
| 24 | EEG_MF | Median Frequency |
| 25 | EEG_SR | Suppression Ratio |
| 26 | EEG_EMG | EMG power |
| 27 | EEG_SQI | Signal Quality Index |
| 28 | EEG_WAV | EEG waveform |

### Airway

| Value | Name | Description |
|-------|------|-------------|
| 29 | AWP_WAV | Airway pressure waveform |
| 30 | PEEP | PEEP |
| 31 | PIP | Peak inspiratory pressure |
| 32 | TV | Tidal volume |
| 33 | MV | Minute ventilation |
| 34 | COMPLIANCE | Lung compliance |
| 35 | RESISTANCE | Airway resistance |

### Anesthetic Agents

| Value | Name | Description |
|-------|------|-------------|
| 36 | AGENT1_NAME | Agent 1 name (string) |
| 37 | AGENT1_CONC | Agent 1 concentration |
| 38 | AGENT2_NAME | Agent 2 name (string) |
| 39 | AGENT2_CONC | Agent 2 concentration |
| 40 | AGENT3_NAME | Agent 3 name (string) |
| 41 | AGENT3_CONC | Agent 3 concentration |

### Drug Infusion

| Value | Name | Description |
|-------|------|-------------|
| 42 | DRUG1_NAME | Drug 1 name (string) |
| 43 | DRUG1_CE | Drug 1 effect-site concentration |
| 44 | DRUG1_RATE | Drug 1 infusion rate |
| 45 | DRUG2_NAME | Drug 2 name (string) |
| 46 | DRUG2_CE | Drug 2 effect-site concentration |
| 47 | DRUG2_RATE | Drug 2 infusion rate |
| 48 | DRUG3_NAME | Drug 3 name (string) |
| 49 | DRUG3_CE | Drug 3 effect-site concentration |
| 50 | DRUG3_RATE | Drug 3 infusion rate |
| 51 | DRUG4_NAME | Drug 4 name (string) |
| 52 | DRUG4_CE | Drug 4 effect-site concentration |
| 53 | DRUG4_RATE | Drug 4 infusion rate |

### Cerebral Oximetry

| Value | Name | Description |
|-------|------|-------------|
| 54 | RSO2_L | Regional cerebral O2 saturation (left) |
| 55 | RSO2_R | Regional cerebral O2 saturation (right) |

### Additional EEG

| Value | Name | Description |
|-------|------|-------------|
| 56 | ENT_SE | State Entropy |
| 57 | ENT_RE | Response Entropy |
| 58 | PSI | Patient State Index |
| 59 | EEG_SEFL | SEF left |
| 60 | EEG_SEFR | SEF right |
| 61 | EEGL_WAV | EEG left waveform |
| 62 | EEGR_WAV | EEG right waveform |

### Advanced Pulse Oximetry

| Value | Name | Description |
|-------|------|-------------|
| 63 | PVI | Pleth Variability Index |
| 64 | SPHB | SpHb (non-invasive hemoglobin) |
| 65 | ORI | Oxygen Reserve Index |

### Pulmonary Artery

| Value | Name | Description |
|-------|------|-------------|
| 66 | PAP_WAV | PA waveform |
| 67 | PAP_SBP | PA systolic |
| 68 | PAP_MBP | PA mean |
| 69 | PAP_DBP | PA diastolic |

### Femoral Artery

| Value | Name | Description |
|-------|------|-------------|
| 70 | FEM_WAV | Femoral artery waveform |
| 71 | FEM_SBP | Femoral systolic |
| 72 | FEM_MBP | Femoral mean |
| 73 | FEM_DBP | Femoral diastolic |

### Intracranial Pressure

| Value | Name | Description |
|-------|------|-------------|
| 74 | ICP_WAV | ICP waveform |
| 75 | ICP | ICP value |
| 76 | CPP | Cerebral perfusion pressure |

### Neuromuscular Monitoring

| Value | Name | Description |
|-------|------|-------------|
| 77 | TOF_RATIO | Train-of-Four ratio |
| 78 | TOF_CNT | TOF count |
| 79 | PTC_CNT | Post-tetanic count |

### SKNA (Skin Sympathetic Nerve Activity)

| Value | Name | Description |
|-------|------|-------------|
| 80 | ISKNA_WAV | Integrated SKNA waveform |
| 81 | SKNA_WAV | SKNA waveform |
| 82 | ASKNA | Average SKNA |

### Miscellaneous

| Value | Name | Description |
|-------|------|-------------|
| 83 | ALARM_LEVEL | Alarm level |
| 84 | ALARM_MSG | Alarm message (string) |
| 85 | ANII | ANI instantaneous |
| 86 | ANIM | ANI mean |
| 87 | HPI | Hypotension Prediction Index |
| 88 | EEG_QCON | qCON index |
| 89 | EEG_QNOX | qNOX index |
| 90 | RRA | Respiratory rate acoustic |
| 91 | RRA_WAV | RRA waveform |

### Additional Waveforms

| Value | Name | Description |
|-------|------|-------------|
| 92 | FLOW_WAV | Flow waveform |
| 93 | VOLUME_WAV | Volume waveform |

### Fetal Monitoring

| Value | Name | Description |
|-------|------|-------------|
| 94 | FETAL_HR | Fetal heart rate |
| 95 | UACT | Uterine activity |

### Filter Outputs

| Value | Name | Description |
|-------|------|-------------|
| 96-111 | FILT1_1 .. FILT8_2 | Filter output channels (8 filters x 2 outputs each) |

> Note: Applications should treat unknown `montype` values gracefully; new types may be added in future versions.
