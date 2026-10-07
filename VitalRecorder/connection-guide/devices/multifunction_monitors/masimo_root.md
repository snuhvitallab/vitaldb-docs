# Masimo ROOT

<!-- meta
category: Multifunction Monitor
manufacturer: Masimo
vr_device_name: Root
-->
> ⚠️ **Power-cycle the ROOT after changing the USB baud rate.** The new rate takes effect after restart.

| Cable | Adapter | Port | Serial | VR Device Name |
|-------|---------|------|--------|----------------|
| Masimo data-acquisition USB cable (preferred) | None | USB1 or USB2 | ASCII 1 — 19200 baud | `Root` |

## Connection Requirements

**Rainbow sensor:** power on the **Radical-7 first**, then the ROOT. If only the ROOT is already on, turn the ROOT off, turn the Radical-7 on, then turn the ROOT on.

## Connection Steps
1. Identify the ports on the rear of the ROOT: the **Iris** ports (1–4) at the top, a round nurse-call jack, the **LAN** (RJ45) port, and the two **USB** ports numbered **2** and **1** at the bottom.

   <img src="../hardware_images/masimo_root_8.png" width="450" alt="ROOT rear panel — Iris ports 1 to 4, round nurse call jack, RJ45 LAN port, and USB ports 2 and 1">

2. **With the Masimo data-acquisition USB cable (preferred):** plug it into **USB1** or **USB2** and connect the other end to the PC. Windows creates a new USB-Serial COM port.

   <img src="../hardware_images/masimo_root_9.png" width="450" alt="USB cable plugged into a USB port on the ROOT rear panel, below the RJ45 LAN port">


## Device Configuration
1. From the **main menu**, select **DEVICE SETTINGS**.

   <img src="../hardware_images/masimo_root_1.png" width="450" alt="ROOT main menu — SOUNDS, DEVICE SETTINGS, ABOUT">

2. The device settings screen offers **BRIGHTNESS**, **ACCESS CONTROL** and **DEVICE OUTPUT**. Select **ACCESS CONTROL**.

   <img src="../hardware_images/masimo_root_2.png" width="450" alt="ROOT device settings screen — BRIGHTNESS, ACCESS CONTROL and DEVICE OUTPUT tiles">

3. An on-screen keyboard prompts for the access-control password. Enter **`6274`**.

   <img src="../hardware_images/masimo_root_3.png" width="450" alt="Enter password screen with on-screen keyboard, shown over the greyed-out access control list">

4. Scroll the access-control list to **USB Port 1 baudrate** and **USB Port 2 baudrate**. From the factory these read **921600**.

   <img src="../hardware_images/masimo_root_4.png" width="450" alt="Access control list — power on profile, alarm and standby options, with USB Port 1 and USB Port 2 baudrate both at the 921600 default">

5. Set **both** to **19200**. The screen warns that the change takes effect only after the next power cycle.

   <img src="../hardware_images/masimo_root_5.png" width="450" alt="USB Port 1 and USB Port 2 baudrate both set to 19200, each with a warning that the change takes effect after the next power cycle">

6. Go back to **DEVICE SETTINGS** and this time select **DEVICE OUTPUT**.

   <img src="../hardware_images/masimo_root_6.png" width="450" alt="Device settings tile row — DEVICE OUTPUT at the right">

7. Set **USB Port 1** and **USB Port 2** to **ASCII 1**. Leave the nurse-call settings alone.

   <img src="../hardware_images/masimo_root_7.png" width="450" alt="Device output screen — nurse call trigger and polarity above USB Port 1 and USB Port 2, both set to ASCII 1">

8. **Power-cycle the ROOT:** hold the power button (bottom right) for **more than 8 seconds** to power off, then power on again. The new baud rate is not active until this is done.

## Vital Recorder Setup
- Add the device in Vital Recorder as **`Root`**.
- Once recording, the Root device exposes tracks such as `PSI`, `EMG`, `SR`, `ARTF`, `SO2_1`, `SO2_2`, `SEFL`, `SEFR`, `DELTA_SO2_1/2`, `SPO2`, `BPM`, `PI`, `SPMET`, `SPHB`, `SPOC` and `PVI`.

<img src="../hardware_images/masimo_root_10.png" width="450" alt="Vital Recorder track list for the Root device — DEVICE_DATE, DEVICE_TIME, PSI, EMG, SR, ARTF, SO2_1, SO2_2, SEFL, SEFR, DELTA_SO2_1, DELTA_SO2_2, SPO2, BPM, PI, SPMET, SPHB, SPOC, PVI">

## Troubleshooting
- **Vital Recorder shows the device but no data.** Check that both USB baud rates are set to **19200** and that the ROOT was power-cycled after the change.

## Known Limitations
- The USB ports on the ROOT are **data ports, not host ports** for the recorder — a Masimo cable or a USB-Serial converter is still what creates the COM port on the PC.
