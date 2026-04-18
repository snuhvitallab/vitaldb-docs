# Purpose of this document

This manual explains how to use Vital Recorder, a software that collects and analyzes vital signs data through communication with various medical devices. Please read them in order. It would be appreciated if you inform us of the question and improvement point of use on Forum page.

# Device setup

## Add a device

The first thing to do after installing Vital Recorder is to add medical devices, which you want to acquire data from. You can add a device by clicking <img src="images/user_manual/image9.png" width="450" /> button on the Devices tab.

<img src="images/user_manual/image14.png" width="450" />

NOTE: If the Device tab is not visible, press Ctrl + D or click the Show Device tab button.

<img src="images/user_manual/image2.png" width="450" />

The list of medical devices supported by Vital Recorder (version 1.8 and higher) is as follows.

## Supported Medical Devices

- Analog to Digital Converter (ADC)

  - SNUH: SNUADC (custom ADC)

  - DataQ: DI-149

  - DataQ: DI-155

  - DataQ: DI-1100

  - DataQ: DI-1120

  - National Instruments: USB-6008

  - Line In (record the Line In connector voltage of the computer sound card)

- Patient monitor

  - GE: Solar 8000

  - GE: Dash 2500-4000

  - GE: MPS

  - GE: Bx50

  - Philips: Intellivue series

- Multifunction monitor

  - Masimo: Root

- Anesthesia machine

  - Drager: anesthesia machines

  - GE: Datex-Ohmeda anesthesia machines

- Drug infuser

  - Fresenius Kabi: Orchestra

  - Fresenius Kabi: Agilia

  - BBraun: SpaceCom

  - Bionet: Pion TCI

- Brain monitor/ Depth of anesthesia monitor

  - Covidien: BIS

  - Covidien: A2000

  - Covidien: Invos

  - Inbody: PLEM100

  - BrainU: CAI

  - Mdoloris Medical Systems: ANI monitor

- Neuromuscular monitor

  - BlinkDC: TwitchView

  - IDMed: TOFScan

- Fluid infuser

  - Belmont: FMS2000

- Cardiac monitor

  - Edwards Lifesciences: Vigilance

  - Edwards Lifesciences: Vigileo

  - Edwards Lifesciences: EV-1000

  - Edwards Lifesciences: HemoSphere

  - Edwards Lifesciences: ClearSight

  - Deltex: CardioQ

- ETC

  - Demo (generates demo signals including waveforms and numeric data)

  - Laxtha : LXD

  - SNUH : SKNA

  - MELAB : SNUPATCH

  - MELAB : SNUEEG

If you click <img src="images/user_manual/image9.png" width="450" /> button, the following dialog box appears. You can add any kind of equipment here. In this guide we will add the DI-149 from DataQ, an analog to digital converter.

CAUTION: Before adding a device, the device driver must be installed and the device connected. For details on how to connect the device, refer to the Hardware Connection Guide.

<img src="images/user_manual/image25.png" width="450" />

If you select DataQ: DI-149 in the Device Type list on the left, the detailed setting window appears on the right. The detailed setting window differs slightly depending on the equipment type.

Since the DI-149 is an ADC device, it has a lot of detailed settings.

First, specify the Sampling Frequency. Sampling Frequency means how many samples are read per second. If you specify 100 Hz, 100 samples are read in one second. For general monitoring purposes, a sampling frequency of 100Hz is sufficient. 500 Hz is sufficient for P-wave or T-wave analysis. Sampling Frequency is the most important factor that affects the size of stored files and CPU usage, so it is recommended that you choose carefully. The value we are using on our team is 500Hz.

Sampling Frequency can also be entered directly. In addition, the maximum possible Sampling Frequency for each ADC is different and may vary depending on the number of channels to be used. However, the Vital Recorder automatically recognizes it and adjusts it to the possible values.

<img src="images/user_manual/image21.png" width="450" />

Next, you need to specify the name and conversion factor for each channel in the ADC. This part is specified in the channel input window under Preset. The number of lists depends on the number of channels in the ADC equipment. In most cases, it is recommended to use Presets. If you do not have a Preset, or if you have a specific reason for changing it, you can enter this value manually. You can select the kind of physical quantity to be transferred according to the track type and input the Voltage to Physical Unit conversion value.

Now you're done. Press OK button to add equipment

<img src="images/user_manual/image27.png" width="450" />

The added device is shown on the Devices tab and will not disappear from the list after exiting and restarting the Vital Recorder program. The Vital Recorder always attempts to connect to the devices on the Devices tab and displays the incoming data on the track. If the device is disconnected or data is not passed from the device for some time, the connection is automatically resumed.

## Multi-bed setup for HL7 gateways (Mindray, BBraun, Nihon Kohden)

Hospital HL7 gateways (Mindray eGateway, BBraun DoseLink, Nihon Kohden HL7 Gateway) typically deliver data for **multiple beds over a single TCP connection**. Vital Recorder 1.18.22 and later automatically route each incoming frame to the correct tab based on the bed identifier embedded in the frame, without any manual intervention on restart.

### Recommended configuration

1. **Create one tab per bed** and set each tab's **Bed Name** to match the identifier the gateway sends.
   - Mindray eGateway: the bed ID in `PV1-3` (e.g. `SU-1`, `BED-001`).
   - Nihon Kohden HL7GW: the `deviceId` JSON field or the 12-byte MFER prefix.
   - BBraun DoseLink: any non-empty value from the `~`-separated `MDC_ATTR_LOCATION` field (e.g. department name like `Forskning`/`Kurs`, table name like `Bord4`, or facility name like `Anilab`).
2. **Add the same HL7 device on the same TCP port** (e.g. 10000 for Mindray, 5000 for BBraun) to every tab. Vital Recorder will let only one tab bind the port (the primary) and automatically turn the others into passive subscribers that receive forwarded frames.
3. **Disable any location filter on the gateway side** so that all bed data reaches Vital Recorder — Vital Recorder will distribute it internally.

### Advanced routing

If the Bed Name cannot match the gateway's identifier directly, use the legacy port-filter syntax to route by keyword: set the port to `<port>#<keyword>` (e.g. `10000#Bord4` or `5000#Forskning Bord4` for an AND match). Multiple OR groups can be combined with additional `#` delimiters. The keyword search is a substring match against the entire HL7 frame, so any value that appears in `MDC_ATTR_LOCATION`, `PV1-3`, or any other segment field works.

### Restart behaviour

When Vital Recorder is closed and reopened, all tabs that share the port automatically re-establish their primary/subscriber relationship within a few seconds. No manual "Add device" or "Recording" click is required per tab. Each tab's original Bed Name and port settings are preserved across restarts.

### BBraun DoseLink specifics

BBraun DoseLink places multiple pumps (VMD blocks) inside a single frame for one rack. One frame still represents one bed; the multiple pumps are different channels at that bed. Configure one tab per rack location and all pumps in that rack will be recorded into the same tab, each on its own set of tracks (PUMP1, PUMP2, ...).

# Recording and storing

## Save to local storage

If the "Start Recording" button is pressed while data is being input from the device, recording and saving will start

<img src="images/user_manual/image15.png" width="450" />

A dialog box asking for the save folder appears on the first save. The specified path will continue to be used thereafter and can be viewed and changed in the Recording tab of the Settings dialog box.

<img src="images/user_manual/image29.png" width="450" />

If you click the Record button, "Date_Time.vital" file will be created in the specified folder. The file name is automatically created and cannot be changed during recording.

NOTE: During recording, the recording button and the recording time display at the top of the program turn red.

<img src="images/user_manual/image20.png" width="450" />

##

## File Management

### Load a file

You can load the saved file by pressing the Open File button on the toolbar.

If you press the Open File with channel selection button, you can read only certain tracks from inside the file. This is useful when you have saved all the cases and extracted specific tracks such as ECG or PLETH.

### Merge files

In Vital Recorder, it is convenient to split and create separate files for each patient by using "Split file based on SpO2 and HR input" function. However, if signal is interrupted in the middle, several files may be created in one case.

With this feature, you can combine several fragments of a file into a single case.

To take advantage of this feature, just drag and drop several fragmented files into the program's track window at once.

##

\
-

# Event marker

Event markers can be added during recording or at a later time.

## Open the Events tab

You can open the Event tab with <img src="images/user_manual/image30.png" width="450" /> button.

<img src="images/user_manual/image19.png" width="450" />

## Add events

There are five ways to add events from the Vital Recorder.

1.  press Enter key **during recording** to add an event at the current time.

> <img src="images/user_manual/image5.png" width="450" />

2.  Click on the desired spot of the EVENTS track.

> <img src="images/user_manual/image32.png" width="450" />

3.  Click <img src="images/user_manual/image10.png" width="450" /> button on the Events tab.

> <img src="images/user_manual/image13.png" width="450" />

4.  Use <img src="images/user_manual/image3.png" width="450" /> function, with which you can set shortcut keys (0-29 number keys).

    1.  Click <img src="images/user_manual/image3.png" width="450" /> button on the Events tab, then the following pop-up window will show up.

    2.  Set event names like the image below and then click OK. Then, you can add events by pressing number keys. For example, an event “VITALLAB” will be added if number 3 key is pressed with the settings in the image below.

> <img src="images/user_manual/image22.png" width="450" /><img src="images/user_manual/image28.png" width="450" />

5.  Use batch recording & bulk

> *time*
>
> *Event recording*
>
> *time*
>
> *Event recording*
>
> Print the record like the above format in the text window of the Events tab. The format of the time is automatically normalized and changed to a unified format.
>
> Click the Apply button afterwards to confirm that events are added to the event track in bulk.
>
> You can move the location of the event marker by dragging it, or double-click it to edit the event.
>
> You can also edit them in bulk.

#

# Options and Settings

Vital Recorder has several setting options. You can open the Settings page by clicking a cog button.

<img src="images/user_manual/image8.png" width="450" />

<img src="images/user_manual/image1.png" width="450" />

## Configuration File

<img src="images/user_manual/image18.png" width="450" />

- Pencil button opens the configuration file, vr.conf.

- Folder button opens the location where vr.conf is stored. By default, the folder path is C:\Users\Username\AppData\Roaming\VitalRecorder.

On-premise Vitalserver requires vr.conf editing. You can open and edit vr.conf with Notepad or any text editing program as shown below.

<img src="images/user_manual/image6.png" width="450" />

All rows are of the form Variable=Value, which can be divided into sections of the form [bedname/equipment name].

Below is a list of recognized configuration variables. Other variables are ignored.

- SERVER_IP: To connect VitalRecorder to Vitalserver, SERVER_IP value is required. As shown above, it should be a form of VITALSERVER_IP_OR_DOMAIN:PORT. The variables below overwrite specific server IP addresses.

  - ADT_SERVER_IP: server that receives the admission-discharge-transfer information

  - MONITOR_SERVER_IP: server that receives the (real-time) web monitoring data

  - UPLOAD_SERVER_IP: server that receives vital files.

  - FILTER_SERVER_IP: server for python filter

- SAVEDIR: Folder to save the vital files

- FILENAME_TEMPLATE: template for the filename. default is %y%m%d\\%r\_%y%m%d\_%h%i%s

  - %p: patient ID

  - %r: bed name

  - %Y: year (4 digits)

  - %y: year (2 digits)

  - %m: month (00-12)

  - %d: date (01-31)

  - %h: hour (00-59)

  - %i: minute (00-59)

  - %s: second (00-59)

- VRCODE: VR code

- SHOW_DSA: Whether to display density spectral arrays (DSA) in ECG and EEG tracks

**After editing the vr.conf file in the other editor (eg. NotePad), please DO NOT click OK or Apply on the Setting Dialog, but Cancel or Close (X) the dialog.** Otherwise, VR will reset the configuration file. Close All the VR windows and restart VR to apply the change.

## General Setting

<img src="images/user_manual/image16.png" width="450" />

You can easily change Settings by clicking the OR, PACU, or ICU button.

### OR button

- Stop recording when SpO2 and HR parameter are not inputted for 5 minutes

- Start recording automatically when VitalRecorder starts

- Play sound when adding an event during recording

- The Display of VitalRecorder will start maximized

### PACU button

- Stop recording when SpO2 and HR parameter are not inputted for 2 minutes

- Start recording automatically when VitalRecorder starts

- The Display of VitalRecorder will start minimized

### ICU button

- Cut file every hour (create a new file every hour)

- Start recording automatically when program starts

- The Display of VitalRecorder will start minimized

## Management Setting

<img src="images/user_manual/image17.png" width="450" />

## Display Setting

<img src="images/user_manual/image12.png" width="450" />

- Start maximized: Set the program to run maximized.

- Start minimized: Set the program to run minimized.

- Always on top: Always set the program to the top level window.

- Minimize to tray icon: makes it a tray icon when minimizing the program.

<img src="images/user_manual/image23.png" width="450" /> <img src="images/user_manual/image33.png" width="450" />

- The tray icon is normally a black stationary icon, but it is displayed as a red animation icon during recording.

# Exploring the data

To move a track in the Vital Recorder, it's easiest to drag the track with your mouse.

To navigate a track, scroll the mouse wheel **in the track list**.

To zoom in and out on the track's data, scroll the mouse wheel **in the track window**.

## Set range

By dragging the time display area of the Vital Recorder, you can set the time range for track editing.

The start and end markers of the selected time range can be moved by dragging again.

NOTE: Setting the time range and editing tracks **only work with recorded files (.vital)**. You CANNOT edit the current recording case.

<img src="images/user_manual/image4.png" width="450" />

## Edit tracks

Select the time zone and right click, then a popup menu will appear.

- “Save As” on the pop-up menu, only the selected time zone can be saved as a separate file. This function is useful for storing some of the cases separately in the study.

- “Copy Values to clipboard” copies selected data to the clipboard as text form. These values can be pasted into Excel, Notepad, R programs, etc.

- “Delete” will erase the data from selected area

- “Crop” leaves the corresponding area.

- “Set track height” changes the height of the track, and the track will look bigger.

<img src="images/user_manual/image24.png" width="450" />

# Filters

Vital Recorder has powerful scripting capabilities. The data read in the Vital Recorder can be programmed and analyzed using the JavaScript language, a scripting language. Since the Vital Recorder is installed with various filters and the source code of the filter can be checked directly, it is possible to apply various algorithms to your data.

Please refer to the following document for how to make the filter.

: Making custom filters for Vital Recorder

## Using filters

Open the saved vital file and click <img src="images/user_manual/image7.png" width="450" /> “Show Filter” button to go to the Filters tab (If you open a file without an event, it will be automatically moved to the Filters tab).

<img src="images/user_manual/image31.png" width="450" />

<img src="images/user_manual/image26.png" width="450" />

Various filters are listed. Let's calculate the Pulse Transit Time (PTT).

The ECG and PLETH tracks are automatically selected in the input track. This is automatically selected because it has the same track name as the variable name (ecg, pleth) entered by the filter creator. If there is no such track, you can manually select the track

The output variables specified by the filter creator are displayed. For PTT filters, these values are Pulse Transit Time variables. You cannot output to an existing track name, so you can modify the track name here.

Press the OK button, then

<img src="images/user_manual/image11.png" width="450" />

Pulse Transit Time is output to the new track.

# Vital File Format

## Introduction

- The vital file is a file format used in vital recorder for saving vital signs and waveforms

  - It is a single gzip compressed binary file starts with (1F 8B 08 00)

  - It contains a header and a body part

  - Multi-byte variables are encoded using littlen-endian

  - All data structures are arranged in 1-byte units.

    - Caution! Some compilers use 4 byte alignment implicitly.[^1]

##

## Data format

- String data format

  - Strings are encoded in UTF8

  - It contains 4 byte length (without length itself) followed by character array of specified length

  - Caution! It does not include the following NULL(\0) character

- Time data format

  - Ttimes are stored in UTC

  - UTC can be converted to the local time using time zone bias (offset) in the header part.

    - UTC = local time + tzbias[^2]

  - All time data are represented as the number of seconds since 1970/01/01 00:00:00 UTC as a double data format

  - This is compatible with Unix timestamps and convenient for addition and subtraction.

  - Changing the time to \_\_int64 makes the speed slower because it require conversion in every operation.

  - The decimal point is used to indicate the precision below seconds. (for example 0.1 means 100 milliseconds)

  - Because the unix timestamp of year 2020 is 1,606,780,800, 31 bits are enough to express integer part of it. IEEE 754 double data type has 52 bit for fraction part, so 21 digits can be used for the representation of sub second time. 2 ^ 20 is about 1 million, so it has about 1 usec resolution.

##

## Header

- The total length of the header is 10 + headerlen.

- The vital file does not include the number or length of tracks in the header, you must parse the file to get the number of tracks or records. This limitation is because vital recorder can not know when recording will stop and you can add tracks at any time while vital files are storing.

| Name | Type | Length | Description |
|----|----|----|----|
| sign | BYTE[4] | 4 | “VITA” |
| format_ver | DWORD | 4 | File format version, currently 3 |
| headerlen | WORD | 2 | header length after this, currently 10 |
| tzbias[^3] | short | 2 | time zone bias (the difference, in minutes, between UTC time and local time) |
| inst_id | DWORD | 4 | The instance ID of the program to be issued when the program starts. It is necessary to verify that the location of several vital files are continuously recorded in the same vital recorder execute. If different vital files have the same inst_id, you can use the same track id, even though there is a probability of 1/4.2 billion for collision. |
| prog_ver | DWORD | 4 | vital recorder version |

##

## Body

- Body is a sequence of packets as specified below.

- Since the length of a packet is not constant, there is no way to directly index a specific packet without reading all packets. However, if you ignore the unwanted packet type and pass it using datalen field, you can read the information you want fairly quickly. (For example, when you want to extract only some track)

### Packet structure

<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Length</th>
<th>Description</th>
</tr>
<tr>
<th>type</th>
<th>BYTE</th>
<th>1</th>
<th><p>SAVE_DEVINFO = 9</p>
<p>SAVE_TRKINFO = 0</p>
<p>SAVE_REC = 1</p>
<p>SAVE_CMD = 6</p></th>
</tr>
<tr>
<th>datalen</th>
<th>DWORD</th>
<th>4</th>
<th><p>length of <strong>data</strong> (<strong>exclude</strong> type and datalen itself)</p>
<p>If you meet the type you dont know, please ignore it and skip the datalen bytes.</p></th>
</tr>
<tr>
<th>data</th>
<th></th>
<th>datalen</th>
<th>The contents of data depends on the type and are described below.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### DEVINFO

- Structure for device information

  - It must be saved before the devid is used.

  - If devid is 0, it indicates the vital recorder itself (for example, filter-generated tracks, event markers)

- A new DEVINFO can appear for the same device id (devid) in a file. In this case, the new value should overwrites the previous value.

- devid and trkid are meaningful only within the same file.

- Even if the program instance is different, the Vital Recorder is implemented with the same devid value if the same kind of equipment is connected to the same physical port.

  - For example, if two BIS devices are connected to COM5 and COM6, the previous devid remains the same even if the program is terminated and then re-executed. (save the devid to the registry)

  - If you intentionally terminate the program and then switch between the two BIS devices and run the program again, the devids may cross each other.

| Name | Type | Length | Description |
|----|----|----|----|
| devid | DWORD | 4 | device identifier |
| typename | string | 4+len | device type |
| devname | string | 4+len | device name |
| port | string | 4+len | Information that allows device types such as COM1, COM10, ETH1, and Line Input Mixer to recognize the port to which the device is connected with this information only. If the device type and port are the same, it is generally considered the same device. |

### TRKINFO

- Structure for track information

- TRKINFO must be appeared before the first record with the track id.

  - Otherwise, the record should be ignored.

- Tracks are separated by trkids, which are 2-byte integers.

  - The numeric value of trkid itself has no meaning and there is no continuity

  - trkids can be changed every time the program is executed.

  - The order of the tracks is not in the order of trkid size, but in the order of appearance and the CMD_ORDER command described later.

- Tracks with a devid of 0 (vital recorder itself) and name of EVENT are treated specially in the vital recorder. It is not displayed on a separate track but displayed in the event bar.

<table style="width:100%;">
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Length</th>
<th>Description</th>
</tr>
<tr>
<th>trkid</th>
<th>WORD</th>
<th>2</th>
<th>track id</th>
</tr>
<tr>
<th>rec_type</th>
<th>BYTE</th>
<th>1</th>
<th><p>TYPE_WAV = 1</p>
<p>TYPE_NUM = 2</p>
<p>TYPE_STR = 5</p></th>
</tr>
<tr>
<th>recfmt</th>
<th>BYTE</th>
<th>1</th>
<th><p>FMT_NULL = 0 // for TYPE_STR</p>
<p>FMT_FLOAT = 1</p>
<p>FMT_DOUBLE = 2</p>
<p>FMT_CHAR = 3</p>
<p>FMT_BYTE = 4</p>
<p>FMT_SHORT = 5</p>
<p>FMT_WORD = 6</p>
<p>FMT_LONG = 7</p>
<p>FMT_DWORD = 8</p></th>
</tr>
<tr>
<th>name</th>
<th>string</th>
<th>4+len</th>
<th></th>
</tr>
<tr>
<th>unit</th>
<th>string</th>
<th>4+len</th>
<th></th>
</tr>
<tr>
<th>mindisp</th>
<th>float</th>
<th>4</th>
<th></th>
</tr>
<tr>
<th>maxdisp</th>
<th>float</th>
<th>4</th>
<th></th>
</tr>
<tr>
<th>color</th>
<th>color</th>
<th>4</th>
<th>4byte ARGB format</th>
</tr>
<tr>
<th>srate</th>
<th>float</th>
<th>4</th>
<th>sample rate</th>
</tr>
<tr>
<th>adc_gain</th>
<th>double</th>
<th>8</th>
<th>measured_value = adc_offset + saved_value * adc_gain</th>
</tr>
<tr>
<th>adc_offset</th>
<th>double</th>
<th>8</th>
<th>measured_value = adc_offset + saved_value * adc_gain</th>
</tr>
<tr>
<th>montype</th>
<th>BYTE</th>
<th>1</th>
<th><p>Specifies the physiologic meaning of the track.</p>
<p>MON_ECG_WAV = 1,</p>
<p>MON_ECG_HR = 2,</p>
<p>MON_ECG_PVC = 3,</p>
<p>MON_IABP_WAV = 4,</p>
<p>MON_IABP_SBP = 5,</p>
<p>MON_IABP_DBP = 6,</p>
<p>MON_IABP_MBP = 7,</p>
<p>MON_PLETH_WAV = 8,</p>
<p>MON_PLETH_HR = 9,</p>
<p>MON_PLETH_SPO2 = 10,</p>
<p>MON_RESP_WAV = 11,</p>
<p>MON_RESP_RR = 12,</p>
<p>MON_CO2_WAV = 13,</p>
<p>MON_CO2_RR = 14,</p>
<p>MON_CO2_CONC = 15,</p>
<p>MON_NIBP_SBP = 16,</p>
<p>MON_NIBP_DBP = 17,</p>
<p>MON_NIBP_MBP = 18,</p>
<p>MON_BT = 19,</p>
<p>MON_CVP_WAV = 20,</p>
<p>MON_CVP_CVP = 21,</p></th>
</tr>
<tr>
<th>devid</th>
<th>DWORD</th>
<th>4</th>
<th>Devid of the device that created the track</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### REC

- Every record stores time specific data (measured sample, sample list, string).

| Name | Type | Length | Description |
|----|----|----|----|
| infolen | WORD | 2 | length of header of the record, currently 10 |
| dt | double | 8 | The time at which the record's value was measured |
| trkid | WORD | 2 | track id |
| values | BYTE[] | datalen-infolen-2 | rec_type specific values described below |

- values are different among the track type (NUM, WAV, STR)

- WAV records

<!-- -->

- Samples that are continuously measured from the time specified by dt are stored as an array.

- The sample rate and data type are taken from the track information.

| Name | Type           | Length              | Description       |
|------|----------------|---------------------|-------------------|
| num  | DWORD          | 4                   | number of samples |
| vals | dat_fmt[num] | sizeof(recfmt)*num | data samples      |

- NUM records

| Name | Type    | Length         | Description |
|------|---------|----------------|-------------|
| val  | dat_fmt | sizeof(recfmt) |             |

- STR records

| Name   | Type   | Length | Description |
|--------|--------|--------|-------------|
| unused | DWORD  | 4      | not used    |
| sval   | string | 4+len  |             |

- CMD records

  - Currently 2 commands are supported.

  - Depending on the cmd, additional data may follow.

  - Unknown commands should skip over the datalen of the packet.

<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Length</th>
<th>Description</th>
</tr>
<tr>
<th>cmd</th>
<th>BYTE</th>
<th>1</th>
<th><p>CMD_ORDER = 5</p>
<p>CMD_RESET_EVENTS = 6</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- CMD_TRK_ORDER

  - Define track order

  - The following additional data are shown below.

| Name   | Type         | Length | Description      |
|--------|--------------|--------|------------------|
| cnt    | WORD         | 2      | number of tracks |
| trkids | WORD [cnt] | cnt*2 | array of trkids  |

- CMD_RESET_EVENTS

  - Removed all event markers prior to this command

  - No additional data

# Vital File Utilities

In the folder below you will find small utility programs to help you use vital files.

C:\Program Files\Vital Recorder\utilities

The sequence of analysis for files recorded with the Vital Recorder is as follows: First, open the file to check the track information, and save some tracks needed for research in a format that can be read by an analysis program such as excel or R (* .csv).

The vital file utility programs allow you to automate this task for many files.

The vital file utility is installed with the Vital Recorder. There are currently three types of vital file utilities.

- vital_list : Creates a list of vital files in the current folder and displays summarized information

- vital_trks : Extract track information from vital file

- vital_recs : Extract the actual records inside the vital file

The output of the vital file utility is output in the standard format of the operating system in the form of csv. Thus, you can get the output by using a pipe in a shell script or using shell command execution functions in various programming languages.

## vital_list

- vital_list [Path name]

- Search the destination path to subdirectory level to list all vital files and extract summary information

- When path name is not specified, it is designated as current directory

- Output field: filename, path, dtstart, dtend, length, gas, drug1, drug2, abp, cvp, co, bis

- It internally uses vital_trks utility, so it must be in the same path at execution time

## vital_trks

- Execution: vital_trks [File name]

- Purpose: Extraction of equipment list and track list

- The lines beginning with \# in the first part are the header

- The header is used to output the attributes of the entire vital file in \# variable name and value format, and extracts dgmt, dtstart, and dtend at present.

- The first line that does not begin with \# is the variable name and contains the followings: tname, tid, dname, did, rectype(wav/num/str), srate(wav), minval(num), maxval(num), firstval(str)

- The following rows are data

- Execution examples

> vital_trks example.vital

\#dgmt,-9.000000

\#dtstart,1469504477.345400

\#dtend,1469508718.631351

tname,tid,dname,did,rectype,dtstart,dtend,srate,minval,maxval,firstval

EEG1_WAV,1,BIS,1047396353,WAV,1469504477.345400,1469508717.880400,128.000000,,,

EEG2_WAV,2,BIS,1047396353,WAV,1469504477.345400,1469508717.880400,128.000000,,,

CO2,3,Primus,1116864513,WAV,1469504477.951400,1469508718.271569,62.500000,,,

AWP,4,Primus,1116864513,WAV,1469504477.951400,1469508718.271569,62.500000,,,

ECG,5,SNUADC,1700790273,WAV,1469504477.635396,1469508718.631351,100.000000,,,

CVP,6,SNUADC,1700790273,WAV,1469504477.635396,1469508718.631351,100.000000,,,

ART1,7,SNUADC,1700790273,WAV,1469504477.635396,1469508718.631351,100.000000,,,

ECG_II,8,SNUADC,1700790273,WAV,1469504477.635396,1469508718.631351,100.000000,,,

ECG_V5,9,SNUADC,1700790273,WAV,1469504477.635396,1469508718.631351,100.000000,,,

RESP,10,SNUADC,1700790273,WAV,1469504477.635396,1469508718.631351,100.000000,,,

PLETH,11,SNUADC,1700790273,WAV,1469504477.635396,1469508718.631351,100.000000,,,

SR_1,12,BIS,1047396353,NUM,1469504478.144400,1469508134.144400,,0.000000,0.000000,

SEF_1,13,BIS,1047396353,NUM,1469504478.144400,1469508134.144400,,13.480000,23.910000,

BIS_1,14,BIS,1047396353,NUM,1469504478.144400,1469508717.144400,,0.000000,76.400002,

AMP_1,15,BIS,1047396353,NUM,1469504478.144400,1469508134.144400,,62.669998,68.720001,

BIT_1,16,BIS,1047396353,STR,1469504478.144400,1469508717.144400,,,,0848

EMG_1,17,BIS,1047396353,NUM,1469504478.144400,1469508134.144400,,21.100000,71.650002,

SQI_1,18,BIS,1047396353,NUM,1469504478.144400,1469508717.144400,,0.000000,100.000000,

BIS_2,19,BIS,1047396353,NUM,1469504478.144400,1469508717.144400,,0.000000,0.000000,

BIT_2,20,BIS,1047396353,STR,1469504478.144400,1469508717.144400,,,,ffff8000

...

PUMP1_DRUG,145,Orchestra,1682243585,STR,1469504481.572400,1469508253.775400,,,,PROPOFOL

PUMP1_RATE,146,Orchestra,1682243585,NUM,1469504481.573400,1469508253.775400,,0.000000,311.625000,

PUMP1_VOL,147,Orchestra,1682243585,NUM,1469504481.573400,1469508253.775400,,37.784000,54.127998,

PUMP1_REMAIN,148,Orchestra,1682243585,NUM,1469504481.574400,1469508253.775400,,0.000000,51.500000,

PUMP1_PRES,149,Orchestra,1682243585,NUM,1469504481.574400,1469508253.775400,,0.000000,50.000000,

PUMP1_CONC,150,Orchestra,1682243585,NUM,1469504481.574400,1469508253.775400,,20.000000,20.000000,

PUMP1_CP,151,Orchestra,1682243585,NUM,1469504481.575400,1469508253.775400,,1.088000,3.933000,

PUMP1_CE,152,Orchestra,1682243585,NUM,1469504481.575400,1469508253.775400,,1.111000,3.501000,

PUMP1_CT,153,Orchestra,1682243585,NUM,1469504481.575400,1469508253.775400,,0.000000,3.500000,

PUMP2_DRUG,154,Orchestra,1682243585,STR,1469504481.575400,1469508253.871400,,,,REMIFENTANIL

PUMP2_RATE,155,Orchestra,1682243585,NUM,1469504481.576400,1469508253.871400,,0.000000,244.858002,

PUMP2_VOL,156,Orchestra,1682243585,NUM,1469504481.577400,1469508253.871400,,17.954000,67.764999,

PUMP2_REMAIN,157,Orchestra,1682243585,NUM,1469504481.577400,1469508253.871400,,0.000000,48.200001,

PUMP2_PRES,158,Orchestra,1682243585,NUM,1469504481.578400,1469508253.871400,,0.000000,230.000000,

PUMP2_CONC,159,Orchestra,1682243585,NUM,1469504481.578400,1469508253.871400,,20.000000,20.000000,

PUMP2_CP,160,Orchestra,1682243585,NUM,1469504481.578400,1469508253.871400,,0.404000,6.007000,

PUMP2_CE,161,Orchestra,1682243585,NUM,1469504481.578400,1469508253.871400,,0.470000,4.504000,

PUMP2_CT,162,Orchestra,1682243585,NUM,1469504481.579400,1469508253.871400,,0.000000,4.500000,

## vital_recs

- Execution: vital_recs.exe [File name] [Track name] [Time interval]

- Purpose: Extract data from a specific track

- When extracting multiple tracks at once, separated by commas

- If you want to specify the device name, specify it as the device name/track name. If the device name contains spaces, enclose the [Track Name] field itself in quotes ( "), for example vital_recs.exe example.vital " Solar 8000M/HR " 1.

- Time interval is 1 second when not specified

- Blank values are treated as blank and duplicate values are treated as first values. Therefore, it should be extracted above the maximum sampling rate of the track. Otherwise sample loss occurs..

- The first line is the header and it is as follows: timestamp, first track name, second track name, third track name, ...

- Execution examples

> vital_recs example.vital ECG,HR

timestamp,ECG,HR

1469472077.635396,-4.956260

1469472137.635396,-0.167093,67.000000

1469472197.635396,0.010649,66.000000

1469472257.635396,0.237764,66.000000

1469472317.635396,0.297011,68.000000

1469472377.635396,-0.028849,68.000000

1469472437.635396,-0.018975,75.000000

1469472497.635396,0.079771,78.000000

1469472557.635396,-0.018975,79.000000

1469472617.635396,0.000774,72.000000

1469472677.635396,0.030398,72.000000

1469472737.635396,0.188391,69.000000

1469472797.635396,0.010649,68.000000

1469472857.635396,0.050147,70.000000

1469472917.635396,0.148893,69.000000

1469472977.635396,0.079771,69.000000

1469473037.635396,-0.097971,68.000000

1469473097.635396,1.027730,68.000000

1469473157.635396,-0.186843,83.000000

1469473217.635396,-0.028849,75.000000

1469473277.635396,0.208140,75.000000

1469473337.635396,0.060022,71.000000

...

[^1]: For visual studio, use the following code

    \#pragma pack (push, 1)

    struct TRKINFO {... code ...};

    \#pragma pack (pop)

[^2]: time_t t = (time_t)(dt - tzbias * 60); // unixtime -> localtime

    tm* ptm = gmtime(&t); // local time (in seconds) → year, month, day, hour, minute, second

[^3]: TIME_ZONE_INFORMATION tzi;

    GetTimeZoneInformation(&tzi);

    return (short) tzi.Bias; // UTC = local time + bias // -540 for Korea
