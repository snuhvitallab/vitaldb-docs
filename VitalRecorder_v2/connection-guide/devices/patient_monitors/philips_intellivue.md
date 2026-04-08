# Philips Intellivue MP / MX Series

<!-- meta
category: Patient Monitor
manufacturer: Philips
vr_device_name: Intellivue
-->
> **Note:** Serial communication via the **MIB port** (RJ-45 style). Works regardless of connection to a central station.

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|----------------|
| Custom RJ-45 ↔ DB-9F | None | MIB port | `Intellivue` |

## Connection Steps
1. Prepare a cable connecting **RJ-45 pins 4, 5, 7** → **DB-9F pins 5, 2, 3**.

   <img src="../hardware_images/philips_intellivue_5.png" width="450" alt="RJ-45 to DB-9F custom cable pinout">

2. Plug the **RJ-45 end** into the MIB port on the monitor.

   <img src="../hardware_images/philips_intellivue_4.png" width="450" alt="MIB port location">

3. Plug the **DB-9F end** into the PC via USB-Serial converter.
4. **MX400–550 series only:** Use the Advanced Interface Card (Rx/Tx pins connect differently).

   <img src="../hardware_images/philips_intellivue_7.png" width="450" alt="MX400-550 Advanced Interface Card pinout">

> MX600–800 series: MIB board must be installed.

## Device Configuration
1. Press **Main Setup → Operation Modes → Service**.

   <img src="../hardware_images/philips_intellivue_6.png" width="450" alt="Main Setup → Operation Modes → Service">

2. Enter service password (default: **`1345`**). Contact manufacturer if this fails.

   <img src="../hardware_images/philips_intellivue_8.png" width="450" alt="Password entry screen">

3. Press **Main Setup → Hardware** (press and hold at bottom of menu).
4. Set **Data Export 1** and **Data Export 2** baud rate to **"Fix 115200"**.

   <img src="../hardware_images/philips_intellivue_3.png" width="300" alt="Data Export baud rate settings">

5. Press **Interfaces**.

   <img src="../hardware_images/philips_intellivue_1.png" width="450" alt="Interfaces menu">

6. Verify port **01a** driver is set to **"DtOut1"**. If not, press **Change Driver → DtOut1**.

   <img src="../hardware_images/philips_intellivue_2.png" width="450" alt="Port 01a — DtOut1 driver selection">

7. **Restart the monitor.**

**Optional — Extract ETCO2 Waveform (via IntelliBridge EC10 Module):**

1. Navigate to **Main Setup → Operating Modes → Config**.
   - Config password: **71034**
2. Press the **Setup** button on the **IntelliBridge EC10 module** connected to the anesthesia machine.
3. On the monitor, select **Setup Device**.
4. Navigate to **Setup Anesth. Machine → Device Driver → Setup Waves**.
5. Press **Add** and select **CO2** and **AWP**.
   - If incorrect waves appear, press **Delete All**, then re-add the correct waves.
6. Select **Select to change operating mode → monitoring**.
7. Press **Confirm** to apply the settings.

> **Note:** MP2 and X2 monitors do not support serial communication and **cannot be used** with Vital Recorder.
