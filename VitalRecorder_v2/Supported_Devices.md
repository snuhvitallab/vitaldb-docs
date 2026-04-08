# VitalRecorder Supported Devices

Complete list of devices supported by VitalRecorder.
Includes connection interfaces, communication settings, and collected parameters.

---

## Table of Contents

1. [VitalDB Devices](#1-vitaldb-devices)
2. [Analog-to-Digital Converters (ADC)](#2-analog-to-digital-converters-adc)
3. [Patient Monitors](#3-patient-monitors)
4. [Multifunction Monitors](#4-multifunction-monitors)
5. [Anesthesia Machines](#5-anesthesia-machines)
6. [Mechanical Ventilators](#6-mechanical-ventilators)
7. [Drug Infusion Pumps](#7-drug-infusion-pumps)
8. [Brain Monitors](#8-brain-monitors)
9. [Neuromuscular Monitors](#9-neuromuscular-monitors)
10. [Fluid Infusors](#10-fluid-infusors)
11. [Cardiac Monitors](#11-cardiac-monitors)
12. [Fetal Monitors](#12-fetal-monitors)
13. [Research Devices](#13-research-devices)

---

## Connection Type Legend

| Symbol | Description |
|--------|-------------|
| RS-232 | Serial port (COM port / USB-to-Serial adapter) |
| TCP | Network TCP socket |
| UDP | Network UDP socket |
| BLE | Bluetooth Low Energy |

---

## 1. VitalDB Devices

| Device | Manufacturer | Interface | Key Parameters |
|--------|-------------|-----------|----------------|
| SNUADC | VitalDB | RS-232, 57600 baud | 8-channel analog input (12-bit, 500 Hz) |
| SNUADCM | VitalDB | RS-232, 57600 baud | Multi-channel ADC (extended SNUADC) |
| BUTTON | VitalDB | RS-232, 57600 baud | Event button input |
| VitalBOLUS | VitalDB | RS-232 | Bolus event recording |

---

## 2. Analog-to-Digital Converters (ADC)

Supports USB ADC devices from DataQ Instruments.
Connected via USB; recognized as a VirtualCOM port after driver installation.

| Device | Manufacturer | Channels | Resolution | Max Sampling | Notes |
|--------|-------------|----------|------------|-------------|-------|
| DI-149 | DataQ | 8 ch | 10-bit | 1,000 Hz | Low-cost basic model |
| DI-155 | DataQ | 4 ch | 14-bit | 10,000 Hz | High resolution |
| DI-245 | DataQ | 2 ch | 14-bit | 2,000 Hz | Isolation support |
| DI-1100 | DataQ | 4 ch | 12-bit | 10,000 Hz | |
| DI-1120 | DataQ | 4 ch | 14-bit | 10,000 Hz | High-resolution extended |

---

## 3. Patient Monitors

### Philips

| Device | Interface | Settings | Key Parameters |
|--------|-----------|----------|----------------|
| Intellivue (MX/MP series) | RS-232 | 115200 baud | ECG, PLETH, ABP, CVP, CO2, RESP, SpO2, NIBP, Temp |
| VueLink | RS-232 | 115200 baud | Same as Intellivue (via external VueLink module) |

> **Connection**: Connect RS-232 cable to the MIB/RS-232 port on the back of the device or via VueLink module.
> MIB output must be enabled in the device menu for Intellivue.

### GE Healthcare

| Device | Interface | Settings | Key Parameters |
|--------|-----------|----------|----------------|
| Solar 8000 / Solar 8000M | RS-232 | 9600 baud | ECG, NIBP, SpO2, Temp, Resp, IBP |
| Dash 2500 / 4000 | RS-232 | 9600 baud | ECG, NIBP, SpO2, Temp, Resp, IBP |
| Bx50 | RS-232 | 9600 baud | ECG, NIBP, SpO2, Temp, IBP |
| B105M / B125M | RS-232 | 9600 baud | ECG, NIBP, SpO2, Temp, IBP |
| GE Canvas | RS-232 | 9600 baud | ECG, NIBP, SpO2, Temp, IBP |
| MPS (Dash 2500) | RS-232 | 9600 baud | ECG, PLETH waveform, NIBP, SpO2 |

### Draeger

| Device | Interface | Settings | Key Parameters |
|--------|-----------|----------|----------------|
| Infinity (Delta/Kappa/Gamma) | RS-232 | 19200 baud | ECG, NIBP, SpO2, Temp, IBP, CO2 |

### Nihon Kohden

| Device | Interface | Settings | Key Parameters |
|--------|-----------|----------|----------------|
| BSM series (Serial) | RS-232 | 9600 baud | ECG, NIBP, SpO2, Temp, IBP |
| BSM series (EGA) | UDP | Network | Waveform + numeric data |
| BSM series (ADT) | TCP | Port 9007 | Patient information (admission/discharge) |
| BSM series (HL7 GW) | TCP | Port 9001 | HL7 v2 gateway |
| BSM series (HL7 GN) | TCP | Port 7999 | HL7 v2 extended gateway |

### MEKICS

| Device | Interface | Settings | Key Parameters |
|--------|-----------|----------|----------------|
| MEKICS patient monitor | TCP | Port 6002 | ECG, Resp, SpO2, IBP, ETCO2, anesthetic gas |

---

## 4. Multifunction Monitors

| Device | Manufacturer | Interface | Settings | Key Parameters |
|--------|-------------|-----------|----------|----------------|
| Radical-7 | Masimo | RS-232 | 9600 baud | SpO2, PR, PVI, PI, SpHb, SpMet |
| Root (with NIBP) | Masimo | RS-232 | 19200 baud | SpO2, PR, NIBP, PVI, SpHb, SpCO |
| SDM (SenTec) | Sentec | RS-232 | 115200 baud | SpO2, PCO2, PO2, PR, PI (transcutaneous) |

---

## 5. Anesthesia Machines

| Device | Manufacturer | Interface | Settings | Key Parameters |
|--------|-------------|-----------|----------|----------------|
| Primus / Zeus / Fabius | Draeger | RS-232 | 9600 baud (8,2) | AWP, AWF, FiO2, EtCO2, MAC, TV, MV |
| Primus IE / Perseus (Medibus X) | Draeger | RS-232 | 19200 baud (8,2) | AWP, AWF, FiO2, EtCO2, MAC, TV, MV (extended) |
| Aisys / Avance / Aestiva | GE Datex-Ohmeda | RS-232 | 19200 baud (7,1) | Paw, Pplat, EtCO2, TV, MV, FiO2 |
| Flowi | Maquet | RS-232 | -- | Flow measurement |

> **Note**: Draeger Primus/Zeus use the Medibus protocol.
> RS-232 output must be enabled in the device Service menu, and Communication must be set to Medibus.

---

## 6. Mechanical Ventilators

| Device | Manufacturer | Interface | Settings | Key Parameters |
|--------|-------------|-----------|----------|----------------|
| SERVO-i / SERVO-s | Maquet | RS-232 | 9600 baud | Paw, PEEP, TV, MV, RR, FiO2 |
| SERVO-U | Maquet | RS-232 | 19200 baud | Paw, PEEP, TV, MV, RR, FiO2 (extended) |
| MR1 / C2 / C6 / T1 | Hamilton Medical | RS-232 | 38400 baud (STX/ETX) | Paw, PEEP, Pplat, TV, MV, RR, FiO2, CO2 |

---

## 7. Drug Infusion Pumps

| Device | Manufacturer | Interface | Settings | Key Parameters |
|--------|-------------|-----------|----------|----------------|
| Agilia / Link+ | Fresenius Kabi | RS-232 | 115200 baud | Infusion volume, rate, alarm status |
| Primea (Orchestra) | Fresenius Kabi | RS-232 | 19200 baud | Infusion volume, rate, alarm status |
| PCBM | Fresenius Kabi | RS-232 | 19200 baud (7,2) | Multi-module pump status (ENQ/ACK protocol) |
| SpaceCom | BBraun | RS-232 | 9600 baud | Infusion volume, rate, drug name |
| DS-5000 | Daiwha | RS-232 | 57600 baud | Infusion volume, rate |
| Pion | Bionet | RS-232 | 115200 baud | Infusion volume, rate |
| Link 4 | -- | RS-232 | -- | 4-channel linked pump status |

---

## 8. Brain Monitors

### EEG / Depth of Anesthesia

| Device | Manufacturer | Interface | Settings | Key Parameters |
|--------|-------------|-----------|----------|----------------|
| BISx (single channel) | Medtronic | RS-232 | 57600 baud | BIS, EMG, SQI, SR, EEG waveform |
| A2000 (BIS 256 Hz) | Medtronic | RS-232 | 57600 baud | BIS, EMG, SQI, SR, EEG waveform (high-res) |
| VISTA (BIS 4-channel) | Medtronic | RS-232 | 57600 baud | BIS x4, EMG, SQI, SR, EEG waveform (4 ch) |
| Conox | Fresenius Kabi | RS-232 | 9600 baud | qCON, qNOX, EEG indices |

### Analgesia Monitors

| Device | Manufacturer | Interface | Settings | Key Parameters |
|--------|-------------|-----------|----------|----------------|
| ANIMonitor | MDMS | RS-232 | -- | ANI (Analgesia Nociception Index) |
| ANIMonitor 2 | MDMS | RS-232 | 115200 baud | ANI, HRV indices |

### Cerebral Oximetry / Hemodynamics

| Device | Manufacturer | Interface | Settings | Key Parameters |
|--------|-------------|-----------|----------|----------------|
| INVOS 5100C | Medtronic | RS-232 | -- | rSO2 (left/right cerebral oxygen saturation) |
| NirsitON | OBELAB | RS-232 | 115200 baud | RSO2, HbO2, HbR, CCO, NIRS waveform |
| PLEM100 | Inbody | RS-232 | 230400 baud | Bioimpedance-based cerebral hemodynamic index |
| CAIS | -- | RS-232 | -- | Cerebral autonomic index (research) |

---

## 9. Neuromuscular Monitors

| Device | Manufacturer | Interface | Settings | Key Parameters |
|--------|-------------|-----------|----------|----------------|
| TwitchView | BlinkDC | RS-232 | 19200 baud | TOF ratio, T1-T4, PTC |
| TOFScan | IDMed | RS-232 | 19200 baud | TOF ratio, T1-T4, PTC |
| TOFcuff | RGB Medical | RS-232 | 38400 baud | TOF ratio, T1-T4 (automatic cuff method) |

---

## 10. Fluid Infusors

| Device | Manufacturer | Interface | Settings | Key Parameters |
|--------|-------------|-----------|----------|----------------|
| FMS 2000 | Belmont Instrument | RS-232 | 19200 baud | Infusion rate, temperature, total volume, alarm |

---

## 11. Cardiac Monitors

### Edwards Lifesciences

| Device | Interface | Settings | Key Parameters |
|--------|-----------|----------|----------------|
| Vigilance II / Vigilance C | RS-232 | 9600 baud (STX/ETX) | CO, CI, SvO2, SVO2, HR, Temp |
| Hemosphere | RS-232 | 9600 baud (STX/ETX) | CO, CI, SV, SVR, DO2, CCO |
| EV1000 | RS-232 | 9600 baud (STX/ETX) | CO, CI, SV, SVV, PPV, SVR |
| ClearSight (non-invasive) | RS-232 | 9600 baud (STX/ETX) | CO, CI, SV, SVV, MAP, HR (non-invasive) |
| Vigileo (FloTrac) | RS-232 | 9600 baud (STX/ETX) | CO, CI, SV, SVV, SVR |

### Other Cardiac Monitors

| Device | Manufacturer | Interface | Settings | Key Parameters |
|--------|-------------|-----------|----------|----------------|
| PulsioFlex (PiCCO) | Getinge | RS-232 | 19200 baud (8,2) | CO, CI, SV, SVV, PPV, SVRI, EVLWI |
| CardioQ | Deltex | RS-232 | 57600 baud | CO, SV, FTc, MA, PV, FLOW waveform |
| LiDCOrapid | LiDCO | RS-232 | 57600 baud (STX/ETX) | CO, CI, SV, SVV, MAP, HR |
| AirTom | Bilab | RS-232 | 115200 baud | CO, CI, SV, SVV, SBP, DBP, MAP, SpO2 |
| HemoVista | Bilab | RS-232 | 115200 baud | Same as AirTom (HemoVista model) |
| CW10 | Edgecare | RS-232 | 115200 baud (MLLP/HL7) | VTIc, VTIf, HRc, HRf, FTcc, FTcf, eSVc, eSVf, eSVVc, eSVVf, BFc, BFf, BFc+f, DPTT, B-line |
| Movesense | Movesense | Bluetooth LE | -- | ECG, accelerometer, heart rate (wearable) |

#### Edgecare CW10 Parameter Details

| Parameter | Unit | Description |
|-----------|------|-------------|
| VTIc | cm | Velocity Time Integral -- carotid |
| VTIf | cm | Velocity Time Integral -- femoral |
| HRc | bpm | Heart rate -- carotid-based |
| HRf | bpm | Heart rate -- femoral-based |
| FTcc | ms | Corrected flow time -- carotid |
| FTcf | ms | Corrected flow time -- femoral |
| eSVc | mL/beat | Stroke volume -- carotid |
| eSVf | mL/beat | Stroke volume -- femoral |
| eSVVc | % | Stroke volume variation -- carotid |
| eSVVf | % | Stroke volume variation -- femoral |
| BFc | L/min | Blood flow -- carotid |
| BFf | L/min | Blood flow -- femoral |
| BFc+f | L/min | Total blood flow (carotid + femoral) |
| DPTT | ms | Differential pulse transit time |
| B-line | EA | B-line count (pulmonary edema indicator) |

---

## 12. Fetal Monitors

| Device | Manufacturer | Interface | Settings | Key Parameters |
|--------|-------------|-----------|----------|----------------|
| Corometrics 250cx | GE Healthcare | RS-232 | 9600 baud | FHR (fetal heart rate), MHR (maternal heart rate), TOCO |

---

## 13. Research Devices

| Device | Manufacturer | Interface | Description |
|--------|-------------|-----------|-------------|
| IAP (Serial) | VitalDB | RS-232 | Invasive arterial pressure waveform collection for research |
| IAP (Radical7) | VitalDB | RS-232 | IAP collection via Masimo Radical7 |
| IAP (TCP) | VitalDB | TCP | Network-based IAP collection |
| IAP (Official) | VitalDB | -- | Official IAP protocol |
| AU | -- | RS-232 | General-purpose serial input |
| Laxtha | Laxtha | RS-232 | Multi-channel EEG/EMG/ECG biosignal |
| SKNA | -- | RS-232 | Skin sympathetic nerve activity (SKNA) |
| SNUPATCH | VitalDB | -- | Patch-type biosignal sensor |
| SNUECG | VitalDB | -- | Research ECG acquisition module |
| SNUEEG | VitalDB | -- | Research EEG acquisition module |

---

## Connection Quick Reference

### RS-232 (COM Port) Common Notes

- When using a USB-to-Serial adapter, install the appropriate driver first.
- Select the COM port number in VitalRecorder's Add Device screen.
- Baud rates are listed in the tables above; other serial parameters (data bits, parity, stop bits) can be found on the device page.

### Network (TCP/UDP) Common Notes

- The PC running VitalRecorder and the device must be on the same network.
- Enter the device's IP address and port number in VitalRecorder settings.
- Firewall exceptions may be required.

### Port Name Filtering (TCP/UDP Framed Communication Only)

Port Name supports `#` and `@` delimiters to filter incoming data. This feature only works with framed communication protocols (some TCP such as HL7, and UDP) where frames are delimited. It does not work with binary protocols or RS-232 serial communication.

**Format**: `PortName#keyword@IP_address`

- **`#` (keyword filter)**: Only accepts frames containing the keyword after `#`.
  - Space-separated keywords within a group are **AND** conditions (all keywords must be present).
  - Multiple `#` groups are **OR** conditions (matching any one group passes).
- **`@` (IP filter, UDP/TCP Server only)**: Only processes data received from the IP address after `@`. Works only in UDP and TCP Server modes; ignored for RS-232 serial. Only digits and `.` are allowed. Supports dot-delimited postfix matching, so you can enter just the trailing portion of the IP address (e.g., `@10.1` matches `192.168.10.1` but not `192.168.110.1`).

**Examples**:

| Port Name | Meaning |
|-----------|---------|
| `7001#PV1` | Port 7001, accept only frames containing "PV1" |
| `7001#PV1 ICU` | Port 7001, accept only frames containing both "PV1" **AND** "ICU" |
| `7001#PV1#MSH` | Port 7001, accept frames containing "PV1" **OR** "MSH" |
| `7001#PV1 ICU#MSH` | Port 7001, ("PV1" AND "ICU") **OR** "MSH" |
| `7001@192.168.0.1` | Port 7001, process only data from 192.168.0.1 |
| `7001@10.1` | Port 7001, process only data from x.x.10.1 (postfix matching) |
| `7001#PV1@192.168.0.1` | Keyword filter and IP filter combined |

### Bluetooth LE (BLE) Common Notes

- Requires Windows 10 or later with a Bluetooth 4.0+ adapter.
- Set the device to pairing mode, then search in VitalRecorder.

### Console Mode and Debugging

VitalRecorder can run in console mode without a GUI. Command line options:

| Option | Description |
|--------|-------------|
| `--console`, `-c` | Run in console mode without GUI (normal recording) |
| `--debug [conf]` | Console + debug mode (no vital file created; optional vr.conf path) |
| `--conf <path>` | Use specified vr.conf file |
| `--help`, `-h` | Show usage |

**Usage examples**:

```bash
# Console mode (record without GUI)
Vital.exe --console

# Console mode with specific config file
Vital.exe --console --conf custom.conf

# Debug mode (using default vr.conf)
Vital.exe --debug

# Debug mode with test config file
Vital.exe --debug test_mindray.conf
```

In debug mode, the following information is printed and no vital file is created:

| Output | Meaning |
|--------|---------|
| `[+tab] BED-001` | Tab created |
| `[+dev] HL7 -> BED-001` | Device added |
| `[+trk] HR -> BED-001` | Track added |
| `[fwd] HL7 -> HL7` | Frame forwarding |
| `[BED-001] HL7/HR = 72.00` | Data received |
