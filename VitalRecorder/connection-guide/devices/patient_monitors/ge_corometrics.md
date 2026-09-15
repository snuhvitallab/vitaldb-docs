# GE Corometrics 170 Series

<!-- meta
category: Patient Monitor
manufacturer: GE
vr_device_name: Coro
-->
> ⚠️ **The RS-232C ports are 8-pin RJ-45 sockets, not DB-9.** A custom RJ-45 ↔ DB-9F cable is required, and the monitor's **CTS input must be asserted** or it will not transmit. Service setup mode must also be used to switch the port into the data-export communication mode — the factory defaults do not export data.

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|----------------|
| Custom RJ-45 ↔ DB-9F (null-modem wiring, CTS looped to RTS) | None | **RS-232 Port 1** or **Port 2** (rear panel, RJ-45) | `Coro` |

The DB-9F end plugs into the PC's DB-9M serial port or into a USB-Serial converter. Because the crossover is built into the custom cable's pin mapping, **no Null Modem gender changer is used**.

## Connection Steps

1. Prepare an RJ-45 ↔ DB-9F cable. The monitor's RJ-45 pinout is:

   | RJ-45 pin | Port 1 signal | Port 2 signal | Direction |
   |---|---|---|---|
   | 1 | +5 V (200 mA, fused) | GND | — |
   | 2 | RTS | RTS | Output from monitor |
   | 3 | RXD | RXD | Input to monitor |
   | 4 | GND | GND | — |
   | 5 | GND | GND | — |
   | 6 | TXD | TXD | Output from monitor |
   | 7 | CTS | CTS | Input to monitor |
   | 8 | +5 V (200 mA, fused) | GND | — |

   *Per the Corometrics 170 Series service manual (P/N 2000947-004), tables 8-6 and 8-7. Note that **pins 1 and 8 of Port 1 carry +5 V** — do not wire them to anything on the PC side.*

2. Wire the three data conductors as a null-modem (crossed) connection: monitor **TXD (pin 6)** → DB-9F **pin 2**, monitor **RXD (pin 3)** ← DB-9F **pin 3**, **GND (pin 4 or 5)** → DB-9F **pin 5**.

   - The manual states that when the monitor is connected directly to another DTE (a PC), **a standard null-modem cable must be used**.

3. **Loop CTS to RTS at the monitor end** — join RJ-45 **pin 7 (CTS)** to RJ-45 **pin 2 (RTS)**. The manual specifies that the CTS input must be asserted to enable transmission and that, with no modem in the path, it may be tied to the monitor's own RTS line. Without this loop the port stays silent.

   - RTS is asserted (+12 V) whenever the monitor is powered on and operating, so the loop doubles as a power-on indication.

4. Plug the RJ-45 end into **RS-232 Port 1** (or Port 2) on the rear panel and the DB-9F end into the PC via a USB-Serial converter.

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
   |---|---|---|
   | `30` | RS-232 Port 1 — communications mode | `5` (= *115 update*) |
   | `31` | RS-232 Port 1 — baud rate | `9600` |
   | `40` | RS-232 Port 2 — communications mode | `5` (= *115 update*) |
   | `41` | RS-232 Port 2 — baud rate | `9600` |

   - **Communications mode values:** `0` = HP, `1` = HP w/notes, `2` = ext. BP, `3` = factory test, `4` = ext. FSpO2, `5` = 115 update, `6` = 115 transmit/receive.
   - **Baud rate values:** 300, 600, 1200, 2400, 4800, 9600, 19200, 38400. The display abbreviates the larger values, so 9600 may appear as `96`.
   - **Factory defaults are not usable as-is:** Port 1 ships as *HP* mode at *1200* baud, Port 2 as *ext. BP* at *600* baud.

5. **Exit with the Setup button.** Exiting service setup mode puts the monitor into standby. If you exit with the **Power** button instead, none of your changes are saved.

- Serial: **9600 baud**, port switched to communications mode **5 (115 update)**. The RTS/CTS loop described in step 3 is what makes a 3-wire cable work.

## Notes

- Recorded parameters: **fetal HR1 / HR2** and **uterine activity (UACT / TOCO)**. From **1.19.7** onward the **maternal vital signs (SpO2, PR, NIBP)** are recorded into the same file as the fetal channels.
- The 170 Series covers models **170, 171, 172, 173 and 174**. The setup-code table above is common to all of them; the *HR offset* and *ECG artifact elimination* codes exist only on 172/173/174.
- **Verify the setup codes on the unit in front of you.** An earlier revision of this guide listed the port-1 baud rate under code `40`; the service manual (P/N 2000947-004) assigns `30`/`40` to the *communications mode* of ports 1/2 and `31`/`41` to their *baud rate*. The manual numbering is used above.
- Vital Recorder's supported-device list names the **Corometrics 250cx** for fetal monitoring (FHR, MHR, TOCO). Confirm the exact model on site before planning a delivery-room install — the 170 Series and the 250 Series have different rear panels, and site requests for "a GE fetal monitor" have turned out to be either.
- **Gap:** there are no field photographs for this device yet — no rear-panel shot, no RS-232 port location, no setup-mode display. Photographs of the rear RJ-45 ports and of the UA/FHR displays while in service setup mode would be a useful addition.
