# Deltex CardioQ / CardioQ-ODM+

<!-- meta
category: Hemodynamic Monitor
manufacturer: Deltex
vr_device_name: CardioQ
-->
| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|---------------- |
| direct serial cable | Null Modem adapter (F/F) | RS-232 serial port | `CardioQ` |

## Connection Steps
1. Connect a direct serial cable to the rear serial port using a **null modem adapter (F/F)**.

   <img src="../hardware_images/deltex_cardioq_1.png" width="450" alt="CardioQ rear panel with the male DB-9 serial port circled, between the RJ-45 network port and the mains inlet">

## Device Configuration
Configure the monitor with **no probe connected**.

1. On the start-up screen, select **Monitor setup**.

   <img src="../hardware_images/deltex_cardioq_4.png" width="450" alt="CardioQ start-up screen reading 'There is no probe connected', with Demo mode, Patients, Monitor setup, Instructions for use and Select user softkeys">

2. Select **General**.

   <img src="../hardware_images/deltex_cardioq_2.png" width="450" alt="Monitor setup functions screen showing the Time/Date, Reset all, Version data, Language, General, User settings, Users and Shift softkeys">

3. Select **Patient monitors**.

   <img src="../hardware_images/deltex_cardioq_3.png" width="450" alt="Monitor setup functions screen after pressing General, now showing the Hospital name and Patient monitors softkeys">

4. Select **CardioQ Serial Protocol v2**, confirm the settings below, and press **Finished**.

   <img src="../hardware_images/deltex_cardioq_5.png" width="450" alt="Patient Monitors list with CardioQ Serial Protocol v2 highlighted and Patient Monitor Settings showing Baud Rate 57600 and No Flow Control">

| Parameter | Value |
|-----------|------- |
| Baud Rate | 57600 |
| Flow Control | None |

## Vital Recorder Setup

Add the device as **`CardioQ`** and select the PC serial port used for the connection.
