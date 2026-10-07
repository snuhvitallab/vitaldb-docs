# GE B105M / B125M / B155M

<!-- meta
category: Patient Monitor
manufacturer: GE
vr_device_name: B1x5M
-->
> **Note:** Protocol: **GE S5 Computer Interface** (the Datex DRI protocol, as on the Bx50 and S/5). On firmware **version 4 and later** the S/5 output has to be switched on and routed to the serial port in the service menu — see Device Configuration below.

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|----------------|
| direct serial cable | None | Serial port marked in **red** on the rear panel | `B1x5M` |

## Connection Requirements

> **Note:** **Use an FTDI-based USB-Serial converter on the PC side.** A 3-wire cable connects but loses most of the waveform samples.

## Connection Steps

1. Connect a **direct serial cable** to the serial port **marked in red** on the rear of the monitor. No Null Modem adapter is used — the monitor-side connector and a direct serial cable line up.

2. Connect the other end to the PC through a USB-Serial converter.

   ```
   B1x5M red serial port -- direct serial cable -- USB-Serial (FTDI) -- PC
   ```

### Alternative: USB Output

The monitor can also emit the S/5 stream on one of its USB ports instead (see the channel selector below).

## Device Configuration

> **Note:** Required on firmware **version 4 and later** only. Earlier firmware emits the S/5 stream without any setup.

> **Note:** **Service login required.** When prompted, enter the credentials below:
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

- Serial frame: **8 data bits, Even parity, 1 stop bit** at the baud rate set above (Datex DRI defaults).

## Vital Recorder Setup

- Add the device in Vital Recorder as **GE :: B1x5M**; in `vr.conf` the type is `B1x5M`.
