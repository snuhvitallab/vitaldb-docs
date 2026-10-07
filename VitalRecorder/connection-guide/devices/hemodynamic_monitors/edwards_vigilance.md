# Edwards Lifesciences Vigilance

<!-- meta
category: Hemodynamic Monitor
manufacturer: Edwards Lifesciences
vr_device_name: Vigilance
-->
| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|---------------- |
| Direct serial cable | Null modem adapter (M/F) | COM 1 or COM 2 | `Vigilance` |

## Connection Steps
1. Connect a direct serial cable to **COM 1** using a **null modem adapter (M/F)**. COM 2 can also be used; configure the port used for the connection.

   <img src="../hardware_images/edwards_vigilance_1.png" width="450" alt="Vigilance rear panel with the female DB-9 port labeled COM 1 circled, COM 2 beside it and the ANALOG IN 1/2 jacks to the right">

## Device Configuration
1. Select **Setup**.

   <img src="../hardware_images/edwards_vigilance_2.png" width="450" alt="Vigilance home screen with the Trend, Patient Data, Setup and Alarms softkeys down the right edge, Setup circled">

2. Select **System Config**.

   <img src="../hardware_images/edwards_vigilance_3.png" width="450" alt="Vigilance Display Format screen with Home, Cursor and Change softkeys and the System Config softkey circled">

3. If the **Patient Information** screen appears, press **Return** to continue to configuration.

   <img src="../hardware_images/edwards_vigilance_4.png" width="450" alt="Vigilance Patient Information screen prompting for height, weight and BSA, with the Return softkey circled">

4. Select **Digital Ports**.

   <img src="../hardware_images/edwards_vigilance_5.png" width="450" alt="Vigilance System Configuration screen listing firmware revisions and the IFMout ID number, with the Digital Ports softkey circled">

5. Select the connected port and use **Change** to apply the settings below.

   <img src="../hardware_images/edwards_vigilance_6.png" width="450" alt="Vigilance Digital Ports screen with COM 1 set to Device IFMout, Baud Rate 9600, Parity None, Stop Bits 1, Data Bits 8 and Flow Control 2 seconds, while COM 2 Device is None">

   | Parameter | Value |
   |-----------|------- |
   | Device | IFMout |
   | Baud Rate | 9600 |
   | Parity | None |
   | Stop Bits | 1 |
   | Data Bits | 8 |
   | Flow Control | 2 seconds |

## Vital Recorder Setup

Add the device as **`Vigilance`** and select the PC serial port used for the connection.
