# Introduction

The VitalDB web application programming interface (API) is a language independent interface that allows users to get the VitalDB open dataset via HTTP secure protocol. All Web API’s endpoint can be accessed by sending HTTP requests with GET method or by entering an address in the web browser.

The responses are files with **GZip-compressed** comma separated values (CSV) format.

**Each CSV file has a header row at the begining** which contains column names.

Supported endpoints and their purposes are as below.

| **Endpoint URL** | **Method** |
|----|----|
| [https://api.vitaldb.net/cases](https://api.vitaldb.net/cases) | GET |
| [https://api.vitaldb.net/trks](https://api.vitaldb.net/trks) | GET |
| [https://api.vitaldb.net/{tid}](https://api.vitaldb.net/d3b01ea0d7080f0d) | GET |
| [https://api.vitaldb.net/labs](https://api.vitaldb.net/labs) | GET |

# Clinical information

Endpoint URL: [**https://api.vitaldb.net/cases**](https://api.vitaldb.net/cases)

This endpoint contains information related to the clinical information.

Parameter lists are available [here](https://vitaldb.net/dataset/?query=overview&documentId=13qqajnNZzkN7NZ9aXnaQ-47NWy7kx-a6gbrcEsi-gak&sectionId=h.ischel1xtl2q).

Please note that all timepoints are in seconds from casestart. Therefore, the casestart is always zero in all cases and the caseend becomes the length of the entire case in seconds.

# Track list

Endpoint URL: [**https://api.vitaldb.net/trks**](https://api.vitaldb.net/trks)

This endpoint contains information related to the track.

The definition of each column is as follows.

| **Column Name** | **Description**  |
|-----------------|------------------|
| caseid          | case identifier  |
| tname           | track name       |
| tid             | track identifier |

Full list of tname is available [here](https://vitaldb.net/dataset/?query=overview&documentId=13qqajnNZzkN7NZ9aXnaQ-47NWy7kx-a6gbrcEsi-gak&sectionId=h.ixjqb61jh5dn).

# Track data

Endpoint URL: [**https://api.vitaldb.net/***TID*](https://api.vitaldb.net/trks/%7Btid)

To download the track data including the actual measurements of the track, you can send a GET request to the address. For *TID*, you can use the track id on the track list.

**All tracks in the same case use the same start time, therefore they are time-synchronized.**

Track data has two columns: Time and Values

The first column has the times (s) and the second column has corresponding values.

However, according to the track type (ttype), the stored form varies.

- Numeric data track

  - Rows with missing values are omitted.

  - Therefore, time intervals between rows can vary.

- Waveform data track

  - The time column has three values: start time (0), time interval (s), and end time (s).

  - Time intervals between rows are assumed constant (monotonically increasing time).

  - Rows with missing values are not omitted, therefore the data is loadable as an array.

<img src="images/web_api_open_dataset/image1.png" width="450" />

# Laboratory results

Endpoint URL: [**https://api.vitaldb.net/labs**](https://api.vitaldb.net/labs)

This endpoint contains the test results.

| **Variable Name** | **Description**                        |
|-------------------|----------------------------------------|
| caseid            | case identifier                        |
| dt                | test time (seconds based on casestart) |
| name              | test name                              |
| result            | test result                            |

Full list of laboratory test names is available [here](https://vitaldb.net/dataset/?query=overview&documentId=13qqajnNZzkN7NZ9aXnaQ-47NWy7kx-a6gbrcEsi-gak&sectionId=h.dn3zjfil6iw6).
