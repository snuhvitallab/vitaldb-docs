# Unverified Items — To Confirm

Every statement in this guide that has **not been confirmed on a real unit**, or that the manufacturer has **not published**, is collected here. Device pages mark these with ❓. When an item is confirmed, update the device page and delete the row.

## A. To confirm on site (we can do this)

Bring a camera. In most cases one photograph of the connector panel and one of the interface menu settles the row.

| # | Device | What is unverified | What to check | Page |
|---|---|---|---|---|
| A1 | Dräger EVITA V300–V800 | Null modem adapter gender (F/F assumed) | Is the RS-232 connector male or female? Which adapter, if any, produced data? | [drager_evita.md](mechanical_ventilators/drager_evita.md) |
| A2 | Maquet Servo-U | Whether the M/F null modem is still needed; which RS-232 port is live (Servo-i uses BOTTOM) | Connector panel photo; interface menu photo; adapter that worked | [maquet_servo.md](mechanical_ventilators/maquet_servo.md) |
| A3 | Hamilton C6 / C2 / T1 / MR1 | Port layout and menu path to set *Block* | Photograph the COM ports and the Configuration → Interface screen | [hamilton.md](mechanical_ventilators/hamilton.md) |
| A4 | GE Corometrics 250cx | RJ11 serial pinout | GE service manual for the 250cx, or a working cable to copy | [ge_corometrics.md](patient_monitors/ge_corometrics.md) |
| A5 | GE Corometrics 170 | Setup-code numbering: service manual says P1 = 30/31, P2 = 40/41; original guide said P1 = 30/40 | Enter service setup on a unit and read the codes | [ge_corometrics.md](patient_monitors/ge_corometrics.md) |
| A6 | LiDCO | COM1 connector gender (M/F adapter assumes female) | Photo of COM1 | [lidco.md](hemodynamic_monitors/lidco.md) |
| A7 | Dräger Zeus / Infinity (anesthesia) | COM connector gender — grouped with Fabius without checking | Photo of the COM port; adapter that worked | [drager_fabius.md](anesthesia_machines/drager_fabius.md) |
| A8 | Dräger Fabius plus | Line was correct (MEDIBUS 9600 8E1, valid checksums) but Vital Recorder recorded nothing on a 1.18 build | Re-test on the latest Vital Recorder; if it still fails, capture with `DEBUG=1` | [drager_fabius.md](anesthesia_machines/drager_fabius.md) |
| A9 | GE B40 / B20 | Null Modem F/F: Korean original says yes (table + text), English original omits it | Try the pin-4 cable with and without the adapter on one unit | [ge_b40_b20.md](patient_monitors/ge_b40_b20.md) |
| A10 | GE CARESCAPE Bx50 | Converter rule differs between the two originals and the field (v3.1.4+ Startech vs "ATEN only"; newer Startech failing) | Record monitor software version + converter model + result at each install | [ge_carescape.md](patient_monitors/ge_carescape.md) |
| A11 | Nihon Kohden CSM 1702 / PSM | Whether the BSM protocol works on these models | Connect one; record the interface board fitted | [nihon_kohden_bsm.md](patient_monitors/nihon_kohden_bsm.md) |
| A12 | Dräger Infinity Kappa | Analog/Sync port label: X10 in the original guide, X16 on the photographed dock | Read the label on the unit being wired | [drager_infinity_kappa.md](patient_monitors/drager_infinity_kappa.md) |
| A13 | GE Datex-Ohmeda (Aisys/Avance/Aestiva) | Serial frame: `Supported_Devices.md` says `19200 (7,1)` with no legend; "Even parity" was removed as unsourced | Read the machine's serial-port page, or confirm the `(7,1)` notation with the developer | [ge_datex_ohmeda.md](anesthesia_machines/ge_datex_ohmeda.md) |
| A14 | Dräger Atlan A300 / A350 | A300: numerics only, no waveforms, repeating `MEDIBUS COM1 FAILURE`; A350: baud menu location | Capture with `DEBUG=1`; ask the Dräger engineer for the A350 menu path | [drager_apollo.md](anesthesia_machines/drager_apollo.md) |

## B. Not published by the manufacturer (ask the vendor if needed)

Vital Recorder applies the correct line settings itself, so these matter only when testing with a third-party terminal.

| # | Device | Missing | Page |
|---|---|---|---|
| B1 | Blink TwitchView | Serial parameters (baud, data bits, parity) | [blink_twitchview.md](others/blink_twitchview.md) |
| B2 | IDMed TOFscan | Serial parameters; whether any firmware needs a menu option enabled | [idmed_tofscan.md](others/idmed_tofscan.md) |
| B3 | Mdoloris ANI Monitor V2 | Serial parameters | [mdms_ani_monitor.md](others/mdms_ani_monitor.md) |
| B4 | Sentec SDM | Data bits / parity / stop bits | [sentec_sdm.md](others/sentec_sdm.md) |
| B5 | Belmont FMS | Serial parameters | [belmont_fms.md](syringe_pumps/belmont_fms.md) |
| B6 | Bionet Pion | Serial parameters | [bionet_pion.md](syringe_pumps/bionet_pion.md) |
| B7 | Maquet Flow-i | Line settings (baud / parity) | [maquet_flow_i.md](anesthesia_machines/maquet_flow_i.md) |
| B8 | GE B1x5M | Serial frame (8/E/1 assumed from Datex DRI defaults) | [ge_b105m.md](patient_monitors/ge_b105m.md) |
| B9 | Deltex CardioQ | RS-232 frame ("contact Deltex") | [deltex_cardioq.md](hemodynamic_monitors/deltex_cardioq.md) |
| B10 | LiDCO | RS-232 frame specification | [lidco.md](hemodynamic_monitors/lidco.md) |

## C. Devices with no photographs

Text-only pages. A rear-panel shot and a port close-up would complete each.

Dräger EVITA · Maquet Servo (BOTTOM port) · Hamilton (Monitoring Interface ports, Interface menu) · OBELAB NIRSIT-ON+ (rear USB, Calibrate screen) · Dräger Perseus (interface panel, COM setup page) · LiDCO (COM1, Engineering screen) · Dräger Infinity C500/C700 (P2500 RJ10 port) · GE Corometrics (RJ45/RJ11 ports, service-setup displays)
