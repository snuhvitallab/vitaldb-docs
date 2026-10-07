# Medtronic (Aspect Medical) BIS VISTA

<!-- meta
category: Brain Monitor
manufacturer: Medtronic
vr_device_name: VISTA
-->
> **Note:** **Use a direct serial cable only. A cross cable can drive the monitor into an "Unrecoverable Monitor Exception" screen, which halts monitoring until the unit is reset.**

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|---------------- |
| direct serial cable | None | RS-232 port | `VISTA` |

## Connection Requirements

| Serial Protocol option | What it carries | Vital Recorder device to select |
|----------|------|------ |
| **ASCII** | All numeric parameters (BIS, EMG, SQI, SR) | `VISTA` |
| **Legacy Binary** | Numerics **plus 128 Hz EEG waveform** | `BIS (binary)` |
| VISTA Binary | Vendor-specific binary format — not used by Vital Recorder | — |

Serial: **57600 baud**. Choose **Legacy Binary** if the EEG waveform is needed; **ASCII** is sufficient for numerics only.

## Connection Steps
1. Connect a **direct serial cable** (NOT a cross cable) to the RS-232 port.

   <img src="../hardware_images/medtronic_bis_vista_9.png" width="450" alt="BIS VISTA error screen after an incorrect (cross) cable connection — 'Unrecoverable Monitor Exception c0000005, 3817c, BSup — Press Reset or use reset button located on the rear panel of the VISTA monitor'">

   If this screen appears, the cable is wrong. Disconnect it, press the on-screen **Reset** or the recessed reset button on the rear panel, and re-connect with a direct cable.

## Device Configuration

1. Press the **MENU** key on the left-hand button strip of the monitoring screen.

   <img src="../hardware_images/medtronic_bis_vista_1.png" width="450" alt="BIS VISTA monitoring screen showing the BIS number, EMG bar, EEG waveform and trend graph, with the MENU key on the left button strip circled">

2. On the first menu page press **Next**.

   <img src="../hardware_images/medtronic_bis_vista_2.png" width="450" alt="BIS VISTA menu page 1 — Target Range, Secondary Variable, Chart Data, Alarm Volume, BIS/EEG, View/Save Settings, Help, Snapshot, with Next circled at the bottom right">

3. On the second menu page press **Next** again.

   <img src="../hardware_images/medtronic_bis_vista_3.png" width="450" alt="BIS VISTA menu page 2 — Display SR, Monitor Mode, Export Data, BIS Smoothing Rate, Print, Configuration, Previous, with Next circled at the bottom right">

4. On the third menu page press **Maintenance**.

   <img src="../hardware_images/medtronic_bis_vista_4.png" width="450" alt="BIS VISTA menu page 3 — EEG Channels, Date and Time, Language, Filters, Impedance Checking, Previous, Demo Case, Diagnostics, with Maintenance circled">

5. In the **Maintenance** menu press **Serial Protocol**.

   <img src="../hardware_images/medtronic_bis_vista_5.png" width="450" alt="BIS VISTA Maintenance menu — BISx Connection History, Software Update, Restore Default Settings for All Modes, Calibrate Touch Screen, Return to Previous Menu, with Serial Protocol circled">

6. Tick the protocol you need, then press **Save Setting**.

   - **ASCII** — all numeric data.

     <img src="../hardware_images/medtronic_bis_vista_6.png" width="450" alt="BIS VISTA Serial Protocol screen with the ASCII checkbox ticked and circled; Legacy Binary and VISTA Binary unticked; Save Setting button at the bottom right">

   - **Legacy Binary** — numerics plus the 128 Hz EEG waveform. Select **BIS (binary)** as the device in Vital Recorder.

     <img src="../hardware_images/medtronic_bis_vista_7.png" width="450" alt="BIS VISTA Serial Protocol screen with the Legacy Binary checkbox ticked and circled; ASCII and VISTA Binary unticked">

7. Press **Return to Previous Menu → Home**, then **restart the monitor**. The new protocol is not active until the unit has been power-cycled.

## Vital Recorder Setup

- With **ASCII** selected on the monitor, add the device as **`VISTA`**.
- With **Legacy Binary** selected, add it as **`BIS (binary)`** instead — this is the only way to record the 128 Hz EEG waveform.
