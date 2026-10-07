# Nihon Kohden PVM-4700 (Vismo)

<!-- meta
category: Patient Monitor
manufacturer: Nihon Kohden
vr_device_name: PVM
-->
> **Note:** Use Vital Recorder 1.19.34 or later. This connection supports numeric data only. Waveforms are not transmitted over RS-232C.

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|----------------|
| Direct serial cable | Null Modem (M/F) | RS-232C connector on the `QI-470P` interface | `PVM` |

## Connection Requirements
1. Confirm with Nihon Kohden which interface board is installed on the monitor before ordering or connecting the cable. This page assumes the **`QI-470P`** RS-232C interface; if it is not installed, contact Nihon Kohden to arrange installation.
2. Use Vital Recorder 1.19.34 or later.

## Connection Steps

1. Connect the RS-232C cable to the RS-232C connector on the QI-470P interface.
2. Connect the other end to the PC's serial port, using null modem (M/F). If the PC has no serial port, use a USB-Serial converter.

## Device Configuration

No changes to the monitor settings are required.

## Vital Recorder Setup

- Add the device as **`PVM`** and select the PC serial port used for the connection.
