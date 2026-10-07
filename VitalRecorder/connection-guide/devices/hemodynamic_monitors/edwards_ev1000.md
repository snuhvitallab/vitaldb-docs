# Edwards Lifesciences EV-1000 / EV-1000A

<!-- meta
category: Hemodynamic Monitor
manufacturer: Edwards Lifesciences
vr_device_name: EV1000
-->
> **Note:** **The adapter gender differs between the two generations.** The old **EV-1000** (label `REF EV1000M`) has a **male** DB-9, so it needs a **Null Modem adapter (F/F)**. The newer **EV-1000A** (label `REF EV1000A`) has a **female** DB-9 and needs a **Null Modem adapter (M/F)**. Check the REF label on the rear panel before ordering the adapter.

| Model | Cable | Adapter | Port | VR Device Name |
|-------|-------|---------|------|---------------- |
| EV-1000 (`REF EV1000M`) | Direct serial cable | Null modem adapter (F/F) | Rear DB-9 male serial port | `EV1000` |
| EV-1000A (`REF EV1000A`) | Direct serial cable | Null modem adapter (M/F) | Rear DB-9 female serial port | `EV1000` |

## Connection Steps
1. Check the rear **REF** label and serial connector. Connect a direct serial cable using the **null modem adapter** listed for that model.

   **EV-1000 (`REF EV1000M`):**

     <img src="../hardware_images/edwards_ev1000_1.png" width="450" alt="Old EV-1000 (REF EV1000M) rear panel with the male DB-9 serial port circled, sited between the USB ports and the VGA connector">

   - **EV-1000A:** the serial connector is a **female** DB-9 immediately to the right of the port marked **LAN2**. Attach a **Null Modem adapter (M/F)**.

     <img src="../hardware_images/edwards_ev1000_2.png" width="450" alt="EV-1000A rear panel with the female DB-9 serial port circled, immediately right of the LAN2 port">

## Device Configuration
1. Select the **Settings** icon.

   <img src="../hardware_images/edwards_ev1000_3.png" width="450" alt="EV-1000 monitoring screen with the gear-shaped settings icon in the left icon strip circled">

2. Select **Monitor Settings**.

   <img src="../hardware_images/edwards_ev1000_4.png" width="450" alt="EV-1000 Settings menu showing Patient Data, Monitor Settings, Parameter Settings, Data Download, Demo Mode, Engineering and Help, with Monitor Settings circled">

3. Select **Serial Port Setup**.

   <img src="../hardware_images/edwards_ev1000_5.png" width="450" alt="EV-1000 Monitor Settings menu showing General, Date/Time, Monitoring Screens, Serial Port Setup, Restore All Defaults and Advanced Features, with Serial Port Setup circled">

4. Set **Device** to **IFMout**.

   <img src="../hardware_images/edwards_ev1000_6.png" width="450" alt="EV-1000 Serial Port Setup screen with Device set to IFMout circled, alongside Stop Bits 1, Data Bits 8, Parity None and Flow Control 2 seconds">

5. Set **Baud Rate** to **9600** and confirm the remaining settings below.

   <img src="../hardware_images/edwards_ev1000_7.png" width="450" alt="EV-1000 baud rate picker listing 9600, 19200, 38400 and 57600, with 9600 circled">

| Parameter | Value |
|-----------|------- |
| Device | IFMout |
| Baud Rate | 9600 |
| Parity | None |
| Stop Bits | 1 |
| Data Bits | 8 |
| Flow Control | 2 seconds |

## Vital Recorder Setup

Add the device as **`EV1000`** and select the PC serial port used for the connection.
