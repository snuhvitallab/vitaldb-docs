# GE Canvas

<!-- meta
category: Patient Monitor
manufacturer: GE
vr_device_name: Canvas
-->
> **Note:** Protocol: **GE S5 Computer Interface** (the Datex DRI protocol, shared with the CARESCAPE Bx50, the B1x5M and the Solar 8000). The cable, adapter and port for the Canvas have not been confirmed on a unit.

| Cable | Adapter | Port | Serial | VR Device Name |
|-------|---------|------|--------|----------------|
| Direct Serial — Not confirmed | Not confirmed | RS-232 — Not confirmed | 9600 baud | `Canvas` |

Confirm the cable, the adapter and the port location with GE before ordering or connecting.

## Connection Steps

1. Locate the monitor's RS-232 computer-interface port.
2. Connect a direct serial cable to it, with a Null Modem adapter if GE specifies one.
3. Connect the other end to the PC through a USB-Serial converter. Use an FTDI-based converter on the PC side rather than a 3-wire adapter.

## Device Configuration

Monitor-side settings for the computer interface have not been confirmed. Check the GE service documentation before connecting.

## Vital Recorder Setup

- Add the device in Vital Recorder as **GE :: Canvas**; in `vr.conf` the type is `Canvas`.
- Recorded parameters: ECG, NIBP, SpO2, temperature and invasive pressure.
- Default waveforms are `ECG1, PLETH, IABP1, CO2, AWP`; request others with `wavs=` — see [Configuration Guide → S5 / Datex Device Settings](../../../Configuration_Guide.md#s5--datex-device-settings-ge-solar--bx50--b1x5m--canvas). Invasive arterial pressure is `IABP1`, not `ART` or `INVP1`.
