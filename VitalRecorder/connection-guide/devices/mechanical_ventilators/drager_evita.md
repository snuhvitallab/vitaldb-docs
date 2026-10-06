# Dräger EVITA (V300 / V500 / V600 / V800, Evita Infinity V500)

<!-- meta
category: Mechanical Ventilator
manufacturer: Dräger
vr_device_name: MedibusX
-->
> **Note:** The EVITA family speaks Dräger **MEDIBUS.X**. Check [Transmitted Data](#transmitted-data) before committing to a data set: the volume waveform is not transmitted, and CO2 requires a capnography module.

| Cable | Adapter | Port | Serial | VR Device Name |
|-------|---------|------|--------|----------------|
| Direct Serial | Null Modem F/F *(gender unverified — see Notes)* | RS-232 **COM1** (or COM2) on the rear | 19200 baud, 8 data bits, Even parity, 1 stop bit — MEDIBUS.X | `MedibusX` |

## Connection Steps

1. Locate the RS-232 COM port on the rear of the ventilator. Newer units (V600 / V800) also carry an HDMI-style connector — that is not the data port.
2. Fit the adapter the connector calls for (see Notes), then connect a direct serial cable to the PC through a USB-Serial converter.
3. In Vital Recorder, add the device as **`MedibusX`** — see [Vital Recorder Setup](#vital-recorder-setup).

## Device Configuration

In the ventilator's system setup, open the **interface / COM port** page and set the cabled port to **Protocol: MEDIBUS.X**, **Baud: 19200**. The frame is fixed at 8 / Even / 1. The menu path varies by model and software; on the V500 it is in the system-setup interface tab.

## Vital Recorder Setup

- Add the device as **`MedibusX`**. In `vr.conf`, `port=` is the converter channel name (e.g. `C1`), not `COM1`.
- **Waveforms:** Vital Recorder asks the ventilator which waveforms it offers and requests up to 4 of them. To choose specific ones, list them with `wavs=`:

  ```ini
  [DEV/MedibusX]
  type=MedibusX
  port=C1
  wavs=AWP,AWF
  ```

- With `AUTO_DETECT=1` the machine is found on the line without a `[DEV/...]` section.

### Transmitted Data

- **Numerics** (setting and measured): PEEP, FiO2, tidal volume, rate, minute volume and about twenty more arrive normally.
- **Airway pressure (AWP) and flow (AWF) waveforms** are transmitted.
- **The volume waveform is not sent over MEDIBUS.** The volume curve on the ventilator screen is the flow integrated locally; Vital Recorder records only what is transmitted and does not derive tracks. Integrate **AWF** offline if a volume waveform is needed.
- **The CO2 waveform is sent only when a capnography module is fitted.** Its absence on a unit without the module is normal.

## Troubleshooting

- **Nothing at all.** Check the adapter (see Notes), the port's protocol setting, and that no other system already owns the port.
- **Port does not open (`opening failed`).** `port=` is set to `COM1`; use the real converter channel name.
- **Numerics arrive but no waveforms, or a waveform is recorded under the wrong name.** Waveform requests and naming for MEDIBUS devices were fixed in 1.19.15/1.19.16 (an Evita V600 sending only AWP had it stored as CO2); upgrade. If `wavs=` is set, remove it and test again.
- **Vital Recorder restarts repeatedly when a MEDIBUS device is attached.** A SIGSEGV loop present from 1.15.11 to 1.18.39 — fixed in 1.18.40; upgrade.
- **`COM1 failure` repeating on the ventilator.** Keep-alive and reply handling were fixed in 1.19.11 — upgrade.

## Notes

- **Adapter gender is unverified.** The Evita Infinity V500 has been grouped with the Fabius and Zeus as taking a null modem; the [Fabius page](../anesthesia_machines/drager_fabius.md) shows that the answer depends on the COM connector's gender (F/F onto a male port, M/F onto a female one). Look at the EVITA's connector and record which adapter worked.
- **No photographs yet** — the rear connector panel and the interface menu would be the most useful additions.
