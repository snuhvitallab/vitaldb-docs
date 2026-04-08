# Introduction

This guide document is intended to guide clinical researchers who wish to conduct research by collecting biosignal data from patient monitors in operating rooms, intensive care units and emergency rooms.

You can quickly install Vital Recorder and collect data by following this document.

## Preparations

- Windows compatible PC to run Vital Recorder

- USB to Serial Converter (1 port, 2 port, 4 port, etc.): This is a converter with a serial port on one side and a USB port on the other side. Many modern computers do not have a serial port, so a converter is required to receive signals from the serial port of the medical device and input them to the USB port of the computer.

- Cross Gender (required on some equipment): On some devices, the pin connection of the serial terminal requires a cross connection. Devices that require cross gender are listed in the document “Device Connection Guide”.

## Type of Serial Cables

Vital Recorder can only acquire data from medical devices with serial communication. Serial communication typically uses a 9-pin connector called DB9. The DB9 connector is divided into male/female terminals according to the shape of the terminal and direct/cross (or null modem) types depending on the pin map. Depending on the medical device, the correct terminal shape and pin connection is mandatory.

The following are examples of cables/genders needed depending on the type of medical device being used.

<table>
<thead>
<tr>
<th style="text-align: center;">Equipment side connector</th>
<th style="text-align: center;">Connection method</th>
<th style="text-align: center;">PC side connector</th>
<th style="text-align: center;">Gender</th>
<th style="text-align: center;">Devices</th>
</tr>
<tr>
<th style="text-align: center;">Female</th>
<th style="text-align: center;">Direct</th>
<th style="text-align: center;">Male</th>
<th style="text-align: center;">Does not require a gender. Directly connected with the USB Serial Converter.</th>
<th style="text-align: center;">GE, BIS</th>
</tr>
<tr>
<th style="text-align: center;">Female</th>
<th style="text-align: center;">Cross</th>
<th style="text-align: center;">Male</th>
<th style="text-align: center;"><p>F-M NULL MODEM</p>
<p><img src="images/getting_started/image1.png" width="450" /><img src="images/getting_started/image11.png" width="450" /></p>
<p>It must be labeled "NULL MODEM" in orange color.</p></th>
<th style="text-align: center;">Orchestra</th>
</tr>
<tr>
<th style="text-align: center;">Male</th>
<th style="text-align: center;">Direct</th>
<th style="text-align: center;">Male</th>
<th style="text-align: center;"><p>F-F gender changer</p>
<p><img src="images/getting_started/image3.png" width="450" /><img src="images/getting_started/image3.png" width="450" /></p>
<p>It is not labeled “NULL MODEM"; instead, labeled “gender changer” or “US Patent” in yellow color.</p></th>
<th style="text-align: center;">None</th>
</tr>
<tr>
<th style="text-align: center;">Male</th>
<th style="text-align: center;">Cross</th>
<th style="text-align: center;">Male</th>
<th style="text-align: center;"><p>F-F NULL MODEM</p>
<p><img src="images/getting_started/image1.png" width="450" /><img src="images/getting_started/image1.png" width="450" /></p>
<p>It must be labeled "NULL MODEM" in orange color.</p>
<p>If not available, it is acceptable to connect an F-F NULL MODEM after the F-M NULL MODEM.</p></th>
<th style="text-align: center;"><p>Invos, Edwards devices,</p>
<p>PHilips MP400-500 monitors,</p>
<p>CardioQ, FMS2000</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Windows Settings

## Turn off Sleep Mode

To prevent Windows from entering sleep mode while recording data, set the Screen Off and Sleep Mode settings to Never in the Settings> System> Power & Sleep tab as shown below.

<img src="images/getting_started/image9.png" width="450" />

## Prevent Automatic Windows Updates

Windows Automatic Updates may cause the Vital Recorder program to stop working.

You can use the following program to force Windows automatic updating to stop..

[http://greatis.com/blog/stopupdates10](http://greatis.com/blog/stopupdates10)

Even if you stop Windows automatic updating, we recommend that you keep your Windows secure by performing periodic manual updates at the time between data recording.

## Password-free Login Configuration in Windows

Right-click the Windows Start button and click Run (R) or press Windows Key + R to bring up the Run window.

Enter “control userpasswords2”.

<img src="images/getting_started/image7.png" width="450" />

Turn off the "Users must enter a user name and password to use this computer." option. If you click OK, you may need to enter your current password once.

<img src="images/getting_started/image4.png" width="450" />

# Vital Recorder Setup

## Vital Recorder Installation

Install the latest version of Vital Recorder from [http://vitaldb.net/vital-recorder/](http://vitaldb.net/vital-recorder/)

## Vital File Storage Path Setting

You create a folder in which to save your vital files and specify them in Vital Recorder's settings. Below, we used the path “C:\vital”.

<img src="images/getting_started/image6.png" width="450" />

## RPM (Remote Patient Monitoring) Setup

Vital Recorder's real-time monitoring capabilities allow you to monitor data collection remotely. To do this, your computer must be connected to the Internet. Copy the VR code in the Management menu from the Vital Recorder's Settings menu.

<img src="images/getting_started/image8.png" width="450" />

Log in to vitaldb.net with your account and register the code you copied in the VR Code field at http://vitaldb.net/web-monitoring/.

<img src="images/getting_started/image2.png" width="450" />

# Data Backup

Vital Recorder stores data in local storage (HDD, SSD) on the computer where the program is installed. However, you can maintain stability by backing up your data using a private or commercial cloud. We recommend using the two-way sync feature of your personal NAS (Network Attached Storage) to back up your data to the cloud and periodically delete data from your local computer. Below is an example of using Synology, a representative personal NAS device.

## Sync Program Settings

Install cloud station drive to synchronize data between Synology NAS and local storage.

[https://global.download.synology.com/download/Tools/CloudStationDrive/4.2.7-4415/Windows/Installer/Synology%20Cloud%20Station%20Drive-4.2.7-4415.msi](https://global.download.synology.com/download/Tools/CloudStationDrive/4.2.7-4415/Windows/Installer/Synology%20Cloud%20Station%20Drive-4.2.7-4415.msi)

Please refer to Synology homepage for detailed usage.

## File Management on Researcher Computers

The folders on the synced NAS can be synced back to the researcher's computer. Install Cloud Station Drive on the researcher’s computer and set up bidirectional synchronization with the data upload folder on your NAS. Deleting files in the Sync folder on the researcher's folder will simultaneously delete them from the local storage on all computers where the NAS and Vital Recorder are installed. You should calculate the storage space of all the depots and repeat the backup and deletion process periodically.

## Automated Backup and Versioning with Hyper Backup

Synology's Hyper Backup package allows you to recover data to an earlier point in time, even if you accidentally delete or overwrite it. See the links below to learn more about Hyper Backup..

[https://www.synology.com/ko-kr/knowledgebase/DSM/tutorial/Backup_Restore/How_to_back_up_your_data_to_a_remote_Synology_NAS_or_file_server_with_Hyper_Backup](https://www.synology.com/ko-kr/knowledgebase/DSM/tutorial/Backup_Restore/How_to_back_up_your_data_to_a_remote_Synology_NAS_or_file_server_with_Hyper_Backup)

# Research Using Collected Data

The biosignal data automatically collected by Vital Recorder is stored as a case file (* .vital).

## Creating Patient Information Summary File

Vital Recorder does not handle any personal information and therefore requires matching of vital files with corresponding patient information. Use Excel or Google Spreadsheets to registry each patient's case number and relevant clinical information and record each patient's case file name (* .vital) together.

<img src="images/getting_started/image10.png" width="450" />

## Batch Extraction of Data

The Vital Utility program, distributed with Vital Recorder, allows you to batch extract the desired tracks from the Vital files in a specific folder at the desired resolution. The extracted files can be loaded in analysis programs such as SPSS, R and Excel in csv format.

<img src="images/getting_started/image5.png" width="450" />

# Batch Processing Using Programming Language

To read or batch process data from multiple vital files, you must use a programming language. You can do this with the help of the utilities that are installed with Vital Recorder.

For example, vital_recs.exe is a utility program for batch extraction of data. This allows you to extract data samples from vital files in any programming language you are familiar with.

## Open Vital File with Python

import csv

import subprocess

ipath = "1.vital"

interval = 1

p = subprocess.Popen('**vital_recs.exe** -h "{}" {}'.format(ipath, interval), stdout=subprocess.PIPE)

output = p.communicate()[0].decode("utf-8")

for row in csv.reader(output.splitlines()):

print(row)

## Open Vital Files Using Python and Pandas libraries

import io

import subprocess

import pandas as pd

ipath = "1.vital"

interval = 1

p = subprocess.Popen('**vital_recs.exe** -h "{}" {}'.format(ipath, interval), stdout=subprocess.PIPE)

df = pd.read_csv(io.StringIO(p.stdout.read().decode('utf-8')), index_col=0)

print(df)

## Extract Vital File Tracks from Specific Folder with Python and Pandas

import io

import os

import csv

import subprocess

import pandas as pd

rootdir = r"//Vitalnew/vital_data/Monthly_Confirmed/SNUH_OR"

for dir, dirs, files in os.walk(rootdir):

for file in files:

ipath = '{}/{}'.format(dir, file)

cmd = '**vital_trks** {}'.format(ipath)

p = subprocess.Popen(cmd, stdout=subprocess.PIPE)

df = pd.read_csv(io.StringIO(p.stdout.read().decode('utf-8')), comment='#')

devs = []

for index, row in df.iterrows():

if row['tname'] != 'SV':

continue

devs.append(row['dname'])

if not devs:

continue

print('{},{}'.format(ipath[len(rootdir)+1:], ','.join(devs)))

## Open Vital File in R

load_vital <- function (path, interval=1) {

cmd <- paste0("**vital_recs.exe** -h ", path, " ", interval)

return (read.csv(pipe(cmd)))

}

\# load vital file and get samples at 1 sec interval

vit <- load_vital("1.vital", 1)

\# print maximum arterial pressure

print(max(vit$SNUADC.ART1, na.rm=TRUE))

# Conclusion

Congratulations on starting your biosignal data collection and research.

You can also use the collected data for collaborative research with other researchers.
