# Edwards Lifesciences Vigilance II

<!-- meta
category: Hemodynamic Monitor
manufacturer: Edwards Lifesciences
vr_device_name: Vigilance
-->
> ⚠️ **Select `Vigilance` in Vital Recorder** — there is no separate "Vigilance II" entry. And a **straight-through serial cable will not work**: the link needs the TX/RX crossover from the **Null Modem (M/F)**. Both mistakes are recurring field reports for this monitor.

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|----------------|
| Direct Serial | Null Modem **M/F** | Port **1** — the **upper** of the two rear **female** DB-9 ports | `Vigilance` |

## Connection Steps
1. Locate port **1** on the rear panel. Two identical **female** DB-9 ports are stacked vertically, marked **1** (upper) and **2** (lower). Use the upper one.

   <img src="../hardware_images/edwards_vigilance2_1.png" width="450" alt="Vigilance II rear panel with the upper of two stacked female DB-9 ports circled, marked 1 with port 2 below it and the RJ-45 and ECG connectors alongside">

2. Attach a **Null Modem (M/F)** adapter to port 1.
3. Connect a direct (straight-through) serial cable from the adapter to the PC via a USB-Serial converter.

## Device Configuration
1. Touch the **wrench (setup)** icon in the tool bar at the bottom left of the screen.

   <img src="../hardware_images/edwards_vigilance2_2.png" width="450" alt="Vigilance II monitoring screen with the wrench-shaped setup icon in the bottom-left tool bar circled">

2. In the **Setup Menu** select **Serial Port Setup**.

   <img src="../hardware_images/edwards_vigilance2_3.png" width="450" alt="Vigilance II Setup Menu listing Display Format, Serial Port Setup, Analog Input Setup, Analog Output Setup, Default Settings, Patient CCO Cable Test, Demo Mode and Message Log, with Serial Port Setup highlighted">

3. On the **Com 1** column set **Device = IFMout** and **Baud Rate = 9600**, then **Return**.

   <img src="../hardware_images/edwards_vigilance2_5.png" width="450" alt="Vigilance II Serial Port Setup screen with Com 1 set to Device IFMout, Baud Rate 9600, Parity None, Stop Bits 1, Data Bits 8 and Flow Control 2 seconds, while Com 2 Device is None">

Resulting serial settings:

| Parameter | Value |
|-----------|-------|
| Device | IFMout |
| Baud Rate | 9600 |
| Parity | None |
| Stop Bits | 1 |
| Data Bits | 8 |
| Flow Control | 2 seconds |

## Vital Recorder Setup

- In the Vital Recorder device list this appears under **Cardiac monitor** as **Edwards Lifesciences: Vigilance** — the same entry as the first-generation Vigilance. Selecting anything else will record nothing.

## Notes

- **Vital Recorder version:** run the latest release (see the [official version history](https://vitaldb.net/vital-recorder/?action=versions)); device-related version notes are collected in [version-notes.md](../version-notes.md).
- **Do not confuse `Analog Input Setup` with `Serial Port Setup`.** The two entries sit next to each other in the Setup Menu, and Analog Input Setup lists **Port 1 / Port 2 / Port 3** which look deceptively like the serial ports. Analog input carries external pressure signals and is not used by Vital Recorder.

  <img src="../hardware_images/edwards_vigilance2_4.png" width="450" alt="Vigilance II Analog Input Setup screen listing Port 1 (None), Port 2 (None) and Port 3 (None) — the wrong menu for Vital Recorder">

- Source: field reports on the VitalDB bug-report board (crossover cable required; only `Vigilance` selectable).
