# GE Dash 2000 / 3000 / 4000 / 5000

<!-- meta
category: Patient Monitor
manufacturer: GE
vr_device_name: Dashx000
-->
> **Note:** This serial connection uses the **AUX** port and a custom **RJ-45 to DB-9F cable**. The separate Ethernet port is not used for this connection.

| Cable | Adapter | Port | VR Device Name |
|---|---|---|--- |
| Custom RJ-45 to DB-9F cable | None | AUX (RJ-45) | `Dashx000` |

## Cable Pinout

| DB-9F Pin (PC end) | PC Signal | RJ-45 Pin (AUX end) | Monitor Signal |
|---|---|---|--- |
| 2 | RxD | 6 | TxD |
| 3 | TxD | 3 | RxD |
| 5 | GND | 4 | GND |

<img src="../hardware_images/ge_dash2000_2.png" width="450" alt="Cable pinout diagram — DB-9 Female pin 2 RX to RJ-45 pin 6 TX, DB-9 pin 3 TX to RJ-45 pin 3 RX, DB-9 pin 5 GND to RJ-45 pin 4 GND">

## Connection Steps

1. Prepare a custom cable using the connections in [Cable Pinout](#cable-pinout).
2. Connect the **RJ-45 end** to the monitor's **AUX** port.

   <img src="../hardware_images/ge_dash2000_1.png" width="450" alt="Rear panel of the monitor — the ETHERNET RJ-45 jack, the Aux RJ-45 terminal with a cable plugged into it, and the round Defib Sync socket, each labeled above">

3. Connect the **DB-9F end** to the PC's serial port. If the PC has no serial port, use a **USB-Serial converter**.

## Device Configuration

No changes to the monitor settings are required.

## Vital Recorder Setup

- Add the device as **`Dashx000`** and select the PC serial port used for the connection.

## Other Connections

- For ECG and arterial pressure through an ADC, see [GE Defib Connectors](ge_defib.md). The Dash 4000 requires its own connector and ADC channel mapping.
- The [GE Dash 2500](ge_dash2500.md) uses a different port and configuration procedure.
