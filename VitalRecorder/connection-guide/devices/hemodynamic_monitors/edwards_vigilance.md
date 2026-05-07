# Edwards Lifesciences Vigilance

<!-- meta
category: Hemodynamic Monitor
manufacturer: Edwards Lifesciences
vr_device_name: Vigilance
-->
> **Note:** Digital port configuration is required before use. See Device Configuration below.

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|----------------|
| Direct Serial | Null Modem M/F | COM1 (or COM2) | `Vigilance` |

## Connection Steps
1. Attach a **Null Modem (M/F)** to COM1.
2. Connect a direct serial cable from the adapter to the PC via USB-Serial converter.

   <img src="../hardware_images/edwards_vigilance_3.png" width="450" alt="Vigilance — rear COM ports">

## Device Configuration
1. Press **Setup → System Config → Return → Digital Ports**.

   <img src="../hardware_images/edwards_vigilance_2.png" width="450" alt="System Config → Digital Ports">

2. Configure COM1:

   | Parameter | Value |
   |-----------|-------|
   | Device | IFMout |
   | Baud Rate | 9600 |
   | Parity | None |
   | Stop Bits | 1 |
   | Data Bits | 8 |
   | Flow Control | 2 seconds |

   <img src="../hardware_images/edwards_vigilance_1.png" width="450" alt="Digital Ports configuration">
