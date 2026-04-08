# Nihon Kohden BSM

<!-- meta
category: Patient Monitor
manufacturer: Nihon Kohden
-->

(Available in VitalRecorder 1.8.16.2 or later version.)

<img src="../hardware_images/image193.png" width="450" />

> To obtain data from the BSM monitor, a QI-373P board must be installed. This board has built-in RS-232C serial port and ECG/BP OUT port. To obtain numeric data, connect a "**Null modem (M/F cross gender)**" to the serial port marked in red, then connect a direct serial cable.

ECG and ART waveform data can be acquired through the ECG/BP output port.

> <img src="../hardware_images/image155.png" width="450" />

To acquire data through the ECG/BP OUT port, an ECG/BP output cable from Nihon Kohden is required.

> <img src="../hardware_images/image33.png" width="450" />

To input the analog signal from the ECG/BP output cable into an ADC (Analog to Digital Converter), a 5.5pi mono to RJ45 cable must be custom-made.

The pin configuration is shown in the image above.

> <img src="../hardware_images/image54.png" width="450" />

After connecting the 5.5pi Mono to RJ45 cable to the ADC, you can extract ECG/ART waveform data by connecting the ADC to a PC via a USB cable.

In the image above, the SNUADCM was used.
