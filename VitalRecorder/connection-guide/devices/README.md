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
  - [Connection Types](#connection-types)
  - [Cable Types](#cable-types)

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
| [Dräger Atlan](anesthesia_machines/drager_apollo.md) | Direct serial cable | Null modem (F/F) | COM1 or COM2 | `MedibusX` |
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

| Spec | Details |
|------|---------|
| USB Ports | Multiple full-size ports recommended; USB hub supported |

> **Tip:** A laptop or low-cost Windows tablet works well. Use a powered USB hub when connecting more than 2 devices.

#### Serial Cables

There are two types of serial cable. They are **physically identical in appearance** — the difference is in the internal wiring.

<img src="hardware_images/serial_cable_1.png" width="360" alt="A DB-9 serial cable with a male connector on one end and a female connector on the other — a direct and a cross cable look exactly like this, so the wiring cannot be told apart by sight">

| Type | Wiring | Use in this guide |
|------|--------|-------------------|
| **Direct serial cable** — also called a *straight-through* cable | Pin 2 ↔ Pin 2 (Rx), Pin 3 ↔ Pin 3 (Tx) | Default cable for standard serial connections |
| **Cross cable** — also called a *crossover* or *null-modem cable* | Pin 2 ↔ Pin 3 (crossed) | Some device pages specify a custom cable with crossed wiring. For standard DB-9 runs, the guide specifies a direct serial cable and, where required, a **Null Modem adapter** |

> ⚠️ Use the cable type and adapter specified on the device page. Incorrect wiring can prevent communication; verify the pinout before connecting.

For standard DB-9 connections, use a direct serial cable and add a **Null Modem adapter** when the device page specifies one. For custom cables, follow the device-specific pinout.

---

### Connection Types

Every device in this guide connects in one of four ways. Identify which type applies to your device, then follow its device page for the exact port and settings.

> The device lists in these diagrams are examples only. Use the [Quick Reference tables](#device-quick-reference) and the device page together; update both when a connection requirement changes.

#### Type A — Direct Serial

Device serial port → direct serial cable → USB-Serial converter → PC. No adapter.

<img src="hardware_images/connection_direct.svg" width="620" alt="Type A: a device 9-pin serial port joins a direct serial cable wired pin 2 to 2 and pin 3 to 3, into a USB-Serial converter that presents a virtual COM port, then by USB to the PC running Vital Recorder">

#### Type B — Null Modem Adapter

Same as Type A, with a Null Modem adapter fitted **at the device port**.

<img src="hardware_images/connection_cross.svg" width="620" alt="Type B: a device serial port takes a Null Modem adapter, M/F or F/F, that swaps pins 2 and 3, then a standard direct serial cable to a USB-Serial converter and by USB to the PC running Vital Recorder">

#### Type C — Custom / Proprietary Cable

The device port is not a standard DB-9 — RJ-45, RJ-10, 15-pin or DIN — so a cable with specific pin wiring is required.

<img src="hardware_images/connection_custom.svg" width="620" alt="Type C: a device with an RJ-45, RJ-10, 15-pin or DIN port needs a custom cable with specific pin wiring, for example RJ-45 to DB-9F, then a USB-Serial converter presenting a virtual COM port to the PC running Vital Recorder">

#### Type D — Wireless (Wi-Fi)

The device sends data over the network instead of a serial line. The router must be configured in advance.

<img src="hardware_images/connection_wireless.svg" width="620" alt="Type D: a MEKICS MP1300 connects by LAN cable to a Wi-Fi router at 192.168.0.1, which reaches the PC running Vital Recorder over Wi-Fi on port 6002; the router must be pre-configured with SSID, WPA2PSK with AES, and the recording PC's IP">

---

### Cable Types

The images below show the cables and adapters referenced throughout this guide.

#### Direct Serial Cable

<img src="hardware_images/cable_direct.svg" width="450" alt="Diagram of a direct serial cable — DB-9 female on the device side, DB-9 male on the PC or converter side, with pin 2 to pin 2, pin 3 to pin 3 and pin 5 to pin 5; the default cable choice for most devices">

#### Null Modem Adapter — F/F (Female / Female)

A **Null Modem adapter** swaps the TX and RX lines (pins 2 and 3) and is specified by the gender of its two connectors, **M/F** or **F/F**. It is also sold as a *cross-gender* adapter.

> Korean cable shops sell Null Modem adapters as **"크로스 젠더" (cross gender)**. Ask for that name when buying locally — a plain *gender changer* (젠더) is wired straight through and will **not** work.

<img src="hardware_images/cable_null_modem_ff.svg" width="450" alt="Diagram of a Null Modem F/F adapter — female DB-9 on both ends, pins 2 and 3 crossed internally, pin 5 straight through; required when the device port is female-type">

<img src="hardware_images/serial_cable_3.png" width="300" alt="A Null Modem F/F serial gender adapter (9F/9F, cross wiring) — female sockets on both sides">

| Adapter | Description | Purchase (Korea) |
|---------|-------------|-----------------|
| Null Modem M/F | Male on one side, Female on the other | [cableguy.com](http://cableguy.com/shop/mall.php?cat=007001001&query=view&no=33688) |
| Null Modem F/F | Female on both sides | [cableguy.com](http://cableguy.com/shop/mall.php?cat=007001001&query=view&no=189324) |

#### Null Modem Adapter — M/F (Male / Female)

<img src="hardware_images/cable_null_modem_mf.svg" width="450" alt="Diagram of a Null Modem M/F adapter — male DB-9 on one end and female on the other, pins 2 and 3 crossed internally, pin 5 straight through; required when the device port is male-type">

<img src="hardware_images/serial_cable_2.png" width="260" alt="A Null Modem M/F serial gender adapter (9M/9F, cross wiring) — male pins on one side, female sockets on the other">

#### USB-Serial Converter

<img src="hardware_images/cable_usb_serial.svg" width="450" alt="Diagram of a USB-Serial converter — USB-A to the PC on one side, DB-9 male to the device cable on the other, creating a virtual COM port; it acts as a direct cable">

Laptops and tablets typically lack a built-in serial port. A **USB-Serial converter**, also sold as a USB-to-RS-232 converter, creates a virtual COM port and **acts as a direct serial cable**. Devices that require a cross connection still need a Null Modem adapter.

**Recommended:** Netmate 4-port USB-Serial converter (Kangwon Electronics) — creates four COM ports from one USB connection. [Purchase link (Korea)](http://cableguy.com/shop/mall.php?cat=005004003&query=view&no=39206)

<img src="hardware_images/usb_serial_converter_1.png" width="400" alt="A 4-port RS-232-to-USB converter cable (NEXT-RS232 4P) — one USB-A plug fanning out to four DB-9 connectors, creating four COM ports from a single USB port">

> Some devices accept only specific converter models. The **GE CARESCAPE** accepts one converter per monitor software version — see its device page before buying.

#### USB Hub

Use a **powered USB hub** (with its own external power adapter) so that every connected device receives sufficient USB power.

[Purchase — ORICO 4-port Powered USB Hub (Korea)](http://www.enuri.com/detail.jsp?modelno=10534644)

<img src="hardware_images/usb_hub_1.png" width="400" alt="Two ORICO 4-port powered USB hubs — each has four USB ports on the front and, on the side, a USB uplink port next to a socket for its own external power adapter">

#### USB Extension Cable

Follow the cable and device manufacturers' guidance for maximum USB cable length. For operating-room installations, use a shielded cable when required by the manufacturer.

[Purchase link (Korea)](http://cableguy.com/shop/mall.php?cat=025011002&query=view&no=541)

<img src="hardware_images/usb_extension_1.png" width="220" alt="A USB 2.0 extension cable — USB-A male on one end, USB-A female on the other">
