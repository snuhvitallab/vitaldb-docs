# GE B105M / B125M / B155M

<!-- meta
category: Patient Monitor
manufacturer: GE
vr_device_name: B1x5M
-->
> **Note:** Protocol: **GE S5 Computer Interface** (the Datex DRI protocol, as on the Bx50 and S/5). On firmware **version 4 and later** the S/5 output has to be switched on and routed to the serial port in the service menu — see Device Configuration below.

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|----------------|
| Direct Serial | None | Serial port marked in **red** on the rear panel | `B1x5M` |

> ⚠️ **Use an FTDI-based USB-Serial converter on the PC side.** A 3-wire cable connects but loses most of the waveform samples.

## Connection Steps

1. Connect a **direct serial cable** to the serial port **marked in red** on the rear of the monitor. No Null Modem adapter is used — the monitor-side connector and a standard direct cable already line up.

2. Connect the other end to the PC through a USB-Serial converter.

   ```
   B1x5M red serial port -- direct serial cable -- USB-Serial (FTDI) -- PC
   ```

   The monitor can also emit the S/5 stream on one of its USB ports instead (see the channel selector below), but the red serial port is the route this guide is written for.

## Device Configuration

> **Note:** Required on firmware **version 4 and later** only. Earlier firmware emits the S/5 stream without any setup.

> ⚠️ **Service login required.** When prompted, enter the credentials below:
>
> | Field | Value |
> |-------|-------|
> | ID | `service` |
> | Password | `lcsmsteam` or `wh1tef1sh` |

1. On the monitor, navigate to **Install/Service → Service → Page 3**.
2. Tap **S5/Anesthesia**.
3. Set **S/5 Channel 1** to **Serial** — this routes the S/5 output to the red-marked serial port. The thumbnails down the right-hand side of the screen show which physical connector each choice (`Serial`, `USB2`, `USB3`) refers to.
4. Set the channel's **Baudrate** to **19200**. If **115200** is selected, change it to **19200**.

   <img src="../hardware_images/ge_b105m_1.jpeg" width="450" alt="Photograph of the monitor's S5/Anesthesia Configuration screen: Anesthesia set to USB3; S/5 Channel 1 set to Serial with its Baudrate drop-down open showing the only two choices, 19200 and 115200, with 115200 currently selected; S/5 Channel 2 set to USB2 at 115200; Cancel and Save buttons at the bottom">

5. Tap **Save**.

- Serial frame: **8 data bits, Even parity, 1 stop bit** at the baud rate set above (Datex DRI defaults — verify with GE if the link does not come up).

## Vital Recorder Setup

- Add the device in Vital Recorder as **GE :: B1x5M**; in `vr.conf` the type is `B1x5M`.

### Waveform Selection

Unlike other Datex DRI devices, the B1x5M family defaults to **ECG1 and PLETH only** — the monitor cannot keep up with the full S5 waveform stream. Any other waveform (invasive arterial pressure, CO2, AWP, etc.) must be requested explicitly using the `wavs` option in `vr.conf`:

```ini
[DEV/B1x5M]
type=B1x5M
port=LU
wavs=ECG1,PLETH,IABP1,CO2,AWP
```

> **Arterial pressure (ART) waveform:** Use `IABP1` — names like `ART` or `INVP1` are not recognized. The first invasive pressure channel (labeled **ART** on the monitor screen) maps to `IABP1`; the second to `IABP2`, and so on up to `IABP8`.

See [Configuration Guide → S5 / Datex Device Settings](../../../Configuration_Guide.md#s5--datex-device-settings-ge-solar--bx50--b1x5m--canvas) for the full list of supported waveform names.

## Troubleshooting

- **No DB-9 on the rear panel.** Some B125M / B105M units ship without the serial port fitted; what looks like the port is the connector for GE's **Multi I/O adapter**, which must be purchased from GE to obtain the RS-232 port. The same applies to the B20 / B40.
- **Nothing is recorded on a unit that monitors only ECG or only SpO2** (dialysis rooms, some wards). Vital Recorder's default case-cut logic waits for **both** HR and SpO2 before it starts recording. Set `CUT_BY` in `vr.conf` (HR-only or by-hour).
- **Waveforms stop after about 40 minutes.** Observed on a B125M running on a plain direct serial cable. Check that the PC-side converter is FTDI-based and, if the site allows, shorten the requested `wavs` list — asking for more waveforms than the monitor can sustain is the usual trigger.

## Notes

- The B155M carries its own serial port, so **no ATEN converter is involved** — a plain direct serial cable, unlike the CARESCAPE Bx50. Protocol and tracks are identical to the B650.
- **Do not confuse the B1x5M with the Bx50.** The CARESCAPE B450/B650/B850 uses a different port (USB, with an ATEN UC-232A), a Null Modem adapter and the `Bx50` device type. Pre-survey forms frequently list one model and the site turns out to have the other — see [GE CARESCAPE B850 / B650 / B450](ge_carescape.md).
