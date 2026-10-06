# Nihon Kohden PVM-4700 (Vismo)

<!-- meta
category: Patient Monitor
manufacturer: Nihon Kohden
vr_device_name: PVM
-->
> **Note:** The serial link carries **numeric data only**. Waveforms are not sent over RS-232C.

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|----------------|
| Nihon Kohden `YS-089P`-series RS-232C cable | Not confirmed | RS-232C connector on the `QI-470P` interface | `PVM` |

## Connection Steps

1. Locate the **RS-232C connector** on the monitor's **`QI-470P`** interface.
2. Connect a Nihon Kohden **`YS-089P`-series** RS-232C cable to it.
3. Connect the other end to the PC through a USB-Serial converter.
4. In Vital Recorder, add the device as **`PVM`** — see [Vital Recorder Setup](#vital-recorder-setup).

## Device Configuration

No monitor-side menu change is normally required. If nothing arrives, confirm the RS-232C port's baud rate with Nihon Kohden.

## Vital Recorder Setup

- Add **Patient monitor → Nihon Kohden : PVM** (`type=PVM` in `vr.conf`).
- A PVM already added as `BSM` also records; no change is needed on existing installations.

## Troubleshooting

- **Nothing arrives on a build before 1.19.34.** Earlier builds sent a request the PVM-4700 rejects, and recorded nothing. Upgrade.
- **Numerics arrive but no waveforms.** Expected — see Known Limitations.

## Known Limitations

- **Numeric data only** over RS-232C: HR, PR, SpO2, RR and temperature, plus NIBP when it is measured.
