# Mdoloris ANI Monitor V2

<!-- meta
category: Multifunction Monitor
manufacturer: MDMS
vr_device_name: ANIMonitor2
-->
> **Note:** **Use the DB-9 port marked `REAL TIME EXPORT`.** The USB port beside it is marked `DATA EXPORT` and is for offline file export only — it will not stream data to Vital Recorder.

| Cable | Adapter | Port | Serial | VR Device Name |
|-------|---------|------|--------|----------------|
| USB-Serial converter | None | `REAL TIME EXPORT` DB-9 (connector panel) | 115200 baud | `ANIMonitor2` |

## Connection Requirements

ANI = Analgesia Nociception Index. The V2 monitor derives it from the ECG-based respiratory pattern.

## Connection Steps

1. Attach the ANI sensor electrodes, press **New Patient**, and wait about **one minute** for the monitor to finish initialising. The ANI trend, respiratory pattern and ECG traces should be running before you connect.

   <img src="../hardware_images/mdms_ani_monitor_1.jpg" width="450" alt="ANI Monitor V2 running — Analgesia Nociception Index trend, respiratory pattern and ECG traces with Stop, Screen shot, ANI navigation, Events and Parameters buttons">

2. Find the connector panel on the side of the monitor. Left to right it carries **ECG IN**, the **REAL TIME EXPORT** DB-9 connector, the **DATA EXPORT** USB port (5 V, 500 mA), and the power connector.

   <img src="../hardware_images/mdms_ani_monitor_2.png" width="450" alt="ANI Monitor connector panel — ECG IN, the highlighted REAL TIME EXPORT DB-9 connector, and the DATA EXPORT USB port below it">

3. Plug the USB-Serial converter **directly into the `REAL TIME EXPORT` DB-9** — no Null Modem adapter is needed.

   <img src="../hardware_images/mdms_ani_monitor_3.jpg" width="450" alt="NEXT-RS232U20 USB-Serial converter plugged into the REAL TIME EXPORT DB-9 port on the ANI Monitor">

4. Connect the USB end to the PC.

## Device Configuration

**No on-device setting is required** — the ANI Monitor V2 streams on the `REAL TIME EXPORT` port as soon as a session is running.


## Vital Recorder Setup

- Add the device in Vital Recorder as **`ANIMonitor2`**.

## Troubleshooting

- **Vital Recorder shows the device but no values.** Confirm that **New Patient** was pressed and that the monitor has finished initializing; the port remains silent until a session starts.

## Notes

- The screwposts on the `REAL TIME EXPORT` connector are usable; fastening the converter prevents it working loose.
