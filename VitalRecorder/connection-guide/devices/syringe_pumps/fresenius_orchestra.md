# Fresenius Vial Orchestra (Base Primea with Module DPS)

<!-- meta
category: Syringe Pump
manufacturer: Fresenius Kabi
vr_device_name: Orchestra
-->
> ⚠️ **The port must be configured in service mode.** Connect a **direct serial cable** with a **Null Modem adapter (M/F)** as specified below. Do not use a cross cable or omit the adapter; either can prevent communication.

| Cable | Adapter | Port | Serial | VR Device Name |
|-------|---------|------|--------|----------------|
| direct serial cable (DB-9M ↔ DB-9F) | Null Modem adapter (M/F) | **RS 232-3** (DB-9F) — rightmost of the three serial ports on the Base Primea | IDMS | `Orchestra` |

## Connection Requirements

The Base Primea's serial ports are DB-9 **female**, and the PC side is DB-9 **male**, so a Null Modem adapter (M/F) reverses the wiring and mates with both connectors.

## Connection Steps
1. Identify the serial ports on the rear of the Base Primea. They are labeled **RS 232-1**, **RS 232-2** and **RS 232-3**; **RS 232-3 is the rightmost**, alongside the round connectors, and is the only one used for data export.

   <img src="../hardware_images/fresenius_orchestra_10.png" width="450" alt="Rear of the Base Primea showing RS 232-1 and RS 232-2 stacked on the left and the rightmost RS 232-3 port circled">

2. Attach the **Null Modem adapter (M/F)** to **RS 232-3**.
3. Connect a **direct** serial cable from the adapter to the PC, via a USB-Serial converter if the PC has no DB-9 port.

## Device Configuration

Two separate menus must be set: the **service-mode** serial configuration (which assigns the supervisor communication channel to port 3 and sets the transmission interval), and the **customisation** menu (which sets the port's attached-device type to IDMS).

**Part 1 — Service mode: assign COMM NEW SUP to port 3**

1. Power the unit off. Hold the **top blue side button + mute button + power button** together to boot into service mode.

   <img src="../hardware_images/fresenius_orchestra_1.png" width="450" alt="Base Primea with two DPS syringe modules mounted, with the top blue side button and the two lower-right buttons circled for the service-mode key combination">

2. In **SPECIAL FUNCTIONS**, press the side button next to **"Serial & ..."** (the fourth blue button from the top).

   <img src="../hardware_images/fresenius_orchestra_2.png" width="450" alt="SPECIAL FUNCTIONS menu listing License, Erase histo, SAV Tests, Serial & ..., Error traces, PC Mode, SAV Data and Neutral product, with Serial & ... and its side button circled">

3. The **Serial, Supervisor and Print Configuration** screen appears. Using the jog dial, set **COM NEW SUP** (second entry in the right-hand column of **SERIAL PORTS**) to **`3`**.
4. In the **COMM NEW SUP** panel at the lower right, leave **"Send a frame on every change"** unchecked and set **"Send every"** to **`1 s`**.

   <img src="../hardware_images/fresenius_orchestra_3.png" width="450" alt="Serial, Supervisor and Print Configuration screen with COMM NEW SUP set to 3 circled, and the COMM NEW SUP panel showing Send a frame on every change unchecked, Send every 1 s, Ack timeout 1 s and Main timeout 10 s">


5. Power the unit off, then on again to leave service mode.

**Part 2 — Customisation: set RS 232-3 to IDMS**

6. At the start-up screen (hospital / ward name, date and **LANGUAGE**), press the **OPT** button at the lower right of the front panel.

   <img src="../hardware_images/fresenius_orchestra_4.png" width="450" alt="Base Primea start-up screen showing hospital and ward name with the OPT button on the lower-right keypad circled">

7. In the **OPTIONS MENU**, select **CUSTOMISATION**.

   <img src="../hardware_images/fresenius_orchestra_5.png" width="450" alt="OPTIONS MENU listing Autonomy, Maintenance, Time change, Customisation, Erase a protocol and Exit, with Customisation circled">

8. On the **CONFIGURATION** screen, enter access code **`00123`** in the **CODE** field. Until a valid code is entered the advanced entries (including *Serial ports and printer*) stay greyed out.

   <img src="../hardware_images/fresenius_orchestra_6.png" width="450" alt="CONFIGURATION screen with CODE 00123 entered and circled, and the advanced menu entries still greyed out">

9. Select **SERIAL PORTS AND PRINTER**, now enabled.

   <img src="../hardware_images/fresenius_orchestra_7.png" width="450" alt="CONFIGURATION screen with code 00123 accepted and SERIAL PORTS AND PRINTER circled among the now-enabled menu entries">

10. In **SERIAL PORTS**, open the **RS232-3** entry and select **IDMS** from the drop-down list (*Not connected / Printer / PCBM / PCBM + Printer / IDMS*).

    <img src="../hardware_images/fresenius_orchestra_8.png" width="450" alt="SERIAL PORTS AND PRINTER screen with the RS232-3 drop-down open showing Not connected, Printer, PCBM, PCBM + Printer and IDMS, with RS232-3 and IDMS circled">


11. Confirm the list now reads **RS232-3  IDMS**, then press **SAVE AND EXIT**. Power-cycle the unit for the setting to take effect.

    <img src="../hardware_images/fresenius_orchestra_9.png" width="450" alt="SERIAL PORTS AND PRINTER screen with RS232-3 IDMS circled and the SAVE AND EXIT button circled">

    - Choosing **DISCARD CHANGES AND EXIT** here loses the assignment silently, and the unit will record nothing.

## Vital Recorder Setup

- Add the device in Vital Recorder as **`Orchestra`**.

## Troubleshooting

- **The Orchestra connects but produces no tracks.** Confirm both configuration steps: **RS 232-3 → IDMS** and **COMM NEW SUP → 3** in service mode.
- **The pump emits bursts on every keypress instead of a steady 1 s frame.** **"Send a frame on every change"** must stay unchecked; Vital Recorder expects the steady 1 s frame.
- **The access code `00123` is rejected.** Menu wording and code behaviour can differ on other firmware revisions — request the current customisation code from Fresenius Kabi service rather than guessing.

## Notes

- **Vital Recorder versions:** recording from the Orchestra Base Primea (including TCI) has been supported since **0.9.11**.
