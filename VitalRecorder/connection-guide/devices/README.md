# Hardware Connection Guide — Device Index

> **Disclaimer:** This document is for reference only. Our team is not responsible for connection errors. If discrepancies exist between this document and the device manufacturer's manual, **always follow the manufacturer's manual**.

See [connection requirements and cable types](../README.md) before connecting any device.

---

## Patient Monitors

| Device | Cable | Adapter | Port | VR Device Name |
|--------|-------|---------|------|----------------|
| [GE CARESCAPE B850/B650/B450](patient_monitors/ge_carescape.md) | ATEN UC-232A (USB-to-RS232) | Null Modem F/F | USB port | `Bx50` |
| [GE S/5 AM](patient_monitors/ge_s5am.md) | Direct Serial | Null Modem F/F | Port X8 | `Bx50` |
| [GE B40 / B20](patient_monitors/ge_b40_b20.md) | 9-pin serial (pin 4 removed) | None | 9-pin | `Bx50` |
| [GE B105M / B125M / B155M](patient_monitors/ge_b105m.md) | Direct Serial | None | Red-marked serial | `B1x5M` |
| [GE Solar 8000m / 8000i](patient_monitors/ge_solar8000.md) | Direct Serial | None | RS-232 1 | `Solar8000` |
| [GE Dash 2000/3000/4000](patient_monitors/ge_dash2000.md) | Custom DB-9F ↔ RJ-45 | None | RJ-45 AUX | `Dashx000` |
| [GE Dash 2500](patient_monitors/ge_dash2500.md) | Direct Serial | None | Host Comm Port | `Dash2500` |
| [GE TRAM-RAC 4A](patient_monitors/ge_tram_rac.md) | ADC required (analog) | — | 15-pin ANALOG OUT | *(per ADC)* |
| [GE Defib Connectors](patient_monitors/ge_defib.md) | 7-pin DIN → ADC | — | Defib.Sync | *(per ADC)* |
| [Philips Intellivue MP/MX](patient_monitors/philips_intellivue.md) | Custom RJ-45 ↔ DB-9F | None | MIB port | `Intellivue` |
| [Draeger Infinity Kappa](patient_monitors/drager_infinity_kappa.md) | Mini-D cable | None | X5 or X3 docking | `Infinity` |
| [Draeger Infinity C500/C700](patient_monitors/drager_infinity_c500.md) | Custom RJ10 ↔ DB-9F | None | P2500 RJ10 port | `Infinity` |
| [MEKICS MP1300](patient_monitors/mekics_mp1300.md) | Wireless (Wi-Fi) | — | LAN port | `MEKICS` |
| [Nihon Kohden BSM](patient_monitors/nihon_kohden_bsm.md) | Direct Serial | Null Modem M/F | RS-232C | `BSM` |

## Anesthesia Machines

| Device | Cable | Adapter | Port | VR Device Name |
|--------|-------|---------|------|----------------|
| [Draeger Apollo / Cicero / Julian / Primus / Vamos](anesthesia_machines/drager_apollo.md) | Direct Serial | None | COM1 | `Primus` |
| [Draeger Fabius / Zeus / Infinity](anesthesia_machines/drager_fabius.md) | Direct Serial | Null Modem | Serial port | `MedibusX` |
| [Draeger Perseus](anesthesia_machines/drager_perseus.md) | Direct Serial | Null Modem F/F | COM1 or COM2 | `MedibusX` |
| [GE Datex-Ohmeda](anesthesia_machines/ge_datex_ohmeda.md) | Custom 9-pin ↔ 15-pin | None | 15-pin (under cover) | `Datex-Ohmeda` |
| [Maquet Flow-i](anesthesia_machines/maquet_flow_i.md) | Direct Serial | Null Modem M/F | Serial port | `Flow-i` |
| [Maquet Servo-i Ventilator](anesthesia_machines/maquet_servo_i.md) | Direct Serial | Null Modem M/F | Bottom RS-232 port | `Servo-i` |
| [Hamilton G5 Ventilator](anesthesia_machines/hamilton_g5.md) | Direct Serial | Null Modem M/F | Monitoring Interface 1 or 2 | `Hamilton` |

## Hemodynamic Monitors

| Device | Cable | Adapter | Port | VR Device Name |
|--------|-------|---------|------|----------------|
| [Edwards EV-1000](hemodynamic_monitors/edwards_ev1000.md) | Direct Serial | Null Modem F/F or M/F | Serial port | `EV1000` |
| [Edwards Vigilance](hemodynamic_monitors/edwards_vigilance.md) | Direct Serial | Null Modem M/F | COM1 | `Vigilance` |
| [Edwards Vigilance II](hemodynamic_monitors/edwards_vigilance2.md) | Direct Serial | Null Modem M/F | Port 1 (top) | `Vigilance` |
| [Edwards Vigileo](hemodynamic_monitors/edwards_vigileo.md) | Direct Serial | Null Modem M/F | Serial port | `Vigileo` |
| [Edwards Hemosphere](hemodynamic_monitors/edwards_hemosphere.md) | Direct Serial | Null Modem M/F | Serial port | `Hemosphere` |
| [Deltex CardioQ](hemodynamic_monitors/deltex_cardioq.md) | Direct Serial | Null Modem F/F | Male serial port | `CardioQ` |
| [LiDCO](hemodynamic_monitors/lidco.md) | Direct Serial | Null Modem M/F | Serial port | `LiDCO` |

## Syringe Pumps

| Device | Cable | Adapter | Port | VR Device Name |
|--------|-------|---------|------|----------------|
| [Fresenius Vial Orchestra](syringe_pumps/fresenius_orchestra.md) | Direct Serial | Null Modem M/F | RS 232-3 (rightmost) | `Orchestra` |
| [Fresenius Kabi Agilia](syringe_pumps/fresenius_agilia.md) | Proprietary Fresenius cable | None | Device-specific | `Agilia` |
| [BBraun SpaceCom](syringe_pumps/bbraun_spacecom.md) | Custom Mini-DIN ↔ DB-9F | None | Mini-DIN port | `SpaceCom` |
| [Bionet Pion TCI](syringe_pumps/bionet_pion.md) | Direct Serial | None | 9-pin port | `Pion` |
| [Belmont FMS (RI-2)](syringe_pumps/belmont_fms.md) | Direct Serial | Null Modem F/F | Serial port | `FMS` |

## Brain Monitors

| Device | Cable | Adapter | Port | VR Device Name |
|--------|-------|---------|------|----------------|
| [Medtronic BIS VISTA](brain_monitors/medtronic_bis_vista.md) | Direct Serial | **None** (cross cable causes errors) | Serial port | `VISTA` |
| [Medtronic BIS A2000](brain_monitors/medtronic_bis_a2000.md) | Direct Serial | None | 9-pin port | `A2000` |
| [Medtronic INVOS](brain_monitors/medtronic_invos.md) | Direct Serial | Null Modem F/F | Male connector port | `Invos` |

## Others

| Device | Cable | Adapter | Port | VR Device Name |
|--------|-------|---------|------|----------------|
| [Masimo Radical7](others/masimo_radical7.md) | Direct Serial | None | P1 RS-232 (Docking Station) | `Radical7` |
| [Masimo ROOT](others/masimo_root.md) | USB or Serial | None | USB1/USB2 or serial | `Root` |
| [Sentec SDM](others/sentec_sdm.md) | USB-Serial Converter | None | Serial port | `SDM` |
| [MDMS ANI Monitor V2](others/mdms_ani_monitor.md) | NEXT USB-Serial | None | Serial port | `ANIMonitor2` |
| [BlinkDC TwitchView](others/blink_twitchview.md) | Custom RJ45 | None | RJ45 (bottom, docked) | `TwitchView` |
| [IDMed TOFscan](others/idmed_tofscan.md) | TOF-RS1 cable | None | Device-specific | `TOFScan` |
| [GE Corometrics 170](others/ge_corometrics.md) | Direct Serial | None | RS232 Port | `Coro` |
