# Dräger Zeus

<!-- meta
category: Anesthesia Machine
manufacturer: Dräger
vr_device_name: Medibus
-->
| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|---------------- |
| Direct serial cable | Null modem adapter; connector gender not confirmed | Rear COM port | `Medibus` |

## Connection Requirements

Confirm the required null modem adapter for the fitted COM connector and serial cable. The adapter's connector gender has not been verified for this guide.

## Connection Steps

1. Connect a direct serial cable to the COM port using a null modem adapter.

## Device Configuration

Open the machine's serial interface settings and configure the connected port as follows.

| Parameter | Value |
|-----------|------- |
| Protocol | MEDIBUS |
| Baud Rate | 9600 |
| Data Bits | 8 |
| Parity | Even |
| Stop Bits | 1 |

## Vital Recorder Setup

Add the device as **`Medibus`** and select the PC serial port used for the connection.
