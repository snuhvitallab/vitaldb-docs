# Nihon Kohden BSM

<!-- meta
category: Patient Monitor
manufacturer: Nihon Kohden
vr_device_name: BSM
-->
> ⚠️ **Whether a BSM has an RS-232C output depends on the model and on which optional interface unit is fitted.** Photograph the monitor's connector panel and confirm the model number before ordering anything.

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|----------------|
| Direct serial DB-9M ↔ DB-9F (numeric) | Null Modem M/F | RS-232C socket on the interface unit | `BSM` |
| Nihon Kohden ECG/BP output cable + custom 5.5pi Mono ↔ RJ45 (waveform) | None | `ECG/BP OUT` port | — (ADC device) |

## Before You Start

| Model | RS-232C output | What is needed |
|-------|----------------|----------------|
| **BSM-1700 series** | Present | Collect directly over serial. If a cable is already fitted, confirm it is free and not feeding another system. |
| **BSM-3000 series (e.g. BSM-3763)** | **Not on the base interface** | Add an RS-232C output interface — **`QF-910P`** or an RS-232C-capable **`QI-373P`** — for numeric data. |
| **BSM-6000 series (BSM-6301 / 6501 / 6701, incl. K variants)** | Present only with the optional interface unit | **`QI-631P`** for BSM-6301; **`QI-671P`** for BSM-6501 / BSM-6701. Both provide the RS-232C socket. |
| ECG / invasive BP **waveforms**, any model | Separate analog path | **`ECG/BP Output Cable`** — `YJ-910P` or `YJ-920P` — on the `ECG/BP OUT` port, plus an ADC. |

Confirm the exact interface unit that applies to a given serial number with Nihon Kohden — the option list differs between the A and K market variants.

## Connection Steps

### Numeric Data

1. Identify the **RS-232C socket** (DB-9 female, marked with the serial `IOIOI` icon) on the interface unit's panel. Do not confuse it with the 15-pin RGB/video socket (`IOI`) directly below it, or with the RJ-45 network socket.

   <img src="../hardware_images/nihon_kohden_bsm_1.png" width="300" alt="BSM interface unit connector panel with the DB-9 RS-232C socket outlined in red, above the 15-pin video socket, the RJ-45 network socket and the ECG/BP OUT connector">

2. Attach a **Null Modem (M/F)** adapter to that socket. Screwing it down keeps it from working loose.
3. Connect a **direct serial cable** from the adapter to the PC's DB-9M port or a USB-Serial converter.

### ECG / ART Waveform

The RS-232C link carries numeric data only. ECG and arterial pressure waveforms come out of the **`ECG/BP OUT`** port as analog voltages, visible on the same connector panel as the serial socket.

1. Plug the Nihon Kohden **ECG/BP output cable** (`YJ-910P` or `YJ-920P`) into the `ECG/BP OUT` port.
2. Build a **5.5pi Mono ↔ RJ45** cable to bring the analog outputs into the ADC (SNU-ADC / SNUADCM, DataQ DI-149/DI-155, …).
3. Connect the ADC to the PC via USB.

## Device Configuration

No monitor-side menu change is normally required.

- Serial: **RS-232C**. The BSM RS-232C socket supports **9600 / 19200 / 38400 baud**. If nothing arrives, confirm the port's configured baud rate with Nihon Kohden.

## Vital Recorder Setup

- In Vital Recorder, add **Patient monitor → Nihon Kohden : BSM**.

## Troubleshooting

- **The port opens but no data arrives.** Confirm the **Null Modem (M/F)** is fitted on the QI-373P RS-232C port. Then confirm the port's baud rate (9600 / 19200 / 38400) with Nihon Kohden.
- **No RS-232C socket on the panel.** The interface unit is missing or is a variant without the serial option — see the [Model / Interface Matrix](#before-you-start). No cable will help.
- **Numerics arrive but no waveforms.** Expected: the RS-232C link carries numeric data only. Waveforms need the `ECG/BP OUT` path and an ADC.
- **Central-server path delivers nothing.** The HL7 plug-in is not installed on the server, or the ADT device was not given the monitor's bed name — see the central-server path under Notes.

## Known Limitations

- The RS-232C link carries **numeric data only**; waveforms need the `ECG/BP OUT` path and an ADC.
- **Ventilator parameters displayed on a BSM** (ventilator wired to the monitor with a Nihon Kohden cable) are **not** available on the monitor's serial port; they only come through the central server, or by connecting the ventilator directly (a Y-cable on the Nihon Kohden ventilator cable works).
- **CSM / LifeScope** models are less well verified than BSM — treat support as unconfirmed. **CSM 1702 / PSM** are expected to speak the BSM protocol but unverified — test before committing an installation. ❓ *Unverified — tracked in [unverified.md](../unverified.md).*

## Notes

- **Central-server path (no per-bed cable).** Where a Nihon Kohden **central station** with the HL7 gateway is installed, Vital Recorder can take data from the server instead of per-bed serial: add **three** devices — `NIHONKOHDEN::ADT` (patient ID, server port **9007**), `NIHONKOHDEN::ORF` (numerics every 30 s, port **7999**) and `NIHONKOHDEN::NealTime` (waveforms, port **9001**, at most three waves — default ECG_II, PLETH, AWP). The ADT device must be given the monitor's bed name. The gateway's *Start Code* setting must match what the client expects, and changing it can break the site's EMR feed — coordinate with Nihon Kohden. Without the HL7 plug-in the server delivers nothing. Where there is no central server, per-bed serial is the only route.
- The `QI-373P` interface carries **both** the RS-232C socket and the `ECG/BP OUT` port, so a single added board can serve numeric and waveform collection — but the waveform side still needs its own output cable and an ADC.
