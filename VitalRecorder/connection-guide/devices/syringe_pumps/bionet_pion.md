# Bionet Pion TCI

<!-- meta
category: Syringe Pump
manufacturer: Bionet
vr_device_name: Pion
-->
> **Note:** When multiple Pion pumps are connected, Vital Recorder distinguishes them by the **number in the device name**. A device named **`Pion2`** produces tracks prefixed **`PUMP2_`**; a name with no number defaults to **`PUMP1_`**.

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|---------------- |
| direct serial cable | None | RS-232 port | `Pion` |

## Connection Steps
1. Connect a direct serial cable to the serial port.

   <img src="../hardware_images/bionet_pion_1.png" width="450" alt="Pion TCI rear panel with the DB-9 female serial port circled, beside the square USB-B socket and below the 100-240V mains rating label">

## Device Configuration

No pump-side configuration is required.

## Vital Recorder Setup

- Add each pump as **`Pion`**, and **name each device to match its pump number** — `Pion1`, `Pion2`, and so on. The number in the device name is what Vital Recorder uses to separate the pumps.
- The screenshot below shows a device named `Pion2` on COM5 producing `PUMP2_`-prefixed tracks.

  <img src="../hardware_images/bionet_pion_2.png" width="450" alt="Vital Recorder with a device named Pion2 on COM5 and tracks PUMP2_CT, PUMP2_RATE, PUMP2_CP, PUMP2_CE, PUMP2_MODE showing TCIE and PUMP2_DRUG showing REMIFENTANIL">
