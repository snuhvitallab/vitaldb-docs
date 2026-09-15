# GE CARESCAPE B850 / B650 / B450

<!-- meta
category: Patient Monitor
manufacturer: GE
vr_device_name: Bx50
-->
> **Note:** Protocol: **GE S5 Computer Interface** (the Datex DRI protocol, also used by the GE S/5, B40/B20 and B1x5M monitors). Data leaves the monitor through a **USB port**, not through the DB-9 serial connector on the rear panel.

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|----------------|
| **ATEN UC-232A** USB-to-RS232 | Null Modem F/F | **USB port** on the rear panel | `Bx50` |

> ⚠️ **ATEN UC-232A is the only USB-Serial converter the monitor accepts.** The CARESCAPE runs its own embedded OS and only carries drivers for that converter — other converters (including the Startech ICUSB232V2) are not recognized and produce no data. Do **not** connect to the monitor's own DB-9 serial port; use a USB port.

> ⚠️ **The Bx50 uses hardware handshaking.** A 3-wire connection will not work. The converter on the **PC** side must carry **DTR and RTS** — an FTDI-based converter is recommended. With a 3-wire cable or a converter that drops the handshake lines the link comes up but roughly 60 % of the waveform samples are lost and reception is intermittent.

## Connection Steps

1. Plug the **ATEN UC-232A** USB-to-RS232 converter into one of the USB ports on the rear of the monitor. The USB block sits on the lower connector strip, to the left of the DVI and DB-9 connectors.

   <img src="../hardware_images/ge_carescape_1.png" width="450" alt="Rear three-quarter view of a CARESCAPE monitor; a red circle marks the block of four USB ports on the lower connector strip, to the left of the DVI video connector and the DB-9 serial connector">

   Field installations most often use **USB port 4**. If no data appears, try the other ports before suspecting the cable.

2. Attach a **Null Modem (F/F)** adapter to the DB-9 end of the ATEN converter. This is what turns the two "direct" ends into a crossed link.

3. Run a **direct serial cable** from the Null Modem adapter to the recording PC. On a laptop or tablet this means a second USB-Serial converter on the PC side — that one must support DTR/RTS (FTDI recommended).

   ```
   CARESCAPE USB -- ATEN UC-232A (DB-9M) -- Null Modem F/F -- direct serial cable -- USB-Serial (FTDI) -- PC
   ```

## Device Configuration

The monitor has to be told to emit the **S/5** data format on its wired device interface. On software version 1/2 monitors this is reached through **Configuration → Network → Wired Interfaces**, where the interface is set to **S/5**. The exact wording, and whether a service login is required, varies by monitor software version — confirm against the CARESCAPE technical manual for your version, or have the GE field engineer set it.

Once the interface is set to S/5, no baud rate has to be chosen on the monitor: Vital Recorder opens the port with the S/5 Computer Interface settings itself.

## Vital Recorder Setup

- Add the device in Vital Recorder as **GE :: Bx50**; in `vr.conf` the type is `Bx50`.
- The Bx50 uses the Datex DRI waveform options. Default waveforms are `ECG1, PLETH, IABP1, CO2, AWP`; request others with `wavs=` — see [Configuration Guide → S5 / Datex Device Settings](../../../Configuration_Guide.md#s5--datex-device-settings-ge-solar--bx50--b1x5m--canvas).
- Invasive arterial pressure is `IABP1` — the names `ART` and `INVP1` are not recognized.

## Notes

- **Converter revision matters.** Field reports indicate that only the older ATEN UC-232A revision (USB vendor ID `0x0557`) is driven by the monitor's built-in driver; newer stock built around a different chipset (`0x067b`) is not. If a freshly bought UC-232A produces nothing, check the revision before changing anything else.
- **Communication stops and does not auto-recover (software version 2).** Data is received normally and then stops at an unpredictable point, and Vital Recorder does not re-establish the link on its own. Workaround: **unplug and re-plug the cable at the monitor end** — reception resumes immediately. Sites with frequent stoppages have fitted a relay to automate the re-connection, which reduced but did not fully eliminate the problem (Chonnam National University Hospital ICU, 2026); the root cause is still under investigation. Before investigating it, verify that the cable and the PC-side converter really carry DTR/RTS, since a missing handshake produces similar symptoms.
- **Avoid PL2303-based converters on the PC side.** They have proved unstable in the field (`pl2303_get_line_request failed`).
- **Confirm the model before the site visit.** The B1x5M (B105M/B125M/B155M) and the Bx50 look alike on a pre-survey form but need different cabling and a different Vital Recorder device type — see [GE B105M / B125M / B155M](ge_b105m.md).
- **VRZero note:** the USB cable that connects to VRZero must support handshaking. Cables known to work:
  - [NETmate KW-525 (0.45 m)](http://www.compuzone.co.kr/product/product_detail.htm?ProductNo=374732)
  - [ATEN UC-232A (0.35 m)](http://www.compuzone.co.kr/product/product_detail.htm?ProductNo=60189)
