# Dräger Atlan

<!-- meta
category: Anesthesia Machine
manufacturer: Dräger
vr_device_name: MedibusX
-->
> **Note:** The Atlan speaks Dräger **MEDIBUS.X** and is added in Vital Recorder as **`MedibusX`**. The COM port must be set to MEDIBUS.X at 19200 before data arrives.

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|---------------- |
| Direct serial cable | Null modem adapter (F/F) | COM1 or COM2 | `MedibusX` |

## Connection Steps
1. Locate the **DB-9 serial port** (**COM 1** or **COM 2**) on the machine.
2. Connect a direct serial cable to the COM1 or COM2 port using a **Null Modem adapter (F/F)**.

## Device Configuration

Open the machine's COM interface settings and configure the connected port as follows. Refer to the model's instructions for the menu path.

| Parameter | Value |
|-----------|------- |
| Protocol | MEDIBUS.X |
| Baud Rate | 19200 |
| Data Bits | 8 |
| Parity | Even |
| Stop Bits | 1 |

## Vital Recorder Setup

Add the device as **`MedibusX`** and select the PC serial port used for the connection.
