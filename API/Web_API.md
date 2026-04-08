# Introduction

Anyone can access and use the VitalDB platform by application programming interface (API). All API’s can be called using the HTTPS standard protocol.

## Endpoints

| **Endpoint URL** | **Method** | **Description** |
|----|----|----|
| [https://vitaldb.net/api/login](https://vitaldb.net/api/login) | POST | Issue an access token which is required to access VitalDB APIs. |
| [https://vitaldb.net/api/send](https://vitaldb.net/api/send) | POST | Upload real-time vital sign data of inputted vrcode to Web Monitoring. |
| [https://vitaldb.net/api/receive](https://vitaldb.net/api/receive) | GET | Get array of vital sign data of designated vrcode from inputted start time to inputted end time. |
| [https://vitaldb.net/api/filelist](https://vitaldb.net/api/filelist) | GET | Read file list of uploaded user files. |
| [https://vitaldb.net/api/tracklist](https://vitaldb.net/api/tracklist) | GET | Get a tracklist of files. |
| [https://vitaldb.net/api/download](https://vitaldb.net/api/download) | GET | Download a vital file from the cloud. |
| [https://vitaldb.net/api/upload](https://vitaldb.net/api/upload) | POST | Upload a vital file to the cloud. |

# Login API

Issue an access token which is required to access VitalDB APIs.

### Endpoint

[https://vitaldb.net/api/login](https://vitaldb.net/api/login)

### Method

POST

### Parameters

Please url-encode (RFC1738) the parameters if it has any special characters.

| **Field** | **Type** |
|-----------|----------|
| id        | String   |
| pw        | String   |

### Return Value

Content-type: application/json

| **Field** | **Type** | **Description** |
|----|----|----|
| access_token | String | An access token which is required to access VitalDB APIs |
| token_type | String | Always “bearer”, which is used for OAuth2. |
| expires_in | Number | Always 3600. The access token expires in an hour. |

### Sample Codes

<img src="images/web_api/image1.png" width="450" />

```
curl -v -d “id=userid&pw=password” https://vitaldb.net/api/login
```

# Web Monitoring API

A protocol for uploading vital signs data to VitalDB web monitoring.

<img src="images/web_api/image3.png" width="450" />

## Send

Upload real-time vital sign data of inputted vrcode to Web Monitoring.

### Endpoint

[https://vitaldb.net/api/send](https://vitaldb.net/api/send)

### Method

POST

### Parameters

Please url-encode (RFC1738) the parameters if it has any special characters.

| **Field** | **Type** | **Required** | **Description** |
|----|----|----|----|
| data | JSON String | Required | The posted data must include variables listed below. |

| **Variable Name** | **Description** |
|----|----|
| vrcode | Unique identification code of Vital Recorder consisting of 9 digit random numbers and alphabets. **The vrcode should be registered by user on the VitalDB Web Monitoring page before use.** |
| rooms | array of real-time vital sign data for each tab (room/bed) in Vital Recorder |

Each room is formatted as follows:

| **Variable Name** | **Description** |
|----|----|
| roomname | name of a tab |
| dtstart | start time of the transmitted data in unix timestamp |
| dtend | end time fo the transmitted data in unix timestamp |
| ptcon | whether or not patient is connected to Vital Recorder |
| recording | whether or not Vital Recorder is recording vital signs data |
| devs | array of information of devices connected to Vital Recorder |
| trks | array of track data such as ECG, HR, etc. |
| evts | array of event |

Each device is formatted as follows:

| **Variable Name** | **Description** |
|----|----|
| name | device name |
| status | ON/OFF status of the device |
| port | name of a serial communications port where the device is connected to |

Each track is formatted as follows:

| **Variable Name** | **Description** |
|----|----|
| name | track name |
| type | type of the track data: wave, number, string |
| srate | sample rate of the data |
| unit | unit of the track |
| recs | array of real-time data consisting of track value and time of the value |

### Sample Data

A sample data string in JSON is as below.

sample_data = '{"ver":"1.8.8.3","vrcode":"9a9uewrsv","rooms":[{"roomname":"DEMO","seqid":59,"dtstart":1607071644.806051,"dtend":1607071645.808981,"dtcase":1607071590.292408,"ptcon":1,"dtapp":1607071577.160322,"recording":1,"dgmt":-32400,"devs":[{"type":"Demo","name":"Demo","status":"on","ycable":"0","port":""}],"trks":[{"id":2109467744,"name":"EEG","type":"wav","montype":"EEG_WAV","srate":100,"mindisp":-100,"maxdisp":100,"color":"#dda0dd","unit":"uV","recs":[{"dt":1607071644.806051,"val":[-56.75,-58.05,-61,-65.2,-69.35,-71.05,-69.95,-66.65,-62.2,-54.05,-54.05,-55.05,-56.25,-61.15,-65.25,-68.15,-65.3,-63.4,-59,-53.7,-51.05,-50.85,-52.4,-56.65,-59.3,-62.1,-65.55,-65.8,-62.25,-58.95,-54.9,-50.65,-49.95,-49.95,-47.35,-46,-46.35,-46.7,-49.95,-52.65,-55.9,-59.5,-57.95,-55.25,-53.35,-49.4,-49.4,-53.05,-59,-56.9,-52.4,-47.1,-35,-32.9,-32.5,-31.9,-36.1,-38.75,-43.25,-49.55,-51.95,-54.9,-53.55,-46.9,-43.65,-39.25,-27.25,-26.05,-25.7,-27.7,-40.2,-47.2,-52.1,-54.65,-54,-51.35,-48.7,-41.25,-40.15,-40.1,-39.8,-44.3,-48.4,-52.4,-56.3,-57.1,-59.2,-60.6,-64.1,-67.2,-68.4,-70.85,-69.25,-66.4,-65.65,-68.15,-68.95,-68.9,-66.6,-64.25]}]},{"id":2109469360,"name":"NIBP_DBP","type":"num","montype":"NIBP_DBP","color":"#ffffff","unit":"mmHg","recs":[{"dt":1607071643.367762,"val":59},{"dt":1607071645.369666,"val":62}]}]}]}'

### Sample Codes

<img src="images/web_api/image1.png" width="450" />

curl -v -X POST https://vitaldb.net/api/send -d "data=sample_data"

<img src="images/web_api/image4.png" width="450" />

<?php

// A sample PHP Script to POST data using cURL

// MUST URL-encodes the data - https://www.php.net/manual/en/function.urlencode.php

$json = "data=".urlencode($sample_data);

// Initiate new cURL

$ch = curl_init('https://vitaldb.net/api/send');

curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

curl_setopt($ch, CURLINFO_HEADER_OUT, true);

curl_setopt($ch, CURLOPT_POST, true);

curl_setopt($ch, CURLOPT_POSTFIELDS, $json);

curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);

curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);

// Submit the POST request

$result = curl_exec($ch);

// Print curl information

var_dump(curl_getinfo($ch));

// Print response

var_dump($result);

## Receive

Get array of vital sign data of designated vrcode from inputted start time to inputted end time.

### Endpoint

[https://vitaldb.net/api/receive](https://vitaldb.net/api/receive)

### Method

GET

### Parameter

| **Field** | **Type**       |
|-----------|----------------|
| vrcode    | String         |
| bedname   | String         |
| dtstart   | Unix Timestamp |
| dtend     | Unix Timestamp |

### Return Value

Content-Type: application/json; charset=utf-8

Content-Encoding: gzip

Gzipped JSON encoded array of data with the same format explained in the **Parameter from the Send section**.

### Sample Codes

<img src="images/web_api/image1.png" width="450" />

curl --compressed -X POST https://vitaldb.net/api/receive -H "Content-Type:application/x-www-form-urlencoded" -d

"vrcode=xxxxxxxx&bedname=xxxx&dtstart=1628831566" > output.txt

<img src="images/web_api/image2.png" width="450" />

Sample code below downloads real-time data from the bed whose vrcode is ‘sample’.

Please use “**pip install vitaldb**” before running our sample code.

import vitaldb

if vitaldb.login(id="vitaldb_test", pw="vitaldb_test"):

res = vitaldb.receive('sample')

print(res)

# Myfiles API

## File List

Read file list of uploaded user files.

### Endpoint

[https://vitaldb.net/api/filelist](https://vitaldb.net/api/filelist)

### Method

GET

### Parameters

Please url-encode (RFC1738) the parameters if it has any special characters.

<table style="width:87%;">
<thead>
<tr>
<th><strong>Field</strong></th>
<th><strong>Type</strong></th>
<th><strong>Required</strong></th>
</tr>
<tr>
<th>access_token</th>
<th>String</th>
<th>Required</th>
</tr>
<tr>
<th>bedname</th>
<th>String</th>
<th>Optional</th>
</tr>
<tr>
<th>dtstart</th>
<th>Unix timestamp</th>
<th>Optional</th>
</tr>
<tr>
<th>dtend</th>
<th>Unix timestamp</th>
<th>Optional</th>
</tr>
<tr>
<th>dtuploadstart</th>
<th><p>Unix</p>
<p>timestamp</p></th>
<th>Optional</th>
</tr>
<tr>
<th>dtuploadend</th>
<th><p>Unix</p>
<p>timestamp</p></th>
<th>Optional</th>
</tr>
<tr>
<th>startdate</th>
<th>Date</th>
<th>Optional</th>
</tr>
<tr>
<th>enddate</th>
<th>Date</th>
<th>Optional</th>
</tr>
<tr>
<th>uploadstartdate</th>
<th>Date</th>
<th>Optional</th>
</tr>
<tr>
<th>uploadenddate</th>
<th>Date</th>
<th>Optional</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Return Value

- Content-Disposition: attachment;filename=json.gz;

- Content-Type: application/x-gzip

| **Field** | **Type** | **Description** |
|----|----|----|
| json.gz | File | A gzip compressed file that contains a list of file information in JSON format |
| filename | String | File name (ex) DEMO_210415_091812.vital |
| filesize | Number | File size in bytes |
| dtstart | Datetime | Recording start time |
| dtend | Datetime | Recording end time |
| dtupload | Datetime | Uploaded or lastly modified datetime |

### Sample Codes

<img src="images/web_api/image1.png" width="450" />

```
curl -i https://vitaldb.net/api/filelist?access_token=xxxxxxxx --output json.gz
```

<img src="images/web_api/image2.png" width="450" />

Please use “**pip install vitaldb**” before running our sample code.

import vitaldb

import os

import datetime

DOWNLOAD_DIR = "path/to/folder"

if not os.path.exists(DOWNLOAD_DIR):

os.mkdir(DOWNLOAD_DIR)

if vitaldb.login('ID', 'PASSWORD'):

for f in vitaldb.filelist(bedname="D1", dtstart="2010-10-01", dtend="2010-10-02")

opath = DOWNLOAD_DIR + "/" + f['filename']

if os.path.exists(opath):

continue

vitaldb.download(f['filename'], DOWNLOAD_DIR)

## Track List

Get a tracklist of files

### Endpoint

[https://vitaldb.net/api/tracklist](https://vitaldb.net/api/tracklist)

### Method

GET

### Parameters

Please url-encode (RFC1738) the parameters if it has any special characters.

<table style="width:87%;">
<thead>
<tr>
<th><strong>Field</strong></th>
<th><strong>Type</strong></th>
<th><strong>Required</strong></th>
</tr>
<tr>
<th>access_token</th>
<th>String</th>
<th>Required</th>
</tr>
<tr>
<th>bedname</th>
<th>String</th>
<th>Optional</th>
</tr>
<tr>
<th>dtstart</th>
<th>Unix timestamp</th>
<th>Optional</th>
</tr>
<tr>
<th>dtend</th>
<th>Unix timestamp</th>
<th>Optional</th>
</tr>
<tr>
<th>dtuploadstart</th>
<th><p>Unix</p>
<p>timestamp</p></th>
<th>Optional</th>
</tr>
<tr>
<th>dtuploadend</th>
<th><p>Unix</p>
<p>timestamp</p></th>
<th>Optional</th>
</tr>
<tr>
<th>startdate</th>
<th>Date</th>
<th>Optional</th>
</tr>
<tr>
<th>enddate</th>
<th>Date</th>
<th>Optional</th>
</tr>
<tr>
<th>uploadstartdate</th>
<th>Date</th>
<th>Optional</th>
</tr>
<tr>
<th>uploadenddate</th>
<th>Date</th>
<th>Optional</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Return Value

- Content-Disposition: attachment;filename=json.gz;

- Content-Type: application/x-gzip

| **Field** | **Type** | **Description** |
|----|----|----|
| json.gz | File | A gzip compressed file that contains a list of file information in JSON format |
| filename | String | File name (ex) DEMO_210415_091812.vital |
| trks | Array/List | Track list (ex) [‘SNUH/SNUADC’,...] |

## Download

Download a vital file from the cloud.

### Endpoint

[https://vitaldb.net/api/download](https://vitaldb.net/api/download)

### Method

GET

### Parameters

Please url-encode (RFC1738) the parameters if it has any special characters.

| **Field**    | **Type** |
|--------------|----------|
| access_token | String   |
| filename     | String   |
| asurl        | Boolean  |

### Return Value

| **Field** | **Type** | **Description** |
|----|----|----|
| Vital File | File | A vital file (if *asurl* is not 1) |
| URL for downloading vital file | String | If *asurl* is 1, the url for downloading the vital file will be sent. |

### Sample Codes

<img src="images/web_api/image1.png" width="450" />

```
curl -i https://vitaldb.net/api/download?access_token=xxxxxxxx&filename=xxx.vital
```

<img src="images/web_api/image2.png" width="450" />

Sample code below downloads a specific vital file from VitalDB to a local PC and prints the track names.

Please use “**pip install vitaldb**” before running our sample code.

import vitaldb

if vitaldb.login(id="vitaldb_test", pw="vitaldb_test"):

vf = vitaldb.VitalFile(vitaldb.download('TEST1_211020_142621.vital'))

print(vf.get_track_names())

<img src="images/web_api/image2.png" width="450" />

Sample code below reads filenames from an Excel file and downloads them to a local PC.

Please use “**pip install vitaldb**” before running our sample code.

import vitaldb

import os

import pandas as pd

DOWNLOAD_DIR = 'path/to/folder'

if not os.path.exists(DOWNLOAD_DIR):

os.mkdir(DOWNLOAD_DIR)

df = pd.read_excel('list.xlsx')

if vitaldb.login('ID', 'PASSWORD'):

for idx, row in df.iterrows():

filename = row['filename']

opath = DOWNLOAD_DIR + '/' + filename

if os.path.exists(opath):

continue

vitaldb.download(filename, DOWNLOAD_DIR)

## Upload

Upload a vital file to the VitalDB.

### Endpoint

[https://vitaldb.net/api/upload](https://vitaldb.net/api/upload)

### Method

POST

### Parameters

Please url-encode (RFC1738) the parameters if it has any special characters.

| **Field** | **Type** | **Required** | **Description** |
|----|----|----|----|
| vrcode | String | Required | Unique identification code of Vital Recorder consisting of 9 digit random numbers and alphabets. **The vrcode should be registered by user on the VitalDB Web Monitoring page before use.** |
| vitalfile | File | Required | File name must be in the right format: bedname_yymmdd_hhmmss.vital (ex) DEMO_210415_091812.vital |

### Return Value

Success
