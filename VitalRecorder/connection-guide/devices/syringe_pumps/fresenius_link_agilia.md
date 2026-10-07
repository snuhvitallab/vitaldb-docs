# Fresenius Kabi Link+ Agilia

<!-- meta
category: Syringe Pump
manufacturer: Fresenius Kabi
vr_device_name: Link+
-->
> **Note:** Data is recorded through USB. Enable Data Export through the LAN connection before recording.

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|---------------- |
| USB 2.0 A-male ↔ mini-B 5-pin | None | USB-B (mini-USB)| `Link+` |

## Connection Steps
1. Connect the **mini-B end** to that port and the **USB-A end** directly to the PC. No USB-Serial converter is needed — the rack presents itself as a USB CDC-ACM serial device.
## Device Configuration

   <img src="../hardware_images/fresenius_link_agilia_1.png" width="450" alt="Link+ connector panel with the mini-USB (USB-B) data port highlighted, above the USB-A socket and beside the RJ-45 and round connectors">

Enabling **Data Export** is a **one-time** procedure performed over LAN from a PC. It must be done before the USB connection will produce any data.

1. Connect the Link+ **LAN (RJ-45) port** — on the left of the same connector panel — to the PC's Ethernet port with the LAN cable supplied with the Link+.

   <img src="../hardware_images/fresenius_link_agilia_3.png" width="450" alt="Link+ connector panel with the RJ-45 LAN port highlighted on the left side of the panel">

2. On the PC, open **Control Panel → Network and Internet → Network Connections**, right-click the **Ethernet** adapter and choose **Properties**.

   <img src="../hardware_images/fresenius_link_agilia_4.png" width="450" alt="Windows Network Connections with the Ethernet adapter right-clicked and Properties highlighted in the context menu">

3. In the adapter properties list, select **Internet Protocol Version 4 (TCP/IPv4)** and click **Properties**.

   <img src="../hardware_images/fresenius_link_agilia_5.png" width="450" alt="Ethernet Properties dialog with Internet Protocol Version 4 (TCP/IPv4) selected and the Properties button highlighted">

4. Choose **Use the following IP address** and enter a static address on the rack's subnet:
   - IP address: `192.168.0.100`
   - Subnet mask: `255.255.255.0`
   - Default gateway: `192.168.0.1`

   Click **OK**.

   <img src="../hardware_images/fresenius_link_agilia_6.png" width="450" alt="IPv4 properties dialog with Use the following IP address selected and 192.168.0.100 / 255.255.255.0 / 192.168.0.1 entered">

5. Open a browser and navigate to **`192.168.0.1`**. The Link+ Agilia configuration page loads. The browser will warn that the connection is not secure — this is expected for the device's local HTTP server.

   <img src="../hardware_images/fresenius_link_agilia_7.png" width="450" alt="Browser address bar showing 192.168.0.1 with the page titled Link+ Agilia and a not-secure warning">

6. On the authorized local setup connection, log in at the **Identification — Password** prompt (ID `admin` / password `fresenius`; if these are rejected, obtain the current credentials from Fresenius Kabi service).

   <img src="../hardware_images/fresenius_link_agilia_8.png" width="450" alt="Link+ Agilia web interface Identification - Password login form with ID and Password fields and a Login button">

7. Open the **Configuration** menu and select **Data Export**.

   <img src="../hardware_images/fresenius_link_agilia_9.png" width="450" alt="Link+ Agilia web interface Configuration menu expanded showing General Parameters, Network, Data Export, Time and Configuration Summary, with Data Export highlighted">

8. Under **Serial export protocol for Agilia SP and VP**, tick **Enabled**, then click **Apply**.
   <img src="../hardware_images/fresenius_link_agilia_10.png" width="450" alt="Data Export page with Serial export protocol for Agilia SP and VP set to Enabled, Serial export protocol Over TCP left disabled with port 52000, and the Apply button highlighted">

9. A dialog confirms the parameters were applied and warns that the Link+ will reboot when configuration is exited. Click **OK**.

   <img src="../hardware_images/fresenius_link_agilia_11.png" width="450" alt="Data Export confirmation dialog reading Applying parameters, please wait .. OK and warning that the settings will force the Link+ to reboot when configuration is exit">

10. Click **Exit Configuration**. The rack reboots on its own, which completes the setup.

## Vital Recorder Setup

- Add a device with **Device Type `Link+`** and leave **Port** empty. Vital Recorder finds the rack by its USB ID and follows it when it re-connects under a new port number. Leave **Y Cable** unchecked.

## Troubleshooting

- **Crashes or a failed reconnection on an older build.** Several Link+-specific crashes and a reconnection failure were fixed across 1.18.50–1.19.5; upgrade before troubleshooting hardware.
