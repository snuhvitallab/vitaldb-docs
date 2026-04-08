# Materials

- 1 Window PC for Vitalserver

- 1 Window PC for VitalRecorder

- (Optional) Wi-Fi Router

# Vitalserver

1.  Download vitalserver.zip from [https://vitaldb.net/vitalserver.php](https://vitaldb.net/vitalserver.php) and unzip the file to the C drive.

2.  Install Redis and NodeJS from C:/vitalserver/install. Node version MUST be v.12.16.2.

3.  Right-click C:/vitalserver/service/include/config.js, and click Edit.

4.  Enter a folder path to store vital files as shown below and Save the config.

> <img src="images/setup_step_by_step/image6.png" width="450" />

5.  Double-click server_start.bat located in C:/vitalserver to run the server. We recommend moving server_start.bat to the Desktop folder for convenience.

6.  Server IP address is set to 127.0.0.1:80 as default. However, it must change to a static IP address, the same IP as the PC’s IP given by your institution’s network team or set by your Wi-Fi router, that is reachable from the other PC within the same network for data exchange.<img src="images/setup_step_by_step/image9.png" width="450" />

    1.  Open a web browser on the PC where you installed the server.

    2.  Enter “localhost” or “127.0.0.1” in the address bar and press Enter.

    3.  Please log in as admin(ID:admin, PW:admin).

    4.  Go to Manage > Server.

    5.  Set Server IP and Server Port and Submit.

    6.  To apply the changes, restart the server by closing the Command Prompt and clicking server_start.bat.

    7.  Now you can access the server with the new IP address, not localhost.

# VitalRecorder For Windows (version >= 1.10.21)

1.  Download [VitalRecorder (click here to download directly)](https://vitaldb.net/getvr.php?type=msi) from [VitalRecorder:VitalDB (vitaldb.net/vital-recorder)](https://vitaldb.net/vital-recorder/) and double-click the installer file.

    - If you execute the installer, a warning popup will appear like the figure below. Please click **More Info > Run anyway** to continue the installation.

<img src="images/setup_step_by_step/image1.png" width="450" /><img src="images/setup_step_by_step/image4.png" width="450" />

2.  Run VitalRecorder (VR), then VR with initial settings will show up .

3.  Change the bed name as instructed below, and click the cog button to set up VR for Vitalserver.

> <img src="images/setup_step_by_step/image5.png" width="450" />

4.  Click Add Device button, select Demo (at the very bottom of the list) and OK. Please add Demo for the first try because you need to make sure if the intranet setting is proper, and the VR communicates with the server properly.

> <img src="images/setup_step_by_step/image7.png" width="450" />

5.  Click the pencil button under the Configuration File section to edit the vr.conf file. Open the file with Notepad.

> <img src="images/setup_step_by_step/image8.png" width="450" />

6.  Add SERVER_IP line as shown below. Enter Vitalserver’s IP address and port, save and close the file.

> <img src="images/setup_step_by_step/image2.png" width="450" />

7.  **Please DO NOT click OK or Apply on the Setting window, but Cancel or X button.** Otherwise, VR will reset the configuration file. Close All the VR windows and restart VR to apply the change.

8.  Access or Refresh the Web Monitoring page on Vitalserver. If the PC, where VR is running, is within the same intranet with the Vitalserver, a new VR monitor will appear.

> <img src="images/setup_step_by_step/image3.png" width="450" />
