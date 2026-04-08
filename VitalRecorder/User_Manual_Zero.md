# 1. Preparations

This document will guide you to set up the Vital Recorder Zero for collecting the biosignal data from the patient monitor.

## Getting Started

<img src="images/user_manual_zero/image14.png" width="450" />

Connect a **USB WiFi adapter (dongle)** to the USB port on the power side of the VitalRecorder (VR). Then, connect the power cable to VR for booting. When booting for the first time, it takes about 2 minutes, and the red light turns on when booting is complete.

In order to access the admin page for VR, you need to connect the VR to the smartphone, PC, or tablet via wired ethernet card. For this, you need to prepare a **USB wired ethernet adapter** for VR and another **wired ethernet adapter** for a PC (it can be a tablet PC or a smartphone). Two wired ethernet adapters can be connected using a plain **ethernet LAN cable**.

<img src="images/user_manual_zero/image13.png" width="450" />

<img src="images/user_manual_zero/image4.png" width="450" />

After being physically connected, enter the admin page address (192.168.137.2) in the address bar in the web browser on the PC. The initial password is “2017”. You can configure VR settings and network settings through this admin page.

## VR settings

<img src="images/user_manual_zero/image17.png" width="450" />

**VR name (VR code)**

**The default VR name is an 8-digit serial number. It is the same as the VR code used for registering the VR in VitalDB**. Change the VR name to something you can identify with.

**Cut file**

This specifies the methods to create vital files automatically without the user's involvement.

- by hour : A vital file is created every hour. For use in the intensive care unit, we recommend selecting by hour.

- by case : Automatically create vital files based on the values of the SpO2 and HR parameters. This option is usually for the operation room. if there is no SpO2 or HR value, vital files will not be created.

When all settings are complete, click the Apply button. Your settings will be saved and VR will restart.

## Network settings

<img src="images/user_manual_zero/image11.png" width="450" />

If a usb WiFi adapter (dongle) is connected, it will display “usb” next to Wireless.

(If not connected, it will display “on-board”.)

Enter SSID and password of the Wifi network to which the VR will be connected.

- For public AP, leave the Pass input field blank.

- For using a hidden network, check Hidden Wifi.

- For using WPA enterprise, enter User, SSID and Pass.

- For using a static IP, enter the IP, Netmask, and Gateway in the advanced settings menu.

When all settings are complete, click the Apply button to save the settings. Then, the device reboots. Please wait until the blue light flashes that indicates the VR is connected to the network successfully.

# 2. Registering VitalRecorder on Web Monitoring Page

If you use the intranet Vital Server, VR is automatically registered when it is connected to the network, but if you use the cloud VitalDB, you need to register the VR code.

## Web Browser Settings

For remote monitoring through a web browser, you must be a member of VitalDB. If you have not signed up yet, please click the following link to accept the terms and complete your membership.

[https://vitaldb.net/registration-agreement](https://vitaldb.net/registration-agreement)

After logging in, go to the Web Monitoring page.

[https://vitaldb.net/web-monitoring/](https://vitaldb.net/web-monitoring/#)

<img src="images/user_manual_zero/image1.png" width="450" />

<img src="images/user_manual_zero/image10.png" width="450" />

Click the "Register VR Code" button.

Enter the 8-digit serial number in the pop-up window and click the "OK" button.

VR code registration VR name is automatically linked with the set name.

You can create a new group by clicking “Add group”.

Device settings

On the Web Monitoring screen, right-click the VR you want to set up > click Device settings.

<img src="images/user_manual_zero/image12.png" width="450" />

<img src="images/user_manual_zero/image9.png" width="450" />

Set the equipment and port to be used as shown in the picture above.

For circular ports, C1, C2, C3, C4, and the USB port on the C1 side are recognized as a LAN card only, and the USB port on the C4 side is recognized as an LU.

<img src="images/user_manual_zero/image19.jpg" width="450" />

Once everything is set up, you can start using the Web Monitoring service on VitalDB!

# 3. Connecting VR to Patient Monitor

## Philips Intellivue MP/MX series

The Philips Intellivue Patient Monitor allows serial communication through the MIB port located on the back of the monitor, which looks like a LAN port.

There are several types of MIB ports as shown below. Please note that the display differs depending on the model.

<img src="images/user_manual_zero/image21.png" width="450" />

<img src="images/user_manual_zero/image15.png" width="450" />

<img src="images/user_manual_zero/image20.jpg" width="450" /><img src="images/user_manual_zero/image18.jpg" width="450" />

Connect the RJ45 to 3.5pi cable to the patient monitor.

Once the physical connection is established, the next step is to change the settings of the patient monitor.

<img src="images/user_manual_zero/image3.png" width="450" /><img src="images/user_manual_zero/image2.png" width="450" />

Press the "Main Setup" button on the monitor and select "Operation Modes". Then click "Service".

<img src="images/user_manual_zero/image7.png" width="450" />

Input a password to enter service mode. The default password is **1345**.

If it fails, please contact the manufacturer.

<img src="images/user_manual_zero/image8.png" width="450" /><img src="images/user_manual_zero/image6.png" width="450" />

Then go back to "Main Setup" and you will see a menu called "Hardware" at the bottom. Press and hold this button, and set the communication speed to "Fix 115200" for "Data Export 1" and "Data Export 2".

<img src="images/user_manual_zero/image16.png" width="450" />

Then click “Interfaces”,

<img src="images/user_manual_zero/image5.png" width="450" />

Make sure that the driver for port 01a is “DtOut1”.

If it is not DrOut1 (e.g. GM or AGM), click the "Change Driver" button at the bottom of the screen and change it to "DtOut1".

The number after DtOut may vary depending on the assigned port.

Changes will not take effect until the monitor is turned off and on.
