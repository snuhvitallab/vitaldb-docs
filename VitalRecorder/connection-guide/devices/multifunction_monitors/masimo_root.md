# Masimo ROOT

<!-- meta
category: Multifunction Monitor
manufacturer: Masimo
vr_device_name: Root
-->
> **Note:** **Power-cycle the ROOT after changing the USB baud rate.** The new rate takes effect after restart.

| Cable | Adapter | Port | Serial | VR Device Name |
|-------|---------|------|--------|---------------- |
| Masimo data-acquisition USB cable (preferred) | None | USB1 or USB2 | ASCII 1 — 19200 baud | `Root` |

## Connection Steps
1. Plug the Masimo data-acquisition USB cable into **USB1** or **USB2** on the rear of Root.
   <img src="../hardware_images/masimo_root_8.png" width="450" alt="ROOT rear panel — Iris ports 1 to 4, round nurse call jack, RJ45 LAN port, and USB ports 2 and 1">

   <img src="../hardware_images/masimo_root_9.png" width="450" alt="USB cable plugged into a USB port on the ROOT rear panel, below the RJ45 LAN port">

2. Connect the other end to the PC.

## Device Configuration
1. From the **main menu**, select **DEVICE SETTINGS**.

   <img src="../hardware_images/masimo_root_1.png" width="450" alt="ROOT main menu — SOUNDS, DEVICE SETTINGS, ABOUT">

2. The device settings screen offers **BRIGHTNESS**, **ACCESS CONTROL** and **DEVICE OUTPUT**. Select **ACCESS CONTROL**.

   <img src="../hardware_images/masimo_root_2.png" width="450" alt="ROOT device settings screen — BRIGHTNESS, ACCESS CONTROL and DEVICE OUTPUT tiles">

3. An on-screen keyboard prompts for the access-control password. Enter **`6274`**.

   <img src="../hardware_images/masimo_root_3.png" width="450" alt="Enter password screen with on-screen keyboard, shown over the greyed-out access control list">

4. Scroll the access-control list to **USB Port 1 baudrate** and **USB Port 2 baudrate**. From the factory these read **921600**.

   <img src="../hardware_images/masimo_root_4.png" width="450" alt="Access control list — power on profile, alarm and standby options, with USB Port 1 and USB Port 2 baudrate both at the 921600 default">

5. Set both baud rates to **19200**.

   <img src="../hardware_images/masimo_root_5.png" width="450" alt="USB Port 1 and USB Port 2 baudrate both set to 19200, each with a warning that the change takes effect after the next power cycle">

6. Go back to **DEVICE SETTINGS** and this time select **DEVICE OUTPUT**.

   <img src="../hardware_images/masimo_root_6.png" width="450" alt="Device settings tile row — DEVICE OUTPUT at the right">

7. Set **USB Port 1** and **USB Port 2** to **ASCII 1**.

   <img src="../hardware_images/masimo_root_7.png" width="450" alt="Device output screen — nurse call trigger and polarity above USB Port 1 and USB Port 2, both set to ASCII 1">

8. Restart Root to apply the baud rate changes.

## Vital Recorder Setup

Add the device as **`Root`** and select the PC serial port assigned to the data-acquisition cable.
