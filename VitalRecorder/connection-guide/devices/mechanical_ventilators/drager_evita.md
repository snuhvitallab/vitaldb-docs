# Dräger EVITA (V300 / V500 / V600 / V800, Evita Infinity V500)

<!-- meta
category: Mechanical Ventilator
manufacturer: Dräger
vr_device_name: MedibusX
-->
> **Note:** The EVITA family speaks Dräger **MEDIBUS.X**. The volume waveform is not transmitted, and CO2 requires a capnography module.

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|---------------- |
| direct serial cable | Null modem; connector gender not confirmed | RS-232 COM1 (or COM2) | `MedibusX` |

## Connection Steps

1. Connect the direct serial cable to the RS-232 COM port on the rear of the ventilator.

## Device Configuration

Open the **COM port / interface** settings and configure the connected port as follows. The menu path varies by model and software version.

| Parameter | Value |
|-----------|------- |
| Protocol | MEDIBUS.X |
| Baud Rate | 19200 |
| Data Bits | 8 |
| Parity | Even |
| Stop Bits | 1 |

## Vital Recorder Setup

- Add the device as **`MedibusX`** and select the PC serial port used for the connection.

## Troubleshooting

- **Vital Recorder restarts repeatedly when a MEDIBUS device is attached.** A SIGSEGV loop present from 1.15.11 to 1.18.39 — fixed in 1.18.40; upgrade.
