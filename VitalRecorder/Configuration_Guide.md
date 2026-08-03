# VitalRecorder Configuration File (vr.conf) Guide

VitalRecorder manages device, bed, and filter settings through a single configuration file called `vr.conf`.
This document describes the file structure and how to write it.

---

## Table of Contents

1. [File Location](#1-file-location)
2. [File Structure](#2-file-structure)
3. [Global Settings](#3-global-settings)
4. [Bed Section](#4-bed-section)
5. [Device Section](#5-device-section)
6. [Filter Section](#6-filter-section)
7. [Command Line Options](#7-command-line-options)
8. [Configuration Examples](#8-configuration-examples)

---

## 1. File Location

| Platform | Path |
|----------|------|
| Windows | `%APPDATA%\VitalRecorder\vr.conf` |
| Linux | `./vr.conf` > `~/vr.conf` > `/boot/vr.conf` (searched in order) |

- Encoding: UTF-8
- Use `--conf <path>` on the command line to specify an alternate configuration file.
- Use `--conf -` to read the configuration from standard input (no file needed). In this mode, settings are treated as read-only — VitalRecorder will not write back to any `.conf` file, so the original on-disk configuration is preserved. Useful for ad-hoc tests and containerized runs.

```bash
# Run with a piped-in config (Git Bash / Linux shell)
./Vital.exe --console --conf - <<'EOF'
SAVEDIR=/tmp/vr_out
[BED/TEST]
[DEV/BIS]
type=BIS
port=127.0.0.1:4343
EOF
```

---

## 2. File Structure

The file follows an INI-like format consisting of global settings and sections.

```ini
# Global settings (top of file)
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
- One `KEY=VALUE` pair per line
- Section headers start with `[`
- Blank lines are ignored
- `[DEV/...]` and `[FILT/...]` sections belong to the preceding `[BED/...]`
- A single `[BED/...]` can contain multiple devices and filters

---

## 3. Global Settings

Settings placed before any `[BED/...]` section.

### General

| Key | Default | Description |
|-----|---------|-------------|
| `SAVEDIR` | (system default) | Recording file save directory |
| `VRCODE` | (auto-generated) | VitalRecorder identification code |
| `DEBUG` | 0 | Debug mode (0: off, 1: on) |
| `FILENAME_TEMPLATE` | `%r_%y%m%d_%h%i%s` | Recording filename template |
| `AUTO_DETECT` | 0 | Detect serial devices automatically (0: off, 1: on). See [Automatic Device Detection](#automatic-device-detection) |

### Recording

| Key | Default | Description |
|-----|---------|-------------|
| `RECORD_WHEN_START` | 1 | Auto-record on launch (0: off, 1: on) |
| `CUT_FILE` | 1 | Split file at patient boundaries (0: off, 1: on) |
| `CUT_HOURLY` | 0 | Split file every hour (0: off, 1: on) |
| `CUT_BY` | (none) | Signal for file split trigger (e.g., `spo2`, `hr`, `any`) |
| `PT_WAITING_TIME` | 5 | Patient waiting time in minutes |

### Server

| Key | Default | Description |
|-----|---------|-------------|
| `SERVER_IP` | (none) | VitalDB server address (IP:port) |
| `UPLOAD_SERVER_IP` | (none) | File upload server address |
| `MONITOR_SERVER_IP` | (none) | Web monitoring server address |
| `SEND_WEB` | 1 | Send data to web server (0: off, 1: on) |
| `CLOUD_UPLOAD` | 0 | Enable cloud upload (0: off, 1: on) |

### TLS / Certificate Trust

VitalRecorder can verify the server TLS certificate for all HTTPS uploads and WebSocket
monitoring connections, or it can accept any certificate (legacy behavior).

> **Note for the 1.x line:** the default is `TLS_INSECURE=1` (verification off). Many hospital
> deployments use private/self-signed CAs that are not installed system-wide, so forcing
> verification would break existing uploads. Sites that do have a trusted CA chain can opt
> in by setting `TLS_INSECURE=0`. Vital Recorder 2.0 is planned to flip this default.

| Key | Default | Description |
|-----|---------|-------------|
| `TLS_INSECURE` | 1 | `1` skips peer and hostname verification (1.x default — preserves compatibility with private/self-signed hospital certificates). `0` enables full TLS verification using the system trust store (and `TLS_EXTRA_CA` if provided). |
| `TLS_EXTRA_CA` | (none) | Absolute path to an additional CA bundle file (PEM). Added to the trust store on Linux/macOS (OpenSSL/curl). On Windows the system certificate store is used — install the hospital CA there instead; this key has no effect under WinInet. Only applies when `TLS_INSECURE=0`. |

**Typical scenarios**

- *Existing hospital deployment (private CA, unchanged)* — keep the default. No change in 1.x needed.
- *Public internet, valid public CA (vitaldb.net)* — set `TLS_INSECURE=0`. The system CA store already trusts the server; no other setup required.
- *Hospital SSL-inspection proxy (Zscaler, Palo Alto, Blue Coat, …) on secure mode* — set `TLS_INSECURE=0` and have the hospital IT team install the proxy's root CA into the Windows certificate store (Group Policy distribution is the normal path). On Linux/macOS/Raspberry Pi builds, point `TLS_EXTRA_CA` at the PEM file provided by IT.

```ini
# Example — enable TLS verification, using a hospital-provided CA bundle on Linux/RPi
TLS_INSECURE=0
TLS_EXTRA_CA=/etc/vitalrecorder/hospital-root-ca.pem
```

```ini
# Example — enable TLS verification using only the Windows system certificate store
TLS_INSECURE=0
```

### Window

| Key | Default | Description |
|-----|---------|-------------|
| `START_MAXIMIZED` | 1 | Start maximized |
| `START_MINIMIZED` | 0 | Start minimized |
| `OPTION_MIN_TO_TRAY` | 0 | Minimize to system tray |
| `OPTION_ALWAYS_ON_TOP` | 0 | Always on top |
| `PLAY_SOUND` | 1 | Play alarm sounds |

### Event Presets

Up to 30 event preset labels can be defined with `EVT_TEXT_0` through `EVT_TEXT_29`.

```ini
EVT_TEXT_0=Induction
EVT_TEXT_1=Intubation
EVT_TEXT_2=Incision
```

---

## 4. Bed Section

Defines a bed (tab). Multiple beds can be defined in a single configuration file.

```ini
[BED/OR1]
```

- The bed name follows `BED/` (e.g., `OR1`, `ICU_BED3`)
- If omitted, the bed name is auto-generated from VRCODE or the PC hostname

---

## 5. Device Section

Devices are added under a `[BED/...]` section.

### Basic Settings

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

### Port Formats

| Format | Example | Description |
|--------|---------|-------------|
| COM port | `COM1`, `COM3` | Windows serial port |
| TCP/IP | `192.168.1.100:4343` | Network device (IP:port) |
| Port number | `4343` | localhost TCP port |
| RPi serial | `F1`-`F4` | Raspberry Pi AMA ports |
| RPi USB | `LU`, `LU1`-`LU4` | USB Left Upper |
| RPi USB | `RU`, `RU1`-`RU4` | USB Right Upper |

### Automatic Device Detection

Setting `AUTO_DETECT=1` in the global settings lets VitalRecorder work out what is
connected to each serial port on its own, so you do not have to write a `[DEV/...]`
section for serial devices at all.

```ini
AUTO_DETECT=1

[BED/OR1]
# no [DEV/...] needed for serial devices - they are found and recorded automatically
```

**Devices you list explicitly always win.** A port named in a `[DEV/...]` section is
never touched by detection, so you can leave some devices declared and let the rest be
found. This also means you can turn detection on for an existing configuration without
changing anything else.

Detection runs continuously in the background. A device that is switched on later, or
moved to a different port, is picked up within a couple of minutes without a restart.

**Supported so far:** Philips IntelliVue, Dräger (Medibus and Medibus.X — Primus,
Atlan, and others), GE/Datex-Ohmeda S/5, Masimo Radical-7/Root, Daiwha DS-5000,
Fresenius Kabi Link+. Devices outside this list still need a `[DEV/...]` section.

**Network and USB-identified devices are unaffected.** TCP ports, Bluetooth devices and
anything addressed by IP still come from the configuration file as before.

#### What it does

Detection asks the port itself rather than guessing from the port name:

1. **Line settings** — the baud rate and frame width are measured from the serial
   line, so a device is found even if it is not on the rate you would expect.
2. **Protocol** — candidate drivers matching those line settings are tried in turn,
   and one is accepted only when it decodes real, checksum-valid data. A driver that
   merely opens the port is not enough.
3. **Recording starts immediately** once a device is identified. The log records what
   was found and where, for example `[autodetect] AMA2 -> Datex-Ohmeda`.

Because acceptance requires decoded data, a port with nothing attached simply stays
empty rather than being assigned to the wrong device.

### Port Filtering

Keyword and IP filters can be appended to the port value.

```
port=PORT#keyword1 keyword2#keyword3@IP_SUFFIX
```

| Delimiter | Description |
|-----------|-------------|
| `#` | Keyword OR group separator |
| (space) | AND condition within the same `#` group |
| `@` | IP address suffix filter |

Examples:
- `COM1#BIS` -- accept only frames containing "BIS" on COM1
- `4343#HR SpO2#BP` -- "HR AND SpO2" or "BP"
- `4343@10.1` -- accept only connections from IPs ending in 10.1

### ADC Device Settings

For ADC (Analog-to-Digital Converter) devices, per-channel settings are available.

| Key | Description |
|-----|-------------|
| `srate` | Sampling rate (Hz) |
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

### S5 / Datex Device Settings (GE Solar / Bx50 / B1x5M / Canvas)

Devices that use the Datex DRI protocol (`S5`, `Solar8000`, `Bx50`, `B1x5M`, `Canvas`) support per-device options to choose which waveforms are requested from the monitor.

| Key | Description |
|-----|-------------|
| `wavs` | Comma-separated list of waveforms to request (up to 8) |
| `waveonly` | `1` = waveforms only, no numeric values; `0` = both (default) |

Available waveform names: `ECG1`, `ECG2`, `PLETH` (alias `PPG`), `CO2`, `O2`, `N2O`, `AWP`, `IABP1`–`IABP8`, `EEG1`, `EEG2`, `EEGBIS`, `EEGENT`, `EEGENT400`.

> **Invasive arterial pressure (ART) waveform:** Use `IABP1` — `ART` and `INVP1` are not recognized. The first invasive pressure channel (commonly labeled **ART** on the monitor screen) is mapped to `IABP1`.

**Default waveforms when `wavs` is not set:**

| Device | Default waveforms |
|--------|-------------------|
| `B1x5M` (B105M / B115M / B125M) | `ECG1, PLETH` only — the B1x5M family cannot keep up with the full S5 stream, so the default is intentionally reduced |
| All other S5 / Solar8000 / Bx50 / Canvas | `ECG1, PLETH, IABP1, CO2, AWP` |

If you need additional waveforms on a B1x5M (e.g., invasive arterial pressure), list them explicitly:

```ini
[DEV/B1x5M]
type=B1x5M
port=LU
wavs=ECG1,PLETH,IABP1,CO2,AWP
```

---

## 6. Filter Section

Adds a real-time signal processing filter. Filter definitions are loaded from the filter server.

```ini
[FILT/filter_module_name]
```

- The module name must match the `modname` of a filter registered on the server.
- No additional settings are needed (filter parameters are provided by the server).

**Filter runtime (1.18.37+)** — VitalRecorder downloads a slim Python 3.11 runtime (~27 MB) on first filter use, replacing the previous 121 MB `pyvital`-based bundle. The local server is provided by [openvital](https://github.com/vitaldb/openvital) (numpy + stdlib `http.server`, no async/web framework deps). Basic ECG / PPG / EEG filters work out of the box; ML-heavy filters (HPI, beat noise detector, rhythm classifier, dlapco SV) are gated behind the **Install ML filters** button in the Add Filter dialog, which runs `pip install openvital[all]` silently (no command window) and pulls PyTorch / TensorFlow only on demand.

---

## 7. Command Line Options

```
vr --conf <path>         Specify configuration file path
vr --console             Run in console mode (no GUI)
vr --debug               Console + debug mode
vr --debug test.conf     Debug mode with specified config file
vr --version             Show version info
vr --devtypes            List supported device types
vr --help                Show help
```

---

## 8. Configuration Examples

### Basic: Single Patient Monitor

```ini
SAVEDIR=D:\VitalData

[BED/OR1]

[DEV/Solar8000]
type=Solar8000
port=COM1
```

### Multiple Devices

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

### Multiple Beds

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

### Debug / Test

```ini
SAVEDIR=C:\Users\lucid\Desktop
DEBUG=1

[BED/test]

[DEV/NK EGA]
type=EGA
company=Nihon Kohden
port=9001
```

### With Filter

```ini
[BED/OR1]

[DEV/Solar8000]
type=Solar8000
port=COM1

[FILT/pleth_spi]
```
