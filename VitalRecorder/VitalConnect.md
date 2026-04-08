# **VitalConnect User Manual**

## **What is VitalConnect?**

Collecting data through Vital Recorder requires multiple wired connections. The numerous cables needed for data collection cause inconvenience and can lead to unintended data loss due to disconnections. To solve this problem, we developed a device that can send serial port output to Vital Recorder using WiFi wireless communication technology. This device was built based on the Arduino-compatible Wemos (ESP-8266) board. In simple terms, this device can be defined as a "Serial to Wi-Fi" device.

The circuit diagram of the device is as follows:

> <img src="images/vitalconnect/image9.png" width="450" />

The actual circuit board is as follows:

> <img src="images/vitalconnect/image23.png" width="450" />

The exterior of the device is as follows:

> <img src="images/vitalconnect/image30.png" width="450" />

The RJ-45 connector has the same shape as an 8-pin LAN port but is designed for serial connections. The Micro USB port can be connected to a computer for firmware modification and device setup, and when used independently, it serves as a power supply port.

## **Required Materials**

### **Computer**

VitalConnect settings can be configured in various operating systems, but this document focuses on Windows systems.

VitalConnect is configured through Vital Recorder. For effective operation of multiple devices, it is recommended to install Vital Recorder and VitalConnect drivers on a separate computer from the data collection computer.

### **Cables**

#### **Micro USB Cable**

VitalConnect communicates with the computer through the micro USB port. To configure the device, a wired connection to the computer must be executed at least once. After setup, VitalConnect operates independently, and the micro USB port is used for power supply.

#### **Serial to RJ-45 Cable**

VitalConnect has an RJ-45 port (identical to an 8-pin wired LAN port). Connection to medical equipment is made through a serial cable. Therefore, a DB-9 to RJ-45 cable is required to connect the VitalConnect device to medical equipment.

To make a cable, prepare as follows (same cable as when connecting to Philips Intellivue MP/MX series):

[ Direct cable ]

> <img src="images/vitalconnect/image33.png" width="450" />

[ Cross cable ]

> <img src="images/vitalconnect/image17.png" width="450" />

## **Driver Installation**

As mentioned earlier, VitalConnect is based on Wemos equipment, and the installation of Wemos Windows driver is necessary for the device to be recognized by the computer. The driver can be downloaded from the site below:

[http://www.wch.cn/download/CH341SER_ZIP.html](http://www.wch.cn/download/CH341SER_ZIP.html)

> <img src="images/vitalconnect/image20.png" width="450" />

Download the file and extract it.

> <img src="images/vitalconnect/image28.png" width="450" />

Run setup.exe to install the driver.

> <img src="images/vitalconnect/image1.png" width="450" />

Connect VitalConnect to the computer with a USB cable and verify in Device Manager that a USB-SERIAL CH340 port has been created.

> <img src="images/vitalconnect/image12.png" width="450" />

## **Configuring VitalConnect**

With VitalConnect connected to the computer via USB cable, run Vital Recorder and click the WiFi icon.

> <img src="images/vitalconnect/image6.png" width="450" />

The CH340 port is automatically selected. When you press the Connect button, a "Connected" message should appear.

> <img src="images/vitalconnect/image24.png" width="450" />

Enter the SSID and password of the hotspot that VitalConnect will connect to. The password is displayed as asterisks (*).

The Connect ID is the name that appears in the Serial Port list when adding equipment to Vital Recorder. It is convenient to set it to the name of the equipment to which VitalConnect will be connected.

> <img src="images/vitalconnect/image15.png" width="450" />

Once the settings are complete, press the "Write" button to transmit the settings. After the transmission is complete, press the "Disconnect" button and disconnect from the computer.

## **Wireless Connection: Connection Using a Wireless Router**

If data loss occurs when using a hotspot connection, it is recommended to switch to a connection using a wireless router. In an open small space (e.g., recovery room), one router can be used to connect data from multiple VitalConnects to multiple Vital Recorders, but it is recommended to use one router per Vital Recorder if possible. The data flow diagram when using a wireless router is as follows:

Medical equipment → VitalConnect → Wireless router → (Wireless or wired connection) Vital Recorder → Wireless router → Internet

### **Router Configuration**

The affordable and high-performance router we tested is the ipTIME mini 2/3 from EFM. It can be purchased from online shopping malls for around 11,000 won. The following explanation focuses on this router. The firmware at the time of documentation is version 10.06.8 (July 26, 2018). If you have an earlier firmware, please upgrade it first.

> <img src="images/vitalconnect/image5.png" width="450" /><img src="images/vitalconnect/image27.png" width="450" />

Wireless setup and wireless extension setup are necessary for the router.

#### **Wireless Network Setup (ipTIME mini 2/3)**

It is easier to configure using a laptop's wireless LAN rather than a smartphone. When using a smartphone, it is convenient to connect to WiFi using a WiFi analyzer app.

Connect power to the router and open the wireless LAN list on your laptop to see an AP named iptime_mini. Click the "Connect" button to connect to the router's wireless LAN. For smartphones, it is better to proceed with the data connection turned off.

<img src="images/vitalconnect/image11.png" width="450" />

Open a web browser and enter 192.168.0.1 in the address bar to access the router's settings screen. The default username is admin. The default password is also admin. Enter the capture letters and log in.

> <img src="images/vitalconnect/image18.png" width="450" />

Click Setup to go to the settings screen.

> <img src="images/vitalconnect/image14.png" width="450" />

This is the initial setup screen when accessed using a laptop.

> <img src="images/vitalconnect/image13.png" width="450" />

Click 'Wireless Setup' and the following screen appears:

> <img src="images/vitalconnect/image8.png" width="450" />

The basic wireless network settings window appears. Here, you will set up the wireless network to be used in the operating room. Set the network name and password as follows. Below, the network name is set to vital_d5 and the password to 111111111. Select the 'Name notification' option under SSID. For encryption options, select 'WPA2PSK+AES (recommended)'. When finished, press the "Apply" button at the bottom right.

> <img src="images/vitalconnect/image25.png" width="450" />

After saving, the router connection is automatically disconnected. This is because the router's SSID has been changed from iptime_mini to vital_d5.

#### **Wireless Extension Setup**

This is necessary when you want to connect to the external internet using an existing wireless LAN. This setting is necessary for web monitoring from outside the data collection facility.

Search for the wireless LAN and connect to vital_d5. When asked for a password, enter 111111111 as set earlier. You will be connected to the router but not to the internet.

<img src="images/vitalconnect/image35.png" width="450" />

Open a web browser again and enter 192.168.0.1 to access the settings screen. Go to Advanced Setup/ Wireless/ Wireless Multibridge.

> <img src="images/vitalconnect/image2.png" width="450" />

Select 'WISP' from Mode. (Wireless Internet Service Provider)

> <img src="images/vitalconnect/image22.png" width="450" />

Press the "AP scan" button below the "Apply" button. Select the SSID (wireless AP) that has external internet access. If authentication is required, enter the password in 'Encryption'.

> <img src="images/vitalconnect/image34.png" width="450" />

Press the "Apply" button to apply all changes and terminate the connection.

### **Wired LAN Setup**

The ipTIME mini2/3 has a wired LAN port. The default setting for the wired port is WAN, which allows internet access when connected to a port that provides wired internet via LAN cable. However, since we set the WAN to wireless above, we can use this port as a local wired network (wired LAN) port connected to the VR computer. In this case, reducing wireless traffic between the VR computer and the wireless router makes the entire wireless network connection smoother.

To set the wired port as a wired LAN port, click "Advanced Setup/ System/ Misc Setup".

> <img src="images/vitalconnect/image7.png" width="450" />

Go to "Wired Port Setup". The initial value is 'WAN port'. Change this to 'LAN port'.

> <img src="images/vitalconnect/image39.png" width="450" />

Press the "Apply" button and the device will restart.

> <img src="images/vitalconnect/image10.png" width="450" />

When the router turns back on, you can see the following Status Summary:

> <img src="images/vitalconnect/image32.png" width="450" />

Connect the router's wired port and the VR computer's wired port with a direct LAN cable. Turn off the VR computer's wireless LAN and turn on the wired LAN. Restart the computer.

## **Adding Equipment in Vital Recorder**

Once VitalConnect is successfully connected to the Windows hotspot or router's wireless AP, you can add the device to Vital Recorder.

Supply power to the VitalConnect connected to the medical equipment. A blue light turns on at the front of VitalConnect.

Press the "Add Device" button.

Select the equipment type from the left column. In the Serial Port selection window in the right column, you can see the Connect ID of VitalConnect set earlier.

> <img src="images/vitalconnect/image36.png" width="450" />

Selecting the Connect ID name adds the equipment.

> <img src="images/vitalconnect/image37.png" width="450" />

When the vitalconnect device is successfully added, the blue light on the device changes from continuously on to blinking at approximately 1-second intervals.

## **Wireless Connection: Connection Using Windows Hotspot**

**Connection using a Windows hotspot may be unstable depending on computer performance and is not recommended at the current stage.**

The flow of data is as follows:

**Medical equipment → VitalConnect → Computer wireless LAN (hotspot) → Vital Recorder → Computer wireless LAN (internet)**

Available on the latest versions of Windows 10 (version 1609 and later, 1803 update recommended). A wireless LAN must be installed on the computer. Laptops can use their built-in wireless LAN, while desktops require the addition of a USB wireless LAN or wireless LAN card.

Click the notification window (bottom right corner) and right-click on the mobile hotspot button to go to 'Go to Settings'.

<img src="images/vitalconnect/image16.png" width="450" />

In Mobile Hotspot, turn on 'Share my internet connection with other devices'. Set my internet connection sharing to 'Wi-Fi'. Click "Edit" in the Share my internet connection item.

> <img src="images/vitalconnect/image21.png" width="450" />

Enter the SSID and password that the VitalConnect device will connect to in the network name and password fields, then save. However, the same information must be entered when setting up the VitalConnect device to connect to the hotspot.

> <img src="images/vitalconnect/image26.png" width="450" />

Supply power to the VitalConnect connected to the medical equipment. A blue light turns on at the front of VitalConnect.

Soon after, VitalConnect connects to the hotspot, and the notification window displays the hotspot name and the number of connected devices. A maximum of 8 can be connected.

> <img src="images/vitalconnect/image29.png" width="450" />

### **Operating a Hotspot Stably**

When VitalConnect is not connected to the hotspot, the computer automatically stops the hotspot. Follow these steps to prevent the hotspot from turning off automatically:

Go to Mobile Hotspot settings and look at the related settings section in the middle. Click "Change adapter options".

> <img src="images/vitalconnect/image4.png" width="450" />

Right-click on the icon displayed as "Local Area Connection*number" and select "Properties".

> <img src="images/vitalconnect/image31.png" width="450" />

Click "Configure (C)".

> <img src="images/vitalconnect/image19.png" width="450" />

Select the last tab (Power Management).

> <img src="images/vitalconnect/image38.png" width="450" />

Uncheck "To save power..." and click OK.

> <img src="images/vitalconnect/image3.png" width="450" />

## **Precautions**

1.  Windows' built-in hotspot does not yet appear to be sufficiently stable. (Current version 1803). Be careful with management as the hotspot may disconnect on its own.

2.  If data transmission is frequently interrupted when using a Windows hotspot with a laptop's built-in wireless LAN, try installing and using an additional USB wireless LAN.

3.  Connecting all devices wirelessly is not recommended. Wireless interference may occur between vitalconnects, and if the total data transmission of all vitalconnects exceeds the bandwidth of the wireless network, data loss may occur.

4.  The recommended setting when using vitalconnect is to limit vitalconnect use to equipment that is several meters or more away from the computer with Vital Recorder installed and does not move to other locations. For equipment that moves frequently, it is recommended to use a wired connection because there is a risk that data may be transmitted to another patient's Vital Recorder. In this case, assign the equipment name to an empty serial port in advance, and when using mobile equipment, connect directly to collect data immediately.
