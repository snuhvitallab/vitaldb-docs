# Bionet Pion TCI

<!-- meta
category: Syringe Pump
manufacturer: Bionet
vr_device_name: Pion
-->
> **Note:** When multiple Pion pumps are connected, Vital Recorder distinguishes them by the **number in the device name**. A device named **`Pion2`** produces tracks prefixed **`PUMP2_`**; a name with no number defaults to **`PUMP1_`**.

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|----------------|
| Direct serial (DB-9M ↔ DB-9F) | None | Serial (DB-9F), rear panel | `Pion` / `Pion1`, `Pion2`, … |

The device port is DB-9 **female** and the PC side is DB-9 **male**, so a direct cable mates correctly and **no Null Modem adapter is needed**.

## Connection Steps
1. Locate the **DB-9 female** serial port on the rear panel, below the mains inlet label and to the left of the square USB-B socket. Both ports carry the same data-link pictogram, so identify the 9-pin one specifically.

   <img src="../hardware_images/bionet_pion_1.png" width="450" alt="Pion TCI rear panel with the DB-9 female serial port circled, beside the square USB-B socket and below the 100-240V mains rating label">

2. Connect a **direct** serial cable to that port, and the other end to the PC via a USB-Serial converter.
## Device Configuration
- No configuration is required on the pump — no service menu, code or output option has to be enabled.
- **Serial parameters are not published in a publicly available Bionet manual — verify with the manufacturer** if a correctly cabled pump produces no usable data.

## Vital Recorder Setup

- Add each pump as **`Pion`**, and **name each device to match its pump number** — `Pion1`, `Pion2`, and so on. The number in the device name is what Vital Recorder uses to separate the pumps.
- The screenshot below shows a device named `Pion2` on COM5 producing `PUMP2_`-prefixed tracks.

  <img src="../hardware_images/bionet_pion_2.png" width="450" alt="Vital Recorder with a device named Pion2 on COM5 and tracks PUMP2_CT, PUMP2_RATE, PUMP2_CP, PUMP2_CE, PUMP2_MODE showing TCIE and PUMP2_DRUG showing REMIFENTANIL">

## Notes
- Recorded tracks per pump are **`CT`** (target concentration), **`RATE`**, **`CP`** (plasma concentration), **`CE`** (effect-site concentration), **`MODE`** (e.g. `TCIE` for effect-site TCI) and **`DRUG`** (the selected agent, e.g. `REMIFENTANIL`).
- Give every pump a distinct numbered name **before** recording starts. Two devices left at the default name both write to `PUMP1_` and their data will collide.
- Each pump needs its own COM port, so a multi-port USB-Serial converter is the practical way to record several Pion units at once.
