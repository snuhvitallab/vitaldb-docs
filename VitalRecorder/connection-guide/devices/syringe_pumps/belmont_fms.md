# Belmont FMS (Rapid Infuser RI-2 / FMS2000)

<!-- meta
category: Syringe Pump
manufacturer: Belmont
vr_device_name: FMS
-->
> **Note:** **The device port is DB-9 male, so a Null Modem adapter (F/F) is required.** The serial port is behind the lower vent panel.

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|----------------|
| direct serial cable (DB-9M ↔ DB-9F) | Null Modem adapter (F/F) | Serial (DB-9M), behind the lower vent panel | `FMS` |

## Connection Requirements

Because the device presents a **male** DB-9 and the PC also presents a male DB-9, a **Null Modem adapter (F/F)** provides the required fit and crossover. An M/F adapter will not mate.

## Connection Steps
1. Locate the serial port on the chassis **beside the lower vent grille**. It is a **DB-9 male** connector recessed into the housing, with a jack screw on either side.

   <img src="../hardware_images/belmont_fms_1.png" width="450" alt="Belmont FMS chassis beside the lower vent grille with the recessed DB-9 male serial connector circled">

2. Screw the **Null Modem adapter (F/F)** onto the male connector on the device.
3. Connect a **direct** serial cable from the adapter to the PC, via a USB-Serial converter if the PC has no DB-9 port.

## Device Configuration
- No menu setting is required on the infuser for data output — the Null Modem adapter (F/F) plus a direct serial cable is the entire connection.

## Vital Recorder Setup

- Add the device in Vital Recorder as **`FMS`**.

## Notes

- The `FMS` device covers the Belmont Rapid Infuser family (RI-2 / FMS2000) as a rapid fluid infuser rather than a syringe pump, but it is configured in Vital Recorder from the same device list.
- The male device port requires a **Null Modem adapter (F/F)**.
