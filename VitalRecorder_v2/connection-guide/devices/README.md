# Hardware Connection Guide

> **Disclaimer:** This document is for reference only. Our team is not responsible for connection errors. If discrepancies exist between this document and the device manufacturer's manual, **always follow the manufacturer's manual**.

This guide covers Vital Recorder hardware setup for **44 medical devices** across 6 categories. Use the Quick Reference tables below to identify your cable type, then click the device name to open its full setup instructions.

---

## Table of Contents

- [Quick Reference — All Devices](#quick-reference--all-devices)
  - [Patient Monitors](#patient-monitors)
  - [Anesthesia Machines](#anesthesia-machines)
  - [Hemodynamic Monitors](#hemodynamic-monitors)
  - [Syringe Pumps](#syringe-pumps)
  - [Brain Monitors](#brain-monitors)
  - [Others](#others)
- [Getting Started](#getting-started)
  - [Requirements](#requirements)
  - [Cable Types](#cable-types)
- [Troubleshooting](#troubleshooting)

---

## Quick Reference — All Devices

> Find your device below and identify the cable type before connecting. Click the device name to open its full setup instructions.

### Patient Monitors

| Device | Cable | Adapter | Port | VR Device Name |
|--------|-------|---------|------|----------------|
| [GE CARESCAPE B850 / B650 / B450](patient_monitors/ge_carescape.md) | **ATEN UC-232A only** | Null Modem F/F | USB port | `Bx50` |
| [GE S/5 AM](patient_monitors/ge_s5am.md) | Direct Serial | Null Modem F/F | Port X8 | `Bx50` |
| [GE B40 / B20](patient_monitors/ge_b40_b20.md) | 9-pin serial (pin 4 removed) | None | 9-pin | `Bx50` |
| [GE B105M / B125M / B155M](patient_monitors/ge_b105m.md) | Direct Serial | None | Red-marked serial | `B1x5M` |
| [GE Solar 8000m / 8000i](patient_monitors/ge_solar8000.md) | Direct Serial | None | RS-232 1 | `Solar8000` |
| [GE Dash 2000 / 3000 / 4000](patient_monitors/ge_dash2000.md) | Custom DB-9F ↔ RJ-45 | None | RJ-45 AUX | `Dashx000` |
| [GE Dash 2500](patient_monitors/ge_dash2500.md) | Direct Serial | None | Host Comm Port | `Dash2500` |
| [GE TRAM-RAC 4A](patient_monitors/ge_tram_rac.md) | ADC required (analog) | — | 15-pin ANALOG OUT | *(per ADC type)* |
| [GE Defib Connectors](patient_monitors/ge_defib.md) | 7-pin DIN → ADC | — | Defib.Sync | *(per ADC type)* |
| [Philips Intellivue MP / MX](patient_monitors/philips_intellivue.md) | Custom RJ-45 ↔ DB-9F | None | MIB port | `Intellivue` |
| [Drager Infinity Kappa](patient_monitors/drager_infinity_kappa.md) | Mini-D cable (part #5206421) | None | X5 or X3 docking | `Infinity` |
| [Drager Infinity C500 / C700](patient_monitors/drager_infinity_c500.md) | Custom RJ10 ↔ DB-9F | None | P2500 RJ10 port | `Infinity` |
| [MEKICS MP1300](patient_monitors/mekics_mp1300.md) | Wireless (Wi-Fi) | — | LAN port | `MEKICS` |
| [Nihon Kohden BSM](patient_monitors/nihon_kohden_bsm.md) | Direct Serial | Null Modem M/F | RS-232C on QI-373P board | `BSM` |
| [GE Corometrics 170](patient_monitors/ge_corometrics.md) | Direct Serial | None | RS232 Port 1 or 2 | `Coro` |

### Anesthesia Machines

| Device | Cable | Adapter | Port | VR Device Name |
|--------|-------|---------|------|----------------|
| [Drager Apollo / Cicero EM Color / Julian / Primus / Vamos](anesthesia_machines/drager_apollo.md) | Direct Serial | None | COM1 | `Primus` |
| [Drager Fabius / Zeus / Infinity](anesthesia_machines/drager_fabius.md) | Direct Serial | Null Modem (cross gender) | Serial port | `MedibusX` |
| [Drager Perseus](anesthesia_machines/drager_perseus.md) | Direct Serial | Null Modem F/F | COM1 or COM2 | `MedibusX` |
| [GE Datex-Ohmeda](anesthesia_machines/ge_datex_ohmeda.md) | Custom 9-pin ↔ 15-pin | None | 15-pin (under cover) | `Datex-Ohmeda` |
| [Maquet Flow-i](anesthesia_machines/maquet_flow_i.md) | Direct Serial | Null Modem M/F | Serial port | `Flow-i` |
| [Maquet Servo-i Ventilator](anesthesia_machines/maquet_servo_i.md) | Direct Serial | Null Modem M/F | **BOTTOM** RS-232 port | `Servo-i` |
| [Hamilton G5 Ventilator](anesthesia_machines/hamilton_g5.md) | Direct Serial | Null Modem M/F | Monitoring Interface 1 or 2 | `Hamilton` |

### Hemodynamic Monitors

| Device | Cable | Adapter | Port | VR Device Name |
|--------|-------|---------|------|----------------|
| [Edwards EV-1000 (old model)](hemodynamic_monitors/edwards_ev1000.md) | Direct Serial | Null Modem **F/F** | 2nd port from right | `EV1000` |
| [Edwards EV-1000A (new model)](hemodynamic_monitors/edwards_ev1000.md) | Direct Serial | Null Modem **M/F** | Serial port | `EV1000` |
| [Edwards Vigilance](hemodynamic_monitors/edwards_vigilance.md) | Direct Serial | Null Modem M/F | COM1 (or COM2) | `Vigilance` |
| [Edwards Vigilance II](hemodynamic_monitors/edwards_vigilance2.md) | Direct Serial | Null Modem M/F | Port 1 (top) | `Vigilance` |
| [Edwards Vigileo](hemodynamic_monitors/edwards_vigileo.md) | Direct Serial | Null Modem M/F | Serial port | `Vigileo` |
| [Edwards Hemosphere](hemodynamic_monitors/edwards_hemosphere.md) | Direct Serial | Null Modem M/F | Serial port | `Hemosphere` |
| [Deltex CardioQ](hemodynamic_monitors/deltex_cardioq.md) | Direct Serial | Null Modem **F/F** | Male serial port | `CardioQ` |
| [LiDCO](hemodynamic_monitors/lidco.md) | Direct Serial | Null Modem M/F | Serial port | `LiDCO` |

### Syringe Pumps

| Device | Cable | Adapter | Port | VR Device Name |
|--------|-------|---------|------|----------------|
| [Fresenius Vial Orchestra](syringe_pumps/fresenius_orchestra.md) | Direct Serial | Null Modem M/F | RS 232-3 (rightmost) | `Orchestra` |
| [Fresenius Kabi Agilia](syringe_pumps/fresenius_agilia.md) | Proprietary Fresenius cable | None | Device-specific | `Agilia` |
| [Fresenius Kabi Link+ Agilia](syringe_pumps/fresenius_link_agilia.md) | USB 2.0 AM-Mini 5-pin | None | USB-B (side, bottom) | `Link+` |
| [BBraun SpaceCom](syringe_pumps/bbraun_spacecom.md) | Custom Mini-DIN ↔ DB-9F | None | Mini-DIN port | `SpaceCom` |
| [Bionet Pion TCI](syringe_pumps/bionet_pion.md) | Direct Serial | None | 9-pin port | `Pion` |
| [Belmont FMS (RI-2)](syringe_pumps/belmont_fms.md) | Direct Serial | Null Modem F/F | Serial port (behind vent panel) | `FMS` |

### Brain Monitors

| Device | Cable | Adapter | Port | VR Device Name |
|--------|-------|---------|------|----------------|
| [Medtronic BIS VISTA](brain_monitors/medtronic_bis_vista.md) | Direct Serial | **None** ⚠️ cross cable causes error | Serial port | `VISTA` |
| [Medtronic BIS A2000](brain_monitors/medtronic_bis_a2000.md) | Direct Serial | None | 9-pin port | `A2000` |
| [Medtronic INVOS Cerebral/Somatic Oximetry](brain_monitors/medtronic_invos.md) | Direct Serial | Null Modem F/F | `\|O\|O\|` port (male connector) | `Invos` |

### Others

| Device | Cable | Adapter | Port | VR Device Name |
|--------|-------|---------|------|----------------|
| [Masimo Radical7](others/masimo_radical7.md) | Direct Serial | None | P1 RS-232 (Docking Station) | `Radical7` |
| [Masimo ROOT](others/masimo_root.md) | Masimo USB data cable (preferred) | None | USB1 or USB2 | `Root` |
| [Sentec SDM](others/sentec_sdm.md) | USB-Serial Converter | None | Serial port | `SDM` |
| [MDMS ANI Monitor V2](others/mdms_ani_monitor.md) | NEXT USB-Serial [NEXT-RS232U20] | None | Serial port (right side) | `ANIMonitor2` |
| [BlinkDC TwitchView](others/blink_twitchview.md) | Custom RJ45 (special wiring) | None | RJ45 (bottom, when docked) | `TwitchView` |
| [IDMed TOFscan](others/idmed_tofscan.md) | TOF-RS1 cable (from IDMed) | None | Device-specific | `TOFScan` |

---

## Getting Started

### Requirements

#### Computer

Vital Recorder runs on Windows (Vista, 7, 8, 8.1, 10 — 32-bit and 64-bit).

| Spec | Details |
|------|---------|
| Minimum CPU | Intel Atom N330 (up to 30% CPU at full-screen recording) |
| Recommended CPU | Intel i3 or higher (<5% CPU utilization) |
| USB Ports | Multiple full-size ports recommended; USB hub supported |

> **Tip:** A laptop or low-cost Windows tablet works well. Use a powered USB hub when connecting more than 2 devices.

#### Serial Cables

There are two types of serial cable. They are **physically identical in appearance** — the difference is in the internal wiring.

| Type | Wiring | Use case |
|------|--------|----------|
| **Direct Cable** | Pin 2 ↔ Pin 2 (Rx), Pin 3 ↔ Pin 3 (Tx) | Most devices |
| **Cross Cable (Null Modem)** | Pin 2 ↔ Pin 3 (crossed) | Some devices (Fresenius Orchestra, Edwards) |

> ⚠️ **WARNING:** Using a cross cable where a direct cable is required (or vice versa) can cause electrical shorts, device malfunction, or fire. **Always verify the cable type before connecting.**

**Recommended approach:** Use only direct cables for all runs. If a cross connection is required, attach a **Null Modem cross gender adapter** at the device port.

---

### Cable Types

The images below show the cables and adapters referenced throughout this guide.

#### Direct Serial Cable

<img src="hardware_images/cable_direct.svg" width="450" alt="Direct Serial Cable">

#### Null Modem Adapter — F/F (Female / Female)

<img src="hardware_images/cable_null_modem_ff.svg" width="450" alt="Null Modem F/F Adapter">

| Adapter | Description | Purchase (Korea) |
|---------|-------------|-----------------|
| Null Modem M/F | Male on one side, Female on the other | [cableguy.com](http://cableguy.com/shop/mall.php?cat=007001001&query=view&no=33688) |
| Null Modem F/F | Female on both sides | [cableguy.com](http://cableguy.com/shop/mall.php?cat=007001001&query=view&no=189324) |

#### Null Modem Adapter — M/F (Male / Female)

<img src="hardware_images/cable_null_modem_mf.svg" width="450" alt="Null Modem M/F Adapter">

#### USB-Serial Converter

<img src="hardware_images/cable_usb_serial.svg" width="450" alt="USB-Serial Converter">

Laptops and tablets typically lack a built-in serial port. A USB-Serial converter creates a virtual COM port and **acts as a direct cable**. Devices that require a cross connection still need a cross gender adapter.

**Recommended:** Netmate 4-port Serial-to-USB Converter (Kangwon Electronics) — creates four COM ports from one USB connection. [Purchase link (Korea)](http://cableguy.com/shop/mall.php?cat=005004003&query=view&no=39206)

#### USB Hub

Use a **powered USB hub** (with its own external power adapter) to prevent power shortage — the most common cause of intermittent data loss.

[Purchase — ORICO 4-port Powered USB Hub (Korea)](http://www.enuri.com/detail.jsp?modelno=10534644)

#### USB Extension Cable

Cables under 10 meters do not risk signal degradation. Use shielded cables in OR environments.

[Purchase link (Korea)](http://cableguy.com/shop/mall.php?cat=025011002&query=view&no=541)

---

## Troubleshooting

Common problems and fixes are documented in [`troubleshooting.md`](troubleshooting.md).

Quick reference:

| Problem | Likely Cause |
|---------|-------------|
| Device not detected | Wrong COM port / driver not installed |
| Data shows but wrong values | Cross cable used instead of direct (or vice versa) |
| Intermittent data loss | Unpowered USB hub / insufficient USB power |
| No data after correct setup | Device config not saved / baud rate mismatch |
| Device disconnects randomly | USB extension cable too long (>10m) or poor contact |

> ⚠️ Always complete device configuration **before** connecting to a patient.
