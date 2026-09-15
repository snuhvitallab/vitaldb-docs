# Maquet / Getinge Servo-i / Servo-s / Servo-U Ventilators

<!-- meta
category: Mechanical Ventilator
manufacturer: Maquet
vr_device_name: Servo-i
-->
> ⚠️ **Connect to the BOTTOM RS-232 port only.** The TOP RS-232 port is a debugging port and cannot be used.
> If the bottom port is already occupied, route data through the patient monitor (Servo-i → Philips Intellivue → Vital Recorder).

| Cable | Adapter | Port | Serial | VR Device Name |
|-------|---------|------|--------|----------------|
| Direct Serial | Null Modem M/F | **BOTTOM** RS-232 port | Servo-i / Servo-s: 9600 baud, Even parity (7 or 8 data bits, 1 or 2 stop bits — auto-detected), XON/XOFF · **Servo-U: 19200** | `Servo-i` |

## Connection Steps
1. Open the connector cover on the rear of the patient unit. Two ports labeled **RS 232** are stacked there; identify the **BOTTOM** one — the upper `RS 232` port is for service/debugging and returns nothing.
2. Attach a **Null Modem (M/F)** adapter to the bottom port.
3. Connect a direct serial cable from the adapter to the PC via a USB-Serial converter.

## Device Configuration
Nothing has to be enabled on the ventilator. The serial port is served by the built-in **Computer Interface Emulator (CIE)**, which answers commands from Vital Recorder as soon as the line is up.

- Serial: **9600 baud, Even parity, XON/XOFF handshake**. Data length (7 or 8 bits) and stop bits (1 or 2) are **auto-detected** by the CIE, so either works.
- The port is opto-isolated on both input and output, so a converter that relies on stealing power from the handshake lines may fail — use a properly powered USB-Serial converter.

> **Model differences:** Servo-i and Servo-s run the CIE at **9600 baud**; **Servo-U runs at 19200 baud**. Set the matching device entry in Vital Recorder.

## Troubleshooting
- **The Servo-i has only one usable serial port**, and in most installations the patient monitor already occupies it. A read-only Y-cable tap does **not** work here: the listening branch never sees the command side of the exchange, so the parameter order cannot be resolved and parsing fails. **A direct connection is required** to collect values — otherwise take the data from the monitor instead (Servo-i → Philips Intellivue → Vital Recorder).
- **Port opens, then a repeating "no data for 20 s → close" loop:** check the cable first — cross/Null Modem type, pin-out and that both connectors are fully seated — and confirm the connection is direct rather than a tap. Confirm the RS-232 output side of the ventilator with Getinge service documentation if the cable is proven good.

## Vital Recorder Setup

- In Vital Recorder, add the device as **`Servo-i`**.

## Notes

- **Servo-U.** Supported at **19200 baud** (per `Supported_Devices.md`) with the same `Servo-i` entry; several sites report Servo-U replacing Servo-i fleets. **Whether the Servo-U needs the Null Modem, and which of its RS-232 ports is live, has not been verified on a unit** — photograph the connector panel and the interface menu on first contact and record it here. ❓ *Unverified — tracked in [unverified.md](../unverified.md).*
- Only 4 waveform channels can be sampled simultaneously over the CIE (a firmware limit of the interface).
- Typical parameters recorded: Paw, PEEP, TV, MV, RR, FiO2.
