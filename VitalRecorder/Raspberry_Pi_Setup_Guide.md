# PiVR Setup Guide (Raspberry Pi Image)

PiVR is a Raspberry Pi that runs Vital Recorder from a ready-made microSD card image. The image includes Vital Recorder, a network watchdog, and a web admin page (**PiVR Control Panel**). This guide covers writing the image to a card, the first boot, and configuration on the admin page.

- Cables and device-side settings: [Hardware Connection Guide](connection-guide/devices/README.md)
- `vr.conf` keys: [Configuration Guide](Configuration_Guide.md)

> ⚠️ The image contains default account credentials. Do not share the image file or the default admin password outside your institution.

---

## Table of Contents

1. [What You Need](#what-you-need)
2. [Check the Image File](#1-check-the-image-file)
3. [Write the Image to the microSD Card](#2-write-the-image-to-the-microsd-card)
4. [First Boot](#3-first-boot)
5. [Open the Admin Page](#4-open-the-admin-page)
6. [Initial Setup Checklist](#5-initial-setup-checklist)
7. [Admin Page Reference](#admin-page-reference)
8. [Troubleshooting](#troubleshooting)

---

## What You Need

| Item | Notes |
|------|-------|
| Raspberry Pi | Raspberry Pi 4 Model B, Raspberry Pi 5, or Raspberry Pi Zero 2 W |
| microSD card | 32 GB, high-endurance type (e.g., SanDisk High Endurance). Recording writes to the card continuously. |
| Power supply | The supply rated for your model (5 V 3 A for Raspberry Pi 4) |
| USB Wi-Fi adapter | Realtek RTL8821CU. Used for the hospital Wi-Fi connection, and required for the hotspot. |
| Serial interface | FTDI FT4232H USB-serial HAT, for serial-connected devices |
| Laptop and LAN cable | For the admin page. Raspberry Pi Zero 2 W has no Ethernet port; use a USB Ethernet adapter. |
| Image files | `pivr-<version>-<date>.img.xz` and its SHA-256 checksum, provided by VitalLab |

---

## 1. Check the Image File

Compare the SHA-256 checksum of the downloaded file with the value supplied with the image (`.sha256` file or `SHA256SUMS.txt`). The `.img.xz` file and the decompressed `.img` file have different checksums.

```bash
# macOS
shasum -a 256 pivr-<version>-<date>.img.xz

# Linux
sha256sum pivr-<version>-<date>.img.xz
```

```powershell
# Windows
certutil -hashfile pivr-<version>-<date>.img.xz SHA256
```

If the values differ, download the file again.

---

## 2. Write the Image to the microSD Card

> ⚠️ Writing the image erases the whole card. On a card that was used in a PiVR before, this includes the data partition with the Wi-Fi settings, `vr.conf`, logs, and recordings. Copy the recordings off the card first.

Raspberry Pi Imager and balenaEtcher accept the `.img.xz` file directly; there is no need to decompress it.

### Raspberry Pi Imager

1. Select your Raspberry Pi model.
2. Under **Operating System**, select **Use custom** and choose the `.img.xz` file.
3. Under **Storage**, select the microSD card.
4. When Imager offers OS customisation (hostname, user, Wi-Fi), do not apply it. The image has its own settings, and Wi-Fi is configured on the admin page.
5. Write the card and wait for verification to finish.

### balenaEtcher

1. **Flash from file** → choose the `.img.xz` file.
2. **Select target** → choose the microSD card.
3. **Flash!** and wait for validation to finish.

### Command Line (macOS / Linux)

Decompress first, then write the `.img` file. Check the disk name carefully: writing to the wrong disk destroys its contents.

```bash
xz -dk pivr-<version>-<date>.img.xz

# macOS (find the card with: diskutil list)
diskutil unmountDisk /dev/diskN
sudo dd if=pivr-<version>-<date>.img of=/dev/rdiskN bs=4m status=progress

# Linux (find the card with: lsblk)
sudo dd if=pivr-<version>-<date>.img of=/dev/sdX bs=4M status=progress conv=fsync
```

---

## 3. First Boot

1. Insert the card, connect the USB Wi-Fi adapter, and power on the Pi.
2. On the first boot, the Pi creates a data partition (`/data`) from the remaining card space and then reboots once by itself.
3. A power loss during this step is safe. The step resumes on the next boot.

After the first boot, Wi-Fi settings, `vr.conf`, logs, and recordings are kept on `/data` and survive reboots.

---

## 4. Open the Admin Page

1. Connect the laptop to the Pi's Ethernet port with a LAN cable.
2. Set the laptop's wired network adapter to obtain an IP address automatically. The Pi assigns an address between `192.168.137.50` and `192.168.137.100`. If the laptop does not receive one, set it manually to IP `192.168.137.10`, subnet mask `255.255.255.0`.
3. Open `http://192.168.137.2` in a web browser.
4. If an orange **First-time setup in progress** banner appears, wait. When it turns green and shows **Setup complete — Rebooting shortly...**, wait for the reboot and reload the page.
5. Log in with the admin password. VitalLab provides the default password with the image. Change it on the **System** page.

**Navigation:** the ☰ button (top left) lists all pages. The left/right arrow keys, or a swipe on a touch screen, move to the previous/next page. Pages with settings have a **Save** button at the top right and ask for confirmation before applying.

---

## 5. Initial Setup Checklist

| # | Page | Action |
|---|------|--------|
| 1 | System | Press **Sync time** (see [System](#system)) |
| 2 | System | Change the admin password |
| 3 | Information | Note the Wi-Fi MAC address if the hospital network requires MAC registration |
| 4 | General | Enter the VR Name, file cutting rule, and Vitalserver address |
| 5 | Network | Enter the hospital Wi-Fi settings |
| 6 | Devices | Add the connected devices |
| 7 | Logs | Check that Vital Recorder is receiving data |

---

## Admin Page Reference

### General

| Field | `vr.conf` | Description |
|-------|-----------|-------------|
| VR Name | `[BED/<name>]` | Bed name used for recordings and on the server. If no name is set, the page shows the last 8 characters of the Pi's serial number. |
| Cut file by: **case** | `CUT_FILE=1`, `CUT_HOURLY=0` | Split files at patient boundaries |
| after *N* min | `PT_WAITING_TIME=N` | Patient waiting time in minutes (shown with **case**, default 5) |
| Cut file by: **hour** | `CUT_FILE=0`, `CUT_HOURLY=1` | Split files every hour |
| Vitalserver Address | `SERVER_IP` | Under **Optional Settings**. Format `host:port`, with an optional `http://` or `https://`. Examples: `192.168.10.20:5000`, `https://vitalserver.example.com:443` |

**Save** writes `vr.conf` and restarts Vital Recorder.

An invalid Vitalserver address (missing port, spaces, port outside 1–65535, scheme other than http/https) is not saved, and the previous value is kept without an error message. Reload the page after saving to confirm the value.

### Devices

The left column lists the configured devices. **Add Device** opens the device list, grouped by category and searchable. The list comes from the installed Vital Recorder, so it matches the devices that version supports.

| Field | `vr.conf` | Description |
|-------|-----------|-------------|
| Name | `[DEV/<name>]` | Device name. Defaults to the device type. |
| Type | `type` | Device type |
| Port | `port` | `LU`, `RU`, `LL`, `RL` (with `1`–`4`), `F1`–`F4`, `C1`–`C4`, `ACM0`, `4202`, `6002`, or **Other** for any other value (e.g., `IP:port`). See Port Formats in the [Configuration Guide](Configuration_Guide.md#port-formats). |
| Y cable | `readonly=1` | Listen-only. Use when the PiVR taps a Y-cable shared with another system. |

Device-specific options:

| Device types | Options |
|--------------|---------|
| SNUADC, SNUADCM, DI-149, DI-155, DI-1100, DI-1120 | Sampling Frequency, Voltage to Physical Unit preset (GE Tram Rec 4A), parameter name and gain for each channel |
| Intellivue, VueLink | Waveform selection. Usual waveforms such as ART and CVP are added without selection. Up to 3 ECG or 8 non-ECG waveforms are stable. |
| Bx50, B1x5M | Waveform selection, **Do not request numeric data** (`waveonly=1`). The S5 protocol allows 600 samples/s in total. |
| ADT | Bed name. Port is set to **Other**; enter the address. |
| EGA, HL7GW | Port is set to **Other**; enter the address. No Y cable option. |
| Demo | No port |

**Save** writes `vr.conf` and restarts Vital Recorder. To remove a device, press **Delete** on its form, then **Save**.

> ⚠️ Saving the Devices page rewrites every `[DEV/...]` section from the fields on this page. Device options that were added on the **Advanced** page and are not shown here (e.g., `auto_wavs=0`) are removed. Check the **Advanced** page after saving.

### Network

**Wireless** — the connection to the hospital Wi-Fi. It uses the USB Wi-Fi adapter when one is connected, otherwise the built-in Wi-Fi.

| Field | Description |
|-------|-------------|
| SSID | Network name |
| PW | Wi-Fi password |
| Hidden Network | Check for a network that does not broadcast its SSID |
| User | WPA2-Enterprise (PEAP / MSCHAPv2) user ID. Leave empty for a password-only (WPA2-Personal) network. |

**Static IP Settings** — leave all fields empty to obtain an address automatically (DHCP). For a fixed address, enter IP, Netmask, and Gateway. Typing the IP fills the Gateway as `x.x.x.1`; correct it if your network uses a different gateway. Primary/Secondary DNS are optional (`1.1.1.1` and `8.8.8.8` are used when empty). The static IP applies only together with a Wi-Fi SSID.

**Hotspot** — a Wi-Fi access point on the built-in Wi-Fi, for equipment that connects to the PiVR wirelessly.

| Field | Description |
|-------|-------------|
| Hotspot On/Off | Available only when a USB Wi-Fi adapter is connected (otherwise the switch is disabled) |
| SSID | Hotspot name. Typing a VR Name on the General page fills it as `vital_<name>`. |
| PW | Hotspot password (WPA2). Leave empty for an open network. |

The hotspot runs on 2.4 GHz, channel 1. The PiVR is `192.168.137.1` on the hotspot network and assigns addresses to connected equipment.

**Save** applies the settings and reconnects Wi-Fi. The admin page stays reachable over the Ethernet cable.

### System

| Button | Action |
|--------|--------|
| VR → Restart | Restarts Vital Recorder |
| OS → Reboot | Reboots the Pi |
| OS → Sync time | Sets the Pi's clock to the laptop's clock. The box next to it shows the difference in seconds. |
| Password → Save | Changes the admin password (current password, new password, confirmation) |

> ⚠️ **Press Sync time after the first boot.** The Pi has no battery-backed clock. A new card starts from a fixed date stored in the image, and recording file names and times use that date until the clock is set. Check that the laptop's clock is correct before pressing the button.

- While the Pi is powered off, its clock stops. After a long power outage, press **Sync time** again.
- Vital Recorder restarts once after the clock changes (a gap of about 11 seconds in the recording).
- Images with NTP enabled set the clock automatically when the network allows NTP traffic. On networks that block NTP, use **Sync time**.

### Information

| Item | Description |
|------|-------------|
| VR code | Code reported by the installed Vital Recorder |
| Serial | Raspberry Pi serial number |
| eth0 | Ethernet MAC address |
| wlan0 | Built-in Wi-Fi MAC address |
| wlan1 | USB Wi-Fi adapter MAC address |

The image does not randomize Wi-Fi MAC addresses, so these values can be registered on hospital networks that use MAC registration. Register the address of the interface that connects to the hospital Wi-Fi (`wlan1` when a USB Wi-Fi adapter is used).

`wlan0` can be empty: when a USB Wi-Fi adapter is connected and the hotspot is off, the built-in Wi-Fi is turned off about a minute after boot.

### Logs

Shows the system log. The drop-down lists the log files by last-modified time. The current log shows its last 30 lines and refreshes every 2 seconds. The refresh button reloads the file list.

### Advanced

Edits `vr.conf` as plain text. Use it for keys that the other pages do not cover (see the [Configuration Guide](Configuration_Guide.md)). **Save** writes the file and restarts Vital Recorder. Saving the General or Devices page rewrites the parts of `vr.conf` those pages manage.

---

## Troubleshooting

| Symptom | Check |
|---------|-------|
| `http://192.168.137.2` does not open | The LAN cable is in the Pi's Ethernet port. The laptop's wired adapter is set to automatic, or to `192.168.137.10` / `255.255.255.0`. On a new card, wait for the first-boot reboot. |
| The first-boot banner shows a message starting with `ERROR` | Write the image again, or use another card. |
| "Incorrect password" | Use the default password supplied with the image, or the password set on the System page. If it is lost, contact VitalLab. |
| The Vitalserver address returns to the old value | The entry was invalid. Enter it as `host:port`. |
| The static IP has no effect | Enter both IP and Gateway, together with the Wi-Fi SSID. |
| The Hotspot switch is disabled | No USB Wi-Fi adapter is detected. Connect the adapter and reboot. |
| Recording file names have the wrong date | Press **Sync time** on the System page. |
| Wi-Fi does not connect, or connects without network access | The hospital network may require MAC registration. Register the MAC address from the Information page. |
