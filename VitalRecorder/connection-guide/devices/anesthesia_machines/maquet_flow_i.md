# Maquet Flow-i

<!-- meta
category: Anesthesia Machine
manufacturer: Maquet
vr_device_name: Flow-i
-->
> **Note:** Available in Vital Recorder **1.8.16.0** or later. No additional device configuration required.

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|----------------|
| Direct Serial | Null Modem M/F | Serial port — lower right of the rear panel | `Flow-i` |

## Connection Steps
1. Locate the **DB-9 serial port** on the lower right of the rear panel and attach a **Null Modem (M/F cross-gender)** adapter to it.

   <img src="../hardware_images/maquet_flow_i_1.png" width="450" alt="Flow-i rear panel with the DB-9 serial port outlined in red, next to a network connector">

2. Connect a direct serial cable from the adapter to the PC via a USB-Serial converter.
3. In Vital Recorder, add the device as **`Flow-i`**.

## Device Configuration
Nothing has to be set on the machine — the serial port streams as soon as it is cabled.

## Notes
- The Flow-i has **two independent serial ports**, so a patient monitor can keep one while Vital Recorder uses the other. (This is unlike the Servo-i, which has a single usable RS-232 port.)
- The exact line settings (baud / parity) are not documented in our records; the `Flow-i` device driver handles them, so no serial parameters are entered in Vital Recorder. Verify with Getinge documentation if a third-party terminal is used for testing.
- If the port opens but no data arrives, check the Null Modem adapter and that the cable is fully seated before suspecting the machine.
