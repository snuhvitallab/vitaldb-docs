# Dräger Fabius / Zeus / Infinity

<!-- meta
category: Anesthesia Machine
manufacturer: Dräger
vr_device_name: Primus
-->
> ⚠️ **Check the machine's manufacture date before ordering a cable.** The Fabius shipped with two different COM1 connectors, and the adapter you need depends on which one is fitted. Read [Before You Start](#before-you-start) first.

| Machine (COM1 connector) | Cable | Adapter | Port | Serial | VR Device Name |
|--------------------------|-------|---------|------|--------|----------------|
| **Female** COM1 — manufactured Oct 2004 onward | Direct Serial | **None** | COM1 | 9600, 8 / Even / 1 — MEDIBUS | `Primus` |
| **Male** COM1 — manufactured before Oct 2004 | Direct Serial | **Null Modem F/F** | COM1 | 9600, 8 / Even / 1 — MEDIBUS | `Primus` |

## Before You Start

Per Dräger's documentation the Fabius COM1 connector changed in **October 2004**, and the two versions assign the transmit and receive pins differently:

| Manufactured | COM1 connector | What to fit |
|---|---|---|
| Before Oct 2004 | **Male** (pins) | Null Modem **F/F** Null Modem adapter at COM1, then a direct serial cable |
| Oct 2004 onward | **Female** (sockets) | Direct serial cable only — **no** adapter |

Identify the connector by looking at COM1 on the machine, not by the model name: the same model was sold across the change. The gender rule is the same one used throughout this guide — an adapter fitted to a **male** device port must be **F/F**, one fitted to a **female** device port must be **M/F**.

If the machine's purchase date is unknown, the connector itself is the answer. Fit nothing on the first attempt if COM1 is female, and see [Troubleshooting](#troubleshooting) if no data arrives.

## Connection Steps

1. Look at **COM1** on the machine and note whether it is male or female.
2. Fit the adapter, if the connector calls for one:
   - **Female COM1** — nothing to fit. Connect a direct serial cable straight from COM1.
   - **Male COM1** — attach a **Null Modem (F/F)** adapter at COM1, then the direct serial cable.
3. Connect the other end of the cable to the PC through a USB-Serial converter.
4. **Fabius only:** enter service mode and set the serial parameters — see [Device Configuration](#device-configuration).
5. In Vital Recorder, add the device as **`Primus`** — see [Vital Recorder Setup](#vital-recorder-setup).

## Device Configuration

**Fabius only.** Zeus and Infinity models are configured from their own system setup / interface menu.

1. Press the **three controls circled in red** at the same time — the **Home** key, the **rotary knob**, and the **Standby** key — to enter service mode. The system diagnostics screen is shown while the machine starts into that mode.

   <img src="../hardware_images/drager_fabius_1.png" width="450" alt="Fabius GS premium front panel with the three controls to press together circled in red — the Home key, the rotary knob and the Standby key — over the SYSTEM DIAGNOSTICS screen">

2. Open **Service → Serial Port Parameters**, select **COM1**, and set:

   | Setting | Value |
   |---|---|
   | Baud rate | **9600** |
   | Data bits | **8** |
   | Parity | **Even** |
   | Stop bits | **1** |
   | Protocol | **MEDIBUS** |

   <img src="../hardware_images/drager_fabius_2.png" width="450" alt="Fabius Service screen &quot;Serial Port Parameters&quot; for COM1 — Baud Rate 9600, Parity EVEN, Stop Bits 1, Data Bits 8, Protocol MEDIBUS">

> ⚠️ **The baud rate must match the protocol version.** MEDIBUS runs at **9600**, MEDIBUS.X at **19200**. A mismatch appears as a `MEDIBUS COM2` message or a repeated `COM1 failure` on the machine.

## Vital Recorder Setup

- The Fabius speaks **MEDIBUS at 9600**, so it is added as **`Primus`** — the entry for MEDIBUS (9600) machines. `MedibusX` is the entry for **MEDIBUS.X (19200)** machines and does **not** apply to a Fabius left at its standard settings.
- What decides the entry is the protocol and baud rate actually set on the machine's COM port, not the model name. If the port has been switched to MEDIBUS.X at 19200, use `MedibusX` instead.
- From Vital Recorder **1.19.22** the Fabius models are listed **by name** in the device dialog, and a generic **`Medibus`** entry covers Dräger models that are not listed.
- With **`AUTO_DETECT=1`** in `vr.conf` (Vital Recorder **1.19.0** or later) the machine is found on the serial line without a `[DEV/...]` section.
- In `vr.conf`, `port=` must be the actual serial port name of the converter channel (e.g. `C1`), not `COM1`.

## Troubleshooting

**The port opens but no data arrives.** Work through these in order — the first two are the common cause, and they are opposites, so establish the COM1 gender before changing anything.

1. **Female COM1 with a Null Modem fitted → remove the adapter.** This is the classic double-crossover: the cable is already straight-through and the adapter swaps pins 2/3 a second time, so both ends transmit at each other.
2. **Male COM1 with no adapter → add a Null Modem F/F adapter** at COM1.
3. **Cable and adapter already match the connector → check the machine, not the cable.** Confirm in service mode that COM1 is set to **MEDIBUS at 9600**, and that the device was added in Vital Recorder as **`Primus`** rather than `MedibusX`.
4. **Everything above checks out → check the Vital Recorder build.** On versions before **1.19.22** a correctly cabled direct connection could open the port and still deliver nothing. *(Version boundary not yet confirmed against a release note — see Notes.)*

## Notes

- MEDIBUS communication was stabilized in **1.19.11** (repeated `COM1 failure`) and **1.19.12** (connection stability, serial-line noise); models that transmit no waveforms were fixed in **1.19.20**.
- **Waveforms** must be requested with `wavs=` in the device section — up to 4 at a time, Vital Recorder **1.19.15** or later.
- Zeus and Infinity are grouped with the Fabius here because they share the MEDIBUS interface, and `Supported_Devices.md` lists Zeus alongside Primus and Fabius at 9600. **Their COM connector gender has not been verified** against Dräger documentation — check the connector before ordering an adapter.
- The 1.19.x version boundaries on this page come from field notes and are **not yet corroborated by a release note in this repository**. Confirm with the Vital Recorder team before treating them as a requirement.

## Sources

- Dräger Fabius service documentation — COM1 connector change of October 2004.
- `VitalRecorder/Supported_Devices.md` — *Primus / Zeus / Fabius, RS-232, 9600 baud*, MEDIBUS protocol.
