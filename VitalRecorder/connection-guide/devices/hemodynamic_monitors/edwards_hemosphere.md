# Edwards Lifesciences HemoSphere

<!-- meta
category: Hemodynamic Monitor
manufacturer: Edwards Lifesciences
vr_device_name: Hemosphere
-->
| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|---------------- |
| direct serial cable | Null modem adapter (M/F) | DB-9 serial port | `Hemosphere` |

## Connection Steps
1. Connect a direct serial cable to the rear serial port using a **null modem adapter (M/F)**.

   <img src="../hardware_images/edwards_hemosphere_1.png" width="450" alt="HemoSphere rear panel with the female DB-9 serial port outlined in the lower connector block, left of the DB-15 connector and below the USB and ECG inputs">

## Device Configuration
1. Select the **Settings** icon.
   <img src="../hardware_images/edwards_hemosphere_2.png" width="450" alt="HemoSphere start-up screen showing Last Patient details, with the gear-shaped settings icon at the bottom left outlined">

2. Select **Advanced Setup**.

   <img src="../hardware_images/edwards_hemosphere_3.png" width="450" alt="HemoSphere Settings screen with General, Advanced Setup, Demo Mode and Export Data buttons, Advanced Setup outlined">

3. Enter the Advanced Setup password (default: **`55555555`**).

   <img src="../hardware_images/edwards_hemosphere_4.png" width="450" alt="HemoSphere Advanced Setup Password prompt with the on-screen numeric keypad">

4. Select **Connectivity**.

   <img src="../hardware_images/edwards_hemosphere_5.png" width="450" alt="HemoSphere Advanced Setup menu with Parameter Settings, Analog Input, Connectivity, System Status, Engineering, GDT Settings, Setting Profile, System Reset, Manage Features and Change Passwords, with Connectivity outlined">

5. Select **Serial Port Setup**.

   <img src="../hardware_images/edwards_hemosphere_6.png" width="450" alt="HemoSphere Connectivity Settings screen showing Wireless, HL7 Setup and Serial Port Setup, with Serial Port Setup highlighted">

6. On the **Serial Port** tab, apply the settings below.

   <img src="../hardware_images/edwards_hemosphere_7.png" width="450" alt="HemoSphere Serial Port Setup screen, Serial Port tab, showing Device IFMout, Baud Rate 9600, Parity None, Compatibility None, Stop Bits 1, Data Bits 8 and Flow Control 2 seconds">

   | Parameter | Value |
   |-----------|------- |
   | Device | IFMout |
   | Baud Rate | 9600 |
   | Parity | None |
   | Stop Bits | 1 |
   | Data Bits | 8 |
   | Flow Control | 2 seconds |
   | Compatibility | None |

7. Restart the monitor to apply the changes.

## Vital Recorder Setup

- Add the device as **`Hemosphere`** and select the PC serial port used for the connection.
