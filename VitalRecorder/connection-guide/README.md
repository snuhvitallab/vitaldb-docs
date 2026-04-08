# Getting Started

### Before You Begin

This guide document explains **how to prepare the hardware** necessary to collect data from various patient monitors using the Vital Recorder program. Please read, prepare, and run in order.

In addition, this manual is for reference only and our team is not responsible for any part of the connection error.

If there are any discrepancies between this document and your clinical device manufacturer’s manual, please follow the manufacturer’s manual.

If you have any questions or suggestions regarding the use of Vital Recorder, please use the forum on the vitaldb.org website.

### Overview

Connecting one or two medical devices to a PC and collecting data using the Vital Recorder is very simple to get started. As you become accustomed to connecting devices and programs, it is possible to collect data from 5-6 devices at the same time.

So let's get started.

<img src="images/hw_guide/image191.png" width="450" />

## Requirements

### Computer

The Vital Recorder works on Windows operating systems, so you need a computer with a Windows system installed. The Vital Recorder has been tested on 32-bit and 64-bit versions of Windows Vista, 7, 8, 8.1, and 10.

The minimum specification of the computer to operate the Vital Recorder is very low. The lowest system specification that we tested for stable operation was the netbook (MSI U-100) based on the Atom CPU (Intel N330) and we observed up to a 30% increase in CPU utilization when recording data on the full screen in real time. CPU usage on Intel i3-based computers was less than 5%.

With a laptop, you can prevent the operating room from being crowded. Considering the expense issue, we also recommend the low-cost Windows Tablet. Most tablets have similar specifications so you can choose whatever you like. However, since multiple devices need to be connected, a system with several full-size USB ports is recommended for stable operation. If necessary, you may use a USB hub to expand the number of available ports.

### Serial Cables

There are two types of serial cable: direct cable and cross cable. Note that this is defined by the connection of the wires inside the cable, so there is no apparent difference in appearance.

A direct cable is a cable with internal wires that do not intersect, often called a serial extension cable, and often it has 9-pin female/male terminals on each side. Please purchase it in the required length. Below is a link to "3 meters Direct Serial Cable (M/F)" that can be purchased in Korea.

[http://cableguy.com/shop/mall.php?cat=025013001&query=view&no=15641](http://cableguy.com/shop/mall.php?cat=025013001&query=view&no=15641)

<img src="images/hw_guide/image109.png" width="450" />

Most medical devices communicate with PCs via direct serial cables, but some medical devices (such as Fresenius Vial Orchestra, Edwards Lifesciences' cardiac output devices) require a cross cable. If you connect a cross cable to a device that requires a direct cable (or vice versa), electrical shorts may occur between the device and the PC, causing malfunction of the device, and rarely explosion or fire. You should always keep this in mind.

Our recommendation is that all cables are only provided with a **direct cable**, and if you need a cross connection, you can purchase a **cross gender** as shown below. By securing the cross gender into the device with a screw, you can prevent it from becoming loose and eliminate concerns about cable types, thereby reducing confusion.

<Null modem(M/F cross gender) >

[http://cableguy.com/shop/mall.php?cat=007001001&query=view&no=33688](http://cableguy.com/shop/mall.php?cat=007001001&query=view&no=33688)

<img src="images/hw_guide/image181.png" width="450" />

<Null modem(F/F cross gender)>

[http://cableguy.com/shop/mall.php?cat=007001001&query=view&no=189324](http://cableguy.com/shop/mall.php?cat=007001001&query=view&no=189324)

<img src="images/hw_guide/image36.png" width="450" />

### Gender Type Summary

Since the terminal on the PC side is male, the device side must always be a female port. In case of direct connection, Pin No. 2 and Pin 3 of PC 9-pin serial port (DB-9) are Rx and Tx, respectively. If a cross connection is required, the connection pins are changed to 3 and 2, respectively. The recommended method is to prepare all cables with a direct cable and use an additional gender if necessary.

| **Device** | **Device port** | **Gender type (Male/Female)** | **Gender (Direct/Cross)** | **Vital connect cable** |
|----|----|----|----|----|
| GE Solar 8000M | Female | M/F | D | M/D |
| BIS | Female | M/F | D | M/D |
| PLEM | Female | M/F | D | M/D |
| Base Primea (Orchestra) | Female | M/F | C | M/C |
| Vigileo, EV1000A, Vigilance, Hemosphere | Female | M/F | C | M/C |
| EV1000 Old Ver. | Male | F/F | C | F/C |
| INVOS | Male | F/F | C | F/C |
| MP400-500 | Male | F/F | C | F/C |
| CardioQ | Male | F/F | C | F/C |
| FMS | Male | F/F | C | F/C |
| MP20-90 | Male | F/F | D | \- |

### VR connections

<table style="width:85%;">
<thead>
<tr>
<th style="text-align: center;"><strong>Device name</strong></th>
<th style="text-align: center;"><strong>Device type</strong></th>
<th style="text-align: center;"><strong>Manufacturer</strong></th>
<th style="text-align: center;"><strong>Device port</strong></th>
<th style="text-align: center;"><strong>Connection 1</strong></th>
<th style="text-align: center;"><strong>Connection 2</strong></th>
</tr>
<tr>
<th style="text-align: center;">Carescape B450, B650, B850</th>
<th style="text-align: center;">Patient monitor</th>
<th style="text-align: center;">GE</th>
<th style="text-align: center;">USB</th>
<th style="text-align: center;">ATEN UC-232A USB serial converter</th>
<th style="text-align: center;"><p>Null modem</p>
<p>(F/F cross gender)</p></th>
</tr>
<tr>
<th style="text-align: center;">Carescape B20, B40</th>
<th style="text-align: center;">Patient monitor</th>
<th style="text-align: center;">GE</th>
<th style="text-align: center;">Serial (DB9F)</th>
<th style="text-align: center;">Direct serial cable (DB9M-DB9F)</th>
<th style="text-align: center;"></th>
</tr>
<tr>
<th style="text-align: center;">Solar 8000m, 8000i</th>
<th style="text-align: center;">Patient monitor</th>
<th style="text-align: center;">GE</th>
<th style="text-align: center;">Serial (DB9F)</th>
<th style="text-align: center;">Direct serial cable (DB9M-DB9F)</th>
<th style="text-align: center;"></th>
</tr>
<tr>
<th style="text-align: center;">Tram Rac-4A</th>
<th style="text-align: center;">Patient monitor</th>
<th style="text-align: center;">GE</th>
<th style="text-align: center;">ANALOG OUT</th>
<th style="text-align: center;"><strong>ADC</strong></th>
<th style="text-align: center;"></th>
</tr>
<tr>
<th style="text-align: center;">Dash 2000, 3000, 4000</th>
<th style="text-align: center;">Patient monitor</th>
<th style="text-align: center;">GE</th>
<th style="text-align: center;">AUX (RJ45)</th>
<th style="text-align: center;"><p><strong>RJ45 to DB9F</strong></p>
<p><strong>custom serial cable</strong></p></th>
<th style="text-align: center;"></th>
</tr>
<tr>
<th style="text-align: center;">Dash 2500</th>
<th style="text-align: center;">Patient monitor</th>
<th style="text-align: center;">GE</th>
<th style="text-align: center;"><p>Host Comm</p>
<p>(DB9F)</p></th>
<th style="text-align: center;">Direct serial cable (DB9M-DB9F)</th>
<th style="text-align: center;"></th>
</tr>
<tr>
<th style="text-align: center;">Defib.Sync.</th>
<th style="text-align: center;">Patient monitor</th>
<th style="text-align: center;">GE</th>
<th style="text-align: center;"><p>Analog</p>
<p>(7pin mini DIN)</p></th>
<th style="text-align: center;"><strong>ADC</strong></th>
<th style="text-align: center;"></th>
</tr>
<tr>
<th style="text-align: center;">Intellivue MP, MX</th>
<th style="text-align: center;">Patient monitor</th>
<th style="text-align: center;">Philips</th>
<th style="text-align: center;">MIB (RJ45)</th>
<th style="text-align: center;"><p><strong>RJ45 to DB9F</strong></p>
<p><strong>custom serial cable</strong></p></th>
<th style="text-align: center;"></th>
</tr>
<tr>
<th style="text-align: center;">Intellivue MX 400-550</th>
<th style="text-align: center;">Patient monitor</th>
<th style="text-align: center;">Philips</th>
<th style="text-align: center;">ASIB (RJ45)</th>
<th style="text-align: center;"><p><strong>RJ45 to DB9F</strong></p>
<p><strong>custom serial cable</strong></p></th>
<th style="text-align: center;"></th>
</tr>
<tr>
<th style="text-align: center;">Infinity</th>
<th style="text-align: center;">Patient monitor</th>
<th style="text-align: center;">Drager</th>
<th style="text-align: center;">X3 or X5 (mini-D)</th>
<th style="text-align: center;"><strong>mini-D to DB9F custom serial cable</strong></th>
<th style="text-align: center;"></th>
</tr>
<tr>
<th style="text-align: center;"><p>Infinity</p>
<p>(analog/sync)</p></th>
<th style="text-align: center;">Patient monitor</th>
<th style="text-align: center;">Drager</th>
<th style="text-align: center;">X10</th>
<th style="text-align: center;"><strong>ADC</strong></th>
<th style="text-align: center;"></th>
</tr>
<tr>
<th style="text-align: center;">MP1300</th>
<th style="text-align: center;">Patient monitor</th>
<th style="text-align: center;">MEKICS</th>
<th style="text-align: center;">WiFi</th>
<th style="text-align: center;"></th>
<th style="text-align: center;"></th>
</tr>
<tr>
<th style="text-align: center;">BSM</th>
<th style="text-align: center;">Patient monitor</th>
<th style="text-align: center;">Nihon Kohden</th>
<th style="text-align: center;">Serial (DB9F)</th>
<th style="text-align: center;">Direct serial cable (DB9M-DB9F)</th>
<th style="text-align: center;"></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

| **Device name** | **Device type**     | **Manufacturer**     |
|-----------------|---------------------|----------------------|
| Primus          | Anesthesia Machine  | Drager               |
| Datex-Ohmeda    | Anesthesia Machine  | GE                   |
| Flow-i          | Anesthesia Machine  | Maquet               |
| EV-1000         | Hemodynamic monitor | Edwards Lifesciences |
| EV-1000 A       | Hemodynamic monitor | Edwards Lifesciences |
| Vigilance       | Hemodynamic monitor | Edwards Lifesciences |
| Vigileo         | Hemodynamic monitor | Edwards Lifesciences |
| HemoSphere      | Hemodynamic monitor | Edwards Lifesciences |
| Cardio Q        | Hemodynamic monitor | Deltex               |

<table style="width:66%;">
<thead>
<tr>
<th style="text-align: center;"><strong>Device name</strong></th>
<th style="text-align: center;"><strong>Device type</strong></th>
<th style="text-align: center;"><strong>Manufacturer</strong></th>
<th style="text-align: center;"><strong>Device port</strong></th>
<th style="text-align: center;"><strong>Connection 1</strong></th>
</tr>
<tr>
<th style="text-align: center;">Orchestra</th>
<th style="text-align: center;">Syringe pump</th>
<th style="text-align: center;">Fresenius Kabi</th>
<th style="text-align: center;">RS232-3 (DB9F)</th>
<th style="text-align: center;">Direct serial cable (DB9M-DB9F)</th>
</tr>
<tr>
<th style="text-align: center;">Agilia</th>
<th style="text-align: center;">Syringe pump</th>
<th style="text-align: center;">Fresenius Kabi</th>
<th style="text-align: center;">Serial (7pin mini DIN)</th>
<th style="text-align: center;"><strong>proprietary cable</strong></th>
</tr>
<tr>
<th style="text-align: center;">SpaceCom</th>
<th style="text-align: center;">Syringe pump</th>
<th style="text-align: center;">BBraun</th>
<th style="text-align: center;">Serial (9pin mini DIN)</th>
<th style="text-align: center;"><strong>proprietary cable</strong></th>
</tr>
<tr>
<th style="text-align: center;">Pion TCI</th>
<th style="text-align: center;">Syringe pump</th>
<th style="text-align: center;">Bionet</th>
<th style="text-align: center;">Serial (DB9F)</th>
<th style="text-align: center;">Direct serial cable (DB9M-DB9F)</th>
</tr>
<tr>
<th style="text-align: center;">BIS</th>
<th style="text-align: center;">Brain monitor</th>
<th style="text-align: center;">Medtronic</th>
<th style="text-align: center;">RS232-3 (DB9F)</th>
<th style="text-align: center;">Direct serial cable (DB9M-DB9F)</th>
</tr>
<tr>
<th style="text-align: center;">Invos</th>
<th style="text-align: center;"><p>Cerebral/</p>
<p>Somatic oximetry</p></th>
<th style="text-align: center;">Medtronic</th>
<th style="text-align: center;">Serial (DB9M)</th>
<th style="text-align: center;">Direct serial cable (DB9M-DB9F)</th>
</tr>
<tr>
<th style="text-align: center;">Radical7</th>
<th style="text-align: center;">Pulse CO-Oximeter</th>
<th style="text-align: center;">Masimo</th>
<th style="text-align: center;">Serial (DB9F)</th>
<th style="text-align: center;">Direct serial cable (DB9M-DB9F)</th>
</tr>
<tr>
<th style="text-align: center;">ROOT</th>
<th style="text-align: center;"></th>
<th style="text-align: center;">Masimo</th>
<th style="text-align: center;">USB1 or USB2</th>
<th style="text-align: center;">generic USB serial converter</th>
</tr>
<tr>
<th style="text-align: center;">ANI Monitor V2</th>
<th style="text-align: center;">Analgesia nociception monitor</th>
<th style="text-align: center;">MDMS</th>
<th style="text-align: center;">Serial (DB9F)</th>
<th style="text-align: center;">generic USB serial converter</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Serial to USB Converter

If your computer does not have a serial port, such as a laptop or tablet PC, use a Serial to USB cable. The Serial to USB converter creates a serial port on the computer and acts as a direct cable simultaneously.Therefore, devices that require a cross connection must be used with this Serial to USB cable.

There is also a multi-port Serial to USB converter for many serial connections and we recommend a converter called Netmate 4 port serial to USB converter(Kangwonjeonja). When you connect this converter to your PC, four COM ports are created in the device manager of the computer, allowing simultaneous data acquisition from four devices via one USB port.

[http://cableguy.com/shop/mall.php?cat=005004003&query=view&no=39206](http://cableguy.com/shop/mall.php?cat=005004003&query=view&no=39206)

<img src="images/hw_guide/image126.png" width="450" />

### USB Hub

If the USB port is not enough, you can also use a USB hub. It is recommended that you select a USB hub that has its own power supply(often labeled as “powered”) separately.

Below is ORICO 4 port which we are usually using.

[http://www.enuri.com/detail.jsp?modelno=10534644&cate=&IsDeliverySum=N](http://www.enuri.com/detail.jsp?modelno=10534644&cate=&IsDeliverySum=N)

<img src="images/hw_guide/image136.png" width="450" />

### USB Extension Cable

You may need a USB extension cable if the distance between the computer and the device is too far. If the distance is less than 10 meters, there is no worry that the signal will be weak so that you can buy a cheaper one. In addition, it is recommended to use products that are shielded from electromagnetic waves.

Below is the product we are usually using.

[http://cableguy.com/shop/mall.php?cat=025011002&query=view&no=541](http://cableguy.com/shop/mall.php?cat=025011002&query=view&no=541)

<img src="images/hw_guide/image20.png" width="450" />

### Summary

The following is the total cost to prepare basic supplies (the configuration for acquiring data from four equipments at the same time)

<table style="width:67%;">
<thead>
<tr>
<th style="text-align: center;"><strong>Product name</strong></th>
<th style="text-align: center;"><strong>Unit price (KRW)</strong></th>
<th style="text-align: center;"><strong>Quantity</strong></th>
</tr>
<tr>
<th style="text-align: center;"><p><a href="http://cableguy.com/shop/mall.php?cat=007001001&amp;query=view&amp;no=33688">Null modem</a></p>
<p><a href="http://cableguy.com/shop/mall.php?cat=007001001&amp;query=view&amp;no=33688">(M/F, F/F cross gender)</a></p></th>
<th style="text-align: center;">1,954</th>
<th style="text-align: center;">6</th>
</tr>
<tr>
<th style="text-align: center;"><a href="http://cableguy.com/shop/mall.php?cat=025013001&amp;query=view&amp;no=15641">direct serial cable (M/F, 3m)</a></th>
<th style="text-align: center;">1,954</th>
<th style="text-align: center;">4</th>
</tr>
<tr>
<th style="text-align: center;"><a href="http://cableguy.com/shop/mall.php?cat=005004003&amp;query=view&amp;no=39206">serial to USB converter</a></th>
<th style="text-align: center;">50,500</th>
<th style="text-align: center;">1</th>
</tr>
<tr>
<th style="text-align: center;"><a href="http://cableguy.com/shop/mall.php?cat=025011002&amp;query=view&amp;no=541">USB hub</a></th>
<th style="text-align: center;">35,000</th>
<th style="text-align: center;">1</th>
</tr>
<tr>
<th style="text-align: center;"><a href="http://cableguy.com/shop/mall.php?cat=025011002&amp;query=view&amp;no=541">USB extension cable (M/F, 5m)</a></th>
<th style="text-align: center;">2,000</th>
<th style="text-align: center;">1</th>
</tr>
<tr>
<th colspan="3" style="text-align: center;">Sum: 107,040 KRW</th>
</tr>
</thead>
<tbody>
</tbody>
</table>


---

# Solutions to Common Problems

Most common problems are related to hardware connections. Program bugs are constantly being fixed, so please let us know on the bulletin board any issues that are not fixed.

**Symptom: Vital Recorder does not specify COM port when setting up device after connecting device to the Vital Recorder appropriately.**

## Device Driver Problems

- Cause : The device driver was not properly installed.

- Diagnosis : Make sure the device's port is visible in Device Manager. If there is a yellow exclamation point on the USB Serial Port device as shown on the left side of the figure below, there is a malfunction of the device or a driver problem. It is normal that the equipment is shown on the port (COM & LPT) as shown on the right.

<img src="images/hw_guide/image140.png" width="450" />

- Solution : Please download and install a driver for Serial to USB converter from its manufacturer website. If the problem persists, it may be a hardware problem, so please change Serial to USB converter.

## Connected to the Wrong Port

- Cause : In the case of a 4-port USB hub, the order of the physical port number and the recognized COM port number may occasionally change.

- Diagnosis and solution : Connect one device at a time, and change the COM port in the Add Device dialog box to recognize it.

**Symptom: After the device is connected in the Vital Recorder, the data comes in initially and then drops off every few seconds to several hours.**

## Hub Power Shortage Problem (Most Common)

- Cause : If the USB port does not provide sufficient power to the device, the device may function normally for a short period but can disconnect or malfunction at any time. This issue is especially likely when using a USB hub to connect multiple devices to a single USB port.

- Solution : You need to use a USB port with a separate power supply from the external adapter.

-

## External Electrical Noise

- Cause : Many electronic devices are used in the operating room such as electrocautery, cardiopulmonary circulator, air warmer, neuromuscular potential monitoring equipment. Current noise from these can interfere with the operation of equipment such as data acquisition computers and ADCs.

- Diagnosis : If the device connection is lost or the computer shuts down when using external equipment such as an electrosurgical unit, this issue may be the cause.

- Solution : Use the power supply of the computer for data acquisition separately from the power supply of other equipment. In particular, the power cable of the electrocautery must be separated from the data acquisition computer and USB hub. The connection between the device and the USB port should be as short as possible and use a shielded or twisted cable.

-

## Poor Connection with USB Port (2nd Most Common)

- Cause : If the device is recognized when the computer port is changed, it is possible that the previously used port is defective. The USB port on the computer may be damaged due to loose contact between the port and the cable, pulling the cable into the port, and so on. In the operating room, if the cable is not securely fastened to the port, the cable is easily pulled and it is common to break the port of the computer.

- Solution : Be sure to secure all cables to fixed equipment, such as the anesthesia machine, to prevent them from being pulled or disconnected. It is recommended to firmly fasten the cables with cable ties so that no force is applied to the ports even if the cables are pulled. If a computer port is damaged, use a different port. If there are not enough available ports, connect devices using a powered USB hub with 2 or 4 ports through a functioning port. If there are no remaining ports, request service from the computer’s motherboard manufacturer or replace the computer.

## Defective USB Cable

- Cause : The USB cable may be stepped on, twisted or pulled, resulting in internal disconnection or broken connectors on the port, resulting in poor contact.

- Diagnosis : Check if the issue is resolved by replacing the USB cable.

- Solution : Replace the USB cable.

## USB Extension Cable

- Cause : If the USB cable is too short, use a USB extension cable to extend its length. However, poor contact may occur between the USB extension cable and the existing USB device, and problems such as signal distortion may arise due to excessively long transmission distances, which can cause the device to malfunction.

- Diagnosis : Remove the USB extension cable and connect the USB device directly to the computer to check if the issue is resolved.

- Solution : Remove the USB extension cable.
