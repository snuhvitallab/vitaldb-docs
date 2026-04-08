# Introduction

Vitalserver is developed to make the VitalDB server available on a hospital's internal network. This manual explains how to set up and run Vitalserver and how to use it.

Notes: This guide is based on the 2025-02-27 version.

# Installation

* Skip this section, if our research team visited your institution for the installation and setup.

1.  Download vitalserver.zip from [https://vitaldb.net/vitalserver.php](https://vitaldb.net/vitalserver.php) and unzip the file to the C drive.

2.  Install Redis and NodeJS from C:/vitalserver/install. Node version MUST be v.12.16.2.

3.  Right-click C:/vitalserver/service/include/config.js, and click Edit.

4.  Enter a folder path to store vital files as shown below.

    1.  const file_folder = “Z:/”;

    2.  **If you are storing vital files on a NAS, please refer to the following link.** [https://kb.synology.com/en-us/DSM/tutorial/How_to_map_shared_folder_Windows_PC](https://kb.synology.com/en-us/DSM/tutorial/How_to_map_shared_folder_Windows_PC)

5.  Double-click server_start.bat located in C:/vitalserver to run the server. We recommend moving server_start.bat to the Desktop folder for convenience.

6.  Server IP and port are set to 127.0.0.1:80 as default. To change the server settings, please see [Server IP Setting](#server-ip-setting) of Server Configuration below.

# Server Configuration

Please log in on Vitalserver as admin to set up the server.

1.  Open a web browser on the PC where you installed the server.

2.  Enter “localhost” in the address bar and press Enter key to access the server.

3.  Log in to the admin account (ID: admin, PW: admin). To change the admin password, see the [Account Settings](#account-settings) section below.

4.  Go to Manage > Server.

> <img src="images/user_manual/image21.png" width="450" />

<img src="images/user_manual/image15.png" width="450" />

## Server IP Setting

Server IP defaults to localhost, so the IP must change to the static IP address for the other PCs and VitalRecorder devices to access the server. And, if the port is other than the default value of 80, modify the Server Port and click the Submit button to save the settings.

**To apply the changes, restart the server by closing the Command Prompt and clicking server_start.bat.**

## Filter Server IP Setting

These settings are required to use the Filter feature in Web Monitoring. This is the same function as the filter in VitalRecorder for Windows.

## VitalRecorder(VR) Upgrade

<img src="images/user_manual/image19.png" width="450" />

This section is for upgrading VR devices.

- If the server PC has access to [VitalDB](https://vitaldb.net), you can upload the latest upgrade file to the server by clicking the “Download From VitalDB” button.

- If you cannot access VitalDB, download the latest upgrade file from [VitalRecorder: VitalDB](https://vitaldb.net/vital-recorder/) with a PC that can use an external network, and then upload the file to the Vitalserver. Drop the file in the box (Drop files here to upload) to upload.

- Once the upgrade file has been uploaded to the server, you can upgrade all VR devices with the Upgrade All button. You can also upgrade from the web monitoring page. Please refer to the [Web Monitoring](#web-monitoring) section.

## User Management

On the Users page, the admin can add or delete users.You can share your Web Monitoring views or recorded files with other researchers by giving them a new account and permissions. It is convenient to create accounts on a per-ward basis when using the server as a central monitor.

<img src="images/user_manual/image2.png" width="450" />

- On the right side of the page, enter User ID, Name, Email and Profile, then click Submit to create a user.

- **Password of the new account is the same as the account’s ID.**

- To delete a user, select the user in the Users list and click the Delete button.

## HL7 Settings

This feature is to help with EMR recording. For inquiries about using HL7 features, please contact us.

# Account Settings

Users can edit their account information on the Manage My Account page.

<img src="images/user_manual/image16.png" width="450" /><img src="images/user_manual/image25.png" width="450" />

Enter the password in the input above the Submit button for the authentication and click Submit to save the changed information.

# Web Monitoring

On the Web Monitoring page, you can view a patient's vital signs in real time broadcasted from the PiVR or VitalRecorder for Windows. Also, you can group the monitors and filter them by group, and manage VRs remotely.<img src="images/user_manual/image17.png" width="450" />

## Group

<img src="images/user_manual/image22.png" width="450" /><img src="images/user_manual/image26.png" width="450" />

Click the Group button on the upper-left of the page to see the group list as shown above.

- If no groups are selected, you will see all monitors, including ungrouped monitors.

- If All is selected, you will see all monitors that are grouped.

- If you select one or more groups, you see the monitors in the selected groups.

- When you mouse over a group, you will see a pencil button next to the group name, as shown in the image at top left. When you click it, the Edit Group Name pop-up appears, allowing you to edit the group name.

## Manage VR

Manage VR allows you to apply VR settings in bulk. You can view all VR names, VR code, OS, and more at once.

<img src="images/user_manual/image7.png" width="450" />

- In the upper left corner, the box labeled CCU is the group selection function. You can see a list of VR devices by group. To the right of the group selection, click Add Group to add a new group.

- All functions in the Actions menu can be applied in bulk. Click the checkboxes of the VRs and select an action from the Actions menu to apply.

  - Change Group: change the group of selected VRs. If you select Add Group and enter a new group name, the VRs are set to the new group.

> <img src="images/user_manual/image20.png" width="450" />

- Change Permission: grant permissions to other accounts..

  - View: permission to view real-time monitoring on the Web Monitoring page.

  - Download: permission to view and download recorded files from My Files page.

  - Manage: permission to control the monitor’s device setting, version control, and etc.

> <img src="images/user_manual/image12.png" width="450" />

- Filter Settings: this feature predicts various factors like low blood pressure. To use this, the Filter server installation is needed.

> <img src="images/user_manual/image8.png" width="450" />

- Upgrade VR: Upgrade selected VRs remotely. Please refer to the [VR Upgrade](#vitalrecordervr-upgrade) section above to upload the upgrade file to the server before using it.

> <img src="images/user_manual/image13.png" width="450" />

- Delete VR: Delete the selected VRs. “delete” must be typed in the input as shown below.

> <img src="images/user_manual/image3.png" width="450" />

## Other Functions

There are functions other than Group and Manage VR such as filtering monitors by patient existence or by network status.

<img src="images/user_manual/image4.png" width="450" /><img src="images/user_manual/image5.png" width="450" />

The picture below is an example that illustrates the functions.

<img src="images/user_manual/image18.png" width="450" />

- Filtering monitors by patient existence

  - When clicked, only the monitors with patients in them will be visible. In the example above, only CCU_1 would be visible.

- Filtering monitors by network status

  - With a single click, you will only see monitors that are connected to the network. For example, CCU_1 and CCU_3 would be visible.

  - Double-click to see only the disconnected monitors like CCU_2. CCU_2 has a disconnected icon next to the name and it says "7d 13h", which means it has been disconnected for 7 days and 13 hours.

  - CCU_3 is the monitor that is connected to the network but is on standby because there is no patient in the bed.

- Arranging monitors by selecting the number of columns per row

  - The number of columns can be set from 1 to 10.

  - Above, it's set to 3, so you can see three monitors in a row, CCU_1, CCU_2, and CCU_3.

- Refresh button: to refresh the page.

- Fullscreen button: The web browser will go fullscreen and the web monitoring page will also switch to fullscreen mode.

## Monitor Menu

<img src="images/user_manual/image14.png" width="450" />

- When you hover over the monitor, you can see the corresponding VR information as shown in the center of the image above: from left to right, the bed name, VR Code, and VitalRecorder software version. The last mosaic is the IP address of the VR device.

- The "+ Add Event" function in the upper right corner adds an event with the current time to the file being recorded.

Double-clicking on a monitor switches the selected monitor to magnified mode, as shown below.

<img src="images/user_manual/image23.png" width="450" />

- The graph on the left side of the screen is the patient’s trend history for the past four hours.

- You can replay the last four hours with the controller on the bottom left of the screen.

Right-clicking on the monitor brings up a dropdown list, as shown below.

- Network Settings (*Only available with PiVR)*: Accessing the network setting page of PiVR remotely. VR’s IP address with port 80 must be open for this function to be working. <img src="images/user_manual/image11.png" width="450" />

- Device Settings: To add/modify device settings to VR.

- Filter Settings: To predict various factors, such as predicting low blood pressure. To use the Filter feature, you need to install the Filter server.

- View Logs (*Only available with PiVR)*: This feature reads PiVR's logs in real-time. You can check the logs from the browser's DevTools console.

- Change Permission: Edit view/download/manage permissions given to other users.

- Change Group

- Upgrade VR (*Only available with PiVR):* PiVR Remote Upgrade Feature

- Delete Bed

- Restart VR

- Reboot: Rebooting VR device remotely.

# My Files

On My files page, you can search, view, and download vital files recorded by PiVR or WinVR.

<img src="images/user_manual/image24.png" width="450" />

## Search Files

On this page, you can search for files under various conditions as shown in the figure above.

- Start Date, End Date: search files based on the date the file was recorded

- Bed: file search by bed name/operating room

- Search Keyword: search by filename.

- Tracks: list files by device/parameter name

## File List

- Filename, recording start time/end time, file uploaded time, and size are shown in the list.

- The list of files in the center of the above image is the result of searched files recorded on 2022-12-27, where ABP, CO2, CVP, ECG_II_WAV, and HR tracks were acquired from the Intellivue device.

## File View

<img src="images/user_manual/image1.png" width="450" /><img src="images/user_manual/image10.png" width="450" />

- When you click a file name in the list, you'll see a preview of the file on the right side of the My Files page.

- You can check the overall history without downloading the file.

- How to operate Track View (left picture)

  - Mouse Scroll1: scroll over the track name to scroll track list up/down.

  - Mouse Scroll2: zoom in/out the view by scrolling over the point you want to take a look.

  - Mouse drag: Drag the mouse left/right to move the time bar.

- Monitor View (right picture)

  - Click the Monitor View button on the top right of the track view to switch to the monitor view mode.

  - The operation is the same as the monitor on the Web Monitoring page.

# Frequently Asked Questions

**The server is running, but the page does not appear in the browser. What should I do?**

Please check if there are multiple Command Prompt (cmd) windows running the server. Make sure only one instance is active.

If you are using a NAS, the following are common causes:

- The NAS is powered off:\
  If the power button on the NAS does not show a blue light as indicated in the image below, please press the power button to turn on the NAS.

<img src="images/user_manual/image9.png" width="450" />

- The connection between the server PC and the NAS is lost:\
  In the example below, the Y drive on the left indicates a disconnected drive, while the Z drive is a properly connected drive. You can check this in File Explorer > This PC on the server PC.\
  If a drive such as Y appears disconnected, please refer to step 3 of the [Installation](#installation) guide.

> <img src="images/user_manual/image6.png" width="450" />

#

# Contacts

**Research and Development**

*Professor*

Hyung Chul Lee

vital@snu.ac.kr

**Vitalserver**

*Researcher*

Eunsun Rachel Lee

eunsun.lee93@snu.ac.kr

**Vital Recorder**

*Researcher*

Dayeon Sim

dayeonsim@snu.ac.kr

# Acknowledgement

The rights of Vitalserver belong to Seoul National University, and the rights of distribution and sales have been transferred to iTech.

Unauthorized reproduction and distribution of this program is subject to legal restrictions.
