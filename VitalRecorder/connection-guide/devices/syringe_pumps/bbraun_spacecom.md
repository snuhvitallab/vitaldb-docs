# B. Braun SpaceCom

<!-- meta
category: Syringe Pump
manufacturer: B. Braun
vr_device_name: SpaceCom
-->
> **Note:** **Two ports, two jobs.** Data is recorded from the **9-pin mini-DIN serial port** at the bottom of the SpaceCom module, but the serial interface must first be enabled and its parameters set through the **SpaceOnline web interface**, reached over the **LAN (RJ-45) port** higher up on the same module.

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|---------------- |
| Cable for 9-pin mini-DIN serial port | None | Serial (9-pin mini-DIN), bottom of the SpaceCom module | `SpaceCom` |
| Ethernet patch cable (configuration only) | None | LAN (RJ-45), SpaceOnline | — |

## Connection Requirements

The SpaceCom has a 9-pin mini-DIN serial port and a separate LAN (RJ-45) port. Use the serial port for Vital Recorder data and the LAN port to configure the serial interface through SpaceOnline.

## Connection Steps
1. Identify the two ports on the SpaceCom module's connector column: the **LAN port (SpaceOnline)** near the top, below the two status LEDs, and the **serial port (9-pin mini-DIN)** at the bottom of the column.

   <img src="../hardware_images/bbraun_spacecom_1.png" width="450" alt="SpaceStation with SpaceCom module, its connector column labeled with the LAN Port (SpaceOnline) near the top and the Serial Port (9pin mini DIN) at the bottom">

2. Connect a cable for the 9-pin mini-DIN serial port to the PC's serial interface or a USB-Serial converter.

## Device Configuration

The serial interface is configured over LAN through **SpaceOnline**, the module's built-in web interface.

1. Connect the SpaceCom **LAN port** to the PC with an Ethernet cable and give the PC a static address on the module's subnet:
   - PC IP: `192.168.100.42` / Subnet: `255.255.255.0` / Gateway: `192.168.100.1`
   - The SpaceCom's own default Ethernet address is **`192.168.100.41`**.
2. Open a browser to **`192.168.100.41`** and log in. B. Braun ships three fixed accounts, each opening a different page — use the configuration one:
   - `status` / `status` — status page
   - `service` / `service` — service page
   - **`config` / `config` — configuration page**
3. Select **Configuration** in the left-hand menu. Set **Language** to *English* first if the interface came up in another language.

   <img src="../hardware_images/bbraun_spacecom_2.png" width="450" alt="SpaceOnline web interface left menu with the Language selector set to English and Status, Service and Configuration entries, Configuration highlighted">

4. Open **BCC Protocol settings** (its panel is titled *Interface Settings*) and set the serial parameters:

   <img src="../hardware_images/bbraun_spacecom_3.png" width="450" alt="SpaceOnline Interface Settings panel with Interface COM1, Baudrate 9600, Parity n, Stopbits 1 and Databits 8">

5. Press **Save**. Power-cycle the SpaceStation so the interface comes up with the new settings.

- Interface: **COM1**
- Serial: **9600 baud, 8 data bits, No parity (`n`), 1 stop bit**

## Vital Recorder Setup

- Add the device in Vital Recorder as **`SpaceCom`**.
