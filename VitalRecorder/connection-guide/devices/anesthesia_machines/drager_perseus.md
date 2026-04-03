# Drager Perseus

<!-- meta
category: Anesthesia Machine
manufacturer: Drager
vr_device_name: MedibusX
-->
| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|----------------|
| Direct Serial | Null Modem F/F | COM1 or COM2 | `MedibusX` |

## Connection Steps
1. Attach a **Null Modem (F/F)** adapter to the serial port.
2. Connect a direct serial cable from the adapter to the PC via USB-Serial converter.

   <img src="../hardware_images/drager_perseus_4.png" width="450" alt="Perseus serial port connection">

## Device Configuration
1. Navigate to **System Settings → System Menu**. Enter password **`0000`**.

   <img src="../hardware_images/drager_perseus_3.png" width="450" alt="System Menu — password entry">

2. Select **Interface Configuration**.

   <img src="../hardware_images/drager_perseus_2.png" width="450" alt="Interface Configuration menu">

3. For the connected port (COM1 or COM2), set **Protocol → MEDIBUS** and **Baud Rate → 9600**.

   <img src="../hardware_images/drager_perseus_1.png" width="450" alt="MEDIBUS + 9600 baud rate">
