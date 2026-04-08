# Introduction

This document explains the VitalDB python library which helps the use of Vital file format and VitalDB data in Python language.

## Installation

VitalDB Python Library can be installed using the package installer for python (PIP).

```
$ pip install vitaldb
```

And then you need to import the vitaldb library.

```
import vitaldb
```

# Vital File API

You can read a track list from a vital file using *vital_trks* function.

<table>
<thead>
<tr>
<th><p>vitaldb.<strong>vital_trks</strong>(<em>ipath</em>)</p>
<p>Parameter list</p>
<ul>
<li><p><em>ipath</em>: vital file path to read</p></li>
</ul>
<p>Return value</p>
<ul>
<li><p>list of track names in the vital file</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

You can read the samples(values) in a vital file using vital_recs function. It returns the samples in a numpy array.

<table>
<thead>
<tr>
<th><p>vitaldb.<strong>vital_recs</strong>(<em>ipath, track_names=None, interval=None, return_timestamp=False, return_datetime=False, return_pandas=False, exclude=None</em>)</p>
<p>Parameter list</p>
<ul>
<li><p><em>ipath</em>: vital file path to read</p></li>
<li><p><em>track_names</em>: list of track names, eg) ['SNUADC/ECG', 'Solar 8000/HR']</p></li>
<li><p><em>interval</em>: interval of each sample. if None, maximum resolution. if there is no wave tracks, 1 sec</p></li>
<li><p><em>return_timestamp</em>: return unix timestamp</p></li>
<li><p><em>return_datetime</em>: return datetime of each sample at first column</p></li>
<li><p><em>return_pandas</em>: return pandas dataframe</p></li>
</ul>
<p>Return value</p>
<ul>
<li><p>numpy array of samples that have the same interval specified by the input argument.</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The library contains a VitalFile class to read and write Vital File Format.

<table>
<thead>
<tr>
<th><p>vitaldb.<strong>VitalFile</strong>(<em>ipath, track_names=None, header_only=False, skip_records=None, exclude=None, userid=None, maxlen=None, interval=None</em>)</p>
<p>Parameter list</p>
<ul>
<li><p><em>ipath</em>:</p>
<ul>
<li><p>caseid: caseid of open dataset</p></li>
<li><p>path: file path</p></li>
<li><p>list: list of file path to merge files</p></li>
</ul></li>
<li><p><em>track_names</em>: list or comma separated track names (with device names). If missing, all tracks are loaded.</p></li>
<li><p><em>header_only / skip_records</em>: read track information only if True. Othersize, all track data (default).</p>
<ul>
<li><p>True: read track names only</p></li>
</ul></li>
<li><p><em>exclude</em>: list or comma separated track names (with device names)</p></li>
<li><p><em>userid</em>: user ID if vitaldb.net when downloading a vital file or parquet file from the cloud</p></li>
<li><p><em>maxlen</em>: set max length of a VitalFile in seconds</p></li>
<li><p><em>interval</em>: interval of each sample. if None, maximum resolution. if there is no wave tracks, 1 sec</p></li>
</ul>
<p>Return value</p>
<ul>
<li><p>VitalFile object</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Sample Code

The following example code downloads a vital file with caseid of 1 to the current working directory.

<table>
<thead>
<tr>
<th><p>vf = vitaldb.VitalFile(1)</p>
<p>vf.to_vital('1.vital')</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Results:

You can open and visualize the downloaded vital file using the Vital Recorder.

<img src="images/python_library/image4.png" width="450" />

The next sample code downloads the SNUADC/ECG_II track only. It is faster than the former example.

<table>
<thead>
<tr>
<th><p>import vitaldb</p>
<p>vf = vitaldb.VitalFile(1, ['SNUADC/ECG_II'])</p>
<p>vf.to_vital('1.vital')</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Results:

<img src="images/python_library/image3.png" width="450" />

<table>
<thead>
<tr>
<th><p>vitaldb.<strong>read_vital</strong>(<em>ipath, track_names=None, exclude=None, header_only=False, maxlen=None</em>)</p>
<p>Parameter list</p>
<ul>
<li><p><em>ipath</em>: vital file path to read</p></li>
<li><p><em>track_names</em>: list of track names, eg) ['SNUADC/ECG', 'Solar 8000/HR']</p></li>
<li><p><em>exclude</em>: list or comma separated track names (with device names)</p></li>
<li><p><em>header_only</em>: read track information only if True.</p></li>
<li><p><em>maxlen</em>: set max length of a VitalFile in seconds.</p></li>
</ul>
<p>Return value</p>
<ul>
<li><p>VitalFile object read from .vital file</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<thead>
<tr>
<th><p>vitaldb.<strong>read_csv</strong>(<em>ipath, track_names=None, exclude=None, interval=None</em>)</p>
<p>Parameter list</p>
<ul>
<li><p><em>ipath</em>: vital file path to read</p></li>
<li><p><em>track_names</em>: list of track names, eg) ['SNUADC/ECG', 'Solar 8000/HR']</p></li>
<li><p><em>exclude</em>: list or comma separated track names (with device names)</p></li>
<li><p><em>interval</em>: interval of each sample. if None, maximum resolution. if there is no wave tracks, 1 sec</p></li>
</ul>
<p>Return value</p>
<ul>
<li><p>VitalFile object read from .csv file</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<thead>
<tr>
<th><p>vitaldb.<strong>read_wfdb</strong>(<em>ipath, track_names=None, exclude=None, header_only=False</em>)</p>
<p>Parameter list</p>
<ul>
<li><p><em>ipath</em>: vital file path to read</p></li>
<li><p><em>track_names</em>: list of track names, eg) ['SNUADC/ECG', 'Solar 8000/HR']</p></li>
<li><p><em>exclude</em>: list or comma separated track names (with device names)</p></li>
<li><p><em>header_only</em>:read track information only if True.</p></li>
</ul>
<p>Return value</p>
<ul>
<li><p>VitalFile object read from .csv.gz file, written in waveform-database format</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<thead>
<tr>
<th><p>vitaldb.<strong>read_parquet</strong>(<em>ipath, track_names=None, exclude=None</em>)</p>
<p>Parameter list</p>
<ul>
<li><p><em>ipath</em>: vital file path to read</p></li>
<li><p><em>track_names</em>: list of track names, eg) ['SNUADC/ECG', 'Solar 8000/HR']</p></li>
<li><p><em>exclude</em>: list or comma separated track names (with device names)</p></li>
</ul>
<p>Return value</p>
<ul>
<li><p>VitalFile object read from .parquet file</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

After loading the vital file, you can convert it to pandas or numpy format for data analysis.

<table>
<thead>
<tr>
<th><p>vitaldb.VitalFile.<strong>to_numpy</strong>(<em>track_names, interval, return_datetime=False, return_timestamp=False</em>)</p>
<p>Parameter list</p>
<ul>
<li><p><em>track_names</em>: list or comma separated track names (with device names)</p></li>
<li><p><em>interva</em>l: time interval of each row</p></li>
<li><p><em>return_datetime</em>: add time in datetime format to each record</p></li>
<li><p><em>return_timestamp</em>: add time in timestamp format to each record</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Sample Code

The following code downloads arterial waveform from the first case of open dataset and show.

<table>
<thead>
<tr>
<th><p>import vitaldb</p>
<p>import matplotlib.pyplot as plt</p>
<p>track_names = ['SNUADC/ART']</p>
<p>vf = vitaldb.VitalFile(1, track_names)</p>
<p>samples = vf.to_numpy(track_names, 1/100)</p>
<p>plt.figure(figsize=(20, 5))</p>
<p>plt.plot(samples[:, 0])</p>
<p>plt.show()</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<img src="images/python_library/image2.png" width="450" />

<table>
<thead>
<tr>
<th><p>vitaldb.VitalFile.<strong>to_pandas</strong>(<em>track_names, interval, return_datetime=False, return_timestamp=False</em>)</p>
<p>Parameter list</p>
<ul>
<li><p><em>track_names</em>: list or comma separated track names (with device names)</p></li>
<li><p><em>interval</em>: time interval of each row</p></li>
<li><p><em>return_datetime</em>: add time in datetime format to each record</p></li>
<li><p><em>return_timestamp</em>: add time in timestamp format to each record</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

You can save the vital files in several formats.

<table>
<thead>
<tr>
<th><p>vitaldb.VitalFile.<strong>to_vital</strong>(<em>opath, compresslevel=1</em>)</p>
<ul>
<li><p>Save as vital file</p></li>
</ul>
<p>Parameter list</p>
<ul>
<li><p><em>opath</em>: file path to save</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<thead>
<tr>
<th><p>vitaldb.VitalFile.<strong>to_csv</strong>(<em>opath, track_names, interval, return_datetime=False, return_timestamp=False</em>)</p>
<ul>
<li><p>Save as csv file</p></li>
</ul>
<p>Parameter list</p>
<ul>
<li><p><em>opath</em>: file path to save</p></li>
<li><p><em>track_names</em>: list of track names</p></li>
<li><p><em>interval</em>: time interval of each row</p></li>
<li><p><em>return_datetime</em>: add time in datetime format to each record</p></li>
<li><p><em>return_timestamp</em>: add time in timestamp format to each record</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<thead>
<tr>
<th><p>vitaldb.VitalFile.<strong>to_wfdb</strong>(<em>opath, track_names=None, interval=None</em>)</p>
<ul>
<li><p>Save as waveform-database file</p></li>
</ul>
<p>Parameter list</p>
<ul>
<li><p><em>opath</em>: file path to save</p></li>
<li><p><em>track_names</em>: list of track names</p></li>
<li><p><em>interval</em>: time interval of each row</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<thead>
<tr>
<th><p>vitaldb.VitalFile.<strong>to_wav</strong>(<em>opath, track_names, srate=None</em>)</p>
<ul>
<li><p>Save as wave file</p></li>
</ul>
<p>Parameter list</p>
<ul>
<li><p><em>opath</em>: file path to save</p></li>
<li><p><em>track_names</em>: list of track names</p></li>
<li><p><em>srate</em>: sample frequency</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<thead>
<tr>
<th><p>vitaldb.VitalFile.<strong>to_parquet</strong>(<em>opath</em>)</p>
<ul>
<li><p>Save as parquet file</p></li>
</ul>
<p>Parameter list</p>
<ul>
<li><p><em>opath</em>: file path to save</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

There are other functions for using and editing VitalFile.

<table>
<thead>
<tr>
<th style="text-align: left;"><p>vitaldb.VitalFile<strong>.crop</strong>(<em>dtfrom=None, dtend=None</em>)</p>
<ul>
<li><p>Cut the vital file to the desired time</p></li>
</ul>
<p>Parameter list</p>
<ul>
<li><p><em>dtfrom</em>: start time in unix timestamp format</p></li>
<li><p><em>dtend</em>: end time in unix timestamp format</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<thead>
<tr>
<th><p>vitaldb.VitalFile.<strong>get_track_names</strong>()</p>
<ul>
<li><p>Return only the track names contained in the vital file</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<thead>
<tr>
<th><p>vitaldb.VitalFile.<strong>get_track_samples</strong>(<em>dtname, interval</em>)</p>
<ul>
<li><p>Get samples of each track</p></li>
</ul>
<p>Parameter list</p>
<ul>
<li><p><em>* dtname:</em> list or comma separated track names (with device names)</p></li>
<li><p><em>* interval:</em> interval of samples in sec. if None, maximum resolution. if no resolution, 1/500</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<thead>
<tr>
<th><p>vitaldb.VitalFile.<strong>remove_track</strong>(<em>dtname</em>)</p>
<ul>
<li><p>Delete track by name</p></li>
</ul>
<p>Parameter list</p>
<ul>
<li><p><em>dtname</em>: device and track name</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<thead>
<tr>
<th><p>vitaldb.VitalFile.<strong>add_track</strong>(<em>dtname, recs, srate=0, unit=’’, mindisp=0, maxdisp=0</em>)</p>
<p>Parameter list</p>
<ul>
<li><p><em>dtname</em>: device and track name</p></li>
<li><p><em>recs</em>: list or comma separated dictionary with ‘val’ and ‘dt’ as key</p></li>
<li><p><em>srate</em>: If wave track, Hz of float type</p></li>
<li><p><em>unit</em>: unit of string type</p></li>
<li><p><em>mindisp</em>: minimum value</p></li>
<li><p><em>maxdisp</em>: maximum value</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<thead>
<tr>
<th><p>vitaldb.VitalFile.<strong>find_track</strong>(<em>dtname</em>)</p>
<ul>
<li><p>Find track from name</p></li>
</ul>
<p>Parameter list</p>
<ul>
<li><p><em>dtname</em>: device and track name</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Platform API

You can access the vital files from cloud storage or intranet server with the api module.

<table>
<thead>
<tr>
<th style="text-align: left;"><p>vitaldb.<strong>login</strong><em>(id, pw, host=None, port=None)</em></p>
<ul>
<li><p>Use the setserver function above to set the site with given host and port</p></li>
</ul>
<p>Parameter list</p>
<ul>
<li><p><em>id</em>: id to login</p></li>
<li><p><em>pw</em>: pw to login</p></li>
<li><p><em>host:</em> IP address (default value: vitaldb.net)</p></li>
<li><p><em>port:</em> string type of port number</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<thead>
<tr>
<th style="text-align: left;"><p>vitaldb.<strong>filelist</strong><em>(bedname=None, dtstart=None, dtend=None)</em></p>
<ul>
<li><p>request file list</p></li>
</ul>
<p>Parameter list</p>
<ul>
<li><p><em>bedname</em>: bed name and bed number connected with “_”</p></li>
<li><p><em>dtstart</em>: start time in “Y-m-d h:m:s” format</p></li>
<li><p><em>dtend</em>: end time in “Y-m-d h:m:s” format</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<thead>
<tr>
<th><p>vitaldb.<strong>download</strong><em>(filename, localpath=None)</em></p>
<ul>
<li><p>Request file download</p></li>
</ul>
<p>Parameter list</p>
<ul>
<li><p><em>filename</em>: file name to download(‘0000_00_000000_000000.vital’)</p></li>
<li><p>localpath: local path to download</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Sample code

The following sample code downloads all vital files with bedname and periods.

<table>
<thead>
<tr>
<th><p>import vitaldb</p>
<p>import pandas as pd</p>
<p>import os</p>
<p># path to save downloaded files</p>
<p>DOWNLOAD_DIR = "Download"</p>
<p>SERVER_IP = 'xxx.xx.xxx.xxx'</p>
<p>SERVER_PORT = '80'</p>
<p>LOGIN_ID = '' # Please enter your login id</p>
<p>LOGIN_PW = '' # Please enter your login password</p>
<p>BED_NAME = "MICU"</p>
<p>START_DATE = "2022-01-01"</p>
<p>END_DATE = "2022-01-31"</p>
<p>if vitaldb.login(LOGIN_ID, LOGIN_PW, SERVER_IP, SERVER_PORT): # login</p>
<p># check filelist</p>
<p>filelist = vitaldb.filelist(bedname=BED_NAME, dtstart=START_DATE, dtend=END_DATE)</p>
<p>print(pd.DataFrame(filelist))</p>
<p>if not os.path.exists(DOWNLOAD_DIR):</p>
<p>os.mkdir(DOWNLOAD_DIR)</p>
<p># files load &amp; download</p>
<p>for file in filelist:</p>
<p>print('downloading ' + file['filename'], end='...')</p>
<p>localpath = DOWNLOAD_DIR + '/' + file['filename']</p>
<p>res = vitaldb.download(file['filename'], localpath)</p>
<p>print('done')</p>
<p>else:</p>
<p>print('login error')</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Dataset API

You can use vitaldb open datasets with vitaldb python library.

## Find cases in the VitalDB open dataset

<table>
<thead>
<tr>
<th><p>caseids = vitaldb.find_cases(['ECG_II', 'ART'])</p>
<p>len(caseids)</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Results: 3644

## Read an open dataset case

<table>
<thead>
<tr>
<th><p>vals = vitaldb.load_case(caseids[0], ['ECG_II','ART'], 1/100)</p>
<p>print(vals)</p>
<p>ecg = vals[:,0]</p>
<p>art = vals[:,1]</p>
<p># plot</p>
<p>import matplotlib.pyplot as plt</p>
<p>plt.figure(figsize=(20,10))</p>
<p>plt.subplot(211)</p>
<p>plt.plot(ecg[110000:111000], color='g')</p>
<p>plt.subplot(212)</p>
<p>plt.plot(art[110000:111000], color='r')</p>
<p>plt.show()</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Results:

[[ nan nan]

[ nan nan]

[ nan nan]

...

[ 0.148893 -32.5087 ]

[ -0.325087 19.8266 ]

[ nan nan]]

<img src="images/python_library/image1.png" width="450" />
