# IDMED TOFscan

<!-- meta
category: Neuromuscular Monitor
manufacturer: IDMED
vr_device_name: TOFScan
-->
> **Note:** **The TOFscan data port is optical, not electrical.** Use the **TOF-RS1** or **TOF-RS2** optic-to-serial cable; a direct serial cable cannot be used.

| Cable | Adapter | Port | Serial | VR Device Name |
|-------|---------|------|--------|----------------|
| TOF-RS1 or TOF-RS2 optic-serial cable (from IDMED) — DB-9F output | None | Optical output port on the device | 19200 baud | `TOFScan` |

## Connection Steps

1. Obtain a **TOF-RS1** or **TOF-RS2** cable from IDMED.

2. Screw the cable's optical connector onto the **optical output port** on the device.

   <img src="../hardware_images/idmed_tofscan_1.png" width="450" alt="Optical output port on the device with the TOF-RS1 cable connector screwed on">

3. Plug the cable's **DB-9F end directly into a USB-Serial converter** — no Null Modem adapter is needed.

4. Connect the USB-Serial converter to the PC.

## Device Configuration

The connection uses 19200 baud.

## Vital Recorder Setup

- Add the device in Vital Recorder as **`TOFScan`**.

## Troubleshooting

- **No data arrives.** Check the optical connector, cable type and USB-Serial converter.
