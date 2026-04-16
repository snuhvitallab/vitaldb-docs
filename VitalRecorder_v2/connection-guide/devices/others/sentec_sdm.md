# Sentec SDM

<!-- meta
category: Other
manufacturer: Sentec
vr_device_name: SDM
-->
> **Note:** Protocol and baud rate must be configured on the device. See Device Configuration below.

| Cable | Adapter | Protocol | Baud Rate | VR Device Name |
|-------|---------|----------|-----------|----------------|
| USB-Serial Converter | None | SenTecLink | 115200 | `SDM` |

## Connection Steps
1. Connect a **USB-Serial Converter** directly to the serial port on the rear.
2. Connect the USB end to the PC.

   <img src="../hardware_images/sentec_sdm_2.png" width="300" alt="Sentec SDM — rear serial port">

## Device Configuration
Navigate to **Interfaces → Serial Interface** and configure:

| Parameter | Value |
|-----------|-------|
| Protocol | SenTecLink |
| Baud Rate | 115200 |

<img src="../hardware_images/sentec_sdm_1.png" width="450" alt="Serial Interface — SenTecLink + 115200">
