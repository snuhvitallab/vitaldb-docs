# Edwards Lifesciences Vigileo

<!-- meta
category: Hemodynamic Monitor
manufacturer: Edwards Lifesciences
vr_device_name: Vigileo
-->
> **Note:** Serial port configuration is required before use. See Device Configuration below.

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|----------------|
| Direct Serial | Null Modem M/F | Serial port | `Vigileo` |

## Connection Steps
1. Attach a **Null Modem (M/F)** to the rear serial port.
2. Connect a direct serial cable to the PC via USB-Serial converter.

   <img src="../hardware_images/edwards_vigileo_2.png" width="450" alt="Vigileo — rear serial port">

## Device Configuration
1. Tap an **empty space at the bottom left** of the screen to open the setup menu.
2. Select **Serial Port Setup → IFMout** (Device field).

   <img src="../hardware_images/edwards_vigileo_1.png" width="450" alt="Device = IFMout">

3. Select **9600** (Baud Rate field) → **Return** → exit.
