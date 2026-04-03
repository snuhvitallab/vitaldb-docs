# Hamilton G5 Ventilator

<!-- meta
category: Anesthesia Machine
manufacturer: Hamilton
vr_device_name: Hamilton
-->
> **Note:** Available in Vital Recorder **v1.10.2 or later**. Either Monitoring Interface port (1 or 2) can be used.

| Cable | Adapter | Port | Protocol | VR Device Name |
|-------|---------|------|----------|----------------|
| Direct Serial | Null Modem M/F | Monitoring Interface 1 or 2 | Block Protocol | `Hamilton` |

## Connection Steps
1. Attach a **Null Modem (M/F)** to either Monitoring Interface port on the rear.
2. Connect a direct serial cable from the adapter to the PC via USB-Serial converter.

   <img src="../hardware_images/hamilton_g5_6.png" width="300" alt="Rear panel — Monitoring Interface ports">

## Device Configuration
> Configuration is only accessible when the device is **not currently operating**.

1. Press the two designated buttons **simultaneously** to open the Configuration menu (bottom left of screen).

   <img src="../hardware_images/hamilton_g5_5.png" width="450" alt="Configuration mode — button combination">

2. Press the two **Test Mode** activation buttons simultaneously to enter Test mode.

   <img src="../hardware_images/hamilton_g5_4.png" width="450" alt="Test mode activation">

3. Navigate to **Configuration → Interface**.

   <img src="../hardware_images/hamilton_g5_3.png" width="450" alt="Configuration → Interface menu">

4. Set the connected port (COM1 or COM2) to **"Block Protocol"**.

   <img src="../hardware_images/hamilton_g5_2.png" width="450" alt="Block Protocol selection">

5. Press **Close → Close/Save**.

   <img src="../hardware_images/hamilton_g5_1.png" width="450" alt="Close and Save confirmation">


---

## Cardiac Monitors


> **Note:** All Edwards Lifesciences devices share the same serial port configuration: **Device = IFMout**, **Baud Rate = 9600**.
