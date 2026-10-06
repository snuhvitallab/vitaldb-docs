# GE CARESCAPE B850 / B650 / B450

<!-- meta
category: Patient Monitor
manufacturer: GE
vr_device_name: Bx50
-->
> **Note:** Protocol: **GE S5 Computer Interface** (the Datex DRI protocol, also used by the GE S/5, B40/B20 and B1x5M monitors). Data leaves the monitor through a **USB port**, not through the DB-9 serial connector on the rear panel.

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|----------------|
| USB-to-RS232 converter — **model depends on monitor software version** (see below) | Null Modem F/F | **USB port** on the rear panel | `Bx50` |

> ⚠️ **The monitor accepts only specific USB-to-RS232 converters, and which one depends on its software version.** The CARESCAPE runs its own embedded OS and carries drivers for these converters only:
>
> | Monitor software | Converter |
> |---|---|
> | **v3.1.4 or later** | **Startech ICUSB232V2**. Newer Startech stock has been seen to fail on some units — the **MBF-RS232** USB-to-RS232 cable is the proven alternative. |
> | **v3.1 – v3.1.3** | Ask GE for the **free firmware upgrade** to 3.1.4 or later, then use the row above. |
> | **v2** | **ATEN UC-232A**, legacy revision only — serial numbers starting **Z3L1** or later alphabetically (USB vendor ID `0x0557`); this revision is discontinued. **MBF-RS232** also works on v2 (chain: MBF-RS232 → Null Modem F/F → MBF-RS232). |
>
> Check the version under **Monitor setup → Defaults & Service → Service** before buying. Field reports of the Startech "not being recognized" come from v2 monitors. Do **not** connect to the monitor's own DB-9 serial port; use a USB port.

> ⚠️ **The Bx50 uses hardware handshaking.** A 3-wire connection will not work. The converter on the **PC** side must carry **DTR and RTS** — an FTDI-based converter is recommended. With a 3-wire cable or a converter that drops the handshake lines the link comes up but roughly 60 % of the waveform samples are lost and reception is intermittent.

## Connection Steps

1. Plug the USB-to-RS232 converter that matches the monitor's software version (see above) into one of the USB ports on the rear of the monitor. The USB block sits on the lower connector strip, to the left of the DVI and DB-9 connectors.

   <img src="../hardware_images/ge_carescape_1.png" width="450" alt="Rear three-quarter view of a CARESCAPE monitor; a red circle marks the block of four USB ports on the lower connector strip, to the left of the DVI video connector and the DB-9 serial connector">

   Field installations most often use **USB port 4**. If no data appears, try the other ports before suspecting the cable.

2. Attach a **Null Modem (F/F)** adapter to the DB-9 end of the converter. This is what turns the two "direct" ends into a crossed link.

3. Run a **direct serial cable** from the Null Modem adapter to the recording PC. On a laptop or tablet this means a second USB-Serial converter on the PC side — that one must support DTR/RTS (FTDI recommended).

   ```
   CARESCAPE USB -- USB-to-RS232 converter (DB-9M) -- Null Modem F/F -- direct serial cable -- USB-Serial (FTDI) -- PC
   ```

## Device Configuration

The monitor has to be told to emit the **S/5** data format on its wired device interface. On software version 1/2 monitors this is reached through **Configuration → Network → Wired Interfaces**, where the interface is set to **S/5**. The exact wording, and whether a service login is required, varies by monitor software version — confirm against the CARESCAPE technical manual for your version, or have the GE field engineer set it.

Once the interface is set to S/5, no baud rate has to be chosen on the monitor: Vital Recorder opens the port with the S/5 Computer Interface settings itself.

## Vital Recorder Setup

- Add the device in Vital Recorder as **GE :: Bx50**; in `vr.conf` the type is `Bx50`.
- The Bx50 uses the Datex DRI waveform options. Default waveforms are `ECG1, PLETH, IABP1, CO2, AWP`; request others with `wavs=` — see [Configuration Guide → S5 / Datex Device Settings](../../../Configuration_Guide.md#s5--datex-device-settings-ge-solar--bx50--b1x5m--canvas).
- Invasive arterial pressure is `IABP1` — the names `ART` and `INVP1` are not recognized.

## Troubleshooting

- **A freshly bought UC-232A produces nothing.** Converter revision matters: field reports indicate that only the older ATEN UC-232A revision (USB vendor ID `0x0557`) is driven by the monitor's built-in driver; newer stock built around a different chipset (`0x067b`) is not. Check the revision before changing anything else.
- **An otherwise-correct installation produces nothing.** Dust in the rear USB ports has stopped such installations — clean the port before suspecting the converter.
- **Communication stops and does not auto-recover (software version 2).** Data is received normally and then stops at an unpredictable point, and Vital Recorder does not re-establish the link on its own. Workaround: **unplug and re-plug the cable at the monitor end** — reception resumes immediately. Sites with frequent stoppages have fitted a relay to automate the re-connection, which reduced but did not fully eliminate the problem. Two causes have since been identified: (1) a missing hardware handshake on the PC-side converter (check DTR/RTS first), and (2) a one-second waveform gap at every re-request, which Vital Recorder fixed by sending the request only once at start-up — **update Vital Recorder** before chasing hardware.
- **The link drops intermittently.** Prolific-based PC-side cables (ATEN new revision, NETmate Prolific, UGREEN Prolific) connect but drop intermittently; changing the monitor's USB port sometimes restores them. Avoid PL2303-based converters — they have proved unstable in the field (`pl2303_get_line_request failed`). Converters proven stable on Linux/PiVR: NETmate **KW-725 / KW-825** (FTDI) and UGREEN FTDI.
- **Waveforms drop out.** Trim the `wavs=` list if the monitor cannot sustain all of the defaults (`wavs=1,4,8,9,13` — ECG1, PLETH, IABP1, CO2, AWP).

## Notes

- **Confirm the model before the site visit.** The B1x5M (B105M/B125M/B155M) and the Bx50 look alike on a pre-survey form but need different cabling and a different Vital Recorder device type — see [GE B105M / B125M / B155M](ge_b105m.md).
- **VRZero note:** the USB cable that connects to VRZero must support handshaking. Cables known to work:
  - [NETmate KW-525 (0.45 m)](http://www.compuzone.co.kr/product/product_detail.htm?ProductNo=374732)
  - [ATEN UC-232A (0.35 m)](http://www.compuzone.co.kr/product/product_detail.htm?ProductNo=60189)

## Sources

- Original Vital Recorder connection guide (legacy English and Korean editions) — *GE CARESCAPE B850, B650, B450*: USB port (not the DB-9 serial port), USB-to-RS232 converter plus Null Modem (F/F), S/5 Computer Interface protocol. The English edition (newer) gives the version rule — **v3.1 or higher: Startech ICUSB232V2; v2: legacy ATEN UC-232A, serial numbers Z3L1 or later, discontinued**; the Korean edition states ATEN only. The VRZero cable links (NETmate KW-525, ATEN UC-232A) are from the same guide.
- `VitalRecorder/Supported_Devices.md` — *Bx50, RS-232, 9600 baud, ECG, NIBP, SpO2, Temp, IBP*.
- `VitalRecorder/Configuration_Guide.md` (S5 / Datex Device Settings) — default waveforms `ECG1, PLETH, IABP1, CO2, AWP`, `wavs=` option and `IABP1` naming.
- Rear-panel USB port location: photographs in this guide.
- Field records (VitalDB installation and support logs, 2024–2026) — v3.1.4 Startech and the free firmware upgrade, MBF-RS232 as the alternative on both v3.1.4+ and v2, "Startech not recognized" reports traced to v2 units, USB port 4, dust in the rear USB ports, ATEN revision by USB vendor ID (`0x0557` vs `0x067b`), the two causes of non-recovering communication loss on v2 (missing handshake; one-second gap per re-request fixed in Vital Recorder), Prolific-based cable drop-outs and the converters proven stable on Linux/PiVR (NETmate KW-725 / KW-825, UGREEN FTDI).
