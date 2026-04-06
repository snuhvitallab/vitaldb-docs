# Hardware Connection Guide

> **Disclaimer:** This document is for reference only. Our team is not responsible for connection errors. If discrepancies exist between this document and the device manufacturer's manual, **always follow the manufacturer's manual**.

---

## Table of Contents

- [**Quick Reference — All Devices**](#quick-reference--all-devices)
- [Getting Started](#getting-started)
  - [Requirements](#requirements)
  - [Cable Types](#cable-types)
- [Patient Monitors](#patient-monitors)
- [Anesthesia Machines](#anesthesia-machines)
- [Hemodynamic Monitors](#hemodynamic-monitors)
- [Syringe Pumps](#syringe-pumps)
- [Brain Monitors](#brain-monitors)
- [Others](#others)
- [Troubleshooting](#troubleshooting)

---

## Quick Reference — All Devices

> Find your device below and identify the cable type before connecting. Click the device name to jump to full instructions.

### Patient Monitors

| Device | Cable | Adapter | Port | VR Device Name |
|--------|-------|---------|------|----------------|
| [GE CARESCAPE B850/B650/B450](#ge-carescape-b850--b650--b450) | **ATEN UC-232A only** | Null Modem F/F | USB port | `Bx50` |
| [GE S/5 AM](#ge-s5-am) | Direct Serial | Null Modem F/F | Port X8 | `Bx50` |
| [GE B40 / B20](#ge-b40--b20) | 9-pin serial (pin 4 removed) | None | 9-pin | `Bx50` |
| [GE B105M / B125M / B155M](#ge-b105m--b125m--b155m) | Direct Serial | None | Red-marked serial | `B1x5M` |
| [GE Solar 8000m / 8000i](#ge-solar-8000m--8000i) | Direct Serial | None | RS-232 1 | `Solar8000` |
| [GE Dash 2000 / 3000 / 4000](#ge-dash-2000--3000--4000) | Custom DB-9F ↔ RJ-45 | None | RJ-45 AUX | `Dashx000` |
| [GE Dash 2500](#ge-dash-2500) | Direct Serial | None | Host Comm Port | `Dash2500` |
| [GE TRAM-RAC 4A](#ge-tram-rac-4a) | ADC required (analog) | — | 15-pin ANALOG OUT | *(per ADC type)* |
| [GE Defib Connectors](#ge-defib-connectors) | 7-pin DIN → ADC | — | Defib.Sync | *(per ADC type)* |
| [Philips Intellivue MP/MX](#philips-intellivue-mp--mx-series) | Custom RJ-45 ↔ DB-9F | None | MIB port | `Intellivue` |
| [Drager Infinity Kappa](#drager-infinity-kappa) | Mini-D cable (part #5206421) | None | X5 or X3 docking | `Infinity` |
| [Drager Infinity C500 / C700](#drager-infinity-c500--c700) | Custom RJ10 ↔ DB-9F | None | P2500 RJ10 port | `Infinity` |
| [MEKICS MP1300](#mekics-mp1300) | Wireless (Wi-Fi) | — | LAN port | `MEKICS` |
| [Nihon Kohden BSM](#nihon-kohden-bsm) | Direct Serial | Null Modem M/F | RS-232C on QI-373P board | `BSM` |
| [GE Corometrics 170](#ge-corometrics-170) | Direct Serial | None | RS232 Port 1 or 2 | `Coro` |

### Anesthesia Machines

| Device | Cable | Adapter | Port | VR Device Name |
|--------|-------|---------|------|----------------|
| [Drager Apollo / Cicero / Julian / Primus / Vamos](#drager-apollo--cicero-em-color--julian--primus--vamos) | Direct Serial | None | COM1 | `Primus` |
| [Drager Fabius / Zeus / Infinity](#drager-fabius--zeus--infinity) | Direct Serial | Null Modem (cross gender) | Serial port | `MedibusX` |
| [Drager Perseus](#drager-perseus) | Direct Serial | Null Modem F/F | COM1 or COM2 | `MedibusX` |
| [GE Datex-Ohmeda](#ge-datex-ohmeda-anesthesia-machine) | Custom 9-pin ↔ 15-pin | None | 15-pin (under cover) | `Datex-Ohmeda` |
| [Maquet Flow-i](#maquet-flow-i) | Direct Serial | Null Modem M/F | Serial port | `Flow-i` |
| [Maquet Servo-i Ventilator](#maquet-servo-i-ventilator) | Direct Serial | Null Modem M/F | **BOTTOM** RS-232 port | `Servo-i` |
| [Hamilton G5 Ventilator](#hamilton-g5-ventilator) | Direct Serial | Null Modem M/F | Monitoring Interface 1 or 2 | `Hamilton` |

### Hemodynamic Monitors

| Device | Cable | Adapter | Port | VR Device Name |
|--------|-------|---------|------|----------------|
| [Edwards EV-1000 (old model)](#edwards-lifesciences-ev-1000) | Direct Serial | Null Modem **F/F** | 2nd port from right | `EV1000` |
| [Edwards EV-1000A (new model)](#edwards-lifesciences-ev-1000) | Direct Serial | Null Modem **M/F** | Serial port | `EV1000` |
| [Edwards Vigilance](#edwards-lifesciences-vigilance) | Direct Serial | Null Modem M/F | COM1 (or COM2) | `Vigilance` |
| [Edwards Vigilance II](#edwards-lifesciences-vigilance-ii) | Direct Serial | Null Modem M/F | Port 1 (top) | `Vigilance` |
| [Edwards Vigileo](#edwards-lifesciences-vigileo) | Direct Serial | Null Modem M/F | Serial port | `Vigileo` |
| [Edwards Hemosphere](#edwards-lifesciences-hemosphere) | Direct Serial | Null Modem M/F | Serial port | `Hemosphere` |
| [Deltex CardioQ](#deltex-cardioq) | Direct Serial | Null Modem **F/F** | Male serial port | `CardioQ` |
| [LiDCO](#lidco) | Direct Serial | Null Modem M/F | Serial port | `LiDCO` |

### Syringe Pumps

| Device | Cable | Adapter | Port | VR Device Name |
|--------|-------|---------|------|----------------|
| [Fresenius Vial Orchestra](#fresenius-vial-orchestra-base-primea-with-module-dps) | Direct Serial | Null Modem M/F | RS 232-3 (rightmost) | `Orchestra` |
| [Fresenius Kabi Agilia](#fresenius-kabi-agilia) | Proprietary Fresenius cable | None | Device-specific | `Agilia` |
| [Fresenius Kabi Link+ Agilia](#fresenius-kabi-link-agilia) | USB 2.0 AM-Mini 5-pin | None | USB-B (side, bottom) | `Link+` |
| [BBraun SpaceCom](#bbraun-spacecom) | Custom Mini-DIN ↔ DB-9F | None | Mini-DIN port | `SpaceCom` |
| [Bionet Pion TCI](#bionet-pion-tci) | Direct Serial | None | 9-pin port | `Pion` |
| [Belmont FMS (RI-2)](#belmont-fms-ri-2) | Direct Serial | Null Modem F/F | Serial port (behind vent panel) | `FMS` |

### Brain Monitors

| Device | Cable | Adapter | Port | VR Device Name |
|--------|-------|---------|------|----------------|
| [Medtronic BIS VISTA](#medtronic-bis-vista) | Direct Serial | **None** ⚠ cross cable causes error | Serial port | `VISTA` |
| [Medtronic BIS A2000](#medtronic-bis-a2000) | Direct Serial | None | 9-pin port | `A2000` |
| [Medtronic INVOS](#medtronic-invos-cerebrالsomatic-oximetry) | Direct Serial | Null Modem F/F | `\|O\|O\|` port (male connector) | `Invos` |

### Others

| Device | Cable | Adapter | Port | VR Device Name |
|--------|-------|---------|------|----------------|
| [Masimo Radical7](#masimo-radical7) | Direct Serial | None | P1 RS-232 (Docking Station) | `Radical7` |
| [Masimo ROOT](#masimo-root) | Masimo USB data cable (preferred) | None | USB1 or USB2 | `Root` |
| [Sentec SDM](#sentec-sdm) | USB-Serial Converter | None | Serial port | `SDM` |
| [MDMS ANI Monitor V2](#mdms-ani-monitor-v2) | NEXT USB-Serial [NEXT-RS232U20] | None | Serial port (right side) | `ANIMonitor2` |
| [BlinkDC TwitchView](#blinkdc-twitchview) | Custom RJ45 (special wiring) | None | RJ45 (bottom, when docked) | `TwitchView` |
| [IDMed TOFscan](#idmed-tofscan) | TOF-RS1 cable (from IDMed) | None | Device-specific | `TOFScan` |

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

**Recommended:** Netmate 4-port Serial-to-USB Converter (Kangwon Electronics) — creates four COM ports from one USB connection. [Purchase link (Korea)](http://cableguy.com/shop/mall.php?cat=005004003&query=view&no=39206)#### USB Hub

Use a **powered USB hub** (with its own external power adapter) to prevent power shortage — the most common cause of intermittent data loss.

[Purchase — ORICO 4-port Powered USB Hub (Korea)](http://www.enuri.com/detail.jsp?modelno=10534644)

#### USB Extension Cable

Cables under 10 meters do not risk signal degradation. Use shielded cables in OR environments.

[Purchase link (Korea)](http://cableguy.com/shop/mall.php?cat=025011002&query=view&no=541)

---

## Patient Monitors

[↑ Quick Reference](#quick-reference--all-devices)

> ⚠️ Always complete device configuration **before** connecting to a patient.

---
