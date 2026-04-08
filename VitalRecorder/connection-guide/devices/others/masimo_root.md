# Masimo ROOT

<!-- meta
category: Other
manufacturer: Masimo
-->

This equipment requires setting on the device first.

<img src="../hardware_images/image129.png" width="450" />

From the main menu, enter DEVICE SETTINGS.

<img src="../hardware_images/image164.png" width="450" />

Swipe right and touch ACCESS CONTROL.

<img src="../hardware_images/image13.png" width="450" />

When the password entry screen appears, enter "6274".

<img src="../hardware_images/image188.png" width="450" /><img src="../hardware_images/image42.png" width="450" />

When entering access control, change both USB Port 1 baudrate and USB Port 2 baudrate to 19200.

<img src="../hardware_images/image19.png" width="450" />

Go to the previous screen and change the output protocol of the device. Touch DEVICE OUTPUT.

<img src="../hardware_images/image82.png" width="450" />

Change both USB Port 1 and USB Port 2 to ASCII 1.

Your changes will take effect only after you reboot the device.

Turn off the power by pressing the power button on the bottom right of the ROOT for more than 8 seconds, then press the power button again to turn on the equipment.

When you finish the setting, then connect the cable.

Masimo's data acquisition USB cable makes it easy to connect. Plug the cable into the USB1 or USB2 port on the back of the ROOT and connect the other end to the PC.

<img src="../hardware_images/image146.png" width="450" />

A new USB serial COM port is created on your PC. On the Vital Recorder, click the Add device button to add the ROOT and specify the newly created COM port.

If you do not use Masimo USB cable, use USB to serial converter and “Null modem (F/F cross gender)”.

(ROOT USB1 or 2 - USB to serial - null modem(F/F cross gender) - serial to USB - PC USB port )

As above, add ROOT from Vital Recorder and assign it to the USB serial COM port.

<img src="../hardware_images/image53.png" width="450" /> <img src="../hardware_images/image6.png" width="450" />

When all the processes are completed, the data is recorded as shown below.

If you have problems such as missing part of data, try rebooting 2 or 3 more times or changing the USB port.

<img src="../hardware_images/image171.png" width="450" />

* NOTE 1

Most USB-serial converters are not recognized properly in ROOT. Only the following products that we have identified work properly.

- NEXT USB 2.0 to SERIAL converter 1 port [NEXT-RS232U20] [**http://cableguy.com/shop/mall.php?cat=005004001&query=view&no=6028**](http://cableguy.com/shop/mall.php?cat=005004001&query=view&no=6028)

** NOTE 2

To get Rainbow Sensor data, you first need to turn on Radical-7 and turn on ROOT later. If only ROOT is on, turn off ROOT, then turn on Radical-7, and finally turn on ROOT. Therefore, we recommend "always turn-on Radical-7" to get data without any mistakes.

To connect with PiVR device using a connector, you need to set it like below.

> <img src="../hardware_images/image129.png" width="450" />

Go to Device Settings from the main menu.

> <img src="../hardware_images/image92.png" width="450" />
>
> Swipe right and touch “ETHERNET”.
>
> <img src="../hardware_images/image3.png" width="450" />
>
> Touch ethernet ON button on the top of the ethernet setting screen for activation.
>
> <img src="../hardware_images/image111.png" width="450" />
>
> Connect LAN cable to LAN port on the rear side of the ROOT device and LAN port of PiVR.
