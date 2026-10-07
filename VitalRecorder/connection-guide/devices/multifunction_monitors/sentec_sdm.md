# Sentec SDM

<!-- meta
category: Multifunction Monitor
manufacturer: Sentec
vr_device_name: SDM
-->
> **Note:** **The serial interface is disabled while trend data are being downloaded over the LAN port.** It is reactivated automatically once the LAN download finishes.

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|---------------- |
| Direct serial cable | None | RS-232 port | `SDM` |

## Cable Pinout

| DB-9 Pin | Signal |
|----------|-------- |
| 2 | TxD (from SDM) |
| 3 | RxD (to SDM) |
| 5 | Signal ground |
| 1, 4, 6–9 | Reserved |

## Connection Steps

1. Connect a direct serial cable to the **Serial Data Port (RS-232)** on the rear of the SDM.

   <img src="../hardware_images/sentec_sdm_2.png" width="450" alt="Sentec SDM rear panel — the RS-232 serial data port among the surrounding interface connectors">

2. Connect the other end to the PC through a USB-Serial converter.

3. If using a USB-Serial converter, connect its USB end to the PC.

## Device Configuration

Open **Interfaces → Serial Interface** and apply the settings below for this Vital Recorder connection.

| Parameter | Value |
|-----------|------- |
| Protocol | SenTecLink |
| Baud Rate | 115200 |

<img src="../hardware_images/sentec_sdm_1.png" width="450" alt="Serial Interface menu with protocol set to SenTecLink and baud rate 115200">

## Vital Recorder Setup

- Add the device in Vital Recorder as **`SDM`**.
