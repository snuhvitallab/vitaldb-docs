# LiDCO (LiDCOplus / LiDCOrapid)

<!-- meta
category: Hemodynamic Monitor
manufacturer: LiDCO
vr_device_name: LiDCO
-->
> ⚠️ **Serial output is off by default.** The RS-232 communications module must be switched on inside the monitor's **Engineering Screen** before Vital Recorder will see anything, and the baud rate here is **57600** — not the 9600 used by the Edwards monitors.

| Cable | Adapter | Port | Serial | VR Device Name |
|-------|---------|------|--------|----------------|
| Direct Serial | Null Modem **M/F** | **COM1** — standard 9-way serial port on the monitor | 57600 baud | `LiDCO` |

## Connection Steps
1. Attach a **Null Modem (M/F)** adapter to **COM1** on the monitor. LiDCO documents COM1 as the hardware connection point for all serial communications output from LiDCO monitors, and describes it as a standard 9-way serial port.
2. Connect a direct serial cable from the adapter to the PC via a USB-Serial converter. The Null Modem supplies the TX/RX crossover; a straight-through cable alone will not work.

## Device Configuration
1. Enable the serial link and set its parameters. On the LiDCO monitor the RS-232 port configuration lives in the **Engineering Screen**, where the communications software module must also be switched on. On the units documented for Vital Recorder the path is **Settings → Communications → Serial**.
2. Set the following:

   | Parameter | Value |
   |-----------|-------|
   | LiDCO Serial | Enabled |
   | Baud Rate | 57600 |
   | Data Bits | 8 |
   | Parity | None |
   | Stop Bits | 1 |
   | Average | Never |
   | Observation | Beat-to-beat |

3. **Average = Never** and **Observation = Beat-to-beat** matter as much as the baud rate: with averaging enabled the monitor emits smoothed values at a slow cadence instead of per-beat data, and Vital Recorder's trend will look sparse or frozen.

## Vital Recorder Setup

- In the Vital Recorder device list this appears under **Cardiac monitor** as **LiDCO: LiDCO**.

## Troubleshooting

- **`Settings → Communications → Serial` is not in the menu.** Menu wording varies between LiDCOplus and LiDCOrapid and across software revisions — look for the RS-232 / port configuration inside the **Engineering Screen**; LiDCO's own documentation places the settings there.
- **Port opens but no data arrives.** Check the adapter against the COM1 connector: the M/F adapter specified above assumes a female port; if the port turns out to be male, an **F/F** adapter is needed instead (the rule throughout this guide is F/F onto a male port, M/F onto a female one). Then confirm the serial values match the table above — LiDCO's published defaults differ per integration (for example, the GE Centricity interface calls for 19200 baud with **even** parity), so do not copy settings from another interface's instructions.

## Notes

- **The COM1 connector gender is unverified.** The usual arrangement on these monitors is a female port, which is what the M/F adapter above assumes.
- LiDCO does not publish the RS-232 frame specification; contact LiDCO to obtain detailed specifications for the RS-232 interface.
- This page has no photographs. LiDCO does not publish its operator manual publicly, so the COM1 location and the serial settings screen are described in text only — **confirm both against your unit's manual before connecting**.
