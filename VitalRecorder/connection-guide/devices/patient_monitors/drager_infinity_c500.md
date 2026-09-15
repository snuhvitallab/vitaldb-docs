# Dräger Infinity C500 / C700

<!-- meta
category: Patient Monitor
manufacturer: Dräger
vr_device_name: Infinity
-->
> ⚠️ **No monitor-side configuration is required, but C700 firmware 7.xx is known to break RS-232 output.** If a C700 stays silent with correct wiring, check the firmware version before rebuilding cables.

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|----------------|
| Custom RJ10 ↔ DB-9F (numeric) | None | `RJ10` port on the P2500 | `Infinity` |
| Analog/Sync cable → custom MDR14 ↔ RJ45 → ADC (waveform) | None | Analog/Sync port | — (ADC device) |

The DB-9F end goes to the PC's DB-9M serial port or a USB-Serial converter. No Null Modem gender changer is used — the crossover is built into the custom cable's pin mapping.

## Connection Steps — Numeric Data

1. Prepare a cable connecting **RJ10 pins 3, 2, 4** → **DB-9F pins 2, 3, 5**.
2. Connect the **RJ10 end** to the RJ10 port on the **P2500**.
3. Connect the **DB-9F end** to the PC via a USB-Serial converter.
4. In Vital Recorder, add **Patient monitor → Draeger : Infinity**.

## Connection Steps — Waveform Data (Optional)

Waveforms are only available as analog voltages, read through an ADC (SNU-ADC, DataQ DI-149/DI-155, …).

1. Obtain a Dräger **Analog/Sync cable**.
   - When the monitor is also using an **Infinity M-Cable Microstream CO2**, the Analog/Sync cable is joined through a **Y cable** and connected to the **M540** monitor.
2. Fabricate an **MDR14 ↔ RJ45** cable to bring the Analog/Sync cable's MDR connector into the ADC. The MDR-14 shell and the finished cable can both be ordered:
   - [Connector purchase link](http://www.cableguy.com/shop/mall.php?cat=007002007&query=view&no=210644)
   - [Pre-made cable purchase link](http://www.cableguy.com/shop/mall.php?cat=025015011&query=view&no=209983)
3. Connect the ADC to the PC via USB.

## Notes
- **No device configuration is needed** for numeric data — the export protocol on the P2500 RJ10 port is always active.
- **Infinity C700 firmware 7.xx breaks RS-232 output.** Reported from the field; verify the installed firmware with Dräger if a correctly wired C700 produces no data.
- Sibling model **Infinity Kappa** uses the X5/X3 14-pin Mini-D port instead — see [Dräger Infinity Kappa](drager_infinity_kappa.md).
- The MDR-14 pin numbering is not photographed in this guide; request the pinout from the cable vendor or Dräger when ordering.
