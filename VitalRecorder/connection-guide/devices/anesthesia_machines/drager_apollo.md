# Dräger Apollo / Cicero EM Color / Julian / Primus / Vamos

<!-- meta
category: Anesthesia Machine
manufacturer: Dräger
vr_device_name: Primus
-->
> **Note:** These machines ship with COM1 already set up for MEDIBUS, so **no additional device configuration is normally required**. Only verify the serial parameters if no data appears.

| Cable | Adapter | Port | Serial | VR Device Name |
|-------|---------|------|--------|----------------|
| Direct Serial | None | COM1 (rear) | 9600 baud, 8 data bits, Even parity, 1 stop bit — MEDIBUS | `Primus` |

## Connection Steps
1. Locate **COM 1** on the rear connector panel. The panel carries **COM 1**, **COM 2** and an **IV System** connector side by side — use **COM 1**.

   <img src="../hardware_images/drager_anesthesia_1.png" width="450" alt="Dräger anesthesia machine rear connector panel — COM 1 (circled in red) with a serial cable attached, beside COM 2 and IV System">

2. Connect a **direct (straight-through) serial cable** to COM 1. No Null Modem adapter is needed on these models.
3. Connect the other end to the PC via a USB-Serial converter.
4. In Vital Recorder, add the device as **`Primus`** — see [Device Name in Vital Recorder](#vital-recorder-setup).

> If COM1 is already in use, see [When the COM1 Port is Already in Use](#when-the-com1-port-is-already-in-use) below.

## Device Configuration
Nothing has to be changed on these models. If no data arrives, check the machine's serial parameters and set them to:

- Serial: **9600 baud, 8 data bits, Even parity, 1 stop bit**
- Protocol: **MEDIBUS**

On machines that expose the setting on screen it is reached from the interface page of the system setup menu (**System setup → System → Interfaces** on newer software). Select the COM port that matches the cable you connected — the other COM port is frequently occupied by the hospital EMR gateway.

> ⚠️ **The baud rate must match the protocol version.** MEDIBUS runs at **9600**, MEDIBUS.X at **19200**. A mismatch appears as a `MEDIBUS COM2` message or as a repeated `COM1 failure` on the machine.

## Vital Recorder Setup
- Machines speaking **MEDIBUS (9600)** are added as **`Primus`**; **`MedibusX`** is the entry for **MEDIBUS.X (19200)** devices.
- From Vital Recorder **1.19.22**, Dräger anesthesia machines can also be selected **by model name**, and a generic **`Medibus`** entry is available for models that are not listed.
- With **`AUTO_DETECT=1`** in `vr.conf` (Vital Recorder **1.19.0** or later), Dräger MEDIBUS / MEDIBUS.X machines are found on the serial line with no `[DEV/...]` section at all. From 1.19.22 detection identifies them by protocol name rather than by model.

## When the COM1 Port is Already in Use

If the Dräger COM1 port is already transmitting data to a patient monitor (e.g., CO2 curve, airway pressure), use a **Y-cable** to read data without disrupting existing communication.

> ⚠️ When using a Y-cable, enable **"Read Only Mode"** in Vital Recorder when adding the device.

**Y-cable Wiring:**

The machine's COM1 is **DB-9 female**, so the Y-cable's machine end is a **DB-9 male plug** and mates with it directly. CON1 is **DB-9 female** and mates with the existing device's DB-9 male connector. **No gender adapter is used anywhere in this assembly.**

```
Dräger COM1 (DB9F) ──┤ DB9M  Y-cable  CON1 (DB9F) ├── existing device (DB9M)
                                      CON2 (DB9F) ├── PC via USB-Serial converter
```

| Machine end — DB-9 male plug | CON1 — to the existing device (DB-9F) | CON2 — to Vital Recorder (DB-9F) |
|-------------------------------|----------------------------------------|-----------------------------------|
| 2 — TX (machine transmit)     | 2 — RX                                 | 2 — RX                            |
| 3 — RX (machine receive)      | 3 — TX                                 | *not connected*                   |
| 5 — GND                       | 5 — GND                                | 5 — GND                           |

Only the machine's transmit line and ground are branched to CON2, so Vital Recorder listens without ever driving the line.

> **Reading the pin numbers.** Signal names here are given **from the machine's side**: on the Dräger COM1, pin 2 transmits and pin 3 receives. The [Cable Types](../README.md#cable-types) table in the main README names the same pins **from the PC's side**, where pin 2 receives and pin 3 transmits. Both describe the same straight-through link.

<img src="../hardware_images/com1_in_use_1.png" width="450" alt="Y-cable pin wiring diagram — machine TX (pin 2) and GND (pin 5) branch to both CON1 and CON2 (PC Vital Recorder, read-only option); RX (pin 3) goes only to CON1">

> **Atlan Anesthesia Machine:** Attach a cross-gender adapter on both the anesthesia machine side and the CON1 side. CON2 is used as-is for data reading.

## Notes
- **Recommended version:** MEDIBUS communication was stabilized in Vital Recorder **1.19.11** (repeated `COM1 failure` fixed with a 2-second keep-alive) and **1.19.12** (connection stability, serial-line noise). Models that transmit no waveforms were fixed in **1.19.20**.
- **Waveforms** must be requested explicitly with `wavs=` in the device section — up to 4 at a time, Vital Recorder **1.19.15** or later (e.g. `wavs=AWP,AWF`).
- **Y-cable (read-only) taps:** waveform naming was fixed in **1.19.16**, manual waveform ordering via `wavs=` added in **1.19.17**, and waveform-type auto-detection for Y-cable connections added in **1.19.18**.
- In `vr.conf`, `port=` must be the actual serial port name of the converter channel (e.g. `C1`), not `COM1`.
