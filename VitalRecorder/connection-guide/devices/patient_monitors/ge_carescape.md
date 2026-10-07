# GE CARESCAPE B850 / B650 / B450

<!-- meta
category: Patient Monitor
manufacturer: GE
vr_device_name: Bx50
-->
> **Note:** Protocol: **GE S5 Computer Interface** (the Datex DRI protocol, also used by the GE S/5, B40/B20 and B1x5M monitors). Data leaves the monitor through a **USB port**, not through the DB-9 serial connector on the rear panel.

| Cable | Adapter | Port | Serial | VR Device Name |
|-------|---------|------|--------|----------------|
| Monitor-side USB-Serial converter — **model depends on monitor software version** (see below) | Null Modem adapter (F/F) | **USB port** on the rear panel | GE S5 Computer Interface | `Bx50` |

## Connection Requirements

The monitor-side USB-Serial converter depends on monitor software version. The CARESCAPE runs its own embedded OS and carries drivers for these converters only:

| Monitor software | Converter |
|---|---|
| **v3.1.4 or later** | **Startech ICUSB232V2** |
| **v3.1 – v3.1.3** | Ask GE for the **free firmware upgrade** to 3.1.4 or later, then use the row above. |
| **v2** | **ATEN UC-232A**, legacy revision only |

Check the version under **Monitor setup → Defaults & Service → Service** before buying. Do **not** connect to the monitor's own DB-9 serial port; use a USB port.

**Use an FTDI-based USB-Serial converter on the PC side.** A 3-wire cable connects but loses most of the waveform samples.

## Connection Steps

1. Plug the **monitor-side USB-Serial converter** that matches the monitor's software version (see above) into one of the USB ports on the rear of the monitor. The USB block sits on the lower connector strip, to the left of the DVI and DB-9 connectors.

   <img src="../hardware_images/ge_carescape_1.png" width="450" alt="Rear three-quarter view of a CARESCAPE monitor; a red circle marks the block of four USB ports on the lower connector strip, to the left of the DVI video connector and the DB-9 serial connector">

2. Attach a **Null Modem adapter (F/F)** to the DB-9 end of the monitor-side converter.

3. Run a **direct serial cable** from the Null Modem adapter to the recording PC. On a laptop or tablet, connect a separate FTDI-based PC-side USB-Serial converter.

   ```
   CARESCAPE USB -- monitor-side USB-Serial converter (DB-9M) -- Null Modem adapter (F/F) -- direct serial cable -- PC-side USB-Serial converter (FTDI) -- PC
   ```

## Device Configuration

The monitor has to be told to emit the **S/5** data format on its wired device interface. On software version 1/2 monitors, open **Configuration → Network → Wired Interfaces** and set the interface to **S/5**.

Once the interface is set to S/5, no baud rate has to be chosen on the monitor: Vital Recorder opens the port with the S/5 Computer Interface settings itself.

## Vital Recorder Setup

- Add the device in Vital Recorder as **GE :: Bx50**; in `vr.conf` the type is `Bx50`.
- The Bx50 uses the Datex DRI waveform options. Default waveforms are `ECG1, PLETH, IABP1, CO2, AWP`; request others with `wavs=` — see [Configuration Guide → S5 / Datex Device Settings](../../../Configuration_Guide.md#s5--datex-device-settings-ge-solar--bx50--b1x5m--canvas).
- Invasive arterial pressure is `IABP1` — the names `ART` and `INVP1` are not recognized.

## Troubleshooting

- **Communication stops and does not recover on software version 2.** Reconnect the cable at the monitor end. Use a PC-side FTDI converter and update Vital Recorder before replacing the monitor-side converter.
- **The link drops intermittently.** Use an FTDI-based converter on the PC side.
- **Waveforms drop out.** Trim the `wavs=` list if the monitor cannot sustain all of the defaults (`wavs=1,4,8,9,13` — ECG1, PLETH, IABP1, CO2, AWP).
