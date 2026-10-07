# GE Datex-Ohmeda Anesthesia Machine

<!-- meta
category: Anesthesia Machine
manufacturer: GE
vr_device_name: Datex-Ohmeda
-->
> **Note:** This guide describes the connection for **Aisys CS2** and **Avance CS2**. Confirm the connector and pinout with GE for other models.

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|---------------- |
| Custom 9-pin ↔ 15-pin serial | None | 15-pin female connector | `Datex-Ohmeda` |

## Cable Pinout

| Machine side — DB-15 male | PC side — DB-9 female |
|---------------------------|------------------------ |
| 13 — TX                   | 2 — RX                 |
| 6 — RX                    | 3 — TX                 |
| 5 — GND                   | 5 — GND                |

<img src="../hardware_images/ge_datex_ohmeda_3.png" width="450" alt="Pin wiring diagram of the custom cable — Datex-Ohmeda DB-15 male pin 13 (TX) to DB-9 female pin 2 (RX), pin 6 (RX) to pin 3 (TX), pin 5 to pin 5 (GND)">

## Connection Steps
1. Open the rear connector cover and connect the **15-pin end** of the custom cable to the serial port.

   <img src="../hardware_images/ge_datex_ohmeda_1.png" width="450" alt="Rear connector panel behind the opened cover, with an arrow marking the 15-pin female connector">

2. Connect the **DB-9F end** to the PC through a USB-Serial converter.

### When the 15-pin Port Is Already in Use

For the connection shown below, use a Y-cable with a receive-only branch to Vital Recorder. Enable **Read Only Mode** when adding the device.

#### Y-Cable Pinout

| Machine end — 15-pin D-sub male | Existing connection — 15-pin D-sub female (CON1) | PC end — DB-9F (CON2) |
|--------------------------------|------------------------------------------------|---------------------- |
| 13 (TxD from machine) | 13 | 2 (RxD at PC) |
| 6 (RxD to machine) | 6 | Not connected |
| 5 (GND) | 5 | 5 (GND) |

Only the machine's transmit signal and ground connect to the PC branch.

<img src="../hardware_images/ge_datex_ohmeda_2.png" width="450" alt="Y-cable pin wiring diagram — machine TX (pin 13) and GND (pin 5) branch to both CON1 (DB-15F, existing GE device) and CON2 (DB-9F, PC Vital Recorder with the read-only option); RX (pin 6) goes only to CON1">

## Device Configuration

No changes to the machine settings are required for this setup.

## Vital Recorder Setup

Add the device as **`Datex-Ohmeda`** and select the PC serial port used for the connection.

For a Y-cable connection, enable **Read Only Mode**. Available data depends on the existing communication between the machine and the connected device.
