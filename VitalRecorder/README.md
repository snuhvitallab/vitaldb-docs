# VitalRecorder Documentation

VitalRecorder is a Windows application for collecting biosignal data from medical devices in operating rooms and ICUs via serial (RS-232) and network connections.

## Documents

| Document | Language | Description |
|----------|----------|-------------|
| [Getting Started](Getting_Started.md) | EN | Installation, cables, quick setup |
| [시작 가이드](Getting_Started_Korean.md) | KO | |
| [User Manual](User_Manual.md) | EN | Full feature reference — UI, recording, server upload, configuration |
| [User Manual Zero](User_Manual_Zero.md) | EN | VitalRecorder Zero (Raspberry Pi / embedded) |
| [VitalConnect](VitalConnect.md) | EN | Network connectivity module |
| [VitalConnect](VitalConnect_Korean.md) | KO | |
| [Intellivue Ventilator Settings](Intellivue_Ventilator_Settings.md) | EN | Philips Intellivue ventilator data collection |
| [Intellivue 환기 설정](Intellivue_Ventilator_Settings_Korean.md) | KO | |
| [Configuration Guide](../VitalRecorder_v2/Configuration_Guide.md) | EN | `vr.conf` reference |
| [Supported Devices](../VitalRecorder_v2/Supported_Devices.md) | EN | Full device & parameter compatibility matrix |
| [Vital File Format](Vital_File_Format.md) | EN | Binary `.vital` file format specification |
| [VitalServer HL7 v2 Spec](../VitalRecorder_v2/VitalServer_HL7_v2_Spec.md) | EN | HL7 v2 protocol for server upload |

## Hardware Connection Guide

Per-device connection instructions for 44 medical devices:

→ **[Browse by Device](connection-guide/devices/README.md)**

| Category | Devices |
|----------|---------|
| [Patient Monitors](connection-guide/devices/patient_monitors/) | GE CARESCAPE, GE Solar 8000, Philips Intellivue, Draeger Infinity, MEKICS, Nihon Kohden, and more |
| [Anesthesia Machines](connection-guide/devices/anesthesia_machines/) | Draeger Apollo/Fabius/Perseus, GE Datex-Ohmeda, Maquet Flow-i/Servo-i, Hamilton G5 |
| [Hemodynamic Monitors](connection-guide/devices/hemodynamic_monitors/) | Edwards EV-1000/Vigilance/Vigileo/Hemosphere, Deltex CardioQ, LiDCO |
| [Syringe Pumps](connection-guide/devices/syringe_pumps/) | Fresenius Vial Orchestra/Agilia, BBraun SpaceCom, Bionet Pion, Belmont FMS |
| [Brain Monitors](connection-guide/devices/brain_monitors/) | Medtronic BIS VISTA/A2000, Medtronic INVOS |
| [Others](connection-guide/devices/others/) | Masimo Radical7/ROOT, Sentec SDM, MDMS ANI Monitor, BlinkDC TwitchView, IDMed TOFscan |

Also available: [Korean Hardware Connection Guide](connection-guide/Hardware_Connection_Guide_Korean.md)
