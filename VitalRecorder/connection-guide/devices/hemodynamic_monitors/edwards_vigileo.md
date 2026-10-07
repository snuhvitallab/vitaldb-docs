# Edwards Lifesciences Vigileo

<!-- meta
category: Hemodynamic Monitor
manufacturer: Edwards Lifesciences
vr_device_name: Vigileo
-->
| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|---------------- |
| Direct serial cable | Null modem adapter (M/F) | RS-232 serial port | `Vigileo` |

## Connection Steps
1. Connect a direct serial cable to the rear serial port using a **null modem adapter (M/F)**.

   <img src="../hardware_images/edwards_vigileo_1.png" width="450" alt="Vigileo rear panel with the recessed female DB-9 serial port circled, below the USB port">

## Device Configuration
1. Tap the **blank strip at the bottom left** of the monitoring screen — there is no labeled button — to open the Status Menu.

   <img src="../hardware_images/edwards_vigileo_2.png" width="450" alt="Vigileo CO/SVV trend screen with the unlabelled blank strip at the bottom left circled">

2. In the **Status Menu** select **Serial Port Setup**.

   <img src="../hardware_images/edwards_vigileo_3.png" width="450" alt="Vigileo Status Menu listing New Patient, Patient Data, Display Setup, Serial Port Setup, Analog In Setup, Analog Out Setup, Default Settings, Engineering and Data Download, with Serial Port Setup highlighted">

3. Set **Device** to **IFMout**.

   <img src="../hardware_images/edwards_vigileo_4.png" width="450" alt="Vigileo Serial Port Setup screen with the Device picker open showing None, IFMout, Batch IFMout and Flexport, and IFMout highlighted">

4. Set **Baud Rate** to **9600**, leave the other serial settings at their defaults, and press **Return**.

   <img src="../hardware_images/edwards_vigileo_5.png" width="450" alt="Vigileo Serial Port Setup screen with the Baud Rate picker open showing 1200, 2400, 9600, 19200, 38400 and 57600, and 9600 circled">

## Vital Recorder Setup

Add the device as **`Vigileo`** and select the PC serial port used for the connection.
