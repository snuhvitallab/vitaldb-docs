# Edwards Lifesciences Vigilance II

<!-- meta
category: Hemodynamic Monitor
manufacturer: Edwards Lifesciences
vr_device_name: Vigilance
-->
> **Note:** Serial port configuration is required before use. See Device Configuration below.

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|----------------|
| Direct Serial | Null Modem M/F | Port 1 — **top** of two serial ports | `Vigilance` |

## Connection Steps
1. Attach a **Null Modem (M/F)** to **Port 1** (top serial port).
2. Connect a direct serial cable to the PC via USB-Serial converter.

   <img src="../hardware_images/edwards_vigilance2_3.png" width="450" alt="Vigilance II — Port 1">

## Device Configuration
1. Press **Setup → Serial Port Setup → Port 1**.

   <img src="../hardware_images/edwards_vigilance2_2.png" width="450" alt="Port 1 selection">

2. Set **Device → IFMout** and **Baud Rate → 9600**.

   <img src="../hardware_images/edwards_vigilance2_1.png" width="450" alt="IFMout + 9600 baud">
