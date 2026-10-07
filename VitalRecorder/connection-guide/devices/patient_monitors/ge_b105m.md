# GE B105M / B125M / B155M

<!-- meta
category: Patient Monitor
manufacturer: GE
vr_device_name: B1x5M
-->
> **Note:** On monitor software version 4 and later, enable the S/5 output and assign it to the serial port as described in **Device Configuration**.

| Cable | Adapter | Port | VR Device Name |
|---|---|---|--- |
| Direct serial cable with hardware handshaking support | None | X5 Serial port | `B1x5M` |

## Connection Requirements

> **Note:** **Use an FTDI-based USB-Serial converter on the PC side.** A 3-wire cable connects but loses most of the waveform samples.

## Connection Steps

1. Connect a **direct serial cable with hardware handshaking support** to the monitor's **X5 Serial** port. No null modem adapter is required.

### Alternative: USB Output

The monitor can also emit the S/5 stream on one of its USB ports instead (see the channel selector below).

## Device Configuration

> **Note:** Required on firmware **version 4 and later** only. Earlier firmware emits the S/5 stream without any setup.

> **Note:** **Service login required.** When prompted, enter the credentials below:
> | Field | Value |
> |-------|------- |
> | ID | `service` |
> | Password | `lcsmsteam` or `wh1tef1sh` |

1. Open **Install/Service → Service → Page 3 → S5/Anesthesia**.
2. Set **S/5 Channel 1** to **Serial**.
3. Set its **Baudrate** to **19200**.

   <img src="../hardware_images/ge_b105m_1.jpeg" width="450" alt="Photograph of the monitor's S5/Anesthesia Configuration screen: Anesthesia set to USB3; S/5 Channel 1 set to Serial with its Baudrate drop-down open showing the only two choices, 19200 and 115200, with 115200 currently selected; S/5 Channel 2 set to USB2 at 115200; Cancel and Save buttons at the bottom">

4. Select **Save**.

## Vital Recorder Setup

- Add the device as **`B1x5M`** and select the PC serial port used for the connection.
- For waveform selection, see [S5 / Datex Device Settings](../../../Configuration_Guide.md#s5--datex-device-settings-ge-solar--bx50--b1x5m--canvas).
