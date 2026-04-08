# Introduction

- The vital file is a file format used in the vital recorder for saving vital signs and waveforms.

  - It is a single gzip compressed binary file starting with (1F 8B 08 00)

  - It contains a header and a body part

  - Multi-byte variables are encoded using little-endian

  - All data structures are arranged in 1-byte units.

    - Caution! Some compilers use 4-byte alignment implicitly.[^1]

- Sample vital file can be downloadable from [https://api.vitaldb.net/0001.vital](https://api.vitaldb.net/0001.vital)

## Data format

- String data format

  - Strings are encoded in UTF8

  - It contains 4-byte length (without length itself) followed by a character array of specified length

  - Caution! It does not include the following NULL(\0) character

- Time data format

  - Times are stored in UTC

  - UTC can be converted to the local time using time zone bias (offset) in the header part.

    - UTC = local time + tzbias[^2]

  - All time data are represented as the number of seconds since 1970/01/01 00:00:00 UTC as a double data format

  - This is compatible with Unix timestamps and convenient for addition and subtraction.

  - Changing the time to \_\_int64 makes the speed slower because it requires conversion in every operation.

  - The decimal point is used to indicate the precision below seconds. (for example, 0.1 means 100 milliseconds)

  - Because the unix timestamp of year 2020 is 1,606,780,800, 31 bits are enough to express the integer part of it. IEEE 754 double data type has 52 bit for the fraction part, so 21 digits can be used for the representation of sub second time. 2 ^ 20 is about 1 million, so it has about 1 usec resolution.

# Header

- The total length of the header is 10 + headerlen.

<table>
<thead>
<tr>
<th style="text-align: center;">Name</th>
<th style="text-align: center;">Type</th>
<th style="text-align: center;">Length</th>
<th style="text-align: center;">Description</th>
</tr>
<tr>
<th style="text-align: center;">sign</th>
<th style="text-align: center;">BYTE[4]</th>
<th style="text-align: center;">4</th>
<th style="text-align: center;">“VITA”</th>
</tr>
<tr>
<th style="text-align: center;">format_ver</th>
<th style="text-align: center;">DWORD</th>
<th style="text-align: center;">4</th>
<th style="text-align: center;">File format version, currently 3</th>
</tr>
<tr>
<th style="text-align: center;">headerlen</th>
<th style="text-align: center;">WORD</th>
<th style="text-align: center;">2</th>
<th style="text-align: center;">header length after this, currently 26</th>
</tr>
<tr>
<th style="text-align: center;">tzbias<a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a></th>
<th style="text-align: center;">short</th>
<th style="text-align: center;">2</th>
<th style="text-align: center;"><p>time zone bias</p>
<p>(the difference, in minutes, between UTC time and local time)</p></th>
</tr>
<tr>
<th style="text-align: center;">inst_id</th>
<th style="text-align: center;">DWORD</th>
<th style="text-align: center;">4</th>
<th style="text-align: center;">The instance ID of the program to be issued when the program starts. It is necessary to verify that the location of several vital files are continuously recorded in the same vital recorder execute. If different vital files have the same inst_id, you can use the same track id, even though there is a probability of 1/4.2 billion for collision.</th>
</tr>
<tr>
<th style="text-align: center;">prog_ver</th>
<th style="text-align: center;">DWORD</th>
<th style="text-align: center;">4</th>
<th style="text-align: center;">vital recorder version</th>
</tr>
<tr>
<th style="text-align: center;">dtstart</th>
<th style="text-align: center;">double</th>
<th style="text-align: center;">8</th>
<th style="text-align: center;">The start time of the records in this vital file. It can be zero if it is undetermined.</th>
</tr>
<tr>
<th style="text-align: center;">dtend</th>
<th style="text-align: center;">double</th>
<th style="text-align: center;">8</th>
<th style="text-align: center;">The end time of the records in this vital file. It can be zero if it is undetermined.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<section id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>TIME_ZONE_INFORMATION tzi;</p>
<p>GetTimeZoneInformation(&amp;tzi);</p>
<p>return (short) tzi.Bias; // UTC = local time + bias // -540 for Korea<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</section>

# Body

- Body is a **sequence of packets** as specified below.

- Since the length of a packet is not constant, there is no way to directly index a specific packet without reading all packets. However, if you ignore the unwanted packet type and pass it using datalen field, you can read the information you want fairly quickly. (For example, when you want to extract only some track)

## Packet structure

<table>
<thead>
<tr>
<th style="text-align: center;">Name</th>
<th style="text-align: center;">Type</th>
<th style="text-align: center;">Length</th>
<th style="text-align: center;">Description</th>
</tr>
<tr>
<th style="text-align: center;">type</th>
<th style="text-align: center;">BYTE</th>
<th style="text-align: center;">1</th>
<th style="text-align: center;"><p>SAVE_DEVINFO = 9</p>
<p>SAVE_TRKINFO = 0</p>
<p>SAVE_REC = 1</p>
<p>SAVE_CMD = 6</p></th>
</tr>
<tr>
<th style="text-align: center;">datalen</th>
<th style="text-align: center;">DWORD</th>
<th style="text-align: center;">4</th>
<th style="text-align: center;"><p>length of <strong>data</strong> (<strong>exclude</strong> type and datalen itself)</p>
<p>If you meet the type you dont know, please ignore it and skip the datalen bytes.</p></th>
</tr>
<tr>
<th style="text-align: center;">data</th>
<th style="text-align: center;"></th>
<th style="text-align: center;">datalen</th>
<th style="text-align: center;"><p>The contents of data depends on the type</p>
<p>and are described below.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## DEVINFO

- Structure for device information

  - It must be saved before the devid is used.

  - If devid is 0, it indicates the vital recorder itself (for example, filter-generated tracks, event markers)

- A new DEVINFO can appear for the same device id (devid) in a file. In this case, the new value should overwrite the previous value.

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

## TRKINFO

- Structure for track information

- TRKINFO must be appeared before the first record with the track id.

  - Otherwise, the record should be ignored.

- Tracks are separated by trkids, which are 2-byte integers.

  - The numeric value of trkid itself has no meaning and there is no continuity

  - trkids can be changed every time the program is executed.

  - The order of the tracks is not in the order of trkid size, but in the order of appearance and the CMD_ORDER command described later.

- Tracks with a devid of 0 (vital recorder itself) and name of EVENT are treated specially in the vital recorder. It is not displayed on a separate track but displayed in the event bar.

<table>
<thead>
<tr>
<th style="text-align: center;">Name</th>
<th style="text-align: center;">Type</th>
<th style="text-align: center;">Length</th>
<th style="text-align: center;">Description</th>
</tr>
<tr>
<th style="text-align: center;">trkid</th>
<th style="text-align: center;">WORD</th>
<th style="text-align: center;">2</th>
<th style="text-align: center;">track id</th>
</tr>
<tr>
<th style="text-align: center;">rec_type</th>
<th style="text-align: center;">BYTE</th>
<th style="text-align: center;">1</th>
<th style="text-align: center;"><p>TYPE_WAV = 1</p>
<p>TYPE_NUM = 2</p>
<p>TYPE_STR = 5</p></th>
</tr>
<tr>
<th style="text-align: center;">recfmt</th>
<th style="text-align: center;">BYTE</th>
<th style="text-align: center;">1</th>
<th style="text-align: center;"><p>FMT_NULL = 0 // for TYPE_STR</p>
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
<th style="text-align: center;">name</th>
<th style="text-align: center;">string</th>
<th style="text-align: center;">4+len</th>
<th style="text-align: center;"></th>
</tr>
<tr>
<th style="text-align: center;">unit</th>
<th style="text-align: center;">string</th>
<th style="text-align: center;">4+len</th>
<th style="text-align: center;"></th>
</tr>
<tr>
<th style="text-align: center;">mindisp</th>
<th style="text-align: center;">float</th>
<th style="text-align: center;">4</th>
<th style="text-align: center;"></th>
</tr>
<tr>
<th style="text-align: center;">maxdisp</th>
<th style="text-align: center;">float</th>
<th style="text-align: center;">4</th>
<th style="text-align: center;"></th>
</tr>
<tr>
<th style="text-align: center;">color</th>
<th style="text-align: center;">color</th>
<th style="text-align: center;">4</th>
<th style="text-align: center;">4byte ARGB format</th>
</tr>
<tr>
<th style="text-align: center;">srate</th>
<th style="text-align: center;">float</th>
<th style="text-align: center;">4</th>
<th style="text-align: center;">sample rate</th>
</tr>
<tr>
<th style="text-align: center;">adc_gain</th>
<th style="text-align: center;">double</th>
<th style="text-align: center;">8</th>
<th style="text-align: center;">measured_value = adc_offset + saved_value * adc_gain</th>
</tr>
<tr>
<th style="text-align: center;">adc_offset</th>
<th style="text-align: center;">double</th>
<th style="text-align: center;">8</th>
<th style="text-align: center;">measured_value = adc_offset + saved_value * adc_gain</th>
</tr>
<tr>
<th style="text-align: center;">montype</th>
<th style="text-align: center;">BYTE</th>
<th style="text-align: center;">1</th>
<th style="text-align: center;"><p>Specifies the physiologic meaning of the track.</p>
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
<th style="text-align: center;">devid</th>
<th style="text-align: center;">DWORD</th>
<th style="text-align: center;">4</th>
<th style="text-align: center;">Devid of the device that created the track</th>
</tr>
<tr>
<th style="text-align: center;">reclen</th>
<th style="text-align: center;">DWORD</th>
<th style="text-align: center;">4</th>
<th style="text-align: center;">Length of all record packets in byte for the track. It must be zero if the records are not stored sequentially. It can be zero if the information was undetermined or not calculated.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## REC

- Every record stores time specific measured value(s).

| Name | Type | Length | Description |
|----|----|----|----|
| infolen | WORD | 2 | length of header of the record, currently 10 |
| dt | double | 8 | The time at which the record's value was measured |
| trkid | WORD | 2 | track id |
| values | BYTE[] | datalen-infolen-2 | rec_type specific values described below |

- values are different among the track type (NUM, WAV, STR)

- WAV records

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

<table style="width:100%;">
<thead>
<tr>
<th style="text-align: center;">Name</th>
<th style="text-align: center;">Type</th>
<th style="text-align: center;">Length</th>
<th style="text-align: center;">Description</th>
</tr>
<tr>
<th style="text-align: center;">cmd</th>
<th style="text-align: center;">BYTE</th>
<th style="text-align: center;">1</th>
<th style="text-align: center;"><p>CMD_TRK_ORDER = 5</p>
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

[^1]: For visual studio, use the following code

    \#pragma pack (push, 1)

    struct TRKINFO {... code ...};

    \#pragma pack (pop)

[^2]: time_t t = (time_t)(dt - tzbias * 60); // unixtime -> localtime

    tm* ptm = gmtime(&t); // local time (in seconds) → year, month, day, hour, minute, second
