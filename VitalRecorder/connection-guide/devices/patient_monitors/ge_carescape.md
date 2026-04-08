# GE CARESCAPE B850, B650, B450

<!-- meta
category: Patient Monitor
manufacturer: GE
-->

Note : This protocol is called the **GE S5 Computer Interface** and is used to connect with GE B850/650/450 monitors and B40/20, Datex-Ohmeda S/5 monitors through this interface. GE S5 Computer Interface is a communication protocol used by an old data collection program from GE (S5 collect). The GE B40 (9 pin cable with pin 4 removed) and the Datex-Ohmeda S/5 monitor (using female-female null modem gender only) communicate with the same protocol.

The version of your monitor can be checked under Monitor setup > defaults&service > service.

If your monitor is a CARESCAPE **B850, B650, B450,** it can be connected if the monitor version is 3.1 or higher, and requires a Startech ICUSB232V2 USB to RS232 converter. ([https://www.amazon.ca/dp/B00GRP8EZU/ref=redir_mobile_desktop/146-2308166-9887501?\_encoding=UTF8&ref\_=ya_aw_od_pi&th=1](https://www.amazon.ca/dp/B00GRP8EZU/ref=redir_mobile_desktop/146-2308166-9887501?_encoding=UTF8&ref_=ya_aw_od_pi&th=1))

For CARESCAPE **Bx50 v2**, only the legacy ATEN UC232A cable (with serial numbers starting with Z3L1 or later alphabetically) is compatible, but this cable is currently discontinued and unavailable.

Connect this converter cable mentioned above to the USB port on the back of the equipment. It can be plugged into any of the four USB ports*(circled in red on the diagram below)* on the back of the monitor.

<img src="../hardware_images/image22.png" width="450" />

Then, connect to the PC's serial port (or a common USB serial converter) through a "**Null modem (F/F cross gender)" cable**. If you are using VRZero, the USB cable connecting to VRZero must be a product that supports handshaking.

<img src="../hardware_images/image31.png" width="450" />

[Kangwon Electronics] NETmate USB 2.0 to RS232 Converter Cable, 0.45M [KW-525] [http://www.compuzone.co.kr/product/product_detail.htm?ProductNo=374732&BigDivNo=&MediumDivNo=1139&DivNo=2659](http://www.compuzone.co.kr/product/product_detail.htm?ProductNo=374732&BigDivNo=&MediumDivNo=1139&DivNo=2659)

[ATEN] USB 1.1 to RS232 Converter Cable, 0.35M [UC232A] [http://www.compuzone.co.kr/product/product_detail.htm?ProductNo=60189&BigDivNo=&MediumDivNo=1139&DivNo=2659](http://www.compuzone.co.kr/product/product_detail.htm?ProductNo=60189&BigDivNo=&MediumDivNo=1139&DivNo=2659)
