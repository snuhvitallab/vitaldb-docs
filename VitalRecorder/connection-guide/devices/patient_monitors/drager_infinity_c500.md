# Dräger Infinity C500 / C700 (Infinity Acute Care System, IACS)

<!-- meta
category: Patient Monitor
manufacturer: Dräger
vr_device_name: Infinity
-->
> **Note:** This Infinity Acute Care System (IACS) connection records **numeric data** through the P2500 export port. ECG and arterial pressure waveforms require the **Analog/Sync** connection and an ADC.

| Connection | Cable or Interface | Adapter | Port | VR Device Name |
|---|---|---|---|--- |
| Numeric data | Dräger export protocol cable MS22948 or custom RJ-10 to DB-9F cable | None for the cable described below | Export port on P2500 | `Infinity` |
| ECG/BP waveforms | Compatible Analog/Sync cable, connection cable for the ADC, and ADC | Depends on the ADC connection | Analog/Sync connection on M540 | Select the device type for your ADC |

## Connection Requirements

Use the **P2500 export port** for this serial connection. No additional null modem adapter is required with the custom pin assignment below.

For analog waveforms, use a compatible **Dräger Analog/Sync cable** and ADC. If an **Infinity M-Cable Microstream CO2** is also connected to the M540, use the compatible Y-cable arrangement for those accessories.

## Cable Pinout

### Numeric Data

| RJ-10 Pin (P2500 end) | DB-9F Pin (PC end) |
|---|--- |
| 3 | 2 |
| 2 | 3 |
| 4 | 5 |

## Connection Steps

### Numeric Data

1. Prepare a custom RJ-10 to DB-9F cable using the connections in [Cable Pinout](#cable-pinout), or use the Dräger export protocol cable **MS22948**.
2. Connect the **RJ-10 end** to the export port on the **P2500**.
3. Connect the **DB-9F end** to the PC's serial port. If the PC has no serial port, use a **USB-Serial converter**.

### ECG/BP Waveforms

Waveforms are only available as analog voltages, read through an ADC (SNU-ADC, DataQ DI-149/DI-155, …).

1. Obtain a Dräger **Analog/Sync cable**.
   - When the monitor is also using an **Infinity M-Cable Microstream CO2**, the Analog/Sync cable is joined through a **Y cable** and connected to the **M540** monitor.
2. Build a **MDR14 ↔ RJ45** cable to bring the Analog/Sync cable's MDR connector into the ADC. The MDR-14 shell and the finished cable can both be ordered:
   - [Connector purchase link](http://www.cableguy.com/shop/mall.php?cat=007002007&query=view&no=210644)
   - [Pre-made cable purchase link](http://www.cableguy.com/shop/mall.php?cat=025015011&query=view&no=209983)
3. Connect the ADC to the PC via USB.
4. In Vital Recorder add the ADC (**SNUADC** or **SNUADCM**) and map the channels: **ART = ch2 with gain ×100**, **ECG = ch3**.

## Device Configuration

No changes to the monitor settings are required for the numeric-data connection described here.

## Vital Recorder Setup

### Numeric Data

- Add the device as **`Infinity`** and select the PC serial port used for the connection.

### ECG/BP Waveforms

- Add the device type corresponding to your **ADC**.
- Configure the channels and signal scaling for the cable used. In the SNUADC example from this guide, **ART uses channel 2 with gain ×100**, and **ECG uses channel 3**. This mapping is specific to that cable and ADC setup.
