# Dräger Atlan

<!-- meta
category: Anesthesia Machine
manufacturer: Dräger
vr_device_name: MedibusX
-->
> **Note:** The Atlan speaks Dräger **MEDIBUS.X** and is added in Vital Recorder as **`MedibusX`**, the same entry as the Perseus. The COM port must be set to MEDIBUS.X at 19200 before data arrives.

| Cable | Adapter | Port | Serial | VR Device Name |
|-------|---------|------|--------|----------------|
| direct serial cable | Null Modem adapter (F/F) | COM 1 or COM 2 | 19200 baud, 8 data bits, Even parity, 1 stop bit — MEDIBUS.X | `MedibusX` |

## Connection Steps
1. Locate the **DB-9 serial port** (**COM 1** or **COM 2**) on the machine.
2. Attach a **Null Modem adapter (F/F)** to the port.
3. Connect a direct serial cable from the adapter to the PC via a USB-Serial converter.

### When the COM Port is Already in Use
If the port is already transmitting to another device, a **Y-cable** can tap the line. Fit a Null Modem adapter matching the connector on both the machine side and the CON1 side; CON2 is used as-is for data reading:

```
Atlan COM (DB9F) --- Null Modem adapter (F/F) --- DB9M  Y-cable  CON1 (DB9F) --- Null Modem adapter (M/F) --- existing device
```

The Y-cable wiring is the same as on the [Dräger Apollo page](drager_apollo.md#when-the-com1-port-is-already-in-use).

## Device Configuration
Set the cabled COM port to **Protocol: MEDIBUS.X**, **Baud rate: 19200**. The frame is 8 data bits, Even parity, 1 stop bit. The menu path on the Atlan is not documented in this guide; check the Dräger documentation or ask Dräger service.

> **Note:** **Keep the baud rate at 19200.** Any other value produces a `MEDIBUS COM2` message or a repeated `COM1 failure` on the machine.

## Vital Recorder Setup

- In Vital Recorder, add the device as **`MedibusX`**.
- **Waveforms:** Vital Recorder asks the machine which waveforms it offers and requests up to 4 of them, so `wavs=` is not needed. Set `wavs=` in the device section only to choose specific ones, e.g. `wavs=AWP,AWF`.

## Troubleshooting

- **Repeated `COM1 failure` on the machine and no waveforms recorded.** Fixed in Vital Recorder 1.19.11 (keep-alive signal and response handling) — see the [official version history](https://vitaldb.net/vital-recorder/?action=versions). Update before changing the cable.

## Notes

- With **`AUTO_DETECT=1`** in `vr.conf` the machine is detected on the serial line without a `[DEV/...]` section.
