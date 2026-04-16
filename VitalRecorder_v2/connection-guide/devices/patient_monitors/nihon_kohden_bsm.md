# Nihon Kohden BSM

<!-- meta
category: Patient Monitor
manufacturer: Nihon Kohden
vr_device_name: BSM
-->
> **Note:** Available in Vital Recorder **v1.8.16.2 or later**. Requires **QI-373P board** installed in the monitor.

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|----------------|
| Direct Serial (numeric) | Null Modem M/F | RS-232C on QI-373P board | `BSM` |
| ECG/BP output cable + custom 5.5pi Mono → RJ45 (waveform) | None | ECG/BP OUT port | `BSM` |

## Connection Steps — Numeric Data

1. Attach a **Null Modem (M/F)** to the serial port on the QI-373P board.

   <img src="../hardware_images/nihon_kohden_bsm_1.png" width="450" alt="QI-373P board — serial port">

2. Connect a direct serial cable from the adapter to the PC via USB-Serial converter.

## Connection Steps — ECG/ART Waveform

1. Plug the **ECG/BP output cable** (from Nihon Kohden) into the ECG/BP OUT port.
2. Fabricate a **5.5pi Mono to RJ45 cable** per the pin diagram to connect to the ADC.
3. Connect the ADC to the PC via USB.