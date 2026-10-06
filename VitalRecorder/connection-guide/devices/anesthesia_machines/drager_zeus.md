# Dräger Zeus

<!-- meta
category: Anesthesia Machine
manufacturer: Dräger
vr_device_name: Primus
-->
> ⚠️ **Check the gender of the COM connector before ordering an adapter.** A Null Modem adapter is specified for the Zeus, but the connector gender — and therefore whether it is F/F or M/F — has not been verified on a unit.

| Cable | Adapter | Port | Serial | VR Device Name |
|-------|---------|------|--------|----------------|
| Direct Serial | Null Modem — **F/F onto a male port, M/F onto a female port** | COM (serial) port on the rear | 9600 baud, 8 data bits, Even parity, 1 stop bit — MEDIBUS | `Primus` |

## Connection Steps

1. Locate the serial (COM) port on the rear of the machine and note whether it is **male** or **female**.
2. Fit a **Null Modem adapter** matching the connector — **F/F** on a male port, **M/F** on a female port.
3. Connect a direct serial cable from the adapter to the PC through a USB-Serial converter.
4. In Vital Recorder, add the device as **`Primus`** — see [Vital Recorder Setup](#vital-recorder-setup).

## Device Configuration

The serial port is configured from the machine's own system setup / interface menu. Confirm that the port used is set to **MEDIBUS** at **9600 baud, 8 data bits, Even parity, 1 stop bit**.

> ⚠️ **The baud rate must match the protocol version.** MEDIBUS runs at **9600**, MEDIBUS.X at **19200**. A mismatch appears as a `MEDIBUS COM2` message or a repeated `COM1 failure` on the machine.

## Vital Recorder Setup

- Add the device as **`Primus`** — the entry for MEDIBUS (9600) machines. `Supported_Devices.md` lists the Zeus with the Primus and Fabius at 9600. If the port has been switched to MEDIBUS.X at 19200, use `MedibusX` instead.
- On current builds a generic **`Medibus`** entry also applies, and with **`AUTO_DETECT=1`** in `vr.conf` the machine is found on the serial line without a `[DEV/...]` section.
- **Waveforms** must be requested with `wavs=` in the device section (up to 4).

## Troubleshooting

- **The port opens but no data arrives.** Check the adapter gender first: a Null Modem adapter of the wrong gender cannot be fitted, but a direct connection without one leaves TX connected to TX. Then confirm the port's protocol and baud rate (MEDIBUS / 9600) and that the device was added as `Primus`, not `MedibusX`.

## Notes

- The Zeus shares the MEDIBUS interface with the [Dräger Fabius](drager_fabius.md) and the [Apollo / Primus](drager_apollo.md) family. The Fabius page explains the connector-gender rule in detail.
