# LiDCO

<!-- meta
category: Hemodynamic Monitor
manufacturer: LiDCO
vr_device_name: LiDCO
-->
| Cable | Adapter | Port | Baud Rate | VR Device Name |
|-------|---------|------|-----------|----------------|
| Direct Serial | Null Modem M/F | Serial port | 57600 | `LiDCO` |

## Connection Steps
1. Attach a **Null Modem (M/F)** to the rear serial port.
2. Connect a direct serial cable to the PC via USB-Serial converter.

   <img src="../hardware_images/lidco_2.png" width="450" alt="LiDCO — rear serial port">

## Device Configuration
Navigate to **Settings → Communications → Serial** and configure:

| Parameter | Value |
|-----------|-------|
| LiDCO Serial | Enabled |
| Baud Rate | 57600 |
| Stop Bits | 1 |
| Data Bits | 8 |
| Parity | None |
| Average | Never |
| Observation | Beat-to-beat |

<img src="../hardware_images/lidco_1.png" width="450" alt="LiDCO serial settings">


---

## Infusion Pumps
