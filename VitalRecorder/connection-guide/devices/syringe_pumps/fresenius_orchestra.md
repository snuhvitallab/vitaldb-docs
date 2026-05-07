# Fresenius Vial Orchestra (Base Primea with Module DPS)

<!-- meta
category: Syringe Pump
manufacturer: Fresenius Kabi
vr_device_name: Orchestra
-->
> ⚠️ **A cross (M/F Cross Gender) adapter is required.** Connecting a direct cable causes incorrect communication or hardware damage.

| Cable | Adapter | Port | Protocol | VR Device Name |
|-------|---------|------|----------|----------------|
| Direct Serial | Null Modem M/F | RS 232-3 — **rightmost** of three serial ports (Base Primea) | IDMS | `Orchestra` |

## Connection Steps
1. Attach a **Null Modem (M/F)** to the **RS 232-3** port (rightmost).
2. Connect a direct serial cable to the PC via USB-Serial converter.

   <img src="../hardware_images/fresenius_orchestra_3.png" width="450" alt="Base Primea — RS 232-3 port">

## Device Configuration
1. Power off. Hold **top blue button + mute button + power button** simultaneously → enter service mode.

   <img src="../hardware_images/fresenius_orchestra_7.png" width="450" alt="Service mode button combination">

2. Press the **fourth blue button** → **"Serial & ..."**.

   <img src="../hardware_images/fresenius_orchestra_6.png" width="450" alt="Serial & ... menu">

3. In **SERIAL PORTS**, select **COM NEW SUP** (second item, upper right) via jog dial → select **3**.

   <img src="../hardware_images/fresenius_orchestra_5.png" width="450" alt="COM NEW SUP selection">

4. Uncheck **"Send a frame on every change"** for COMM NEW SUP. Set **"Send every" → 1s**.
5. Power off → power on → press **OPT** button (lower right).

   <img src="../hardware_images/fresenius_orchestra_4.png" width="300" alt="OPT button">

6. Select **CUSTOMIZATION → CODE → `00123`**.

   <img src="../hardware_images/fresenius_orchestra_2.png" width="450" alt="Code entry: 00123">

7. Select **SERIAL PORTS AND PRINTER → RS-232-3 → IDMS**.

   <img src="../hardware_images/fresenius_orchestra_1.png" width="450" alt="RS-232-3 → IDMS">

8. Confirm **RS 232-3 = IDMS** → **save and exit** → power cycle.
