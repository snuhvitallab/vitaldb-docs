# Dräger Infinity C500 / C700 (Infinity Acute Care System, IACS)

<!-- meta
category: Patient Monitor
manufacturer: Dräger
vr_device_name: Infinity
-->
> ⚠️ No monitor-side configuration is required. **Some C700 units with firmware 7.xx may have no RS-232 output.** If a correctly wired unit is silent, check its firmware version with Dräger.

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|----------------|
| Custom RJ10 ↔ DB-9F (numeric) — or Dräger **Export Protocol Cable MS22948** | None | `RJ10` port on the P2500 | `Infinity` |
| Analog/Sync cable → custom MDR14 ↔ RJ45 → ADC (waveform) | None | Analog/Sync port | — (ADC device) |

The DB-9F end goes to the PC's DB-9M serial port or a USB-Serial converter. No Null Modem adapter is used — the crossover is built into the custom cable's pin mapping.

## Connection Steps

### Numeric Data

1. Prepare a cable connecting **RJ10 pins 3, 2, 4** → **DB-9F pins 2, 3, 5**.
2. Connect the **RJ10 end** to the RJ10 port on the **P2500**.
3. Connect the **DB-9F end** to the PC via a USB-Serial converter.

### Waveform Data (Optional)

Waveforms are only available as analog voltages, read through an ADC (SNU-ADC, DataQ DI-149/DI-155, …).

1. Obtain a Dräger **Analog/Sync cable**.
   - When the monitor is also using an **Infinity M-Cable Microstream CO2**, the Analog/Sync cable is joined through a **Y cable** and connected to the **M540** monitor.
2. Build a **MDR14 ↔ RJ45** cable to bring the Analog/Sync cable's MDR connector into the ADC. The MDR-14 shell and the finished cable can both be ordered:
   - [Connector purchase link](http://www.cableguy.com/shop/mall.php?cat=007002007&query=view&no=210644)
   - [Pre-made cable purchase link](http://www.cableguy.com/shop/mall.php?cat=025015011&query=view&no=209983)
3. Connect the ADC to the PC via USB.
4. In Vital Recorder add the ADC (**SNUADC** or **SNUADCM**) and map the channels: **ART = ch2 with gain ×100**, **ECG = ch3**.

## Device Configuration

No monitor-side configuration is required for numeric data — the export protocol on the P2500 RJ10 port is always active.

## Vital Recorder Setup

- In Vital Recorder, add **Patient monitor → Draeger : Infinity**.

## Known Limitations

- **The P2500 COM ports are inputs.** On installed systems COM1 is reserved for a Dräger anesthesia machine, COM2 for a TOFscan and COM3 for BIS Vista / EV-1000 data coming *into* the monitor, usually through a Capsule Tech adapter. Recording from the monitor uses the RJ10 export port and the Analog/Sync port described above, not those COMs.

## Notes

- Dräger markets this family as the **Infinity Acute Care System (IACS)** — sites and vendors often say "IACS C500". Same connection.
- Confirm the pinout with Dräger or the cable vendor before building the custom MDR14 ↔ RJ45 cable.
- Sibling model **Infinity Kappa** uses the X5/X3 14-pin Mini-D port instead — see [Dräger Infinity Kappa](drager_infinity_kappa.md).
