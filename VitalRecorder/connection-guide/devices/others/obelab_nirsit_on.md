# OBELAB NIRSIT-ON+ (fNIRS)

<!-- meta
category: Other
manufacturer: OBELAB
vr_device_name: NirsitON
-->
> ⚠️ **Open TCP port 5525 in the firewall of the NIRSIT tablet.** Without it the link works for a few minutes and then drops repeatedly. Data starts only after **Calibrate** is pressed on the device.

| Cable | Adapter | Port | Serial | VR Device Name |
|-------|---------|------|--------|----------------|
| Direct Serial | None | USB port on the rear of the device (serial over USB) | 115200 baud | `NirsitON` |

## Connection Steps

1. Connect a direct serial cable (via a USB-Serial converter) to the **USB port on the rear** of the NIRSIT-ON+ unit. No null modem is used.
2. On the NIRSIT tablet, open the firewall and **allow inbound TCP 5525**.
3. In Vital Recorder, add the device as **`NirsitON`**.
4. Start a measurement on the device: press **Calibrate**. Data flows once calibration completes.

## Device Configuration

No protocol or baud setting is exposed on the device. The link runs at **115200 baud** (Vital Recorder 1.11.4 or later; earlier builds used 9600). The device streams at **1 Hz or 32 Hz**; 32 Hz recording is supported from **1.13.9**.

## Vital Recorder Setup

- Add the device as **`NirsitON`**. Recorded parameters: rSO2, HbO2, HbR, CCO and the NIRS waveform.

## Troubleshooting

- **Works, then drops every few minutes:** the tablet firewall is blocking port 5525.
- **Connected but no values / `-nan` on the web monitor:** an older protocol version mismatch — upgrade Vital Recorder (fixes landed in 1.11.5–1.13.9).
- **Recording restarts repeatedly during a NIRSIT session:** seen with 1.13.x builds; upgrade.
- **Nothing until Calibrate is pressed** is normal.

## Notes

- Developed with the manufacturer in 2024; the protocol went through several revisions (sign byte, 32 Hz timing) — keep Vital Recorder current.
- **No photographs yet** of the rear USB port or the Calibrate screen.
