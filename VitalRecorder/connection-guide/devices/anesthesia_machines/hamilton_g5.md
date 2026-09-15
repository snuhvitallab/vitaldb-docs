# Hamilton G5 Ventilator

<!-- meta
category: Anesthesia Machine
manufacturer: Hamilton
vr_device_name: Hamilton
-->
> **Note:** Available in Vital Recorder **1.10.2** or later. Either Monitoring Interface port (1 or 2) can be used, but the port's protocol must be switched to **Block** first.

| Cable | Adapter | Port | Protocol | Serial | VR Device Name |
|-------|---------|------|----------|--------|----------------|
| Direct Serial | Null Modem M/F | Monitoring Interface 1 or 2 | `HAMILTON-G5 / Block` | 38400 baud, 8 data bits, No parity, 1 stop bit, no handshake | `Hamilton` |

## Connection Steps
1. Find the connector column on the side/rear of the ventilator. Three connectors are stacked there:
   - **Special Interface connector** (15-pin, topmost) — **not** a COM port, do not use it
   - **Monitoring Interface 1 connector** (9-pin) = COM1
   - **Monitoring Interface 2 connector** (9-pin) = COM2
2. Attach a **Null Modem (M/F)** adapter to Monitoring Interface **1** or **2**.
3. Connect a direct serial cable from the adapter to the PC via a USB-Serial converter.

The COM (RS-232) connector pin assignment is: **2 RxD, 3 TxD, 4 DTR, 5 GND, 6 DSR, 7 RTS, 8 CTS** (pins 1 and 9 unused, shield = chassis ground).

## Device Configuration
> The interface controls only appear when the ventilator is **in Standby** (not ventilating a patient).

1. Enter **Configuration mode**: press the **O₂ enrichment** and **Manual breath** keys **at the same time**. A **Configuration** button appears at the bottom left of the screen.
2. Enable **Test mode**: press the **Screen Lock/Unlock** and **Nebulizer On/Off** keys **at the same time**. Both Configuration and Test modes must be enabled for the interface controls to be editable — but **do not actually enter Test mode**.
3. Touch **Configuration**, then **Interface**.
4. On the block for the port you cabled (**COM1 protocol** or **COM2 protocol**), select **`HAMILTON-G5 / Block`**.
5. Touch **Close**, then **Close/Save** to store the setting.

- Block protocol line settings: **38400 baud, 8 data bits, No parity, 1 stop bit, no handshake**
- Do **not** select `HAMILTON-G5 / Polling` or `Galileo / Polling` — polling runs at 9600 baud, 7 data bits, Even parity, 2 stop bits with XON/XANY handshake and transmits only a subset of the data. `DraegerTestProtocol` is for Dräger MIB II converters and `HAMILTON-G5 / Block (ACK)` for distributed alarm systems.

## Vital Recorder Setup

- In Vital Recorder, add the device as **`Hamilton`**.

## Notes
- Block mode carries all settings, measurements, alarms and up to 8 high-resolution waveforms; polling mode is limited to 4 low-resolution waveforms and a data subset — this is why Vital Recorder requires Block.
- The two Monitoring Interface ports are independent, so a patient monitor can stay on one port while Vital Recorder uses the other. Each port has its own protocol setting.
- Typical parameters recorded: Paw, PEEP, Pplat, TV, MV, RR, FiO2, CO2.
