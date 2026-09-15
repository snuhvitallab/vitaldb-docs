# GE Dash 2000 / 3000 / 4000

<!-- meta
category: Patient Monitor
manufacturer: GE
vr_device_name: Dashx000
-->
> **Note:** Protocol: **GE Unity Network** — shared with the GE Solar 8000m / 8000i. Serial communication runs through the **RJ-45 Aux terminal**, so a custom DB-9F ↔ RJ-45 cable is required. No monitor-side configuration is needed.

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|----------------|
| Custom DB-9F ↔ RJ-45 | None | **Aux** (RJ-45) on the rear panel | `Dashx000` |

The DB-9F end plugs into the PC's DB-9M serial port or into a USB-Serial converter. Because the crossover is built into the custom cable's pin mapping, **no Null Modem gender changer is used**.

> The Aux terminal sits between the **Ethernet** jack and the **Defib Sync** socket, and the two RJ-45 jacks look identical. The Ethernet jack is *not* the serial port — check the silk-screen label before connecting.

## Connection Steps

1. Locate the **Aux** terminal on the rear panel.

   <img src="../hardware_images/ge_dash2000_1.png" width="450" alt="Rear panel of the monitor — the ETHERNET RJ-45 jack, the Aux RJ-45 terminal with a cable plugged into it, and the round Defib Sync socket, each labeled above">

2. Fabricate or order a DB-9F ↔ RJ-45 cable wired as follows. You can build it from a USB-Serial converter and a length of LAN cable, or send this pinout to a cable shop.

   <img src="../hardware_images/ge_dash2000_2.png" width="450" alt="Cable pinout diagram — DB-9 Female pin 2 RX to RJ-45 pin 6 TX, DB-9 pin 3 TX to RJ-45 pin 3 RX, DB-9 pin 5 GND to RJ-45 pin 4 GND">

   | DB-9 Female (PC side) | Signal | RJ-45 (monitor Aux) | Signal |
   |---|---|---|---|
   | 2 | RX | 6 | TX |
   | 3 | TX | 3 | RX |
   | 5 | GND | 4 | GND |

   Only these three conductors are needed; RJ-45 pins 1, 2, 5, 7 and 8 are left unconnected. Instead of soldering, a standard Cat5/Cat6 patch cable plus an off-the-shelf **RJ-45 female → DB-9 female modular adapter** (screw-terminal type) can be wired to the same three positions.

3. Plug the **RJ-45 end** into the Aux terminal on the rear of the monitor.

4. Plug the **DB-9F end** into the PC via a USB-Serial converter.

## Device Configuration

No service-mode change is required on the monitor — the Aux terminal emits the Unity Network stream as delivered.

- Serial: **9600 baud**, per the Vital Recorder supported-device list for the Dash family.

## Vital Recorder Setup

- Add the device in Vital Recorder as **GE :: Dash x000**; in `vr.conf` the type is `Dashx000`.

## Notes

- The **Dash 2500** is a different device — it uses the GE **Dinamap** protocol on a DB-9 *Host Comm* port and does require configuration. See [GE Dash 2500](ge_dash2500.md).
- The **Dash 5000** speaks the same Unity Network protocol and is expected to work the same way, but it is not in the Vital Recorder supported-device list and has not been verified — confirm the Aux terminal pinout on site before ordering a cable.
- For ECG and ABP as analog voltages (e.g. when higher-fidelity waveforms are needed), the front-panel Defib Sync socket can be used instead — see [GE Defib Connectors](ge_defib.md). On the **Dash 4000** the defib cable pin mapping differs from the SNUADCM default and needs the dedicated `Dash defib-SNUADCM` mapping.
