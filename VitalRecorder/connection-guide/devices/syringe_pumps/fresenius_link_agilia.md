# Fresenius Kabi Link+ Agilia

<!-- meta
category: Syringe Pump
manufacturer: Fresenius Kabi
vr_device_name: Link+
-->
> **Note:** Requires a **USB 2.0 AM-Mini 5-pin cable** connected to the USB-B port on the side-bottom of the device. Initial setup also requires a **crossover LAN cable** for web-based configuration.

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|----------------|
| USB 2.0 AM-Mini 5-pin (USB-B) | None | USB-B (side, bottom) | `Link+` |

## Connection Steps
1. Connect the **USB 2.0 AM-Mini 5-pin cable** to the **USB-B port** on the side-bottom of the Link+.
2. Connect the other end (USB-A) to the PC.
3. In Vital Recorder Device Settings, select port **ACM0**.

**Initial Setup (Required — LAN Configuration):**

1. Connect the Link+ to the PC using a **crossover LAN cable**.
2. On the PC, navigate to **Control Panel → Network & Internet → Network Connections → Ethernet**.
3. Right-click **Ethernet** → **Properties** → select **Internet Protocol Version 4 (TCP/IPv4)** → **Properties**.
4. Select **Use the following IP address** and enter:
   - IP address: `192.168.0.100`
   - Subnet mask: (auto-filled)
   - Default gateway: `192.168.0.1`
5. Click **OK**.
6. Open a browser and navigate to `192.168.0.1`.
7. Log in: ID `admin` / Password `fresenius`.
8. Navigate to **Configuration → Data Export**.
9. Check **Enabled** → click **Apply** → click **OK** when prompted.
10. Click **Exit Configuration** — the device restarts automatically, completing setup.
