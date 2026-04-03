# GE Corometrics 170

<!-- meta
category: Patient Monitor
manufacturer: GE
vr_device_name: 41
-->
| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|----------------|
| Direct Serial | None | RS232 Port 1 or 2 | `Coro` |

## Connection Steps
1. Connect a direct serial cable to **RS232 Port 1** (or Port 2) on the device.
2. Connect the other end to the PC via USB-Serial converter.

## Device Configuration
> To enter setup mode: hold the **setup button (clock/calendar icon)** while pressing the power button. Keep holding throughout the setup process.

<img src="../hardware_images/ge_corometrics_2.png" width="300" alt="Setup button location">

1. Use the **UA Reference button** to activate settings for FHR or UA display.

   <img src="../hardware_images/ge_corometrics_1.png" width="450" alt="UA Reference button">

2. Set values using the **volume button**:

   | Port | Setting | FHR Display | UA Display |
   |------|---------|-------------|------------|
   | RS232 Port 1 | Communication mode | `30` | `5` |
   | RS232 Port 1 | Baud rate | `40` | `96` |
   | RS232 Port 2 | Communication mode | `31` | `5` |
   | RS232 Port 2 | Baud rate | `41` | `96` |


---

## Anesthesia Machines
