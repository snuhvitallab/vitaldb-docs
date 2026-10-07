# Dräger Perseus

<!-- meta
category: Anesthesia Machine
manufacturer: Dräger
vr_device_name: MedibusX
-->
| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|---------------- |
| Direct serial cable | Null modem adapter (F/F) | COM1 or COM2 | `MedibusX` |

## Connection Steps

1. Attach a **null modem adapter (F/F)** to **COM1** or **COM2** on the machine's interface panel.
2. Connect a **direct serial cable** between the null modem adapter and the PC's USB-Serial converter.

Use an available COM port for this connection. A Y-cable connection is not supported by this setup.

## Device Configuration

1. Open **System setup → System**.
2. Enter the configuration password and select **OK**. The default password is **`0000`**; use the site's current password if it has been changed.
3. Select **Interface**.
4. Set the connected port's **Protocol** to **MEDIBUS.X** and **Baud rate** to **19200**.

The serial settings for this connection are:

| Parameter | Value |
|-----------|------- |
| Protocol | MEDIBUS.X |
| Baud Rate | 19200 |
| Data Bits | 8 |
| Parity | Even |
| Stop Bits | 1 |

## Vital Recorder Setup

Add the device as **`MedibusX`** and select the PC serial port used for the connection.
