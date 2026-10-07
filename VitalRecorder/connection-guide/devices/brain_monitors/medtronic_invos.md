# Medtronic INVOS Cerebral/Somatic Oximetry (5100C)

<!-- meta
category: Brain Monitor
manufacturer: Medtronic
vr_device_name: Invos
-->
> ⚠️ **The INVOS RS-232 port is a DB-9 *male* connector, so a Null Modem adapter (F/F) is required.** This is the opposite of the BIS monitors, whose ports are female and take a direct serial cable.
> Select **PC LINK**, not **VUELINK** — VueLink is the Philips module format and runs at a different baud rate.

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|----------------|
| direct serial cable (DB-9M ↔ DB-9F) | **Null Modem adapter (F/F)** | `\|O\|O\|` RS-232 port (DB-9 **male**), rear panel | `Invos` |

## Connection Requirements

- Serial: **9600 baud, 8 data bits, No parity, 1 stop bit**.

## Connection Steps
1. Locate the **RS-232 port** on the rear panel — the upper DB-9 marked with the `|O|O|` serial symbol. It has **pins** (male). The DB-9 directly below it is the **VGA/monitor output**; do not use it.

   <img src="../hardware_images/medtronic_invos_1.png" width="450" alt="INVOS rear panel — upper DB-9 male RS-232 port circled beside the |O|O| serial symbol, with the VGA/monitor DB-9 connector below it">

2. Screw a **Null Modem adapter (F/F)** onto the male RS-232 port.
3. Connect a **direct serial cable** from the adapter to the PC's DB-9M serial port, or to a USB-Serial converter.

## Device Configuration
Digital output is off by default and is reached through the softkey row at the bottom of the monitoring screen.

1. On the monitoring screen press **NEXT MENU**.

   <img src="../hardware_images/medtronic_invos_2.png" width="450" alt="INVOS monitoring screen showing left and right rSO2 values and trend graphs, with the NEXT MENU softkey circled at the bottom right">

2. Press **OUTPUT SELECT**.

   <img src="../hardware_images/medtronic_invos_3.png" width="450" alt="INVOS second softkey row — OUTPUT SELECT circled, alongside USER CONFIGURATION, TIME SCALE and NEXT MENU">

3. Press **DIGITAL OUTPUT** (the other option, USB STORAGE, writes to a USB drive instead).

   <img src="../hardware_images/medtronic_invos_4.png" width="450" alt="INVOS Output Select softkey row — DIGITAL OUTPUT circled, next to USB STORAGE and PREVIOUS MENU">

4. Press **PC LINK**. **Do not** select **VUELINK** — that format targets the Philips VueLink / IntelliBridge interface module and uses a different baud rate.

   <img src="../hardware_images/medtronic_invos_5.png" width="450" alt="INVOS Digital Output softkey row — PC LINK circled, next to VUELINK, PREVIOUS MENU and MAIN MENU">

5. On the **RS-232 DIGITAL OUTPUT FORMAT SELECTION** screen choose **OUTPUT FORMAT 1**. The screen lists which monitor software versions each format belongs to, and an asterisk marks the format currently in use.

   <img src="../hardware_images/medtronic_invos_6.png" width="450" alt="INVOS RS-232 Digital Output Format Selection screen listing OUTPUT FORMAT 1 for software 30.06.06 and newer, FORMAT 2 for 30.02.02-30.05.05B and FORMAT 3 for 30.01.01, with the OUTPUT FORMAT 1 softkey circled">

   | Output format | Monitor software version |
   |---|---|
   | **OUTPUT FORMAT 1** | 30.06.06 and newer |
   | OUTPUT FORMAT 2 | 30.02.02 – 30.05.05B |
   | OUTPUT FORMAT 3 | 30.01.01 |

   **OUTPUT FORMAT 1** is the format for current software. On an older monitor whose software predates 30.06.06, pick the format matching the version shown on this screen.

## Vital Recorder Setup

- In Vital Recorder, select the device as **`Invos`**. Recorded parameters are left and right **rSO2** (cerebral/somatic regional oxygen saturation).

## Notes

- The INVOS serial port uses pins 2 (RxD), 3 (TxD) and 5 (GND).
- Newer INVOS models place the serial port on the **docking station** rather than on the monitor body, and label the digital-output formats **PC LINK 1 / PC LINK 2** instead of OUTPUT FORMAT 1/2/3. The cable and gender requirements are unchanged.
