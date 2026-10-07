# Dräger Perseus

<!-- meta
category: Anesthesia Machine
manufacturer: Dräger
vr_device_name: MedibusX
-->
> **Note:** The COM port is off by default and is enabled from a **password-protected** configuration page. See [Device Configuration](#device-configuration).

| Cable | Adapter | Port | Serial | VR Device Name |
|-------|---------|------|--------|----------------|
| direct serial cable | Null Modem adapter (F/F) | COM 1 or COM 2 | 19200 baud, 8 data bits, Even parity, 1 stop bit — MEDIBUS.X | `MedibusX` |

## Connection Steps
1. Open the interface panel on the machine column. It carries a **male DB-9 serial connector** together with a USB port and a LAN (RJ-45) socket.
2. Attach a **Null Modem adapter (F/F)** to the DB-9 serial port.
3. Connect a direct serial cable from the adapter to the PC via a USB-Serial converter.

> The Perseus has **two RS-232 ports (COM 1 and COM 2)**. Either can be used, but only the port you enable in the interface page transmits — the other is often already assigned to the hospital EMR gateway.

## Device Configuration
1. Open **System setup** and go to the **System** tab.
2. Enter the **configuration password** on the numeric keypad and confirm with **OK**. The factory default is **`0000`**; sites can change it, so ask biomedical engineering if it is rejected.
3. Choose **Interface** from the list on the right — the page holding the DHCP / IP address / subnet mask / default gateway, **RS232**, LAN and USB settings.
4. In the **COM 1** (or **COM 2**) block, set:

- **Protocol:** **MEDIBUS.X**. *None* disables the port.
- **Baud rate:** **19200**
- The frame format is fixed and shown next to the baud rate as **8, e, 1** (8 data bits, Even parity, 1 stop bit)

> ⚠️ **Keep the baud rate at 19200.** Any other value produces a `MEDIBUS COM2` message or a repeated `COM1 failure` on the machine.

## Vital Recorder Setup

- In Vital Recorder, add the device as **`MedibusX`**.
- **Waveforms:** Vital Recorder asks the machine which waveforms it offers and requests up to 4 of them, so `wavs=` is not needed. Set `wavs=` in the device section only to choose specific ones, e.g. `wavs=AWP,AWF`.

## Known Limitations

- **A Y-cable tap does not work on the Perseus.** A direct connection on a free COM port is required.

## Notes

- With **`AUTO_DETECT=1`** in `vr.conf` the machine is detected on the serial line without a `[DEV/...]` section.
- The same Interface page also sets the machine name and the MEDIBUS time-synchronisation source; neither is needed for recording.
