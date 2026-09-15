# Belmont FMS (Rapid Infuser RI-2 / FMS2000)

<!-- meta
category: Syringe Pump
manufacturer: Belmont
vr_device_name: FMS
-->
> ⚠️ **The device port is DB-9 male, so an F/F Null Modem adapter is required** — the opposite of most devices in this guide. The port is also hidden behind the lower vent panel and is easy to miss.

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|----------------|
| Direct serial (DB-9M ↔ DB-9F) | Null Modem **F/F** | Serial (DB-9M), behind the lower vent panel | `FMS` |

Because the device presents a **male** DB-9 and the PC also presents a male DB-9, the **F/F** Null Modem adapter is what makes the connection fit while providing the required crossover. An M/F changer will not mate.

## Connection Steps
1. Locate the serial port on the chassis **beside the lower vent grille**. It is a **DB-9 male** connector recessed into the housing, with a jack screw on either side.

   <img src="../hardware_images/belmont_fms_1.png" width="350" alt="Belmont FMS chassis beside the lower vent grille with the recessed DB-9 male serial connector circled">

2. Screw the **Null Modem (F/F)** adapter onto the male connector on the device. Leaving it permanently attached avoids repeated confusion over which cable is in use.
3. Connect a **direct** serial cable from the adapter to the PC, via a USB-Serial converter if the PC has no DB-9 port.

## Device Configuration
- No menu setting is required on the infuser for data output — the F/F Null Modem adapter plus a direct cable is the entire connection.
- **Serial parameters (baud rate, parity, data bits, stop bits) are not published in the publicly available Belmont operator's manual — verify with the manufacturer** if the device connects but decodes nothing. Do not guess these values.

## Vital Recorder Setup

- Add the device in Vital Recorder as **`FMS`**.

## Notes
- The `FMS` device covers the Belmont Rapid Infuser family (RI-2 / FMS2000) as a rapid fluid infuser rather than a syringe pump, but it is configured in Vital Recorder from the same device list.
- The port's location behind the vent panel means the cable is easily snagged when the unit is repositioned. Route it clear of the vent so airflow is not obstructed.
- **Do not improvise the adapter.** An M/F changer will not mate with the device's male port, and stacking adapters to force a fit strains the connector. If no F/F Null Modem is on hand, order one rather than substituting a cross cable or another adapter combination.
