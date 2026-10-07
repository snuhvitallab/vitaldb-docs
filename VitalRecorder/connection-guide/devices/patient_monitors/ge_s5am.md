# GE S/5 AM

<!-- meta
category: Patient Monitor
manufacturer: GE
vr_device_name: Bx50
-->
| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|-------- |
| direct serial cable | Null Modem (F/F) | X8 | `Bx50` |

## Connection Steps

1. Connect a direct serial cable to the monitor’s X8 port using a null modem (F/F).

   <img src="../hardware_images/ge_s5am_1.png" width="450" alt="Rear of a GE Healthcare Finland S/5 frame (type F-CU8-12-VG1) showing the fan, the External Battery 24 Vdc terminal and the rating plate on the left and the plug-in boards on the right; a red circle marks the 9-pin D-type connector labeled X8, below the round X5 and X7 connectors and beside the 25-pin X3 connector">

## Device Configuration

No changes to the monitor settings are required.

## Vital Recorder Setup

- Add the device as **`Bx50`** and select the PC serial port used for the connection.
- Default waveforms are `ECG1, PLETH, IABP1, CO2, AWP`; request others with `wavs=` — see [Configuration Guide → S5 / Datex Device Settings](../../../Configuration_Guide.md#s5--datex-device-settings-ge-solar--bx50--b1x5m--canvas). Invasive arterial pressure is `IABP1`, not `ART` or `INVP1`.
