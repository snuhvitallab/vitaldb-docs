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

No protocol or baud setting is exposed on the device. The link runs at **115200 baud** on current builds (very old builds used 9600). The device streams at **1 Hz or 32 Hz**; both are recorded.

## Vital Recorder Setup

- Add the device as **`NirsitON`**. Recorded parameters: rSO2, HbO2, HbR, CCO and the NIRS waveform.

## Troubleshooting

- **Nothing until Calibrate is pressed.** This is normal — data starts only after calibration completes.
- **Works, then drops every few minutes.** The tablet firewall is blocking port 5525.
- **Connected but no values / `-nan` on the web monitor.** An older protocol version mismatch — upgrade Vital Recorder.
- **Recording restarts repeatedly during a NIRSIT session.** Seen with 1.13.x builds; upgrade.

## Notes

- **Vital Recorder version:** run the latest release (see the [official version history](https://vitaldb.net/vital-recorder/?action=versions)); device-related version notes are collected in [version-notes.md](../version-notes.md).
- Developed with the manufacturer in 2024; the protocol went through several revisions (sign byte, 32 Hz timing) — keep Vital Recorder current.
- **No photographs yet** of the rear USB port or the Calibrate screen.

## Sources

- `VitalRecorder/Supported_Devices.md` — *NirsitON, OBELAB, RS-232, 115200 baud, RSO2, HbO2, HbR, CCO, NIRS waveform*.
- Field records (VitalDB installation and support logs, 2024–2026) — protocol developed with the manufacturer in 2024 and its revisions (sign byte, 32 Hz timing, early 9600 builds), rear USB serial port with no null modem, tablet firewall **TCP 5525** requirement and the periodic drop when it is blocked, data starting only after **Calibrate**, 1 Hz / 32 Hz streams, `-nan` on protocol-version mismatch, and repeated recording restarts on 1.13.x builds.
- Vital Recorder official version history — <https://vitaldb.net/vital-recorder/?action=versions> (version guidance in Notes; device-related entries in [version-notes.md](../version-notes.md)).
