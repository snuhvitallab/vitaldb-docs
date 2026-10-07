# Medtronic (Aspect Medical) BIS A-2000

<!-- meta
category: Brain Monitor
manufacturer: Medtronic
vr_device_name: A2000
-->
> **Note:** Medtronic BIS A2000 is similar to BIS Vista, but BIS A2000 can obtain 2-channel 256Hz EEG.

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|---------------- |
| direct serial cable | None | RS-232 port | `A2000` |

## Connection Steps
1. Connect a direct serial cable to the RS-232 serial port on the lower right of the rear panel.

   <img src="../hardware_images/medtronic_bis_a2000_1.png" width="450" alt="BIS A-2000 rear panel — DB-9 J1 RS-232 serial port circled, below the model label (MONITOR Model A-2000, P/N 185-0070) and beside the AC power inlet">

## Device Configuration
The serial protocol lives several levels deep, in the diagnostic/service area of the menu tree. Navigate with the front-panel keys.

1. Press **Menu** to open the **Setup Menu**, then select **Advanced Setup** (bottom row).

   <img src="../hardware_images/medtronic_bis_a2000_2.png" width="450" alt="A-2000 Setup Menu — Event, Sensor Check, Display Type, BIS Smoothing Rate, with Advanced Setup highlighted on the bottom row">

2. In the **Advanced Setup Menu**, select **Diagnostic Menu**.

   <img src="../hardware_images/medtronic_bis_a2000_3.png" width="450" alt="A-2000 Advanced Setup Menu — Secondary Variable, Time/Date, Print Event, Display Parameter Setup, with Diagnostic Menu highlighted; Save Settings and Return to Setup Menu at the bottom">

3. In the **Diagnostic Menu**, select **System Configuration Menu**.

   <img src="../hardware_images/medtronic_bis_a2000_4.png" width="450" alt="A-2000 Diagnostic Menu — DSC Self Test, Display Self Test, Sensor Data Display, Clear Data, Diagnostic Codes, Impedance Checking, with System Configuration Menu highlighted">

4. On **Serial Port Protocol** choose **Binary**.
5. Press **Return To Diagnostic Menu → Return to Advanced Setup Menu → Save Settings**. Without **Save Settings**, the protocol reverts on the next power cycle.
   <img src="../hardware_images/medtronic_bis_a2000_5.png" width="450" alt="A-2000 System Configuration Menu — Serial Port Protocol row with ASCII / Binary options, Binary selected; Extended Memory and ICU Mode rows below">

## Vital Recorder Setup

- Add the device as **`A2000`** and select the PC serial port used for the connection.
