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
9. [Command Line Options](#command-line-options)
10. [Supported Devices](#supported-devices)
11. [Troubleshooting](#troubleshooting)

---

## Installation

### Windows

Download and install from the Microsoft Store:
- Store URL: https://apps.microsoft.com/detail/9MVBQL8R0TFL

Or download the MSI installer or MSIX package from the release page.

### Raspberry Pi / Ubuntu

Download the platform-specific binary (`pivr64` or `ubuntu64`) from the release page and run it directly.

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
