### MEKICS MP1300

> **Note:** Connects **wirelessly** via a dedicated Wi-Fi router. Router must be configured before first use.

| Connection | Router IP | Server IP (VR PC) | Server Port | VR Device Name |
|------------|-----------|-------------------|-------------|----------------|
| Wireless (Wi-Fi) | `192.168.0.1` | `192.168.137.1` | `6002` | `MEKICS` |

**Step 1 — Router Setup:**

1. Connect PC to the router AP **`iptime-mini`** via Wi-Fi.
2. Open browser → `192.168.0.1` → login: `admin` / `admin`.

   <img src="hardware_images/mekics_mp1300_1.png" width="600" alt="Router login screen">

3. Press **Setup**.

   <img src="hardware_images/mekics_mp1300_3.png" width="600" alt="Router setup screen">

4. Navigate to **Advanced Settings → Wireless LAN Management → Wireless Settings/Security**. Set SSID, password, encryption: **WPA2PSK+AES**, uncheck **"Broadcast SSID"** → **Apply**.

   <img src="hardware_images/mekics_mp1300_2.png" width="600" alt="Wireless settings configuration">

> Reconnect by manually entering the new SSID and password as a hidden network.

5. *(Optional — hospital network)* Navigate to **Advanced Settings → Wireless LAN Management → Wireless Extension Settings**. Set method to **"Wireless WAN"**, enter VR hotspot SSID and password.

   <img src="hardware_images/mekics_mp1300_4.png" width="293" alt="Wireless extension settings">

6. Navigate to **Advanced Settings → System Management → Other Settings**. Under wired port function, select **"LAN Port"** → **Apply**.

   <img src="hardware_images/mekics_mp1300_5.png" width="600" alt="Wired port function — LAN port">

**Step 2 — MP1300 Device Setup:**

1. Connect the **router's power cable** to the USB port on the rear of the MP1300. Connect a **LAN cable** from router to MP1300.

   <img src="hardware_images/mekics_mp1300_8.png" width="600" alt="LAN cable and power — MP1300 rear">

2. Navigate to **System → Network**. Set IP and gateway:
   - **IP:** `192.168.0.xxx` (last octet: 2–255, unused)
   - **Gateway:** `192.168.0.1`

   <img src="hardware_images/mekics_mp1300_7.png" width="600" alt="MP1300 Network settings">

3. Navigate to **System → Network → Central → Mode → MP601**.

   <img src="hardware_images/mekics_mp1300_10.png" width="600" alt="Central mode — MP601">

4. Under Central settings, set **Server IP:** `192.168.137.1` / **Server Port:** `6002`.

   <img src="hardware_images/mekics_mp1300_9.png" width="600" alt="Server IP and Port settings">

5. **Restart the device.**

**Step 3 — Vital Recorder Setup:**

In Vital Recorder, press **Add Device → MEKICS → Port `6002`**.

<img src="hardware_images/mekics_mp1300_6.png" width="600" alt="Vital Recorder — Add Device">

[↑ Quick Reference](#quick-reference--all-devices)

---
