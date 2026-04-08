# Introduction

Anyone can access and use the Vitalserver platform by application programming interface (API). All API’s can be called using the http standard protocol.

## Endpoints

| **Endpoint** | **Method** | **Description** |
|----|----|----|
| http://SERVER_IP:PORT/api/login | POST | Issue an access token which is required to access Vitalserver APIs. |
| http://SERVER_IP:PORT/api/bedlist | GET | Retrieve a bed list registered on Vitalserver. |
| http://SERVER_IP:PORT/api/receive | GET | Returns web monitoring data by bedname and dt |
| http://SERVER_IP:PORT/adt/yyyy/mm/dd | GET | Returns hid-filename list in csv file. |
| http://SERVER_IP:PORT/api/filelist | GET | Read file list of uploaded user files. |
| http://SERVER_IP:PORT/api/tracklist | GET | Get a tracklist of files. |
| http://SERVER_IP:PORT/api/download | GET | Download a vital file from the cloud. |

# Login API

Issue an access token which is required to access Vitalserver APIs.

### Endpoint

http://SERVER_IP:PORT/api/login

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
| access_token | String | An access token which is required to access Vitalserver APIs. |
| token_type | String | Always “bearer”, which is used for OAuth2. |
| expires_in | Number | Always 3600. The access token expires in an hour. |

### Sample Codes

<img src="images/intranet_api/image3.png" width="450" />

```
curl -v -d “id=userid&pw=password” http://SERVER_IP:PORT/api/login
```

# Bed list API

Retrieve a bed list registered on Vitalserver.

### Endpoint

http://SERVER_IP:PORT/api/bedlist

### Method

GET

### Parameters

Please url-encode (RFC1738) the parameters if it has any special characters.

| **Field**    | **Type** |
|--------------|----------|
| access_token | String   |

### Return Value

Content-Type: application/json; charset=utf-8

Array of bed list

### Sample Codes

<img src="images/intranet_api/image3.png" width="450" />

```
curl -v -d “access_token=xxxxxxxxx” http://SERVER_IP:PORT/api/bedlist
```

# Real-time API

## Receive

Returns vital sign data of input bed name, start time, and end time as long as the account has permission.

### Endpoint

http://SERVER_IP:PORT/api/receive

### Method

GET

### Parameter

<table>
<thead>
<tr>
<th><strong>Field</strong></th>
<th><strong>Type</strong></th>
<th><strong>Required</strong></th>
<th><strong>Description</strong></th>
</tr>
<tr>
<th>access_token</th>
<th>String</th>
<th>Required</th>
<th>An Access token which is required to access Vitalserver APIs.</th>
</tr>
<tr>
<th>bedname</th>
<th>String</th>
<th>Required</th>
<th><p>Bedname</p>
<ul>
<li><p>case-sensitive</p></li>
<li><p>comma-separation available for multiple bed request</p></li>
</ul></th>
</tr>
<tr>
<th>dtstart</th>
<th>Unix Timestamp</th>
<th>Optional</th>
<th><p>Start time in Unix Timestamp format</p>
<ul>
<li><p><strong>Default:</strong> current time - 10 in second.</p></li>
</ul></th>
</tr>
<tr>
<th>dtend</th>
<th>Unix Timestamp</th>
<th>Optional</th>
<th><p>End time in Unix Timestamp format.</p>
<ul>
<li><p><strong>Default:</strong> dtstart + 60, which is a minute after from dtstart</p></li>
<li><p><strong>Max value:</strong> dtstart + 3600, must be within an hour from dtstart.</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Return Value

Content-Type: application/json; charset=utf-8

Content-Encoding: gzip

Gzipped JSON encoded data

### Sample Codes

<img src="images/intranet_api/image2.png" width="450" />

Sample code below downloads real-time data from the bed whose vrcode is ‘sample’.

Please use “**pip install vitaldb**” before running our sample code.

import vitaldb

import json

if vitaldb.login('ID', 'PASSWORD', 'SERVER_IP', 'SERVER_PORT'):

res = vitaldb.receive(bedname='TEST1, TEST2')

for key in res:

res[key] = res[key]

print(res[key].keys())

with open('result.json', 'w', encoding='utf-8') as f:

json.dump(res, f, ensure_ascii=False, indent=4)

# Myfiles API

## ADT

returns .csv file of adt list (filename - hid matching list)

** might not be applicable to some hospitals for the security issue*

### Endpoint

http://SERVER_IP:PORT/adt/yyyy/mm/dd

### Method

GET

### Parameters

| **Field** | **Type** | **Required** |
|-----------|----------|--------------|
| yyyy      | string   | Required     |
| mm        | string   | Optional     |
| dd        | string   | Optional     |

### Return Value

- Content-Disposition: attachment;filename=yyyymmdd.csv;

- Content-Type:text/csv

| **Field** | **Type** | **Description**                              |
|-----------|----------|----------------------------------------------|
| hid1      | String   | Patient ID                                   |
| hid2      | String   | Patient ID                                   |
| filename  | String   | Vital Filename (bedname_yymmdd_hhmmss.vital) |

## File List

Read file list of uploaded user files.

### Endpoint

http://SERVER_IP:PORT/api/filelist

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
<th>hid</th>
<th>String</th>
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

<img src="images/intranet_api/image3.png" width="450" />

```
curl -i http://SERVER_IP:PORT/api/filelist?access_token=xxxxxxxx --output json.gz
```

<img src="images/intranet_api/image2.png" width="450" />

Please use “**pip install vitaldb**” before running our sample code.

import vitaldb

import os

import datetime

DOWNLOAD_DIR = "path/to/folder"

if not os.path.exists(DOWNLOAD_DIR):

os.mkdir(DOWNLOAD_DIR)

if vitaldb.login('ID', 'PASSWORD', 'SERVER_IP', 'SERVER_PORT'):

for f in vitaldb.filelist(bedname="D1", dtstart="2010-10-01", dtend="2010-10-02")

opath = DOWNLOAD_DIR + "/" + f['filename']

if os.path.exists(opath):

continue

vitaldb.download(f['filename'], opath)

## Track List

Get a tracklist of files

### Endpoint

http://SERVER_IP:PORT/api/tracklist

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

### Sample Codes

<img src="images/intranet_api/image2.png" width="450" />

Please use “**pip install vitaldb**” before running our sample code.

import vitaldb

if vitaldb.login('ID', 'PASSWORD', 'SERVER_IP', 'SERVER_PORT'):

res = vitaldb.tracklist(bedname='SICU2_12', dtstart="2023-07-10", dtend="2023-07-10")

print(res)

\# Result Example: [{'filename': 'SICU2_12_230710_000010.vital', 'trks': ['Intellivue/FLOW_WAV', 'Intellivue/AWP_WAV', 'Intellivue/ECG_II_WAV']}, ...]

## Download

Download a vital file from the cloud.

### Endpoint

http://SERVER_IP:PORT/api/download

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

<img src="images/intranet_api/image3.png" width="450" />

```
curl -i http://SERVER_IP:PORT/api/download?access_token=xxxxxxxx&filename=xxx.vital
```

<img src="images/intranet_api/image2.png" width="450" />

Sample code below downloads a specific vital file from Vitalserver to a local PC and prints the track names.

Please use “**pip install vitaldb**” before running our sample code.

import vitaldb

if vitaldb.login('ID', 'PASSWORD', 'SERVER_IP', 'SERVER_PORT'):

vf = vitaldb.VitalFile(vitaldb.download('TEST1_211020_142621.vital'))

print(vf.get_track_names())

<img src="images/intranet_api/image2.png" width="450" />

Sample code below reads filenames from an Excel file and downloads them to a local PC.

Please use “**pip install vitaldb**” before running our sample code.

import vitaldb

import os

import pandas as pd

DOWNLOAD_DIR = 'path/to/folder'

if not os.path.exists(DOWNLOAD_DIR):

os.mkdir(DOWNLOAD_DIR)

df = pd.read_excel('list.xlsx')

if vitaldb.login('ID', 'PASSWORD', 'SERVER_IP', 'SERVER_PORT'):

for idx, row in df.iterrows():

filename = row['filename']

opath = DOWNLOAD_DIR + '/' + filename

if os.path.exists(opath):

continue

vitaldb.download(filename, DOWNLOAD_DIR)
