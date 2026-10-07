# Deltex CardioQ / CardioQ-ODM+

<!-- meta
category: Hemodynamic Monitor
manufacturer: Deltex
vr_device_name: CardioQ
-->
> **Note:** **The CardioQ rear serial port is male and needs a Null Modem adapter (F/F).** Monitor settings cannot be changed while a probe is connected. Verify the output in **Demo mode**.

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|----------------|
| direct serial cable | Null Modem adapter (F/F) | Rear **male** DB-9 serial port | `CardioQ` |

## Connection Steps
1. Locate the serial (RS-232) port on the rear panel. It is a **male DB-9** between the RJ-45 network port and the mains inlet; USB, ADC and the equipotential earth terminal are on the same panel.

   <img src="../hardware_images/deltex_cardioq_1.png" width="450" alt="CardioQ rear panel with the male DB-9 serial port circled, between the RJ-45 network port and the mains inlet">

2. Attach a **Null Modem adapter (F/F)** to that port. A Null Modem adapter (M/F) will not mate with a male device port.
3. Connect a direct serial cable from the adapter to the PC via a USB-Serial converter.

## Device Configuration
Do this with **no probe connected** — the monitor blocks setup changes otherwise.

1. On the start-up screen press **Monitor setup**. (The same screen carries the **Demo mode** softkey used for verification in step 5.)

   <img src="../hardware_images/deltex_cardioq_4.png" width="450" alt="CardioQ start-up screen reading 'There is no probe connected', with Demo mode, Patients, Monitor setup, Instructions for use and Select user softkeys">

2. On the **Monitor setup functions** screen press **General**.

   <img src="../hardware_images/deltex_cardioq_2.png" width="450" alt="Monitor setup functions screen showing the Time/Date, Reset all, Version data, Language, General, User settings, Users and Shift softkeys">

3. Press **Patient monitors**.

   <img src="../hardware_images/deltex_cardioq_3.png" width="450" alt="Monitor setup functions screen after pressing General, now showing the Hospital name and Patient monitors softkeys">

4. In the **Patient Monitors** list select **CardioQ Serial Protocol v2**, check the values shown under **Patient Monitor Settings**, then press **Finished**.

   <img src="../hardware_images/deltex_cardioq_5.png" width="450" alt="Patient Monitors list with CardioQ Serial Protocol v2 highlighted and Patient Monitor Settings showing Baud Rate 57600 and No Flow Control">


- Select **CardioQ Serial Protocol v2**. The other listed options are not the protocol specified for this Vital Recorder connection.
- Serial: **57600 baud, No Flow Control**.
- Data bits, parity and stop bits are not exposed on the CardioQ setup screens.

## Vital Recorder Setup

- In the Vital Recorder device list this appears under **Cardiac monitor** as **Deltex: CardioQ**; recorded tracks are prefixed `CardioQ/`.

## Notes

- After a protocol is selected the monitor shows a connection-status icon (not connected / connecting / connected), which is a quick way to confirm the link.
