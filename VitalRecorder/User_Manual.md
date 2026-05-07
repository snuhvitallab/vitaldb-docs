# VitalRecorder User Manual

VitalRecorder is a real-time vital signs recording application for Windows, Raspberry Pi, and Ubuntu. It captures data from over 80 medical devices and stores them in the `.vital` file format.

---

## Table of Contents

1. [Installation](#installation)
2. [Quick Start](#quick-start)
3. [User Interface](#user-interface)
4. [Adding Devices](#adding-devices)
5. [Connection Types](#connection-types)
6. [Port Filtering](#port-filtering)
7. [Recording](#recording)
8. [Server Upload](#server-upload)
9. [Configuration File (vr.conf)](#configuration-file-vrconf)
10. [Command Line Options](#command-line-options)
11. [Supported Devices](#supported-devices)
12. [Troubleshooting](#troubleshooting)

---

## Installation

### Windows

Download and install from the Microsoft Store:
- Store URL: https://apps.microsoft.com/detail/9MVBQL8R0TFL

Or download the MSI installer or MSIX package from the release page.

### Linux (Desktop, AppImage)

Download the AppImage (`VitalRecorder-*-x86_64.AppImage`) from the release page, mark it executable, and run it:

```bash
chmod +x VitalRecorder-*-x86_64.AppImage
./VitalRecorder-*-x86_64.AppImage
```

Tested on Ubuntu 22.04 and later. Works on most modern Linux distributions (Fedora, Debian 12+) without additional setup — Qt6 is bundled inside the AppImage.

For serial / USB device access (`/dev/ttyUSB*`, `/dev/ttyACM*`), add your user to the `dialout` group once:

```bash
sudo usermod -aG dialout $USER
```

Log out and back in for the group change to take effect.

### Raspberry Pi / Headless Linux

For unattended server-style recording without a GUI, download the platform-specific console binary (`pivr64` for Raspberry Pi ARM64 or `ubuntu64` for Ubuntu x64) from the release page and run it directly.

---

## Quick Start

1. Launch VitalRecorder.
2. Click the **Add Device** button to add a medical device.
3. Select the device type (e.g., `Medtronic : BIS`, `Philips : Intellivue`).
4. Choose the connection port (COM port, IP address, or port number).
5. Click **OK**. VitalRecorder will begin communicating with the device.
6. Click **Record** to start recording data.

---

## User Interface

VitalRecorder uses a tab-based interface. Each tab represents a "room" or "bed" and can have multiple devices attached.

- **Tracks**: Each device generates one or more tracks (e.g., HR, SpO2, BIS). Tracks are displayed as waveforms or numeric values.
- **Events**: You can add event markers during recording.
- **Monitor**: A configurable monitor panel displays selected parameters in large text.

### Bed Name

Each tab can have a **bed name** assigned. This is used for:
- Identifying the room when uploading data to a server.
- Separating multi-bed data from HL7 gateway devices.

---

## Adding Devices

Go to **Add Device** and select from the device groups:

| Group | Examples |
|-------|----------|
| VitalDB devices | SNUADC, SNUADCM, BUTTON, VitalBOLUS |
| Analog to digital converter | DataQ DI-149, DI-155, DI-245, DI-1100, DI-1120 |
| Patient monitor | Philips Intellivue, GE Solar/Dash/Bx50, Nihon Kohden, Mindray HL7, MEKICS |
| Multifunction monitor | Masimo Radical-7/Root, Sentec SDM |
| Anesthesia machine | Draeger Primus/Zeus/Fabius, GE Datex-Ohmeda Aisys/Avance |
| Mechanical ventilator | Maquet SERVO-i/s/U, Hamilton MR1/C2/C6/T1 |
| Drug infusor | Fresenius Agilia/Primea/PCBM, BBraun SpaceCom/HL7, Daiwha, Pion |
| Brain monitor | Medtronic BIS/VISTA/INVOS, Fresenius Conox, OBELAB NirsitON |
| Neuromuscular monitor | TwitchView, TOFScan, TOFcuff |
| Fluid infusor | Belmont FMS 2000 |
| Cardiac monitor | Edwards Hemosphere/Vigilance/EV1000/Vigileo, Getinge PulsioFlex |
| Fetal monitor | GE Corometrics 250cx |

---

## Connection Types

### RS-232 (Serial / COM Port)

Most devices use RS-232 serial communication via a physical COM port or USB-to-Serial adapter.

- Select the COM port number (e.g., `COM3`).
- Baud rate and other serial parameters are automatically configured per device type.
- Install the USB-to-Serial driver before connecting.

### TCP (Network)

For network-connected devices. VitalRecorder can act as either a TCP **client** or **server**.

- **Client mode**: Enter the device's IP address and port as `IP:PORT` (e.g., `192.168.1.100:9001`).
- **Server mode**: Enter only the port number (e.g., `2575`). VitalRecorder listens and waits for the device to connect.

HL7 devices (Mindray HL7, Nihon Kohden HL7GW, BBraun HL7) typically use server mode with MLLP framing.

### UDP (Network)

Some devices broadcast data via UDP.

- Enter the port number to listen on.

### BLE (Bluetooth Low Energy)

For wireless sensors such as Movesense.

- Requires Windows 10+ with Bluetooth 4.0 adapter.
- The device must be in pairing mode.

---

## Port Filtering

When connecting TCP/UDP devices, you can append filters to the port string to selectively accept connections or messages.

### Format

```
PORT#KEYWORD@IP_ADDRESS
```

All parts except PORT are optional.

### Keyword Filter (`#`)

Filters incoming messages by searching for a keyword string within the message content. Messages that do not contain the keyword are silently discarded.

```
2575#BED-001
```

This listens on port 2575 and only processes messages containing `BED-001`. This is useful when a single HL7 gateway (e.g., DoseLink, Mindray Gateway) sends data for multiple beds over one connection.

### IP Filter (`@`)

Filters incoming TCP connections by source IP address. Connections from other IP addresses are rejected at the TCP accept stage.

```
2575@192.168.100.22
```

This listens on port 2575 and only accepts connections from `192.168.100.22`.

### Combined

```
2575#BED-001@192.168.100.22
```

This listens on port 2575, only accepts connections from `192.168.100.22`, and only processes messages containing `BED-001`.

### Use Cases

- **BBraun DoseLink**: When DoseLink's Endpoint Filtering is enabled, use `#` to filter by pump serial or bed identifier.
- **Mindray HL7 Gateway**: Multiple beds sharing one gateway port can be separated using the bed name keyword.
- **Multiple DoseLink servers**: Use `@` to distinguish which DoseLink server should connect to which VitalRecorder tab.

### Multi-Bed HL7 Gateway Routing

When a single HL7 gateway (Mindray eGateway, BBraun DoseLink, Nihon Kohden HL7GW) delivers data for several beds over one TCP connection, VitalRecorder routes each frame to the correct tab automatically:

1. **Only one tab binds** the TCP port (the *primary*); all other tabs using the same port and device type automatically become passive subscribers. This eliminates the Windows `SO_REUSEADDR` race that previously required a manual "Add device" click on every restart.

2. **Bed-name routing (preferred, takes priority over keyword filter)** — set each tab's Bed Name to match any identifier the gateway sends. No port filter is needed:
   - **Mindray**: `PV1-3` bed ID (e.g. `SU-1`, `BED-001`)
   - **Nihon Kohden**: `deviceId` JSON field or the 12-byte MFER prefix
   - **BBraun**: any non-empty token from the `~`-separated `MDC_ATTR_LOCATION` OBX (e.g. `Forskning`, `Bord4`, `Anilab`, `Operasjon`)

   If multiple tabs could match the same frame (e.g. both `Forskning` and `Bord4` tabs exist and the frame's LOCATION is `Forskning~Operasjon~Bord4~Anilab~~~~~Bord4`), **the more specific token wins**. Tokens are tried in reverse order, so `Bord4` (last `~`-repetition, conventionally the display short-name) beats `Forskning` (first repetition, a broader department label). Only one tab receives any given frame.

3. **Keyword-filter routing (fallback)** — when the Bed Name cannot match the gateway identifier directly, use the `port#keyword` syntax described above. Applied only if bed-name routing finds no match.

4. **Automatic tab creation** — if no existing tab matches and the frame carries a bed identifier, a new tab is created using the most specific (last non-empty) token. This prevents packet loss during first-time setup.

5. **Restart auto-recovery** — on VitalRecorder restart, all tabs reestablish their primary/subscriber relationship within ~15 seconds without any manual intervention.

For BBraun DoseLink specifically, one HL7 frame represents one rack (one bed); multiple pumps in the rack are carried as VMD blocks within that frame and are recorded on separate tracks (PUMP1 … PUMP16) inside the same tab.

#### Pump display in Monitor View (1.18.30+)

Monitor View shows up to **8 pumps simultaneously** (previously 4). Each pump slot displays the drug name and one large value:

- **TCI pumps with effect-site concentration (CE)** — slot shows `CE` + drug name (unchanged behavior).
- **Non-TCI pumps (most BBraun / Fresenius configurations)** — slot shows `RATE` (mL/h) + drug name, and the cumulative infused volume (`VOL`, mL) is rendered as a small grey annotation in the top-right corner of the slot.

All other pump fields (pressure, concentration, dose rate, syringe volume, bolus, delivery time, patient weight, drug library, care area, etc.) are still **recorded to the `.vital` file** and visible in the default track view — only the Monitor View curates to keep the display uncluttered during running experiments.

Supported devices: BBraun SpaceCom/HL7, Fresenius Agilia/Primea/PCBM, Daiwha, Pion. No configuration required — this is the default layout.

> The `minimal=1` vr.conf option introduced in 1.18.29 is removed in 1.18.30: it was skipping the extra fields from the `.vital` file entirely (unrecoverable). 1.18.30's Monitor View redesign preserves all recorded data.

> **1.18.23 notes for non-English Windows** — earlier versions were affected by a Windows C-runtime issue where infusion rates below 1.0 mL/h were recorded as 0 on locales that use `,` as the decimal separator (Norwegian, German, French, etc.). VitalRecorder 1.18.23 forces numeric parsing to always accept `.` as the decimal separator, regardless of Windows regional settings. BBraun pump limit was also raised from 8 to 16 pumps per device.

---

## Recording

### Automatic Recording

By default, VitalRecorder starts recording automatically when it launches (`RECORD_WHEN_START` setting).

### File Format

Recordings are saved as `.vital` files, a compressed binary format with track-based organization.

### Save Directory

Configure the save directory in Settings. The default is the user's Documents folder.

### Filename Template

The filename is generated from a template. Default: `%r_%y%m%d_%h%i%s`

| Code | Meaning |
|------|---------|
| `%r` | Room/bed name |
| `%y` | Year (4 digits) |
| `%m` | Month (2 digits) |
| `%d` | Day (2 digits) |
| `%h` | Hour (2 digits) |
| `%i` | Minute (2 digits) |
| `%s` | Second (2 digits) |

---

## Server Upload

VitalRecorder can upload data in real-time to a VitalServer instance via WebSocket.

### Settings

| Setting | Description |
|---------|-------------|
| `SERVER_IP` | VitalServer IP address or hostname |
| `SEND_WEB` | Enable/disable server upload (`1` or `0`) |
| `CLOUD_UPLOAD` | Enable/disable cloud upload (`1` or `0`) |
| `VRCODE` | Unique identifier for this VitalRecorder instance |

### What Gets Uploaded

- **Version, OS, architecture** of the VitalRecorder instance.
- **Configuration** and **supported device types** (sent once on first successful upload after boot).
- **Room data**: bed name, device list, track values, and waveforms for each tab.

Data is compressed with zlib before upload.

### HL7 Mode

When the `HL7` setting is enabled, VitalRecorder sends room data in HL7 format instead of JSON.

---

## Configuration File (vr.conf)

VitalRecorder stores all settings in a single configuration file called `vr.conf`. This file uses an INI-like format and can be edited manually for headless deployments or batch provisioning.

### File Location

| Platform | Path |
|----------|------|
| Windows | `%APPDATA%\VitalRecorder\vr.conf` |
| Linux | `./vr.conf` > `~/vr.conf` > `/boot/vr.conf` (searched in order) |

- Encoding: UTF-8
- Use `--conf <path>` to specify an alternate configuration file.

### File Structure

```ini
# Global settings (before any section)
KEY=VALUE

# Bed (tab) definition
[BED/bedname]

# Device under this bed
[DEV/devicename]
type=DeviceType
port=PortSpec

# Filter under this bed
[FILT/filter_module_name]
```

**Rules:**
- One `KEY=VALUE` pair per line.
- Section headers start with `[`.
- Blank lines are ignored.
- `[DEV/...]` and `[FILT/...]` sections belong to the preceding `[BED/...]`.
- A single `[BED/...]` can contain multiple devices and filters.

### Global Settings

#### General

| Key | Default | Description |
|-----|---------|-------------|
| `SAVEDIR` | (system default) | Recording file save directory |
| `VRCODE` | (auto-generated) | Unique VitalRecorder identification code |
| `DEBUG` | 0 | Debug mode (0: off, 1: on) |
| `FILENAME_TEMPLATE` | `%r_%y%m%d_%h%i%s` | Recording filename template |

#### Recording

| Key | Default | Description |
|-----|---------|-------------|
| `RECORD_WHEN_START` | 1 | Auto-record on launch (0: off, 1: on) |
| `CUT_FILE` | 1 | Split file at patient boundaries (0: off, 1: on) |
| `CUT_HOURLY` | 0 | Split file every hour (0: off, 1: on) |
| `CUT_BY` | (none) | Signal for file split trigger (e.g., `spo2`, `hr`, `any`) |
| `PT_WAITING_TIME` | 5 | Patient waiting time in minutes |

#### Server

| Key | Default | Description |
|-----|---------|-------------|
| `SERVER_IP` | (none) | VitalDB server address (IP:port) |
| `UPLOAD_SERVER_IP` | (none) | File upload server address |
| `MONITOR_SERVER_IP` | (none) | Web monitoring server address |
| `SEND_WEB` | 1 | Send data to web server (0: off, 1: on) |
| `CLOUD_UPLOAD` | 0 | Enable cloud upload (0: off, 1: on) |

#### Window

| Key | Default | Description |
|-----|---------|-------------|
| `START_MAXIMIZED` | 1 | Start maximized |
| `START_MINIMIZED` | 0 | Start minimized |
| `OPTION_MIN_TO_TRAY` | 0 | Minimize to system tray |
| `OPTION_ALWAYS_ON_TOP` | 0 | Always on top |
| `PLAY_SOUND` | 1 | Play alarm sounds |

#### Event Presets

Up to 30 event preset labels can be defined with `EVT_TEXT_0` through `EVT_TEXT_29`.

```ini
EVT_TEXT_0=Induction
EVT_TEXT_1=Intubation
EVT_TEXT_2=Incision
```

### Bed Section

Defines a bed (tab). Multiple beds can be defined in a single configuration file.

```ini
[BED/OR1]
```

- The bed name follows `BED/` (e.g., `OR1`, `ICU_BED3`).
- If omitted, the bed name is auto-generated from VRCODE or the PC hostname.

### Device Section

Devices are added under a `[BED/...]` section.

```ini
[DEV/devicename]
type=DeviceType
port=PortSpec
```

| Key | Required | Description |
|-----|----------|-------------|
| `type` | Yes | Device type (e.g., `BIS`, `Intellivue`, `Solar8000`) |
| `port` | Yes | Connection port (see Port Formats below) |
| `company` | No | Manufacturer (e.g., `Nihon Kohden`) |
| `readonly` | No | Read-only mode (0: off, 1: on) |

#### Port Formats

| Format | Example | Description |
|--------|---------|-------------|
| COM port | `COM1`, `COM3` | Windows serial port |
| TCP/IP | `192.168.1.100:4343` | Network device (IP:port) |
| Port number | `4343` | TCP server mode on localhost |
| RPi serial | `F1`-`F4` | Raspberry Pi AMA ports |
| RPi USB | `LU`, `LU1`-`LU4` | USB Left Upper |
| RPi USB | `RU`, `RU1`-`RU4` | USB Right Upper |

#### Port Filtering in Config

The port value supports keyword and IP filters (same syntax as described in [Port Filtering](#port-filtering)):

```
port=PORT#keyword1 keyword2#keyword3@IP_SUFFIX
```

#### ADC Device Settings

For ADC (Analog-to-Digital Converter) devices, additional per-channel settings are available:

| Key | Description |
|-----|-------------|
| `srate` | Sampling rate in Hz |
| `parname1`, `parname2`, ... | Parameter name for each channel |
| `gain1`, `gain2`, ... | Voltage-to-physical-unit conversion gain for each channel |

```ini
[DEV/SNUADC]
type=SNUADC
port=COM3
srate=500
parname1=ECG
gain1=1.0
parname2=ART
gain2=100.0
```

### Filter Section

Adds a real-time signal processing filter. Filter definitions are loaded from the filter server.

```ini
[FILT/filter_module_name]
```

- The module name must match the `modname` of a filter registered on the server.
- No additional settings are needed (filter parameters are provided by the server).

### Configuration Examples

#### Single Patient Monitor

```ini
SAVEDIR=D:\VitalData

[BED/OR1]

[DEV/Solar8000]
type=Solar8000
port=COM1
```

#### Multiple Devices

```ini
SAVEDIR=D:\VitalData
VRCODE=OR1_PC

[BED/OR1]

[DEV/Intellivue]
type=Intellivue
port=192.168.1.100:4343

[DEV/BIS]
type=BIS
port=COM3

[DEV/Primus]
type=Primus
port=COM4
```

#### Multiple Beds

```ini
SAVEDIR=D:\VitalData

[BED/OR1]

[DEV/Solar8000]
type=Solar8000
port=COM1

[BED/OR2]

[DEV/Philips]
type=Intellivue
port=192.168.1.101:4343
```

#### Debug / Test

```ini
SAVEDIR=C:\Users\lucid\Desktop
DEBUG=1

[BED/test]

[DEV/NK EGA]
type=EGA
company=Nihon Kohden
port=9001
```

#### With Filter

```ini
[BED/OR1]

[DEV/Solar8000]
type=Solar8000
port=COM1

[FILT/pleth_spi]
```

---

## Command Line Options

```
vital.exe [options] [filename]
```

| Option | Description |
|--------|-------------|
| `--version`, `-v` | Show version number |
| `--devtypes`, `-d` | List all supported device types |
| `--console`, `-c` | Run in console mode (no GUI) |
| `--demo` | Run in console mode with a demo device |
| `--upgrade`, `-u` | Upgrade to the latest version |
| `-u1.18.0` | Upgrade to a specific version |
| `--help`, `-h` | Show help |
| `filename.vital` | Open a `.vital` file for playback |

### Console Mode

Console mode (`--console` or `-c`) runs VitalRecorder without the GUI. This is useful for headless deployments on Raspberry Pi or Ubuntu servers. Devices are loaded from the saved configuration.

### Debug Mode

Enable the `DEBUG` setting to log raw protocol data to the `.vital` file. This is useful for troubleshooting device communication issues.

---

## Supported Devices

For the complete list of supported devices with connection details and parameters, see [Supported Devices](../VitalRecorder/Supported_Devices.md).

### Quick Reference: Common Devices

| Device | Connection | Port Setting |
|--------|-----------|-------------|
| Philips Intellivue | RS-232 | COM port, 115200 baud |
| GE Solar 8000 | RS-232 | COM port, 9600 baud |
| Nihon Kohden (Serial) | RS-232 | COM port, 9600 baud |
| Nihon Kohden (HL7GW) | TCP Server | Port 9001 |
| Nihon Kohden (EGA) | UDP | Port number |
| Mindray (HL7) | TCP Server | Port 10000 |
| Draeger (Medibus) | RS-232 | COM port, 9600 baud (8N2) |
| GE Datex-Ohmeda | RS-232 | COM port, 19200 baud (7E1) |
| Medtronic BIS | RS-232 | COM port, 57600 baud |
| BBraun SpaceCom | RS-232 | COM port, 9600 baud |
| BBraun HL7 (DoseLink) | TCP Server | Port 2575 |
| Masimo Radical-7 | RS-232 | COM port, 9600 baud |
| Edwards Hemosphere | RS-232 | COM port, 9600 baud |
| Hamilton ventilator | RS-232 | COM port, 38400 baud |

---

## Troubleshooting

### Device Not Connecting

1. **RS-232**: Verify the correct COM port is selected. Check Device Manager for the port number. Ensure the USB-to-Serial driver is installed.
2. **TCP Server mode**: Check that the firewall allows incoming connections on the specified port.
3. **TCP Client mode**: Verify the device IP address is reachable (`ping` test).

### No Data Displayed

- Some devices require specific configuration on the device side (e.g., enabling RS-232 output in Draeger Service menu, activating MIB output on Philips Intellivue).
- Check that the baud rate and serial parameters match the device settings.
- Enable `DEBUG` mode and check the raw data log to verify communication.

### Multiple Devices on Same Port

For HL7 devices sharing a single gateway port, use the [Port Filtering](#port-filtering) feature with `#` keyword to separate beds.

### BBraun HL7 Multi-Pump

BBraun DoseLink sends data for multiple pumps over a single TCP connection. VitalRecorder automatically identifies each pump using the serial number in OBX-18 (Equipment Instance Identifier) and maps them to PUMP1 through PUMP8.

If pumps are not being separated correctly:
- Enable `DEBUG` mode and capture a `.vital` file.
- Check the raw HL7 messages for OBX-18 values.
- When using DoseLink Endpoint Filtering, use `#` keyword filter if needed.

### Server Upload Not Working

- Verify `SERVER_IP` is set correctly.
- Check that `SEND_WEB` is set to `1`.
- Ensure network connectivity to the server.
- Configuration and device type list are sent on the first successful upload after boot. If VitalRecorder boots without any active devices, the initial upload may be deferred until a device connects.
