# Fresenius Kabi Agilia

<!-- meta
category: Syringe Pump
manufacturer: Fresenius Kabi
vr_device_name: Agilia
-->
> ⚠️ **Use the proprietary Fresenius Kabi cable.** The pump has a circular screw-lock connector that a generic serial cable cannot fit.

| Cable | Adapter | Port | VR Device Name |
|-------|---------|------|----------------|
| Proprietary Fresenius Kabi cable (7-pin mini-DIN pump side, DB-9F output) | None | Serial (7-pin mini-DIN, circular screw-lock), pump housing | `Agilia` |

## Connection Requirements

The cable's output end is DB-9 **female**, which mates directly with the DB-9 male of a PC serial port or USB-Serial converter. **No Null Modem adapter is used** — the crossover is built into the proprietary cable.

## Connection Steps
1. Obtain the proprietary cable from Fresenius Kabi.
2. Flip open the rubber cap over the pump's circular connector, align the plug with the keyway, insert it, and **tighten the knurled locking collar** by hand until the connector is seated. The collar is what retains the plug — an un-tightened connector works loose during use.

   <img src="../hardware_images/fresenius_agilia_1.png" width="450" alt="Pictogram showing the rubber cap flipped open, the plug inserted, and the collar rotated to tighten, above a photograph of the proprietary cable's knurled screw-lock connector being mated to the pump's circular port">

3. Connect the **DB-9F end directly** to a USB-Serial converter — no adapter in between.
4. Connect the USB-Serial converter to the PC.

## Device Configuration
No pump-side configuration is required; connect the proprietary cable as described above.

## Vital Recorder Setup

- Add the device in Vital Recorder as **`Agilia`**.

## Notes

- This page covers a **standalone Agilia pump** cabled directly to the PC. Where several Agilia SP / VP modules are mounted on a **Link+ / Agilia Link rack**, use the rack's USB connection instead and configure it as the `Link+` device — see [Fresenius Kabi Link+ Agilia](fresenius_link_agilia.md). Do not cable individual pumps separately when a Link+ rack is present.
