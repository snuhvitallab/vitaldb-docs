# Masimo Radical-7

<!-- meta
category: Multifunction Monitor
manufacturer: Masimo
vr_device_name: Radical7
-->
| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|---------------- |
| direct serial cable | None | **P1 (RS-232)** | `Radical7` |

## Connection Steps

1. Connect a direct serial cable to **P1 (RS-232)** on the rear of the Docking Station.

   <img src="../hardware_images/masimo_radical7_3.png" width="450" alt="Docking Station rear panel — P1 marked RS-232 next to the wider P2 nurse-call/analog connector">

2. Connect a **direct serial cable** from P1 to the PC's serial port. A USB-Serial converter can also be plugged straight into P1 — **no Null Modem adapter is required**.

3. Confirm that the handheld is fully docked before recording.

## Device Configuration

1. From the **main menu**, select **DEVICE SETTINGS**.

   <img src="../hardware_images/masimo_radical7_1.png" width="450" alt="Radical-7 main menu — SOUNDS, DEVICE SETTINGS, ABOUT, 3D">

2. The device settings screen offers **ACCESS CONTROL** and **DEVICE OUTPUT**. Select **DEVICE OUTPUT**.

   <img src="../hardware_images/masimo_radical7_2.png" width="450" alt="Radical-7 device settings screen — ACCESS CONTROL and DEVICE OUTPUT tiles">

3. Set **serial → ASCII 1**, and **analog 1** and **analog 2 → Pleth**.

   <img src="../hardware_images/masimo_radical7_4.png" width="450" alt="Device output screen — serial set to ASCII 1, analog 1 and analog 2 set to Pleth">

4. Scroll down and set **docking station baud rate → 9600**. **SatShare diagnostics** may be left **Enable**.

   <img src="../hardware_images/masimo_radical7_5.png" width="450" alt="Device output screen scrolled down — SatShare diagnostics Enable and docking station baud rate 9600">

- Serial: **9600 baud, 8 data bits, No parity, 1 stop bit, no handshaking (RS-232)**

## Vital Recorder Setup

- Add the device in Vital Recorder as **`Radical7`**.
