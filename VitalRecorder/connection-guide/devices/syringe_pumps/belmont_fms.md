# Belmont FMS (Rapid Infuser RI-2 / FMS2000)

<!-- meta
category: Syringe Pump
manufacturer: Belmont
vr_device_name: FMS
-->
> **Note:** **The device port is DB-9 male, so a Null Modem adapter (F/F) is required.** The serial port is behind the lower vent panel.

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|---------------- |
| direct serial cable | Null modem (F/F) | Serial port, behind the lower vent panel | `FMS` |

## Connection Steps
1. Connect a direct serial cable to the serial port using a **null modem adapter (F/F)**.

   <img src="../hardware_images/belmont_fms_1.png" width="450" alt="Belmont FMS chassis beside the lower vent grille with the recessed DB-9 male serial connector circled">

## Device Configuration

No pump-side configuration is required.

## Vital Recorder Setup

- Add the device in Vital Recorder as **`FMS`** and select the PC serial port used for the connection.
