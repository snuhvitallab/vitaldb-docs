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

# Patient monitors

Now, let's connect medical equipment and PC. Depending on the equipment, you may receive data immediately when you plug in the cable, or you may need to enter the administrator mode and change the settings after entering the password. Fortunately, once you have made the connection, you do not have to touch it again. For safety, be sure to set up the equipment before it is connected to the patient or subject.

The important thing about connecting the equipment is that depending on the equipment(e.g. Fresenius Vial Orchestra, Edwards lifescience), it is necessary to connect with a cross cable instead of a direct serial cable. We will tell you again when the equipment is needed.

## GE CARESCAPE B850, B650, B450

Note : This protocol is called the **GE S5 Computer Interface** and is used to connect with GE B850/650/450 monitors and B40/20, Datex-Ohmeda S/5 monitors through this interface. GE S5 Computer Interface is a communication protocol used by an old data collection program from GE (S5 collect). The GE B40 (9 pin cable with pin 4 removed) and the Datex-Ohmeda S/5 monitor (using female-female null modem gender only) communicate with the same protocol.

The version of your monitor can be checked under Monitor setup > defaults&service > service.

If your monitor is a CARESCAPE **B850, B650, B450,** it can be connected if the monitor version is 3.1 or higher, and requires a Startech ICUSB232V2 USB to RS232 converter. ([https://www.amazon.ca/dp/B00GRP8EZU/ref=redir_mobile_desktop/146-2308166-9887501?\_encoding=UTF8&ref\_=ya_aw_od_pi&th=1](https://www.amazon.ca/dp/B00GRP8EZU/ref=redir_mobile_desktop/146-2308166-9887501?_encoding=UTF8&ref_=ya_aw_od_pi&th=1))

For CARESCAPE **Bx50 v2**, only the legacy ATEN UC232A cable (with serial numbers starting with Z3L1 or later alphabetically) is compatible, but this cable is currently discontinued and unavailable.

Connect this converter cable mentioned above to the USB port on the back of the equipment. It can be plugged into any of the four USB ports*(circled in red on the diagram below)* on the back of the monitor.

<img src="images/hw_guide/image22.png" width="450" />

Then, connect to the PC's serial port (or a common USB serial converter) through a "**Null modem (F/F cross gender)" cable**. If you are using VRZero, the USB cable connecting to VRZero must be a product that supports handshaking.

<img src="images/hw_guide/image31.png" width="450" />

[Kangwon Electronics] NETmate USB 2.0 to RS232 Converter Cable, 0.45M [KW-525] [http://www.compuzone.co.kr/product/product_detail.htm?ProductNo=374732&BigDivNo=&MediumDivNo=1139&DivNo=2659](http://www.compuzone.co.kr/product/product_detail.htm?ProductNo=374732&BigDivNo=&MediumDivNo=1139&DivNo=2659)

[ATEN] USB 1.1 to RS232 Converter Cable, 0.35M [UC232A] [http://www.compuzone.co.kr/product/product_detail.htm?ProductNo=60189&BigDivNo=&MediumDivNo=1139&DivNo=2659](http://www.compuzone.co.kr/product/product_detail.htm?ProductNo=60189&BigDivNo=&MediumDivNo=1139&DivNo=2659)

## GE S/5 AM

> For the GE S/5 AM monitor, connect to port X8 as shown in the diagram below. (Requires "**Null modem (F/F cross gender)**")
>
> <img src="images/hw_guide/image161.png" width="450" />

## GE B40, B20

> For B40/B20 monitors, connect to the 9-pin serial port as shown below. A 9-pin cable with pin 4 removed must be used.
>
> <img src="images/hw_guide/image8.png" width="450" />

## GE B105M, B125M, B155M

> Connect the direct serial cable to the serial port marked in red on the back of the equipment. When adding equipment in Vital Recorder, select GE: Bx50.

<img src="images/hw_guide/image1.png" width="450" />

## GE Solar 8000m, 8000i

This is the simplest method. Simply connect the direct serial cable to the port labeled "RS-232 1" on the right side of the equipment's back panel. No other special settings are required.

<img src="images/hw_guide/image63.png" width="450" />

When adding equipment in Vital Recorder, select GE::Solar 8000m.

Note: This protocol is called the GE Unity protocol. GE Solar 8000m, Solar 8000i, Dash 3000, 4000 and 5000 use this protocol.

## GE Dash 2000/3000/4000

<img src="images/hw_guide/image37.png" width="450" />

Serial communication is performed through the RJ45 connector on the rear AUX terminal. Therefore, a cable with a serial cable terminal (DB9F) on one side and a LAN terminal (RJ-45) on the other side is required.

You can directly manufacture the cable using a USB serial converter and LAN cable, but it's also an option to request cable manufacturing through internet-based cable fabrication companies. When making a request, you can ask for manufacturing with the wiring shown below.

> <img src="images/hw_guide/image101.png" width="450" />

Select “GE :: Dash x000” when adding device in the Vital Recorder program.

When adding equipment in Vital Recorder, select GE::Dash x000.

Note: This protocol is called the GE Unity protocol. GE Solar 8000m, Solar 8000i, Dash 3000, 4000 and 5000 use this protocol.

## GE Dash 2500

<img src="images/hw_guide/image48.png" width="450" />

Likewise, a direct serial cable is used. Plug it into the “Host Comm Port” on the back.

If communication is not established, set the following in the monitor.

1\. Turn the Trim Knob to open the Main Menu

2\. Select “other system setting”

3\. Select “go to config mode” and select “yes”

4\. Enter “2508” and select “done”

5\. Device rebooted

6\. Turn the Trim Knob to select the “Configuration Menu”

7\. Select “other system settings”

8\. Select “Config HostComm”

9\. Select “remote access” and select “Serial 2”

10\. Select “Serial 2 setup” and select “ASCII cmd”, “9600 baud” (default)

11\. Select “go to previous menu”

12\. Choose “save default changes”

13\. Select “exit configuration mode” and select “yes”

14\. Device rebooted

Select “GE :: Dash 2500” when adding device in the Vital Recorder program.

Note: This protocol is called the GE Dinamap protocol and is only used with the Dash 2500.

## GE TRAM-RAC 4A

Waveform data such as ECG and arterial pressure can only be received through the 15-pin ANALOG OUT connector located at the back of the GE monitor's Tram-RAC 4A (device for inserting multiple modules).

<img src="images/hw_guide/image18.png" width="450" />

This port is not a digital port for the transmission of numerical values, but an analog port that outputs the waveform change as a voltage value. Since the voltage value of the analog port can not be read directly from the computer, it needs an equipment called an analog-to-digital converter (ADC) which converts it to digital.

ADCs range in variety, from low-cost products in the $ 50 range to high-performance products in the thousands of dollars. Currently tested equipment is DataQ's DI-149 and DI-155, which are the cheapest but show sufficient performance for research purposes. The most significant difference between the two products is the difference in voltage resolution. For general monitoring purposes, the cheaper DI-149 is sufficient, but DI-155 is recommended for analyzing T-wave or P-waves in electrocardiograms ([http://www.dataq.com/products](http://www.dataq.com/products/di-149/)).

After purchasing the ADC, you must create a cable to feed the voltage output from the ANALOG OUT port of the GE TRAM RAC into the ADC input. You can also make this cable yourself, but you can leave it to the cable manufacturer. At the time of order, you should ask for production as below. When placing an order, request manufacturing with the pins connected as shown below.

This shows the cable custom-ordered from [http://www.cableguy.com/](http://www.cableguy.com/) connected to the DI-149.

<img src="images/hw_guide/image17.png" width="450" />

When using DataQ's DI-149 according to the above method, additional costs for customs clearance and shipping are incurred, plus you need to separately order a 15-pin adapter to connect to the analog channels, resulting in a final cost of approximately 100,000-200,000 KRW per unit.

Newer DataQ analog-to-digital converters such as the DI-1110 can operate in two modes (libusb mode and CDC mode). Among these, Vital Recorder can only recognize the device when operating in CDC mode, so to use these devices, please change the device mode according to the manufacturer's manual below: [https://www.dataq.com/blog/data-acquisition/usb-daq-products-support-libusb-cdc](https://www.dataq.com/blog/data-acquisition/usb-daq-products-support-libusb-cdc)

To address these cost issues and enable anyone to acquire data affordably, we have independently designed and manufactured a device called SNU-ADC. The SNU-ADC not only has 8-channel ADC functionality but also allows connection of wired/wireless push buttons for inserting event markers.

> <img src="images/hw_guide/image41.png" width="450" />

An important point to note is that you must connect the cable to the specified connector on the TRAM RAC module to receive the waveform signal correctly. Regardless of which ADC is used, the cable must not be connected to the BP connector (BP2, second left connector) to receive the PLETH waveform from the TRAM RAC. If a cable such as CVP is plugged into BP2, BP2 will be recorded instead of PLETH. PLETH and BP's waves look similar, so it's hard to notice when they're connected incorrectly. The figure below shows this incorrect connection. CVP is recorded to the PLETH channel and CVP is not displayed properly.

<img src="images/hw_guide/image139.png" width="450" />

| <img src="images/hw_guide/image21.png" width="450" /> | <img src="images/hw_guide/image196.png" width="450" /> |
|----|----|
| Wrong connection: The CVP Transducer cable is connected from the left to the second BP connector (BP2) | Correct connection: The CVP transducer cable is connected from the left to the third BP connector (BP3) |

<img src="images/hw_guide/image107.png" width="450" />

Additionally, when monitoring ICP, the ICP must be plugged into the first slot in the TRAM RAC.

## GE Defib connectors

If the analog port is used for other purposes, you can receive ECG, ABP from the Defib.Sync port on the front panel in the form of voltage. The pin numbers are as follows, and the voltage output value is the same as the Tram-Rac analog port. Purchase a 7-pin DIN cable (or 8-pin DIN cable is also compatible, then cut the middle of the cable and modify it.

<img src="images/hw_guide/image28.png" width="450" />

<img src="images/hw_guide/image144.png" width="450" />

## Philips Intellivue MP/MX series

The Philips Intellivue patient monitor is capable of serial communication via a MIB port that looks like a LAN port. It does not matter whether it is connected to a central monitor or not.

<img src="images/hw_guide/image128.png" width="450" />

There are several types of MIB ports as shown below. Please note that labels vary depending on the model.

<img src="images/hw_guide/image165.png" width="450" />

To connect via MIB port, you need to prepare a serial cable to connect RJ-45 terminal 4,5,7 and DB-9 female terminal 5,2,3 respectively. The RJ-45 terminal is connected to the MIB port of the monitor, and the DB-9 female terminal is connected to the PC via USB to Serial Converter.

<img src="images/hw_guide/image10.png" width="450" />

In case of MX400-550 series, communication is possible via the Advanced Interface Card (however, the MX600-800 series must have a MIB board). In this case, note that the Rx and Tx pins are connected differently.

<img src="images/hw_guide/image66.png" width="450" />

Next, you need to change the settings of the patient monitor.

Press the "Main Setup" button on the monitor and select "Operation Modes". Then click "Service".

<img src="images/hw_guide/image90.png" width="450" /><img src="images/hw_guide/image132.png" width="450" />

You must enter a password to enter service mode. The default password is **1345**. If it fails, please contact the manufacturer.

<img src="images/hw_guide/image50.png" width="450" />

Then go back to "Main Setup" and you will see a menu called "Hardware" at the bottom. Press and hold this button and set the communication speed to "Fix 115200" for "Data Export 1" and "Data Export 2".

<img src="images/hw_guide/image7.png" width="450" /><img src="images/hw_guide/image187.png" width="450" />

Then click “Interfaces”,

<img src="images/hw_guide/image112.png" width="450" />

<img src="images/hw_guide/image91.png" width="450" />

Make sure that the driver for port 01a is “DtOut1”. If it is not DtOut1 (e.g. GM or AGM), click the "Change Driver" button at the bottom of the screen and change it to "DtOut1". The number after DtOut may vary depending on the assigned port.

Changes will not take effect until the monitor is turned off and on.

Note) In case of MP2 and X2 monitor, serial communication is not available and data acquisition is not possible.

Lastly, to extract ETCO2 wave, the following steps are required.

Go to “Main Setup” - “Operating Modes” - “Config”.

Password is “71034”.

<img src="images/hw_guide/image153.png" width="450" />

Press the setup button on the IntelliBridge EC10 module.

<img src="images/hw_guide/image124.png" width="450" />\
Enter “Setup Device” at the bottom of the monitor.

<img src="images/hw_guide/image186.png" width="450" /><img src="images/hw_guide/image110.png" width="450" />

Go to “Setup Anesth. Machine” - “Device Driver” - “Setup Waves”. You can add any wave you want with the Add button. Select “CO2”, “AWP”.

(If the wrong wave is generated, delete all of the waves and reset them by pressing the Add button.)

<img src="images/hw_guide/image117.png" width="450" />

Go to “Select to change operating mode” - “Monitoring”.

<img src="images/hw_guide/image141.png" width="450" />

Press “Confirm” button to apply the changes.

## Drager Infinity Kappa

<img src="images/hw_guide/image70.png" width="450" />

This series monitor communicates via module, monitor, or Mini-D cable of X5 or X3 of docking station. Cables can be manufactured as shown below or ordered through distributors. (drager part number 5206441 export protocol cable)

<img src="images/hw_guide/image147.png" width="450" />

In Vital Recorder, communication is possible by adding an Infinity monitor, and most numeric data can be recorded every 2 seconds, but waveform data cannot be extracted.

To extract waveform data, you will need to connect to the X10 Analog/Sync port.

(DRAGER part number 4314618)

<img src="images/hw_guide/image150.png" width="450" />

12: CH1 (+)

13: CH1 (-)

7: CH2 (+)

6: CH2 (-)

## Drager Infinity C500/C700

Infinity C500/ C700 devices do not require additional configuration.

<img src="images/hw_guide/image108.png" width="450" />

<img src="images/hw_guide/image69.png" width="450" />

Numeric data can be extracted from the P2500's RJ10 port.

You need to prepare a serial cable where pins 3, 2, and 4 of the RJ10 connector are connected to pins 2, 3, and 5 of the DB-9 female connector, respectively.

> <img src="images/hw_guide/image105.png" width="450" />
>
> The RJ10 connector connects to the P2500's RJ10 port, and the DB-9 female connector connects to the PC via a USB to Serial Converter.

<img src="images/hw_guide/image148.png" width="450" /><img src="images/hw_guide/image157.png" width="450" />

> To extract waveform data, an Analog sync cable is required. When using the Analog/Sync cable with the Infinity Mcable - Microstream CO2, it connects to the M540 monitor through a Y cable. An MDR14 to RJ45 cable is required to connect the MDR port of the Analog/Sync cable to the ADC. The cables can be manufactured as shown below or ordered through the company. The MDR 14 pin numbers are shown in the photo below. The connector must be purchased separately. (Connector purchase link: [http://www.cableguy.com/shop/mall.php?cat=007002007&query=view&no=210644](http://www.cableguy.com/shop/mall.php?cat=007002007&query=view&no=210644))

<img src="images/hw_guide/image102.png" width="450" />

(Pre-made cable purchase link: [http://www.cableguy.com/shop/mall.php?cat=025015011&query=view&no=209983](http://www.cableguy.com/shop/mall.php?cat=025015011&query=view&no=209983))

## MEKICS MP1300

For wireless connection between MEKICS device and VR, you need to set up a wireless router first. In this manual, we will guide you on how to set up using the iptime wireless router (Other routers are not much different).

### Wireless router settings

<img src="images/hw_guide/image65.png" width="450" />

Connect the power to the router, open Wi-Fi list on your PC, and connect to the AP named iptime-mini.

<img src="images/hw_guide/image156.png" width="450" />

Open a web browser and enter 192.168.0.1 in the address bar to set up the router.

The default Login ID and Password is admin.

<img src="images/hw_guide/image88.png" width="450" />

Click Setup.

<img src="images/hw_guide/image96.png" width="450" />

Go to Advanced Settings - Wireless LAN Management - Wireless Settings/Security menu. Set the network name and password as shown above.

Select ‘WPA2PSK+AES (recommended)’ for the encryption option, uncheck “Broadcast SSID”, and click the Apply button.

The connection to the router will be disconnected since the SSID of the router is changed from iptime_mini to mekics_r7.

<img src="images/hw_guide/image98.png" width="450" />

Connect to a Hidden Network by entering the SSID (“mekics_r7”) and password. The changed SSID would not show up on the Wi-Fi list since “Broadcast SSID” is unchecked from the previous step.

Open a web browser and enter 192.168.0.1 in the address bar to enter the router setting screen.

<img src="images/hw_guide/image149.png" width="450" />

If you plan to connect the router to a higher-level network (Internet or hospital network), perform this step. If not, you can skip it.

Go to Advanced Settings - Wireless LAN Management - Wireless Extension Settings menu.

Set the wireless extension method to wireless WAN and input the hotspot SSID and password of the VR to which the MEKICS device connects.

<img src="images/hw_guide/image131.png" width="450" />

Go to Advanced Settings - System Management - Other Settings menu.

In the wired port function setting, click LAN port and then click the Apply button in the lower right corner.

### MP1300 Settings

<img src="images/hw_guide/image16.png" width="450" />

Connect the router that has been set up with the MP1300 device.

Connect the power supply of the router to the USB port on the back of the device and connect the LAN cable.

<img src="images/hw_guide/image5.png" width="450" />

Select System - Network, then the setting screen will appear as shown above. Set IP and gateway address.

Except the digits after the last period, the rest digits must be the same as the router IP address (192.168.0 as the example above). Choose a random number between 2 and 255 that is not used by other devices for the last digits.

- IP : 192.168.0.***

- Gateway: 192.168.0.1 (IP address of the router)

<img src="images/hw_guide/image59.png" width="450" />

Go to System - Network - Central - Mode and select MP601.

<img src="images/hw_guide/image34.png" width="450" />

On Central settings, enter 192.168.137.1 for Server IP and 6002 for Server Port.

The changed settings will be applied after restarting the device.

<img src="images/hw_guide/image119.png" width="450" />

To add MP1300 on VitalRecorder for Windows, click “Add Device”, choose MEKICS, and set Port 6002.

## Nihon Kohden BSM

(Available in VitalRecorder 1.8.16.2 or later version.)

<img src="images/hw_guide/image193.png" width="450" />

> To obtain data from the BSM monitor, a QI-373P board must be installed. This board has built-in RS-232C serial port and ECG/BP OUT port. To obtain numeric data, connect a "**Null modem (M/F cross gender)**" to the serial port marked in red, then connect a direct serial cable.

ECG and ART waveform data can be acquired through the ECG/BP output port.

> <img src="images/hw_guide/image155.png" width="450" />

To acquire data through the ECG/BP OUT port, an ECG/BP output cable from Nihon Kohden is required.

> <img src="images/hw_guide/image33.png" width="450" />

To input the analog signal from the ECG/BP output cable into an ADC (Analog to Digital Converter), a 5.5pi mono to RJ45 cable must be custom-made.

The pin configuration is shown in the image above.

> <img src="images/hw_guide/image54.png" width="450" />

After connecting the 5.5pi Mono to RJ45 cable to the ADC, you can extract ECG/ART waveform data by connecting the ADC to a PC via a USB cable.

In the image above, the SNUADCM was used.

# Anesthesia machines

## Drager Apollo, Cicero EM Color, Julian, Primus, Vamos

The Apollo, Cicero EM Color, Julian, Primus, and Vamos devices do not require any additional configuration. Simply connect the direct serial cable to the COM1 port on the rear panel like the following picture.

<img src="images/hw_guide/image97.png" width="450" />

> If the anesthesia machine is not connected to the patient monitor, no further setup is required. If the anesthesia machine is already connected to the patient monitor, please refer to the section "When COM1 port is already in use."

## Drager Fabius, Zeus, Infinity

The Fabius GS, Fabius Tiro, Infinity Evita V500, and Zeus devices require a null modem (cross-gender) to be connected in between.

Additionally, for the Fabius devices, you need to press the three buttons marked with a red circle in the image simultaneously to enter service mode and change the serial communication settings.

<img src="images/hw_guide/image121.png" width="450" /><img src="images/hw_guide/image185.png" width="450" />

##

## Drager Perseus

For the Perseus, connect a "null modem (F/F cross-gender)" adapter first, then connect the direct serial cable.

<img src="images/hw_guide/image95.png" width="450" />

Enter service mode by selecting System Settings > System Menu. The password is 0000.

<img src="images/hw_guide/image43.png" width="450" />

Then, select the Interface Configuration menu.

<img src="images/hw_guide/image44.png" width="450" />

For either COM1 or COM2—whichever port is connected—set the protocol to MEDIBUS and the baud rate to 9600.

<img src="images/hw_guide/image115.png" width="450" />

##

## When the COM1 port is already in use

If the Drager COM1 port is already used to transmit information such as CO2 curve, airway pressure curve, etc., from the anesthesia machine to the patient monitor, the following Y-cable for data peeping should be made and used to extract information without disturbing the existing data communication. In this case, you must select the "Read only mode" option when adding a device in the Vital Recorder program.

<img src="images/hw_guide/image87.png" width="450" />For the Atlan Anesthesia machine, a cross-gender adapter matching the connector shape must be attached on both the anesthesia machine side and the CON1 side of the cable. The CON2 port used for data reading can be used as is.

Drager DB9F —-- F/F Cross gender — DB9M —---------- CON1 (DB9F) —--- M/F Cross gender

## GE Datex-Ohmeda Anesthesia Machine

The Datex-Ohmeda anesthesia machine is connected using the 15-pin connector (Female) that comes out when you open the back cover. The 15-pin connector has the same height as the 9-pin connector used for typical serial communications, but it is longer.

<img src="images/hw_guide/image170.png" width="450" />

Since the usual Serial To USB connector has a 9 pin male port, we need to make a cable that changes it to a 15 pin male connector.

<img src="images/hw_guide/image77.png" width="450" />

If the anesthesia machine is not connected to the patient monitor, no further setup is required.

However, if the Datex-Ohmeda 15 pin port is already used to transmit information such as CO2 curve, airway pressure curve, etc., from the anesthesia machine to the patient monitor, the following Y-cable for data peeping should be made and used to extract information without disturbing the existing data communication. In this case, you must select the "Read only mode" option when adding a device in the Vital Recorder program.

<img src="images/hw_guide/image55.png" width="450" />

Note: This protocol is called the GE Ohmeda Serial protocol and is used by Aespire, Aespire View, Aestiva, Avance, Avance CS2, Aisys, Aisys CS2 and Carestation 620/650/650c.

## Maquet Flow-i

The Flow-i does not require any additional configuration on the device.

<img src="images/hw_guide/image176.png" width="450" />

For Flow-i, connect “Null modem (M/F cross gender)” and a direct serial cable to the serial port on the lower right side of the back of the device. (Available in Vital Recorder 1.8.16.0 or later version.)

##

## Maquet Servo-i Ventilator

No additional settings are required on the Servo-i device. The Servo-i has two RS-232 ports. Connect to the RS-232 port on the “BOTTOM” of these using a Null modem(M/F cross gender).

If the port is preoccupied with another device such as a patient monitor, data collection is not possible. (It cannot be done on the “TOP” RS-232 port because it is a debugging port) In this case, data must be transmitted through the patient monitor. (For example, Maquet Servo-i → Philips Intellivue → Vital Recorder)

<img src="images/hw_guide/image23.png" width="450" />

## Hamilton G5 Ventilator

<img src="images/hw_guide/image79.png" width="450" /><img src="images/hw_guide/image172.jpg" width="450" /><img src="images/hw_guide/image14.png" width="450" />

> Hamilton G5 is supported on version 1.10.2 or later.
>
> The Hamilton G5 device has two RS-232 ports on the back: Monitoring Interface 1 and Monitoring Interface 2. You can connect to either of these ports. Use a null modem (M/F cross gender) and a direct serial cable for the connection. After connecting the cable to the port, you need to enter configuration mode and change the serial settings.
>
> <img src="images/hw_guide/image76.png" width="450" />

You can enter Configuration mode when the device is not operating.

> <img src="images/hw_guide/image83.png" width="450" />Press these two buttons simultaneously, and the configuration menu will appear at the bottom left corner of the screen.
>
> <img src="images/hw_guide/image198.png" width="450" />
>
> To apply the changes, you need to activate Test mode. <img src="images/hw_guide/image160.png" width="450" /> Press these two buttons simultaneously to activate Test mode.

<img src="images/hw_guide/image113.png" width="450" />

> Once Test mode is activated, navigate to the Configuration → Interface menu.Change the port (COM1 or COM2) that is connected to the Vital Recorder to the Block protocol. Then, press the Close and Close/Save buttons in order to apply the settings.

# Cardiac monitors

## Edwards Lifesciences EV-1000

All of Edwards Lifesciences' equipments have the same settings. However, the location of the serial port and the menu configuration may vary depending on the device. Please follow the guidance below to set up your device accordingly.

When connecting the products of Edwards Lifesciences (Vigileo, EV1000A, Vigilance, Vigilance II, Hemosphere, etc) all should be connected using **"Null modem(M/F cross gender)"**. However, old models of EV1000 have different terminals and must be connected using **"Null modem(F/F cross gender)"**.

Let’s start with EV-1000 old model. Connect **"Null modem(F/F cross gender)"** and direct serial cable to the second port on the right.

<img src="images/hw_guide/image103.png" width="450" />

The new model (1000A) is shown below. Connect using **"Null modem(M/F cross gender)"**.

<img src="images/hw_guide/image57.png" width="450" />

The settings on the device are as follows.

<img src="images/hw_guide/image58.png" width="450" />

Select “Settings” button.

<img src="images/hw_guide/image197.png" width="450" />

Select “Monitor Settings”.

<img src="images/hw_guide/image39.png" width="450" />

Select “Serial Port Setup”.

<img src="images/hw_guide/image45.png" width="450" />

Set "Device" to "IFMout".

<img src="images/hw_guide/image100.png" width="450" />

Set "Baud Rate" to "9600".

## Edwards Lifesciences Vigilance

There are two serial ports on the back panel of the Vigilance. This will be explained based on the use of COM1 (either COM1 or COM2 can be used depending on the system configuration). Similar to other Edwards Lifesciences products, connect the **“Null modem(M/F cross gender)”** and then the serial cable.

<img src="images/hw_guide/image26.png" width="450" />

<img src="images/hw_guide/image73.png" width="450" />

Press “Setup” button.

<img src="images/hw_guide/image194.png" width="450" />

Select “System Config”.

<img src="images/hw_guide/image162.png" width="450" />

Select “Return”.

<img src="images/hw_guide/image192.png" width="450" />

Select “Digital Ports”.

<img src="images/hw_guide/image138.png" width="450" />

If you have decided to use COM1 port in advance, change its settings as shown below.

Device : IFMout

Baud Rate : 9600

Parity : None

Stop Bits : 1

Data Bits : 8

Flow Control : 2 seconds

## Edwards Lifesciences Vigilance II

<img src="images/hw_guide/image114.png" width="450" />

Connect the **“Null modem(M/F cross gender)”** to port 1 on the top of the two serial ports on the back of the monitor and connect the serial cable.

<img src="images/hw_guide/image81.png" width="450" />

Press “Setup” button.

<img src="images/hw_guide/image38.png" width="450" />

Select “Serial Port Setup”.

<img src="images/hw_guide/image29.png" width="450" />

Select “Port 1”.

<img src="images/hw_guide/image130.png" width="450" />

Set "Device" to "IFMout" and "Baud Rate" to "9600".

## Edwards Lifesciences Vigileo

<img src="images/hw_guide/image158.png" width="450" />

There is one serial port on the back. Connect **“Null modem(M/F cross gender)”** and connect the serial cable.

<img src="images/hw_guide/image106.png" width="450" />

Selecting an empty space at the bottom left of the screen will enter the setup menu.

<img src="images/hw_guide/image62.png" width="450" />

Select “Serial Port Setup”.

<img src="images/hw_guide/image64.png" width="450" />

Select "IFMout" in "Device".

<img src="images/hw_guide/image11.png" width="450" />

Select "9600" in "Baud Rate".

Select "Return" and exit.

## Edwards Lifesciences Hemosphere

<img src="images/hw_guide/image174.png" width="450" />

Connect **“Null modem(M/F cross gender)”** and a direct serial cable to the serial port on the back of the device.

<img src="images/hw_guide/image24.png" width="450" />

Press the setup button at the bottom left of the monitor.<img src="images/hw_guide/image27.png" width="450" />

Press “Advanced Setup” button.

<img src="images/hw_guide/image179.png" width="450" />

The default password for the Advanced setup is “55555555”.

<img src="images/hw_guide/image133.png" width="450" />

Press “Connectivity”.

<img src="images/hw_guide/image35.png" width="450" />

Press “Serial Port Setup”.

<img src="images/hw_guide/image168.png" width="450" />

Select “IFMout” for Device and 9600 for Baud Rate. Restart the device to apply the changed settings (Available on Vital Recorder 1.8.16.4 or later).

## Deltex CardioQ

You can not adjust the settings while using the device, so you need to set it up before applying it to the patient. When the setting is completed, you can check whether data is being transferred through the DEMO mode.

There is one Male-type serial port on the back. Connect **“Null modem(F/F cross gender)”** and connect the serial cable.

<img src="images/hw_guide/image125.png" width="450" />

At boot time, click General> Patient monitors> Monitor Setup, then select CardioQ Serial Protocol v2. After confirming that Baud Rate is set to 57600, No Flow Control (if not, change it) and press the Finished button to exit.

<img src="images/hw_guide/image177.png" width="450" />

<img src="images/hw_guide/image123.png" width="450" />

<img src="images/hw_guide/image182.png" width="450" />

<img src="images/hw_guide/image189.png" width="450" />

## LiDCO

There is one serial port on the back.Connect **“Null modem (M/F cross gender)”** and a direct serial cable to the serial port on the back of the device.

<img src="images/hw_guide/image86.png" width="450" />

Set as shown below.

Settings > Communications > Serial > LiDCOserial Enabled

Baud rate 57600, Stop Bits 1, Data bits 8, Parity None (defaults)

Average Never, Observation beat-to-beat.

<img src="images/hw_guide/image183.png" width="450" />

# Infusion pumps

## Fresenius Vial Orchestra (Base Primea with Module DPS)

It is somewhat complicated, so please follow along.

<img src="images/hw_guide/image78.png" width="450" />

First turn off the power and turn on the power by pressing the three buttons (the top blue button, the mute button, the power button) at the same time indicated by the red circle.

<img src="images/hw_guide/image40.png" width="450" />

Press the fourth blue button above to select "Serial & ...".

<img src="images/hw_guide/image169.png" width="450" />

In the "SERIAL PORTS" item, select the second "COM NEW SUP" from the upper right (select by turning the jog dial).

Select "3" after the selection.

Uncheck "Send a frame on every change" of "COMM NEW SUP" on the bottom right and select 1s under "Send every" below.

Press the power button to turn off the power. Then press the power button again to turn on the power.

<img src="images/hw_guide/image68.png" width="450" />

When the power is on, press the "OPT" button on the bottom right.

<img src="images/hw_guide/image94.png" width="450" />

Select "CUSTOMIZATION".

<img src="images/hw_guide/image52.png" width="450" />

Turn the jog dial clockwise until "CODE" is selected.

When you are ready to enter the code, enter "00123" using the jog dial.

<img src="images/hw_guide/image2.png" width="450" />

You can now select "SERIAL PORTS AND PRINTER".

Rotate the jog dial to select it.

<img src="images/hw_guide/image46.png" width="450" />

Select "RS-232-3" and then "IDMS".

<img src="images/hw_guide/image167.png" width="450" />

After confirming that the RS 232-3 port is set to IDMS, save and exit.

If any changes are made, they will not take effect until you turn them off again.

<img src="images/hw_guide/image60.png" width="450" />

There are several terminals on the right side of the Base Primea (bottom of the Orchestra). We will use the RS 232-3 port on the right end of the three serial ports. Connect **“M/F cross gender”** here and connect a direct serial cable.

## Fresenius Kabi Agilia

Fresenius Kabi Agilia requires its own cable that can be purchased by contacting Fresenius Kabi, and the price is about 130,000 won.

The other side of the cable is DB9 female, so you can connect it with a general USB Serial cable (DB9 male) without a gender.

<img src="images/hw_guide/image127.png" width="450" />

## BBraun SpaceCom

<img src="images/hw_guide/image61.png" width="450" />

A apecial cable is required.Parts can be purchased and manufactured.

Make a cable that connects No. 2, No. 3, and No. 5 of 9-pin mini DIN terminal to No. 3, No. 2, and No. 5 of Female 9-pin DSUB terminal.

Then you need to change your SpaceCom settings.

SpaceCom provides a web interface (SpaceOnline) for configuration changes. Connect the SpaceCom to your computer with a direct LAN cable to access the web interface. The default IP setting for SpaceCom is 192.168.100.41. Therefore, set the computer IP address to 192.168.100.42 (subnet mask 255.255.255.0 gateway 192.168.100.1). Open a web browser and enter the address 192.168.100.41 to access the web interface. Enter the Configuration menu. The initial user name and password are config, config, respectively.

<img src="images/hw_guide/image142.png" width="450" />

Enter the BCC Protocol settings submenu and make the settings as shown below.

<img src="images/hw_guide/image49.png" width="450" /><img src="images/hw_guide/image180.png" width="450" /><img src="images/hw_guide/image75.png" width="450" />

Click the Save button to save your changes.

## Bionet Pion TCI

The device communicates through the 9-pin port on the back side, and it requires a direct serial cable.\
<img src="images/hw_guide/image4.png" width="450" />

There may be cases where multiple Pion pumps are connected to one VitalRecorder at the same time. VitalRecorder recognizes the first number of Pion pump's equipment name (can be specified when adding device on ViterRecorder) and reflects it in the track name. For example, if the device name is Pion2, the data obtained from it is prefixed with PUMP2. If there is no number, it becomes PUMP1.

<img src="images/hw_guide/image175.png" width="450" />

## Belmont FMS (RI-2)

The communication port is hidden by the lower vent.

#### <img src="images/hw_guide/image32.png" width="450" />

Since the equipment has a male connector, use **“F/F cross gender”** and direct serial cable.

# Cerebral monitors

## Medtronic BIS VISTA

<img src="images/hw_guide/image120.png" width="450" />

Press Menu.

<img src="images/hw_guide/image173.png" width="450" />

Press "NEXT".

<img src="images/hw_guide/image195.png" width="450" />

Press "NEXT" again.

<img src="images/hw_guide/image85.png" width="450" />

Select “Maintenance”.

<img src="images/hw_guide/image56.png" width="450" />

Select “Serial Protocol”.

<img src="images/hw_guide/image118.png" width="450" />

If you select "ASCII", you can get all the numerical data generated by the BIS monitor.

<img src="images/hw_guide/image72.png" width="450" />

You can get a 128Hz EEG wave by selecting "Legacy Binary" and selecting the BIS (binary) option in the Vital Recorder program. When the setting is finished, save and return to Home.

* NOTE**:** The protocol change will only take effect after the device is restarted, so please restart the BIS device.

<img src="images/hw_guide/image9.png" width="450" />

You can see the serial port on the back of the device. Connect a direct serial cable here. If you connect the cross cable by mistake, you will see the following screen.

<img src="images/hw_guide/image30.png" width="450" />

## Medtronic BIS A2000

Medtronic BIS A2000 is similar to BIS Vista, but BIS A2000 can obtain 2-channel 256Hz EEG.

<img src="images/hw_guide/image12.png" width="450" />

Connect a direct cable to the 9-pin port on the back of the device, and the setup method is as follows:

<img src="images/hw_guide/image99.png" width="450" />

Press the menu button and select Advanced Setup.

<img src="images/hw_guide/image163.png" width="450" />

Press Diagnostic Menu.

<img src="images/hw_guide/image74.png" width="450" />

Press System Configuration Menu.

<img src="images/hw_guide/image178.png" width="450" />

On Serial Port Protocol, choose Binary and press “Return To Diagnostic Menu” - “Return to Advanced Setup Menu”

\- “Save Settings”.

## Medtronic INVOS Cerebral/Somatic Oximetry

Connect the cable to the \|O\|O\| port on the back of the device. Since the RS-232 port of INVOS is a male terminal, **“F/F cross gender”** should be used.

<img src="images/hw_guide/image67.png" width="450" />

<img src="images/hw_guide/image15.png" width="450" />

You need to go to the next screen to open the settings window. Press the Next Menu button.

<img src="images/hw_guide/image104.png" width="450" />

Press “Output Select”.

<img src="images/hw_guide/image71.png" width="450" />

Press “Digital Output”.

<img src="images/hw_guide/image47.png" width="450" />

Press “PC Link”.

<img src="images/hw_guide/image152.png" width="450" />

Press “OUTPUT FORMAT 1” and finish the setting.

# Multifunction monitors

## Masimo Radical7

This device extracts real-time SpO₂, HR, and PI data, as well as digital waveforms, through the P1 (RS-232) port on the rear panel of the Docking Station. The plethysmographic waveform is provided via the P2 analog port. A direct male cable is required for connection. If using a Serial to USB converter, it can be connected directly without a gender adapter.

<img src="images/hw_guide/image143.png" width="450" />

Start with Device setup.

<img src="images/hw_guide/image145.png" width="450" />

Go to Device Settings from the main menu.

<img src="images/hw_guide/image116.png" width="450" />

Swipe to the right and touch “Device output”.

<img src="images/hw_guide/image151.png" width="450" />

Set ASCII 1 for serial, and Pleth for analog 1 and analog 2.

<img src="images/hw_guide/image166.png" width="450" />

Swipe down and set 9600 the docking station baud rate.

## Masimo ROOT

This equipment requires setting on the device first.

<img src="images/hw_guide/image129.png" width="450" />

From the main menu, enter DEVICE SETTINGS.

<img src="images/hw_guide/image164.png" width="450" />

Swipe right and touch ACCESS CONTROL.

<img src="images/hw_guide/image13.png" width="450" />

When the password entry screen appears, enter "6274".

<img src="images/hw_guide/image188.png" width="450" /><img src="images/hw_guide/image42.png" width="450" />

When entering access control, change both USB Port 1 baudrate and USB Port 2 baudrate to 19200.

<img src="images/hw_guide/image19.png" width="450" />

Go to the previous screen and change the output protocol of the device. Touch DEVICE OUTPUT.

<img src="images/hw_guide/image82.png" width="450" />

Change both USB Port 1 and USB Port 2 to ASCII 1.

Your changes will take effect only after you reboot the device.

Turn off the power by pressing the power button on the bottom right of the ROOT for more than 8 seconds, then press the power button again to turn on the equipment.

When you finish the setting, then connect the cable.

Masimo's data acquisition USB cable makes it easy to connect. Plug the cable into the USB1 or USB2 port on the back of the ROOT and connect the other end to the PC.

<img src="images/hw_guide/image146.png" width="450" />

A new USB serial COM port is created on your PC. On the Vital Recorder, click the Add device button to add the ROOT and specify the newly created COM port.

If you do not use Masimo USB cable, use USB to serial converter and “Null modem (F/F cross gender)”.

(ROOT USB1 or 2 - USB to serial - null modem(F/F cross gender) - serial to USB - PC USB port )

As above, add ROOT from Vital Recorder and assign it to the USB serial COM port.

<img src="images/hw_guide/image53.png" width="450" /> <img src="images/hw_guide/image6.png" width="450" />

When all the processes are completed, the data is recorded as shown below.

If you have problems such as missing part of data, try rebooting 2 or 3 more times or changing the USB port.

<img src="images/hw_guide/image171.png" width="450" />

* NOTE 1

Most USB-serial converters are not recognized properly in ROOT. Only the following products that we have identified work properly.

- NEXT USB 2.0 to SERIAL converter 1 port [NEXT-RS232U20] [**http://cableguy.com/shop/mall.php?cat=005004001&query=view&no=6028**](http://cableguy.com/shop/mall.php?cat=005004001&query=view&no=6028)

** NOTE 2

To get Rainbow Sensor data, you first need to turn on Radical-7 and turn on ROOT later. If only ROOT is on, turn off ROOT, then turn on Radical-7, and finally turn on ROOT. Therefore, we recommend "always turn-on Radical-7" to get data without any mistakes.

To connect with PiVR device using a connector, you need to set it like below.

> <img src="images/hw_guide/image129.png" width="450" />

Go to Device Settings from the main menu.

> <img src="images/hw_guide/image92.png" width="450" />
>
> Swipe right and touch “ETHERNET”.
>
> <img src="images/hw_guide/image3.png" width="450" />
>
> Touch ethernet ON button on the top of the ethernet setting screen for activation.
>
> <img src="images/hw_guide/image111.png" width="450" />
>
> Connect LAN cable to LAN port on the rear side of the ROOT device and LAN port of PiVR.

## Sentec: SDM

Sentec SDM requires a USB Serial Converter to extract data. The converter must be connected to the serial port on the back.

<img src="images/hw_guide/image80.png" width="450" />

Go to Interfaces - Serial Interface, and set SenTecLink for Protocol and 115200 for Baud Rate.

<img src="images/hw_guide/image93.png" width="450" />

##

## MDMS ANI Monitor V2

<img src="images/hw_guide/image84.jpg" width="450" />

After installing the sensor, press New patient menu and wait for about a minute, then the above screen will appear.

<img src="images/hw_guide/image25.png" width="450" />

<img src="images/hw_guide/image137.jpg" width="450" />

Connect the USB to Serial Converter ( NEXT USB 2.0 to SERIAL converter 1 port [NEXT-RS232U20] ) to the serial port on the right side of the device.

## GE: Corometrics 170

<img src="images/hw_guide/image135.png" width="450" /><img src="images/hw_guide/image89.png" width="450" />

To enter the monitor’s setup mode, press and hold the setup button (the clock and calendar icon) while pressing the power button. You must continue holding the setup button during the entire setup process.

<img src="images/hw_guide/image190.png" width="450" />

You can use the UA reference button to activate the settings for the FHR display or UA display.

You need to change the communication mode and baud rate settings. For the communication mode, set it to 30 or 31 on the FHR display and to 115 (5 on the UA display). For the baud rate settings, set it to 40 or 41 on the FHR display and to 9600 (96 on the UA display). You can change these numbers using the volume button.

- When connecting to RS232 port 1 :\
  FHR display (30) : UA display (5), FHR display (40) : UA display (96)

- When connecting to RS232 port 2 :\
  FHR display (31) : UA display(5), FHR display (41) : UA display (96)

# Neuromuscular monitors

## BlinkDC: TwitchView

When the Monitor is docked in the Charging Station, data is output via RJ45 connector at the bottom of the device. The appropriate TwitchView output format can be selected by entering a configuration code, which will bring up the following menu:

> <img src="images/hw_guide/image159.png" width="450" />
>
> <img src="images/hw_guide/image199.png" width="450" />
>
> Touch Clock - SET.
>
> <img src="images/hw_guide/image200.png" width="450" />
>
> Change the clock to Hour 1AM, Minute 2, Month March, Day 4, Year 2018, and touch the Set button.
>
> <img src="images/hw_guide/image51.png" width="450" />
>
> Select Serial and touch the Set button to change the setting.

To use a typical USB-to-serial converter, you must make the following connection cables.

> <img src="images/hw_guide/image122.png" width="450" />

## IDMed TOFscan

<img src="images/hw_guide/image184.png" width="450" /><img src="images/hw_guide/image134.png" width="450" />

TOFscan requires TOF-RS1 (you can purchase this from IDMed). Connect TOF-RS1 cable directly to the USB-Serial-Converter without a gender.

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
