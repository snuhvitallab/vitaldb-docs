# Nihon Kohden BSM

<!-- meta
category: Patient Monitor
manufacturer: Nihon Kohden
vr_device_name: BSM
-->
> **Note:** Whether a BSM has an RS-232C output depends on the model and on which optional interface unit is fitted.** Photograph the monitor's connector panel and confirm the model number before ordering anything.

| Cable | Adapter | Port | Serial | VR Device Name |
|-------|---------|------|--------|----------------|
| direct serial cable DB-9M ↔ DB-9F (numeric) | Null Modem adapter (M/F) | RS-232C socket on the interface unit | RS-232C; 9600 / 19200 / 38400 baud (match the interface setting) | `BSM` |
| Nihon Kohden ECG/BP output cable + custom 5.5pi Mono ↔ RJ45 (waveform) | None | `ECG/BP OUT` port | — | — (ADC device) |

## Connection Requirements

| Model | RS-232C output | What is needed |
|-------|----------------|----------------|
| **BSM-1700 series** | Present | Collect directly over serial. If a cable is already fitted, confirm it is free and not feeding another system. |
| **BSM-3000 series (e.g. BSM-3763)** | **Not on the base interface** | Add an RS-232C output interface — **`QF-910P`** or an RS-232C-capable **`QI-373P`** — for numeric data. The `QI-373P` also carries the `ECG/BP OUT` port. |
| **BSM-6000 series (BSM-6301 / 6501 / 6701, incl. K variants)** | Present only with the optional interface unit | **`QI-631P`** for BSM-6301; **`QI-671P`** for BSM-6501 / BSM-6701. Both provide the RS-232C socket. |
| ECG / invasive BP **waveforms**, any model | Separate analog path | **`ECG/BP Output Cable`** — `YJ-910P` or `YJ-920P` — on the `ECG/BP OUT` port, plus an ADC. |

Confirm the exact interface unit that applies to a given serial number with Nihon Kohden — the option list differs between the A and K market variants.

## Connection Steps

### Numeric Data

1. Identify the **RS-232C socket** (DB-9 female, marked with the serial `IOIOI` icon) on the interface unit's panel. Do not confuse it with the 15-pin RGB/video socket (`IOI`) directly below it, or with the RJ-45 network socket.

   <img src="../hardware_images/nihon_kohden_bsm_1.png" width="450" alt="BSM interface unit connector panel with the DB-9 RS-232C socket outlined in red, above the 15-pin video socket, the RJ-45 network socket and the ECG/BP OUT connector">

2. Attach a **Null Modem adapter (M/F)** to that socket. Secure the adapter with the connector screws.
3. Connect a **direct serial cable** from the adapter to the PC's DB-9M port or a USB-Serial converter.

### ECG and Arterial Pressure Waveforms

ECG and arterial pressure waveforms come out of the **`ECG/BP OUT`** port as analog voltages, visible on the same connector panel as the serial socket.

1. Plug the Nihon Kohden **ECG/BP output cable** (`YJ-910P` or `YJ-920P`) into the `ECG/BP OUT` port.
2. Build a **5.5pi Mono ↔ RJ45** cable to bring the analog outputs into the ADC (SNU-ADC / SNUADCM, DataQ DI-149/DI-155, …).
3. Connect the ADC to the PC via USB.

### Network Collection Through a Central Station

Where a Nihon Kohden central station with the HL7 gateway is installed, Vital Recorder can collect data over the network without a per-bed serial cable. Add these three devices:

| Vital Recorder device | Data | Port |
|---|---|---:|
| `NIHONKOHDEN::ADT` | Patient ID | 9007 |
| `NIHONKOHDEN::ORF` | Numeric data every 30 seconds | 7999 |
| `NIHONKOHDEN::NealTime` | Waveforms, up to three — default ECG_II, PLETH and AWP | 9001 |

- Give the ADT device the monitor's bed name.
- The HL7 plug-in must be installed and configured on the server for this network collection path to work.
- The gateway's Start Code must match what Vital Recorder expects. Changing it can break the site's EMR feed, so coordinate with Nihon Kohden.
- Where there is no central station, per-bed serial is the only route.

## Device Configuration

No monitor-side menu change is normally required.

- Serial: **RS-232C**. The BSM RS-232C socket supports **9600 / 19200 / 38400 baud**. If nothing arrives, confirm the port's configured baud rate with Nihon Kohden.

## Vital Recorder Setup

- In Vital Recorder, add **Patient monitor → Nihon Kohden : BSM**.

## Troubleshooting

- **The port opens but no data arrives.** Confirm that the installed interface unit has an RS-232C output and that a **Null Modem adapter (M/F)** is fitted at its socket. Check that the device is added as `BSM` and that the baud rate matches the port's setting (9600 / 19200 / 38400).
- **A BSM-3000 / BSM-6000 or CSM-1500 / CSM-1700 records nothing over serial on a build before 1.19.34.** These models reject the extended request earlier builds sent. Upgrade.

## Known Limitations

- The RS-232C link carries **numeric data only**; waveforms need the `ECG/BP OUT` path and an ADC.
- **Ventilator parameters displayed on a BSM** (ventilator wired to the monitor with a Nihon Kohden cable) are **not** available on the monitor's serial port; they only come through the central station, or by connecting the ventilator directly (a Y-cable on the Nihon Kohden ventilator cable works).
- **CSM-1500 / CSM-1700** are added as `BSM`. **PSM** models have not been tested.
