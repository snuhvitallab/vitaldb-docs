# Maquet Flow-i

<!-- meta
category: Anesthesia Machine
manufacturer: Maquet
vr_device_name: Flow-i
-->
> **Note:** No additional device configuration required.

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|----------------|
| direct serial cable | Null Modem adapter (M/F) | Serial port — lower right of the rear panel | `Flow-i` |

## Connection Steps
1. Locate the **DB-9 serial port** on the lower right of the rear panel and attach a **Null Modem adapter (M/F)** to it.

   <img src="../hardware_images/maquet_flow_i_1.png" width="450" alt="Flow-i rear panel with the DB-9 serial port outlined in red, next to a network connector">

2. Connect a direct serial cable from the adapter to the PC via a USB-Serial converter.

## Device Configuration
Nothing has to be set on the machine — the serial port streams as soon as it is cabled.

## Vital Recorder Setup

- In Vital Recorder, add the device as **`Flow-i`**.

## Troubleshooting

- **The port opens but no data arrives.** Check that the Null Modem adapter is fitted and the cable is fully seated.

## Known Limitations

- **Set TV is not transmitted** by Flow-i protocol v5 (the channel was removed). In volume modes derive it as **Set MV ÷ Set RR**. Eleven set-parameters, including Set MV, RR, PEEP, PC, PS, FGF, FGF O2 % and Agent %, are recorded.

## Notes

- The Flow-i has **two independent serial ports**, so a patient monitor can keep one while Vital Recorder uses the other. (This is unlike the Servo-i, which has a single usable RS-232 port.)
