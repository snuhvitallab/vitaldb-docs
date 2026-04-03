# Maquet Servo-i Ventilator

<!-- meta
category: Anesthesia Machine
manufacturer: Maquet
vr_device_name: Servo-i
-->
> ⚠️ **Connect to the BOTTOM RS-232 port only.** The TOP RS-232 port is a debugging port and cannot be used.
> If the bottom port is already occupied, route data through the patient monitor (Servo-i → Philips Intellivue → Vital Recorder).

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|----------------|
| Direct Serial | Null Modem M/F | **BOTTOM** RS-232 port | `Servo-i` |

## Connection Steps
1. Identify the **BOTTOM RS-232 port** on the device.

   <img src="../hardware_images/maquet_servo_i_1.png" width="450" alt="Bottom RS-232 port location">

2. Attach a **Null Modem (M/F)** adapter to this port.
3. Connect a direct serial cable from the adapter to the PC via USB-Serial converter.
