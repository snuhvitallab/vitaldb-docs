# MEKICS MP1300

<!-- meta
category: Patient Monitor
manufacturer: MEKICS
-->

For wireless connection between MEKICS device and VR, you need to set up a wireless router first. In this manual, we will guide you on how to set up using the iptime wireless router (Other routers are not much different).

### Wireless router settings

<img src="../hardware_images/image65.png" width="450" />

Connect the power to the router, open Wi-Fi list on your PC, and connect to the AP named iptime-mini.

<img src="../hardware_images/image156.png" width="450" />

Open a web browser and enter 192.168.0.1 in the address bar to set up the router.

The default Login ID and Password is admin.

<img src="../hardware_images/image88.png" width="450" />

Click Setup.

<img src="../hardware_images/image96.png" width="450" />

Go to Advanced Settings - Wireless LAN Management - Wireless Settings/Security menu. Set the network name and password as shown above.

Select ‘WPA2PSK+AES (recommended)’ for the encryption option, uncheck “Broadcast SSID”, and click the Apply button.

The connection to the router will be disconnected since the SSID of the router is changed from iptime_mini to mekics_r7.

<img src="../hardware_images/image98.png" width="450" />

Connect to a Hidden Network by entering the SSID (“mekics_r7”) and password. The changed SSID would not show up on the Wi-Fi list since “Broadcast SSID” is unchecked from the previous step.

Open a web browser and enter 192.168.0.1 in the address bar to enter the router setting screen.

<img src="../hardware_images/image149.png" width="450" />

If you plan to connect the router to a higher-level network (Internet or hospital network), perform this step. If not, you can skip it.

Go to Advanced Settings - Wireless LAN Management - Wireless Extension Settings menu.

Set the wireless extension method to wireless WAN and input the hotspot SSID and password of the VR to which the MEKICS device connects.

<img src="../hardware_images/image131.png" width="450" />

Go to Advanced Settings - System Management - Other Settings menu.

In the wired port function setting, click LAN port and then click the Apply button in the lower right corner.

### MP1300 Settings

<img src="../hardware_images/image16.png" width="450" />

Connect the router that has been set up with the MP1300 device.

Connect the power supply of the router to the USB port on the back of the device and connect the LAN cable.

<img src="../hardware_images/image5.png" width="450" />

Select System - Network, then the setting screen will appear as shown above. Set IP and gateway address.

Except the digits after the last period, the rest digits must be the same as the router IP address (192.168.0 as the example above). Choose a random number between 2 and 255 that is not used by other devices for the last digits.

- IP : 192.168.0.***

- Gateway: 192.168.0.1 (IP address of the router)

<img src="../hardware_images/image59.png" width="450" />

Go to System - Network - Central - Mode and select MP601.

<img src="../hardware_images/image34.png" width="450" />

On Central settings, enter 192.168.137.1 for Server IP and 6002 for Server Port.

The changed settings will be applied after restarting the device.

<img src="../hardware_images/image119.png" width="450" />

To add MP1300 on VitalRecorder for Windows, click “Add Device”, choose MEKICS, and set Port 6002.
