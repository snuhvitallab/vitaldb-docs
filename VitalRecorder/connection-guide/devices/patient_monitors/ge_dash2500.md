# GE Dash 2500

<!-- meta
category: Patient Monitor
manufacturer: GE
vr_device_name: Dash2500
-->
> **Note:** This connection uses the **HostComm** port and requires the monitor settings below. It differs from the AUX connection used by the Dash 2000 / 3000 / 4000 / 5000.

| Cable | Adapter | Port | VR Device Name |
|---|---|---|--- |
| Direct serial cable | None | HostComm (DB-9) | `Dash2500` |

## Connection Requirements

Use the **9-pin HostComm port** for this RS-232 connection. The separate 15-pin communication-adapter connector is not a PC RS-232 port.

## Connection Steps

1. Connect a **direct serial cable** to the **HostComm** port on the rear of the monitor. No null modem adapter is required.

   <img src="../hardware_images/ge_dash2500_1.png" width="450" alt="Line drawing of the Dash 2500 rear panel with callouts: Speaker at top, AC Power Operation inlet and the HostComm Port D-sub connector beside it in the same recessed bay, the Potential Equalization Terminal stud below, and the Ethernet and Serial Connectors (two RJ-45 jacks) on the right">

2. Plug a **direct serial cable** into the HostComm port. No Null Modem adapter is used.

3. Connect the other end to the PC through a USB-Serial converter.

   ```
   Dash 2500 HostComm (DB-9) -- direct serial cable -- USB-Serial -- PC
   ```

### HostComm DB-9 pin assignment

The isolated host communications connector is wired as:

| Pin | Signal |
|-----|-------- |
| 2 | TX (RS-232) |
| 3 | RX (RS-232) |
| 5 | Ground |

Pins 2, 3 and 5 carry the serial data and ground used by Vital Recorder.

## Device Configuration

1. Turn the Trim Knob → **Main Menu**.
2. Select **Other System Setting → Go to Config Mode → Yes**. The monitor reboots.
3. Enter code **`2508`** → **Done**.
4. Select **Configuration Menu → Other System Settings → Config HostComm**.
5. Select **Remote Access → Serial 2**.
6. Select **Serial 2 Setup → ASCII cmd → 9600 baud** (default).
7. Select **Go to Previous Menu → Save Default Changes**.
8. Select **Exit Configuration Mode → Yes**. The monitor reboots.

- Serial: **9600 baud**, ASCII command mode, as set above.

## Vital Recorder Setup

- Add the device as **`Dash2500`** and select the PC serial port used for the connection.
