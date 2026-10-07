# Edwards Lifesciences Vigilance II

<!-- meta
category: Hemodynamic Monitor
manufacturer: Edwards Lifesciences
vr_device_name: Vigilance
-->
| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|---------------- |
| Direct serial cable | Null modem adapter (M/F) | Rear serial port 1 (upper DB-9) | `Vigilance` |

## Connection Steps
1. Connect a direct serial cable to serial port **1** using a **null modem adapter (M/F)**.

   <img src="../hardware_images/edwards_vigilance2_1.png" width="450" alt="Vigilance II rear panel with the upper of two stacked female DB-9 ports circled, marked 1 with port 2 below it and the RJ-45 and ECG connectors alongside">

## Device Configuration
1. Select the **Setup** icon (wrench).

   <img src="../hardware_images/edwards_vigilance2_2.png" width="450" alt="Vigilance II monitoring screen with the wrench-shaped setup icon in the bottom-left tool bar circled">

2. In the **Setup Menu** select **Serial Port Setup**.

   <img src="../hardware_images/edwards_vigilance2_3.png" width="450" alt="Vigilance II Setup Menu listing Display Format, Serial Port Setup, Analog Input Setup, Analog Output Setup, Default Settings, Patient CCO Cable Test, Demo Mode and Message Log, with Serial Port Setup highlighted">

3. In the **Com 1** column, apply the settings below and press **Return**.

   <img src="../hardware_images/edwards_vigilance2_5.png" width="450" alt="Vigilance II Serial Port Setup screen with Com 1 set to Device IFMout, Baud Rate 9600, Parity None, Stop Bits 1, Data Bits 8 and Flow Control 2 seconds, while Com 2 Device is None">

Resulting serial settings:

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
