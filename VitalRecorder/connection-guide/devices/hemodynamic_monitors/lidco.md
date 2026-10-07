# LiDCO (LiDCOplus / LiDCOrapid)

<!-- meta
category: Hemodynamic Monitor
manufacturer: LiDCO
vr_device_name: LiDCO
-->
> **Note:** **Serial output is off by default.** The RS-232 communications module must be switched on inside the monitor's **Engineering Screen** before Vital Recorder will see anything, and the baud rate here is **57600** — not the 9600 used by the Edwards monitors.

| Cable | Adapter | Port | Serial | VR Device Name |
|-------|---------|------|--------|---------------- |
| direct serial cable | Null Modem adapter (M/F) (assumes female COM1; unverified) | **COM1** — standard 9-way serial port on the monitor | 57600 baud | `LiDCO` |

## Connection Steps
1. Attach a **Null Modem adapter (M/F)** to **COM1**, the standard 9-way serial port on the monitor.
2. Connect a direct serial cable from the adapter to the PC via a USB-Serial converter. The Null Modem supplies the TX/RX crossover; a direct serial cable alone will not work.

## Device Configuration
1. Enable the serial link and set its parameters in the monitor's **Engineering Screen**. The communications software module must also be switched on. The menu path is **Settings → Communications → Serial**.
2. Set the following:

   | Parameter | Value |
   |-----------|------- |
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

- **`Settings → Communications → Serial` is not in the menu.** Menu wording varies between LiDCOplus and LiDCOrapid and across software revisions. Look for the RS-232 port configuration inside the **Engineering Screen**.
- **Port opens but no data arrives.** Check the adapter against the COM1 connector. If the port is male, use a **Null Modem adapter (F/F)**. Confirm that the serial values match the table above.
