# Philips Intellivue MP/MX series

<!-- meta
category: Patient Monitor
manufacturer: Philips
-->

The Philips Intellivue patient monitor is capable of serial communication via a MIB port that looks like a LAN port. It does not matter whether it is connected to a central monitor or not.

<img src="../hardware_images/image128.png" width="450" />

There are several types of MIB ports as shown below. Please note that labels vary depending on the model.

<img src="../hardware_images/image165.png" width="450" />

To connect via MIB port, you need to prepare a serial cable to connect RJ-45 terminal 4,5,7 and DB-9 female terminal 5,2,3 respectively. The RJ-45 terminal is connected to the MIB port of the monitor, and the DB-9 female terminal is connected to the PC via USB to Serial Converter.

<img src="../hardware_images/image10.png" width="450" />

In case of MX400-550 series, communication is possible via the Advanced Interface Card (however, the MX600-800 series must have a MIB board). In this case, note that the Rx and Tx pins are connected differently.

<img src="../hardware_images/image66.png" width="450" />

Next, you need to change the settings of the patient monitor.

Press the "Main Setup" button on the monitor and select "Operation Modes". Then click "Service".

<img src="../hardware_images/image90.png" width="450" /><img src="../hardware_images/image132.png" width="450" />

You must enter a password to enter service mode. The default password is **1345**. If it fails, please contact the manufacturer.

<img src="../hardware_images/image50.png" width="450" />

Then go back to "Main Setup" and you will see a menu called "Hardware" at the bottom. Press and hold this button and set the communication speed to "Fix 115200" for "Data Export 1" and "Data Export 2".

<img src="../hardware_images/image7.png" width="450" /><img src="../hardware_images/image187.png" width="450" />

Then click “Interfaces”,

<img src="../hardware_images/image112.png" width="450" />

<img src="../hardware_images/image91.png" width="450" />

Make sure that the driver for port 01a is “DtOut1”. If it is not DtOut1 (e.g. GM or AGM), click the "Change Driver" button at the bottom of the screen and change it to "DtOut1". The number after DtOut may vary depending on the assigned port.

Changes will not take effect until the monitor is turned off and on.

Note) In case of MP2 and X2 monitor, serial communication is not available and data acquisition is not possible.

Lastly, to extract ETCO2 wave, the following steps are required.

Go to “Main Setup” - “Operating Modes” - “Config”.

Password is “71034”.

<img src="../hardware_images/image153.png" width="450" />

Press the setup button on the IntelliBridge EC10 module.

<img src="../hardware_images/image124.png" width="450" />\
Enter “Setup Device” at the bottom of the monitor.

<img src="../hardware_images/image186.png" width="450" /><img src="../hardware_images/image110.png" width="450" />

Go to “Setup Anesth. Machine” - “Device Driver” - “Setup Waves”. You can add any wave you want with the Add button. Select “CO2”, “AWP”.

(If the wrong wave is generated, delete all of the waves and reset them by pressing the Add button.)

<img src="../hardware_images/image117.png" width="450" />

Go to “Select to change operating mode” - “Monitoring”.

<img src="../hardware_images/image141.png" width="450" />

Press “Confirm” button to apply the changes.
