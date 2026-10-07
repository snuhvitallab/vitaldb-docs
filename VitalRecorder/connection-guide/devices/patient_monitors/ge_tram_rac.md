# GE TRAM-RAC 4A

<!-- meta
category: Patient Monitor
manufacturer: GE
vr_device_name: (none — ADC device)
-->
> **Note:** This connection collects analog signals from the 15-pin ANALOG OUT connector on the rear of the TRAM-RAC 4A. An analog-to-digital converter (ADC) is required to record these signals on a PC. The TRAM-RAC 2 does not provide this analog output.

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|---------------- |
| Custom 15-pin D-sub male cable and ADC | — | 15-pin **ANALOG OUT** | Select the device type for your ADC |

## Cable Pinout

<img src="../hardware_images/ge_tram_rac_2.png" width="450" alt="Wiring diagram — ANALOG OUT DB-15 pins 2, 3, 5, 9, 10, 11 and 13 to ADC analog inputs Ch1 to Ch7 (+), with pins 1 and 8 as the common ground for all channel (−) inputs">

## Connection Requirements

1. An ADC supported by Vital Recorder, connected to the PC via USB.
2. A custom cable connecting the required ANALOG OUT pins to the ADC's analog inputs.
3. The TRAM module in the top slot for the TRAM outputs listed below.

DATAQ DI-149 and DI-155 have been used with this setup. SNUADC is an alternative with eight analog input channels and support for wired or wireless event-marker buttons.

## Connection Steps

1. Locate the **ANALOG OUT** connector on the rear of the TRAM-RAC 4A housing. It is a 15-pin D-type connector (yellow label), next to the two DB-9 **TRAM-NET** ports.

   <img src="../hardware_images/ge_tram_rac_1.png" width="450" alt="Rear of the TRAM-RAC 4A housing — the 15-pin ANALOG OUT connector circled in red, beside the two DB-9 TRAM-NET ports">

2. Build or order a cable that routes the ANALOG OUT pins to the ADC's analog inputs as shown in [Cable Pinout](#cable-pinout). Only the pins you actually need have to be wired.

3. Connect the finished cable to the ADC's analog input terminals, then connect the ADC to the PC over USB.

   <img src="../hardware_images/ge_tram_rac_3.png" width="450" alt="Custom DB-15 cable wired into the screw-terminal block of a DataQ DI-149 ADC, with the USB lead that runs to the PC">

   - **SNU-ADC** is an in-house 8-channel ADC built to avoid that cost. Besides the 8 analog channels it accepts a wired or wireless push button for event markers.

     <img src="../hardware_images/ge_tram_rac_4.png" width="450" alt="SNU-ADC board — USB-B connector on one bracket and the D-type analog input connector on the other">

## Device Configuration

No configuration is required on the TRAM-RAC — the analog outputs are always live. All setup happens on the ADC side in Vital Recorder: channel mapping, gain and unit (see Notes for the scaling values).

### Connection Setup for PLETH and CVP

1. Confirm that each channel in Vital Recorder contains the expected waveform. In the example below, CVP is recorded on the channel labeled PLETH, while the CVP channel does not show the expected signal.

   <img src="../hardware_images/ge_tram_rac_5.png" width="450" alt="Vital Recorder screen with ECG and ART1 tracing normally while the CVP pane is empty and the PLETH channel is a flat line">

2. BP2 connected: the CVP transducer cable is connected to BP2, so pin 13 outputs CVP instead of PLETH.
   <img src="../hardware_images/ge_tram_rac_6.png" width="450" alt="Tram module front panel labeled ARTERIAL / RA-CVP with a transducer cable occupying the second BP connector and the third BP socket left empty — incorrect">

3. Configuration for collecting both signals: connect the CVP transducer to BP3 and leave BP2 unused. Pin 3 provides CVP, and pin 13 provides PLETH. Assign the corresponding ADC channels to CVP and PLETH in Vital Recorder.

   <img src="../hardware_images/ge_tram_rac_7.png" width="450" alt="Tram module front panel with the second BP socket left empty and the transducer cables moved to the third and fourth positions — correct">

## Vital Recorder Setup

1. Add the device type corresponding to your ADC.
2. Configure the connected analog channels and sampling rate according to the ADC guide.
3. Assign each channel a track name and unit.
4. Apply the appropriate signal scaling.
5. Start recording and confirm that each channel contains the expected signal.

## Troubleshooting

- **A DataQ DI-1110 (or newer) is not recognised.** These can run in either libusb or CDC mode, and Vital Recorder only recognises **CDC mode** — switch the device to CDC mode before use.
- Analog output scaling: ECG **1 V/mV ± 10%**, invasive BP **1 V / 100 mmHg**, SpO2 **0–100 % equivalent to 0–1 V**. Use these to set the per-channel gain and unit in Vital Recorder.
- **ICP:** when monitoring ICP, the ICP module must be in the **first slot** of the TRAM-RAC.
- **Choosing an ADC:** the DI-149 and DI-155 differ mainly in voltage resolution. The DI-149 is adequate for general monitoring; use the DI-155 if you intend to analyse ECG detail such as P- or T-waves.
