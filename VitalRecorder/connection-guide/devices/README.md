# Vital Recorder Hardware Connection Guide

Find your device in the tables below, then open its guide for cable wiring, device settings, and Vital Recorder setup.

> **Disclaimer:** This guide is for reference. Our team is not responsible for connection errors. Follow the manufacturer's instructions for equipment operation and electrical safety. If this guide conflicts with the manufacturer's manual, follow the manual.

Use the latest Vital Recorder release. See the [device-related version notes](version-notes.md) or the [official version history](https://vitaldb.net/vital-recorder/?action=versions).

## Contents

- [Device Quick Reference](#device-quick-reference)
  - [Patient Monitors](#patient-monitors)
  - [Anesthesia Machines](#anesthesia-machines)
  - [Mechanical Ventilators](#mechanical-ventilators)
  - [Hemodynamic Monitors](#hemodynamic-monitors)
  - [Infusion Devices](#infusion-devices)
  - [Brain Monitors](#brain-monitors)
  - [Multifunction monitors](#multifunction-monitors)
  - [Neuromuscular monitors](#neuromuscular-monitors)
- [Getting Started](#getting-started)
  - [Requirements](#requirements)
  - [Serial Cables](#serial-cables)

## Device Quick Reference

These tables summarize the connection requirements for each device. Follow the linked device guide for connection and setup instructions.

**Null modem adapters** use crossover wiring. M/F and F/F indicate connector gender.


### Patient Monitors

| Device | Cable or Interface | Adapter | Device Port | Vital Recorder Device Type |
|--------|-------|---------|------|----------------|
| [GE CARESCAPE B850 / B650 / B450](patient_monitors/ge_carescape.md) | Monitor-side USB-Serial converter (compatible with the monitor’s software version) | Null modem (F/F) | USB port | `Bx50` |
| [GE S/5 AM](patient_monitors/ge_s5am.md) | Direct serial cable | Null modem (F/F) | Port X8 | `Bx50` |
| [GE B40 / B20](patient_monitors/ge_b40_b20.md) | 9-pin serial cable with pin 4 removed | GE Multi I/O adapter (if not already installed) | 9-pin RS-232 port on the Multi I/O adapter | `Bx50` |
| [GE B105M / B125M / B155M](patient_monitors/ge_b105m.md) | Direct serial cable | None | X5 Serial port | `B1x5M` |
| [GE Solar 8000m / 8000i](patient_monitors/ge_solar8000.md) | Direct serial cable | None | RS-232 1 | `Solar8000` |
| [GE Dash 2000 / 3000 / 4000 / 5000](patient_monitors/ge_dash2000.md) | Custom RJ-45 to DB-9F cable | None | RJ-45 AUX | `Dashx000` |
| [GE Dash 2500](patient_monitors/ge_dash2500.md) | Direct serial cable | None | HostComm port | `Dash2500` |
| [GE TRAM-RAC 4A](patient_monitors/ge_tram_rac.md) | ADC required (analog) | None | 15-pin ANALOG OUT | Select the ADC device type |
| [GE Defib Connectors](patient_monitors/ge_defib.md) | 7-pin DIN to ADC | None | Defib.Sync | Select the ADC device type |
| [Philips IntelliVue MP / MX](patient_monitors/philips_intellivue.md) | Custom RJ-45 to DB-9F cable | None | MIB/RS232 port | `Intellivue` |
| [Dräger Infinity Kappa](patient_monitors/drager_infinity_kappa.md) | 14-pin Mini-D to DB-9F cable (Dräger export protocol cable #5206441) | None | X5 port | `Infinity` |
| [Dräger Infinity C500 / C700](patient_monitors/drager_infinity_c500.md) | Custom RJ-10 to DB-9F cable | None | RJ-10 port on P2500 | `Infinity` |
| [MEKICS MP1300](patient_monitors/mekics_mp1300.md) | Wi-Fi via an external router | — | LAN port | `MEKICS` |
| [Nihon Kohden BSM — numeric data](patient_monitors/nihon_kohden_bsm.md) | Direct serial cable | Null modem (M/F) | RS-232C on a model-specific interface; contact Nihon Kohden for interface requirements. | `BSM` |
| [Nihon Kohden BSM — ECG/BP waveforms](patient_monitors/nihon_kohden_bsm.md#ecg-and-arterial-pressure-waveforms) | ECG/BP output cable + custom cable to ADC + ADC | — | ECG/BP OUT; check interface requirements for your model | Select the device type for your ADC |
| [Nihon Kohden PVM-4700](patient_monitors/nihon_kohden_pvm.md) | Direct serial cable | Null modem (M/F) | RS-232C on a model-specific interface; contact Nihon Kohden for interface requirements. | `PVM` |
| [GE Corometrics 170 Series](patient_monitors/ge_corometrics.md) | Custom RJ-45 to DB-9F cable | None | RS-232 Port 1 or 2 | `Coro` |
| [GE Corometrics 250cx](patient_monitors/ge_corometrics.md#corometrics-250cx) | Custom RJ-11 to DB-9F cable | None | RJ-11 serial port | `Coro` |

### Anesthesia Machines

| Device | Cable or Interface | Adapter | Device Port | Vital Recorder Device Type |
|--------|-------|---------|------|----------------|
| [Dräger Apollo / Cicero EM Color / Julian / Vamos](anesthesia_machines/drager_apollo.md) | Direct serial cable | None | COM1 | `Medibus` |
| [Dräger Primus](anesthesia_machines/drager_primus.md) | Direct serial cable | None | COM1 | `Primus` |
| [Dräger Fabius GS](anesthesia_machines/drager_fabius.md) | Direct serial cable | Check the COM1 connector:<br>Male (before Oct 2004): Null modem (F/F)<br>Female (Oct 2004 onward): None | COM1 | `Fabius` |
| [Dräger Zeus](anesthesia_machines/drager_zeus.md) | Direct serial cable | Null modem; connector gender not confirmed | Rear COM port | `Medibus` |
| [Dräger Perseus A500](anesthesia_machines/drager_perseus.md) | Direct serial cable | Null modem (F/F) | COM1 or COM2 | `MedibusX` |
| [Dräger Atlan](anesthesia_machines/drager_atlan.md) | Direct serial cable | Null modem (F/F) | COM1 or COM2 | `MedibusX` |
| [GE Datex-Ohmeda](anesthesia_machines/ge_datex_ohmeda.md) | Custom 15-pin D-sub (M) to DB-9F serial cable | None | 15-pin (under cover) | `Datex-Ohmeda` |
| [Maquet Flow-i](anesthesia_machines/maquet_flow_i.md) | Direct serial cable | Null modem (M/F) | Serial port | `Flow-i` |


### Mechanical Ventilators

| Device | Cable or Interface | Adapter | Device Port | Vital Recorder Device Type |
|--------|-------|---------|------|----------------|
| [Dräger EVITA V300 / V500 / V600 / V800](mechanical_ventilators/drager_evita.md) | Direct serial cable | Null modem; connector gender not confirmed | RS-232 COM1 | `MedibusX` |
| [Maquet / Getinge Servo-i / Servo-s](mechanical_ventilators/maquet_servo.md) | Direct serial cable | Null modem (M/F) | **Bottom** RS-232 port | `Servo-i` |
| [Maquet / Getinge Servo-U](mechanical_ventilators/maquet_servo.md) | Direct serial cable  | Null modem; connector gender not confirmed | RS-232 port | `Servo-u` |
| [Hamilton G5](mechanical_ventilators/hamilton.md) | Direct serial cable | Null modem (M/F) | Monitoring Interface 1 or 2 | `Hamilton` |


### Hemodynamic Monitors

| Device | Cable or Interface | Adapter | Device Port | Vital Recorder Device Type |
|--------|-------|---------|------|----------------|
| [Edwards EV-1000](hemodynamic_monitors/edwards_ev1000.md) | Direct serial cable | Null modem (F/F) | Second serial port from the right | `EV1000` |
| [Edwards EV-1000A](hemodynamic_monitors/edwards_ev1000.md) | Direct serial cable | Null modem (M/F) | Serial port | `EV1000` |
| [Edwards Vigilance](hemodynamic_monitors/edwards_vigilance.md) | Direct serial cable | Null modem (M/F) | COM1 (or COM2) | `Vigilance` |
| [Edwards Vigilance II](hemodynamic_monitors/edwards_vigilance2.md) | Direct serial cable | Null modem (M/F) | Port 1 (top) | `Vigilance` |
| [Edwards Vigileo](hemodynamic_monitors/edwards_vigileo.md) | Direct serial cable | Null modem (M/F) | Serial port | `Vigileo` |
| [Edwards HemoSphere](hemodynamic_monitors/edwards_hemosphere.md) | Direct serial cable | Null modem (M/F) | Serial port | `Hemosphere` |
| [Deltex CardioQ](hemodynamic_monitors/deltex_cardioq.md) | Direct serial cable | Null modem (F/F) | Male serial port | `CardioQ` |
| [LiDCO](hemodynamic_monitors/lidco.md) | Direct serial cable | Null modem (M/F) | COM1 | `LiDCO` |

### Infusion Devices

| Device | Cable or Interface | Adapter | Device Port | Vital Recorder Device Type |
|--------|-------|---------|------|----------------|
| [Fresenius Vial Orchestra](syringe_pumps/fresenius_orchestra.md) | Direct serial cable | Null modem (M/F) | RS232-3 | `Orchestra` |
| [Fresenius Kabi Agilia](syringe_pumps/fresenius_agilia.md) | Proprietary Fresenius cable | None | Device-specific | `Agilia` |
| [Fresenius Kabi Link+ Agilia](syringe_pumps/fresenius_link_agilia.md) | USB-A ↔ USB mini-B (5-pin) | None | USB mini-B | `Link+` |
| [B. Braun SpaceCom](syringe_pumps/bbraun_spacecom.md) | Cable for 9-pin mini-DIN | None | Mini-DIN | `SpaceCom` |
| [Bionet Pion TCI](syringe_pumps/bionet_pion.md) | Direct serial cable | None | 9-pin port | `Pion` |
| [Belmont FMS (RI-2)](syringe_pumps/belmont_fms.md) | Direct serial cable | Null modem (F/F) | Serial port (behind vent panel) | `FMS` |

### Brain Monitors

| Device | Cable or Interface | Adapter | Device Port | Vital Recorder Device Type |
|--------|-------|---------|------|----------------|
| [Medtronic BIS VISTA](brain_monitors/medtronic_bis_vista.md) | Direct serial cable | None | RS-232 port | `BIS` |
| [Medtronic BIS A-2000](brain_monitors/medtronic_bis_a2000.md) | Direct serial cable | None | RS-232 port | `BIS` |
| [Medtronic INVOS Cerebral/Somatic Oximetry](brain_monitors/medtronic_invos.md) | Direct serial cable | Null modem (F/F) | RS-232 port | `Invos` |
| [OBELAB NIRSIT-ON+](brain_monitors/obelab_nirsit_on.md) | Direct serial cable | None | USB port | `NirsitON` |

### Multifunction monitors

| Device | Cable or Interface | Adapter | Device Port | Vital Recorder Device Type |
|--------|-------|---------|------|----------------|
| [Masimo Radical-7](multifunction_monitors/masimo_radical7.md) | Direct serial cable | None | P1 RS-232 (docking station) | `Radical7` |
| [Masimo ROOT](multifunction_monitors/masimo_root.md) | Masimo data-acquisition USB cable | None | USB1 or USB2 | `Root` |
| [Sentec SDM](multifunction_monitors/sentec_sdm.md) | Direct serial cable | None | RS-232 port | `SDM` |
| [Mdoloris ANI Monitor V2](multifunction_monitors/mdms_ani_monitor.md) | Direct serial cable | None | REAL TIME EXPORT | `ANIMonitor2` |

### Neuromuscular monitors

| Device | Cable or Interface | Adapter | Device Port | Vital Recorder Device Type |
|--------|-------|---------|------|----------------|
| [Blink Device TwitchView](neuromuscular_monitors/blink_twitchview.md) | Custom RJ-45 to DB-9F serial cable  | None | RJ-45 on the charging station (monitor docked)  | `TwitchView` |
| [IDMED TOFscan](neuromuscular_monitors/idmed_tofscan.md) | TOF-RS1 / TOF-RS2 Optic-Serial (RS232) cable | None | Optical output | `TOFScan` |

---

## Getting Started

### Requirements

#### Computer

Vital Recorder runs on Windows, Raspberry Pi, and Ubuntu. See the [Vital Recorder User Manual](../../User_Manual.md) for platform-specific setup instructions.

### Serial Cables

**Direct cables** connect corresponding pins at both ends. **Cross cables** cross the transmit and receive lines. The cable type cannot be reliably identified by appearance alone.

For standard DB-9 connections, use a **direct cable** and add a **null modem adapter** when specified in the device guide. Follow that guide for any custom or manufacturer-specific cable requirements.

**M/F** and **F/F** indicate connector gender (M = male; F = female). A null modem adapter provides crossed pin connections; a straight-through gender changer does not.

#### Purchase Links (Korea)

- [Null modem adapter — M/F](http://cableguy.com/shop/mall.php?cat=007001001&query=view&no=33688)
- [Null modem adapter — F/F](http://cableguy.com/shop/mall.php?cat=007001001&query=view&no=189324)