# GE TRAM-RAC 4A

<!-- meta
category: Patient Monitor
manufacturer: GE
-->

Waveform data such as ECG and arterial pressure can only be received through the 15-pin ANALOG OUT connector located at the back of the GE monitor's Tram-RAC 4A (device for inserting multiple modules).

<img src="../hardware_images/image18.png" width="450" />

This port is not a digital port for the transmission of numerical values, but an analog port that outputs the waveform change as a voltage value. Since the voltage value of the analog port can not be read directly from the computer, it needs an equipment called an analog-to-digital converter (ADC) which converts it to digital.

ADCs range in variety, from low-cost products in the $ 50 range to high-performance products in the thousands of dollars. Currently tested equipment is DataQ's DI-149 and DI-155, which are the cheapest but show sufficient performance for research purposes. The most significant difference between the two products is the difference in voltage resolution. For general monitoring purposes, the cheaper DI-149 is sufficient, but DI-155 is recommended for analyzing T-wave or P-waves in electrocardiograms ([http://www.dataq.com/products](http://www.dataq.com/products/di-149/)).

After purchasing the ADC, you must create a cable to feed the voltage output from the ANALOG OUT port of the GE TRAM RAC into the ADC input. You can also make this cable yourself, but you can leave it to the cable manufacturer. At the time of order, you should ask for production as below. When placing an order, request manufacturing with the pins connected as shown below.

This shows the cable custom-ordered from [http://www.cableguy.com/](http://www.cableguy.com/) connected to the DI-149.

<img src="../hardware_images/image17.png" width="450" />

When using DataQ's DI-149 according to the above method, additional costs for customs clearance and shipping are incurred, plus you need to separately order a 15-pin adapter to connect to the analog channels, resulting in a final cost of approximately 100,000-200,000 KRW per unit.

Newer DataQ analog-to-digital converters such as the DI-1110 can operate in two modes (libusb mode and CDC mode). Among these, Vital Recorder can only recognize the device when operating in CDC mode, so to use these devices, please change the device mode according to the manufacturer's manual below: [https://www.dataq.com/blog/data-acquisition/usb-daq-products-support-libusb-cdc](https://www.dataq.com/blog/data-acquisition/usb-daq-products-support-libusb-cdc)

To address these cost issues and enable anyone to acquire data affordably, we have independently designed and manufactured a device called SNU-ADC. The SNU-ADC not only has 8-channel ADC functionality but also allows connection of wired/wireless push buttons for inserting event markers.

> <img src="../hardware_images/image41.png" width="450" />

An important point to note is that you must connect the cable to the specified connector on the TRAM RAC module to receive the waveform signal correctly. Regardless of which ADC is used, the cable must not be connected to the BP connector (BP2, second left connector) to receive the PLETH waveform from the TRAM RAC. If a cable such as CVP is plugged into BP2, BP2 will be recorded instead of PLETH. PLETH and BP's waves look similar, so it's hard to notice when they're connected incorrectly. The figure below shows this incorrect connection. CVP is recorded to the PLETH channel and CVP is not displayed properly.

<img src="../hardware_images/image139.png" width="450" />

| <img src="../hardware_images/image21.png" width="450" /> | <img src="../hardware_images/image196.png" width="450" /> |
|----|----|
| Wrong connection: The CVP Transducer cable is connected from the left to the second BP connector (BP2) | Correct connection: The CVP transducer cable is connected from the left to the third BP connector (BP3) |

<img src="../hardware_images/image107.png" width="450" />

Additionally, when monitoring ICP, the ICP must be plugged into the first slot in the TRAM RAC.
