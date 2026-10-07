# Maquet / Getinge Servo-i / Servo-s / Servo-U Ventilators

<!-- meta
category: Mechanical Ventilator
manufacturer: Maquet
vr_device_name: Servo-i
-->
> ⚠️ **On Servo-i and Servo-s, connect to the BOTTOM RS-232 port.** The TOP port is for service/debugging. The live port and adapter requirement for Servo-U have not been verified; confirm both with Getinge before connecting.

| Cable | Adapter | Port | Serial | VR Device Name |
|-------|---------|------|--------|----------------|
| direct serial cable | Servo-i / Servo-s: Null Modem adapter (M/F); Servo-U: unverified | Servo-i / Servo-s: **BOTTOM** RS-232; Servo-U: unverified | Servo-i / Servo-s: 9600 baud, Even parity (7 or 8 data bits, 1 or 2 stop bits — auto-detected), XON/XOFF · **Servo-U: 19200** | `Servo-i` |

## Connection Steps
1. Open the connector cover on the rear of the patient unit. On Servo-i and Servo-s, identify the **BOTTOM** of the two ports labeled **RS 232**; the upper port is for service/debugging.
2. On Servo-i and Servo-s, attach a **Null Modem adapter (M/F)** to the bottom port.
3. Connect a direct serial cable from the adapter to the PC via a USB-Serial converter.

## Device Configuration
Nothing has to be enabled on the ventilator. The serial port is served by the built-in **Computer Interface Emulator (CIE)**, which answers commands from Vital Recorder as soon as the line is up.

- Serial: **9600 baud, Even parity, XON/XOFF handshake**. Data length (7 or 8 bits) and stop bits (1 or 2) are **auto-detected** by the CIE, so either works.
- The port is opto-isolated on both input and output, so a converter that relies on stealing power from the handshake lines may fail — use a properly powered USB-Serial converter.

> **Model differences:** Servo-i and Servo-s run the CIE at **9600 baud**; **Servo-U runs at 19200 baud**. Set the matching device entry in Vital Recorder.

## Vital Recorder Setup

- In Vital Recorder, add the device as **`Servo-i`**.

## Troubleshooting

- **The port opens but no data arrives.** Check that the cable and adapter match the model and are fully seated. Confirm that the connection is direct rather than a read-only tap (see Known Limitations).

## Known Limitations

- **The Servo-i has only one usable serial port.** If the patient monitor already occupies it, a read-only Y-cable tap does **not** work: the listening branch cannot resolve the parameter order. Connect directly or collect the data through the patient monitor (Servo-i → Philips IntelliVue → Vital Recorder).
- Only 4 waveform channels can be sampled simultaneously over the CIE (a firmware limit of the interface).

## Notes

- Typical parameters recorded: Paw, PEEP, TV, MV, FiO2.
