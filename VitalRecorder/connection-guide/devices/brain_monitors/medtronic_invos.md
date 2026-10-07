# Medtronic INVOS Cerebral/Somatic Oximetry (5100C)

<!-- meta
category: Brain Monitor
manufacturer: Medtronic
vr_device_name: Invos
-->
| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|---------------- |
| direct serial cable | Null Modem (F/F) | `\|O\|O\|` RS-232 port | `Invos` |

## Connection Steps
1. Connect a direct serial cable to the |O|O| port on the rear of the device using a null modem adapter (F/F).
   <img src="../hardware_images/medtronic_invos_1.png" width="450" alt="INVOS rear panel — upper DB-9 male RS-232 port circled beside the |O|O| serial symbol, with the VGA/monitor DB-9 connector below it">

## Device Configuration

1. On the monitoring screen press **NEXT MENU**.

   <img src="../hardware_images/medtronic_invos_2.png" width="450" alt="INVOS monitoring screen showing left and right rSO2 values and trend graphs, with the NEXT MENU softkey circled at the bottom right">

2. Press **OUTPUT SELECT**.

   <img src="../hardware_images/medtronic_invos_3.png" width="450" alt="INVOS second softkey row — OUTPUT SELECT circled, alongside USER CONFIGURATION, TIME SCALE and NEXT MENU">

3. Press **DIGITAL OUTPUT**

   <img src="../hardware_images/medtronic_invos_4.png" width="450" alt="INVOS Output Select softkey row — DIGITAL OUTPUT circled, next to USB STORAGE and PREVIOUS MENU">

4. Press **PC LINK**.

   <img src="../hardware_images/medtronic_invos_5.png" width="450" alt="INVOS Digital Output softkey row — PC LINK circled, next to VUELINK, PREVIOUS MENU and MAIN MENU">

5. On the **RS-232 DIGITAL OUTPUT FORMAT SELECTION** screen choose **OUTPUT FORMAT 1**.

   <img src="../hardware_images/medtronic_invos_6.png" width="450" alt="INVOS RS-232 Digital Output Format Selection screen listing OUTPUT FORMAT 1 for software 30.06.06 and newer, FORMAT 2 for 30.02.02-30.05.05B and FORMAT 3 for 30.01.01, with the OUTPUT FORMAT 1 softkey circled">

## Vital Recorder Setup

- Add the device as **`INVOS`** and select the PC serial port used for the connection.
