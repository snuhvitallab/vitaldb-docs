# Blink Device TwitchView

<!-- meta
category: Neuromuscular Monitor
manufacturer: Blink Device Company
vr_device_name: TwitchView
-->
> ⚠️ **The Monitor itself has no data port.** Data leaves the system only through the **RJ45 connector on the Charging Station**, and only while the Monitor is docked.

| Cable | Adapter | Port | Serial | VR Device Name |
|-------|---------|------|--------|----------------|
| Custom RJ45 ↔ DB-9F (see pinout) | None | RJ45 on the Charging Station | 19200 baud | `TwitchView` |

## Connection Requirements

The Charging Station carries a **combined RS-232 serial + Ethernet port on a single industry-standard RJ45 connector**. Selecting which of the two is active is done on the Monitor (see [Device Configuration](#device-configuration)). Exported values are the **TOF Ratio, TOF Count and PTC Count**.

## Connection Steps

1. Dock the Monitor in the Charging Station.

2. Build the custom cable. Only three conductors are used:

   | DB-9 Female (PC side) | | RJ45 (Charging Station side) |
   |---|---|---|
   | 2 — RX | ← | 4 — TX |
   | 3 — TX | → | 5 — RX |
   | 5 — GND | ↔ | 7 — GND |

   <img src="../hardware_images/blink_twitchview_5.png" width="450" alt="Custom cable pinout — DB-9 Female pins 2/3/5 (RX/TX/GND) to RJ45 pins 4/5/7 (TX/RX/GND)">

3. Plug the **RJ45 end** into the Charging Station and the **DB-9F end** into a USB-Serial converter, then into the PC.

## Device Configuration

1. In **Dock Output Configuration**, select **Serial**, then press **Set**.

   <img src="../hardware_images/blink_twitchview_4.png" width="450" alt="Dock Output Configuration dialog — Serial selected among IntelliBridge, Ethernet-UDP and Ethernet-TCP">


## Vital Recorder Setup

- Add the device in Vital Recorder as **`TwitchView`**.

## Known Limitations

- No data is output while the Monitor is undocked.
