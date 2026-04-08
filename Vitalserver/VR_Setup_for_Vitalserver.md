# Introduction

This manual explains how to use Vital Recorder, a software that collects and analyzes vital signs data through communication with various medical devices. Please read them in order.

# Device setup

## **Add a device**

The first thing to do after installing Vital Recorder is to add medical devices, which you want to acquire data from. You can add a device by clicking <img src="images/vr_setup/image3.png" width="450" /> button on the Devices tab.

<img src="images/vr_setup/image9.png" width="450" />

NOTE: If the Device tab is not visible, press Ctrl + D or click the Show Device tab button.

<img src="images/vr_setup/image8.png" width="450" />

The list of medical devices supported by Vital Recorder (version 1.10.4 and higher) is as follows.

## **Supported Medical Devices**

- Analog to Digital Converter (ADC)

<!-- -->

- SNUH: SNUADC (custom ADC)

- SNUH: SNUADCM (custom ADC)

- DataQ: DI-149

- DataQ: DI-155

- DataQ: DI-1100

- DataQ: DI-1120

- National Instruments: USB-6008

- Line In (record the Line In connector voltage of the computer sound card)

<!-- -->

- Patient monitor

<!-- -->

- GE: Solar 8000

- GE: Dash 2500-4000

- GE: MPS

- GE: Bx50

- Philips: Intellivue series

- Draeger: Infinity

- Nihon Kohden: BSM

- MEKICS: MEKICS

<!-- -->

- Multifunction monitor

<!-- -->

- Masimo: Root

- Masimo: Radical 7

- Sentec: SDM

<!-- -->

- Anesthesia machine

<!-- -->

- Drager: Primus

- Drager: Medibus X

- GE: Datex-Ohmeda

<!-- -->

- Mechanical ventilator

- Maquet: Servo-i

- Hamilton: Hamilton

- Drug infuser.

<!-- -->

- Fresenius Kabi: Orchestra

- Fresenius Kabi: Link +

- Fresenius Kabi: Agilia

- BBraun: SpaceCom

- Bionet: Pion TCI

<!-- -->

- Brain monitor/ Depth of anesthesia monitor

<!-- -->

- Covidien: BIS

- Covidien: A2000

- Covidien: Invos

- MDMS: ANIMonitor

- MDMS: ANIMonitor2

- Inbody: PLEM100

- BrainU: CAI

<!-- -->

- Neuromuscular monitor

<!-- -->

- BlinkDC: TwitchView

- IDMed: TOFScan

- RGB: Tofcuff

<!-- -->

- Fluid infuser

<!-- -->

- Belmont: FMS2000

<!-- -->

- Cardiac monitor

<!-- -->

- Edwards Lifesciences: Vigilance

- Edwards Lifesciences: Vigileo

- Edwards Lifesciences: EV-1000

- Edwards Lifesciences: HemoSphere

- Edwards Lifesciences: ClearSight

- Deltex: CardioQ

- LiDCO: LiDCO

- Bilab: AirTom

- Bilab: HemoVista

<!-- -->

- ETC

<!-- -->

- Demo (generates demo signals including waveforms and numeric data)

- Laxtha : LXD

- SNUH : SKNA

- MELAB : SNUPATCH

- MELAB : SNUEEG

If you click <img src="images/vr_setup/image3.png" width="450" /> button, the following dialog box appears. You can add any kind of equipment here.

CAUTION: Before adding a device, the device driver must be installed and the device must be physically, with the proper cable, connected to the PC where Vital Recorder is running. For details on how to connect the device, refer to the [Hardware Connection Guide.](https://vitaldb.net/docs/?documentId=1PvrUpbi4RlUW6tmjpGJVQHaLTgSiY2SDTjki30qOYtY)

#

# Settings

The Vital Recorder has a variety of options that make it easy to use. You can change these options by pressing the Settings button on the toolbar.

<img src="images/vr_setup/image6.png" width="450" />

## **Options for Display and Sound**

<img src="images/vr_setup/image7.png" width="450" />

The display and sound setting options are on the lower side of the Settings window.

- Start maximized: Set the program to run maximized.

- Start minimized: Set the program to run minimized. Useful with the Minimize to tray option.

- Always on top: Always set the program to the top level window.

- Minimize to tray icon: makes it a tray icon when minimizing the program.

<!-- -->

- Play sound when adding an event during recording: "Ding dong" sounds.

## **Settings for File Recording**

<img src="images/vr_setup/image1.png" width="450" />

- Cut file every hour : A vital file is created every hour. For use in the intensive care unit, we recommend selecting by hour.

- Auto-splitting based on SpO2 and HR input: Automatically cut file according to whether the SpO2 and HR parameters are coming in.

## **Network Settings for Remote Monitoring**

To use the real-time Web Monitoring feature on intranet, the configuration file (vr.conf) must be modified. Clicking the pencil button from the Setting window, you can edit the vr.conf.

<img src="images/vr_setup/image4.png" width="450" />

<img src="images/vr_setup/image5.png" width="450" />

- SERVER_IP: enter the static IP address and the port value of the Vital Server.

- BED: This is the name to distinguish the operating room (or computer) from which data is collected.

After finishing editing, click the Cancel button and restart VR.

When VR is connected to the hospital network, it is automatically registered to the Intranet Vital Server.

# Contacts

**Research and Development**

*Professor*

Hyung Chul Lee

vital@snu.ac.kr

**Vital Server**

*Researcher*

Eunsun Rachel Lee

eunsun.lee93@snu.ac.kr

**Vital Recorder**

*Researcher*

Dayeon Sim

dayeonsim@snu.ac.kr
