# GE CARESCAPE B850 / B650 / B450

<!-- meta
category: Patient Monitor
manufacturer: GE
vr_device_name: Bx50
-->
> **Note:** Protocol: **GE S5 Computer Interface** (the Datex DRI protocol, also used by the GE S/5, B40/B20 and B1x5M monitors). Data leaves the monitor through a **USB port**, not through the DB-9 serial connector on the rear panel.

| Cable | Adapter | Port | Serial | VR Device Name |
|-------|---------|------|--------|---------------- |
| Monitor-side USB-Serial converter — **model depends on monitor software version** (see below) | Null Modem adapter (F/F) | **USB port** on the rear panel | GE S5 Computer Interface | `Bx50` |

## Connection Requirements

The **monitor-side USB-Serial converter** must be compatible with the monitor's software version:

| Monitor Software | Monitor-Side Converter |
|---|--- |
| v3.1.4 or later | StarTech ICUSB232V2 |
| v3.1–v3.1.3 | Contact GE about updating the software to a compatible version |
| v2 | ATEN UC-232A, compatible legacy revision (discontinued) |
| v2 — alternative | [MBF-RS232](https://www.compuzone.co.kr/product/product_detail.htm?ProductNo=603276) (Prolific PL2303TA; frequent disconnections reported) |

The **MBF-RS232** has been reported to work as a monitor-side alternative on software **v2**, but the connection may drop frequently and interrupt recording.

Check the software version under **Monitor Setup → Defaults & Service → Service** and confirm converter compatibility for the installed version.

## Connection Steps

1. Plug the **monitor-side USB-Serial converter** that matches the monitor's software version (see above) into one of the USB ports on the rear of the monitor.

   <img src="../hardware_images/ge_carescape_1.png" width="450" alt="Rear three-quarter view of a CARESCAPE monitor; a red circle marks the block of four USB ports on the lower connector strip, to the left of the DVI video connector and the DB-9 serial connector">

2. Connect a **direct serial cable** to the converter using a **null modem adapter (F/F)**.
3. Connect the other end to the PC's serial port or an FTDI-based USB-Serial converter.

   ```
   CARESCAPE USB -- monitor-side USB-Serial converter (DB-9M) -- Null Modem adapter (F/F) -- direct serial cable -- PC-side USB-Serial converter (FTDI) -- PC
   ```

## Device Configuration

No changes to the monitor settings are required for the connection described here.

## Vital Recorder Setup

- Add the device as **`Bx50`** and select the PC serial port used for the connection.
- Default waveforms are `ECG1`, `PLETH`, `IABP1`, `CO2`, and `AWP`. Use `IABP1` for invasive arterial pressure.
- For waveform selection, see [S5 / Datex Device Settings](../../../Configuration_Guide.md#s5--datex-device-settings-ge-solar--bx50--b1x5m--canvas).

## Troubleshooting

- **Communication stops and does not recover on software version 2.** Reconnect the cable at the monitor end. Use a PC-side FTDI converter.
- **Waveforms drop out.** Trim the `wavs=` list if the monitor cannot sustain all of the defaults (`wavs=1,4,8,9,13` — ECG1, PLETH, IABP1, CO2, AWP).
