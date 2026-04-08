# GE Datex-Ohmeda Anesthesia Machine

<!-- meta
category: Anesthesia Machine
manufacturer: GE
-->

The Datex-Ohmeda anesthesia machine is connected using the 15-pin connector (Female) that comes out when you open the back cover. The 15-pin connector has the same height as the 9-pin connector used for typical serial communications, but it is longer.

<img src="../hardware_images/image170.png" width="450" />

Since the usual Serial To USB connector has a 9 pin male port, we need to make a cable that changes it to a 15 pin male connector.

<img src="../hardware_images/image77.png" width="450" />

If the anesthesia machine is not connected to the patient monitor, no further setup is required.

However, if the Datex-Ohmeda 15 pin port is already used to transmit information such as CO2 curve, airway pressure curve, etc., from the anesthesia machine to the patient monitor, the following Y-cable for data peeping should be made and used to extract information without disturbing the existing data communication. In this case, you must select the "Read only mode" option when adding a device in the Vital Recorder program.

<img src="../hardware_images/image55.png" width="450" />

Note: This protocol is called the GE Ohmeda Serial protocol and is used by Aespire, Aespire View, Aestiva, Avance, Avance CS2, Aisys, Aisys CS2 and Carestation 620/650/650c.
