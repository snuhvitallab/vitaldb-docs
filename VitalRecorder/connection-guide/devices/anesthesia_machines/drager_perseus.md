# Dräger Perseus

<!-- meta
category: Anesthesia Machine
manufacturer: Dräger
vr_device_name: MedibusX
-->
> **Note:** The COM port is off by default and is enabled from a **password-protected** configuration page. See [Device Configuration](#device-configuration).

| Cable | Adapter | Port | Serial | VR Device Name |
|-------|---------|------|--------|----------------|
| Direct Serial | Null Modem F/F | COM 1 or COM 2 | **MEDIBUS.X 19200** → `MedibusX`, or **MEDIBUS 9600** → `Primus` — match the protocol set on the port | `MedibusX` / `Primus` |

## Connection Steps
1. Open the interface panel on the machine column. It carries a **male DB-9 serial connector** together with a USB port and a LAN (RJ-45) socket.
2. Attach a **Null Modem (F/F)** adapter to the DB-9 serial port.
3. Connect a direct serial cable from the adapter to the PC via a USB-Serial converter.

> The Perseus has **two RS-232 ports (COM 1 and COM 2)**. Either can be used, but only the port you enable in the interface page transmits — the other is often already assigned to the hospital EMR gateway.

## Device Configuration
1. Open **System setup** and go to the **System** tab.
2. Enter the **configuration password** on the numeric keypad and confirm with **OK**. The factory default is **`0000`**; sites can change it, so ask biomedical engineering if it is rejected.
3. Choose **Interface** from the list on the right — the page holding the DHCP / IP address / subnet mask / default gateway, **RS232**, LAN and USB settings.
4. In the **COM 1** (or **COM 2**) block, set:

- **Protocol:** **MEDIBUS.X** with **19200** baud (add as `MedibusX`), or **MEDIBUS** with **9600** baud (add as `Primus`) — the original connection guide uses the MEDIBUS / 9600 pairing. *None* disables the port.
- **Baud rate:** selectable values are 1200, 2400, 4800, 9600, 19200 and 38400
- The frame format is fixed and shown next to the baud rate as **8, e, 1** (8 data bits, Even parity, 1 stop bit)

> ⚠️ **Match the baud rate to the protocol.** MEDIBUS.X runs at **19200** and pairs with the `MedibusX` device entry; legacy MEDIBUS runs at **9600** and pairs with `Primus`. A mismatch produces a `MEDIBUS COM2` message or a repeated `COM1 failure` on the machine.

## Vital Recorder Setup

- In Vital Recorder, add the device as **`MedibusX`**.

## Notes
- **Recommended version:** MEDIBUS / MEDIBUS.X communication was stabilized in Vital Recorder **1.19.11** (repeated `COM1 failure` fixed with a keep-alive) and **1.19.12**. Model-name selection and the generic `Medibus` entry arrived in **1.19.22**.
- With **`AUTO_DETECT=1`** in `vr.conf` (Vital Recorder **1.19.0** or later), Dräger MEDIBUS / MEDIBUS.X machines are detected on the serial line without a `[DEV/...]` section.
- **Waveforms** must be requested with `wavs=` in the device section — up to 4 at a time, Vital Recorder **1.19.15** or later (e.g. `wavs=AWP,AWF`).
- In `vr.conf`, `port=` must be the actual serial port name of the converter channel (e.g. `C1`), not `COM1`.
- The same Interface page also sets the machine name and the MEDIBUS time-synchronisation source; neither is needed for recording.
