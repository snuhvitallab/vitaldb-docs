# GE Corometrics 170 Series / 250cx

<!-- meta
category: Patient Monitor
manufacturer: GE
vr_device_name: Coro
-->
> **Note:** The **170 Series** and **250cx** use different serial connectors and setup procedures. Use the section for your model.

| Model | Cable | Adapter | Port | VR Device Name |
|---|---|---|---|--- |
| 170 Series | Custom RJ-45 to DB-9F cable with RTS–CTS loop | None | RS-232 Port 1 or Port 2 | `Coro` |
| 250cx | Compatible RJ-11 serial cable | Confirm for the cable used | RS-232C: J109, J110, or J111 | `Coro` |

## Connection Requirements

The custom cross cable provides the TX/RX crossover, so no separate Null Modem adapter is used.

## Cable Pinout

Monitor RJ-45 port:

| RJ-45 pin | Port 1 signal | Port 2 signal | Direction |
|---|---|---|--- |
| 1 | +5 V (200 mA, fused) | GND | — |
| 2 | RTS | RTS | Output from monitor |
| 3 | RXD | RXD | Input to monitor |
| 4 | GND | GND | — |
| 5 | GND | GND | — |
| 6 | TXD | TXD | Output from monitor |
| 7 | CTS | CTS | Input to monitor |
| 8 | +5 V (200 mA, fused) | GND | — |

**Pins 1 and 8 of Port 1 carry +5 V** and are not connected to the PC side.

Cable wiring — three data conductors, crossed:

| RJ-45 (monitor) | Signal | DB-9F (PC side) | Signal |
|---|---|---|--- |
| 6 | TXD | 2 | RX |
| 3 | RXD | 3 | TX |
| 4 or 5 | GND | 5 | GND |

Connect RJ-45 **pin 7 (CTS)** to RJ-45 **pin 2 (RTS)** at the monitor end.

## Connection Steps
1. Build the RJ-45 ↔ DB-9F cable as shown in [Cable Pinout](#cable-pinout), including the CTS–RTS loop at the monitor end.

2. Plug the RJ-45 end into **RS-232 Port 1** (or Port 2) on the rear panel and the DB-9F end into the PC via a USB-Serial converter.

### Corometrics 250cx

The **250cx** has **RJ-11** RS-232C ports (**J109**, **J110** and **J111**), not the 170 Series' RJ-45 ports, so it needs a separate **compatible RJ-11 serial cable**. Confirm whether an adapter is required for the cable used. The 170 Series pinout above does not apply.

## Device Configuration
The communication mode and baud rate for each port live in **service setup mode**, which can only be entered from a power-off state.

1. **Enter service setup mode:**
   - Press and hold the **Setup** button (clock/calendar icon).
   - While still holding it, press and hold the blue **Power** button.
   - Release both buttons. Service mode is now active.

2. Use the **UA Reference** button to toggle between the **setup code** (shown in the **UA display**) and its **value** (shown in the primary **FHR display**). The UA display is active when the `±` qualifier is lit; the FHR display is active when the heartbeat indicator is lit.

3. Use the **Volume up / down** buttons to change whichever display is active. On models 172, 173 and 174 use the **leftmost** set of volume controls.

4. Set the following codes — only the port you actually cabled needs to be changed:

   | Setup code (UA display) | Parameter | Value (FHR display) |
   |---|---|--- |
   | `30` | RS-232 Port 1 — communications mode | `5` (= *115 update*) |
   | `31` | RS-232 Port 1 — baud rate | `9600` |
   | `40` | RS-232 Port 2 — communications mode | `5` (= *115 update*) |
   | `41` | RS-232 Port 2 — baud rate | `9600` |

   - **Communications mode values:** `0` = HP, `1` = HP w/notes, `2` = ext. BP, `3` = factory test, `4` = ext. FSpO2, `5` = 115 update, `6` = 115 transmit/receive.
   - **Baud rate values:** 300, 600, 1200, 2400, 4800, 9600, 19200, 38400. The display abbreviates the larger values, so 9600 may appear as `96`.
   - **Factory defaults are not usable as-is:** Port 1 ships as *HP* mode at *1200* baud, Port 2 as *ext. BP* at *600* baud.

5. **Exit with the Setup button.** Exiting service setup mode puts the monitor into standby. If you exit with the **Power** button instead, none of your changes are saved.

- Serial: **9600 baud**, port switched to communications mode **5 (115 update)**.

## Vital Recorder Setup
- Add the device in Vital Recorder as **`Coro`**.

## Troubleshooting
- **The port is configured but nothing arrives.** Verify the setup codes: `30`/`40` select the communications mode for ports 1/2 and `31`/`41` set their baud rate.

## Notes
- Recorded parameters: **fetal HR1 / HR2** and **uterine activity (UACT / TOCO)**. On current builds the **maternal vital signs (SpO2, PR, NIBP)** are also recorded into the same file as the fetal channels.
- The 170 Series covers models **170, 171, 172, 173 and 174**. The setup-code table above is common to all of them; the *HR offset* and *ECG artifact elimination* codes exist only on 172/173/174.
