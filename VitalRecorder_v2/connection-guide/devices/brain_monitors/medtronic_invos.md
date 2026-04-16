# Medtronic INVOS Cerebral/Somatic Oximetry

<!-- meta
category: Brain Monitor
manufacturer: Medtronic
vr_device_name: Invos
-->
> **Note:** The INVOS RS-232 port is **male-type** — an F/F adapter is required.

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|----------------|
| Direct Serial | Null Modem F/F | `\|O\|O\|` port (male connector) | `Invos` |

## Connection Steps
1. Attach a **Null Modem (F/F)** adapter to the `|O|O|` male port on the rear.
2. Connect a direct serial cable from the adapter to the PC via USB-Serial converter.

   <img src="../hardware_images/medtronic_invos_1.png" width="450" alt="INVOS — rear |O|O| port">

## Device Configuration
1. Press **Next Menu → Output Select → Digital Output → PC Link → OUTPUT FORMAT 1**.

   <img src="../hardware_images/medtronic_invos_2.png" width="450" alt="OUTPUT FORMAT 1">
