# Vital Recorder Version Notes (device-related)

**Run the latest Vital Recorder.** The authoritative list is the official version history — <https://vitaldb.net/vital-recorder/?action=versions>. Only changes that add a device or change what is collected from one are summarised here; bug fixes and entries older than about two years are left out.

| Version | Date | Device | Change |
|---|---|---|---|
| 1.19.34 | 2026-10-06 | Nihon Kohden PVM-4700 | New **`PVM`** entry for the Vismo PVM-4700 series. Numerics are collected over RS-232C. |
| 1.19.34 | 2026-10-06 | Nihon Kohden BSM-3000/6000, CSM-1500/1700 | Units that recorded nothing over serial now record numerics: Vital Recorder falls back to a request these models accept. |
| 1.19.32 | 2026-10-05 | Philips IntelliVue | **`auto_wavs=0`** (device-dialog checkbox) requests only the selected waveforms. By default a waveform is added for every numeric present. |
| 1.19.27 | 2026-09-05 | TwitchView, TOFscan | Serial auto-detection (`AUTO_DETECT=1`) now waits long enough for these monitors, which report only every ~5 min. |
| 1.19.22 | 2026-08-30 | Dräger (MEDIBUS) | Machines selectable **by model** (`Fabius` added) plus a generic **`Medibus`** entry; `Primus`, `Fabius` and `Medibus` behave identically. Auto-detection identifies Dräger machines by protocol, not model. |
| 1.19.20 | 2026-08-29 | SyncPulseSerial | New device: sync pulse generator sending a 6-digit counter every second, recorded in the `PULSE` track. |
| 1.19.20 | 2026-08-29 | Dräger Fabius GS | Machines with no waveform capability now record numerics (previously nothing was collected). Fabius has AWP/AWF but no CO2 waveform. |
| 1.19.19 | 2026-08-27 | Dräger (MEDIBUS) | New tracks: ventilation phase `VENT_PHASE`, mode `VENT_MODE`, device messages `VENT_MSG`. |
| 1.19.15 – 1.19.18 | 2026-08-27 | Dräger (MEDIBUS) | Waveforms are requested from the list the machine offers, up to 4 (previously fixed to CO2 and AWP); **`wavs=`** selects specific ones (AWP AWF PLETH VOL O2 CO2 …). On Y-cable taps the waveform type is auto-detected when the other device's requests are visible (1.19.18); otherwise `wavs=` fixes it (1.19.17). |
| 1.19.7 | 2026-08-12 | GE Corometrics | **Maternal SpO2 / PR / NIBP** recorded alongside fetal HR1/HR2 and UACT. |
| 1.19.0 | 2026-08 | All serial devices | **`AUTO_DETECT=1`** — serial devices identified automatically. |
| 1.18.49 | 2026-07-29 | Maquet Flow-i | 11 set-parameters added; TV no longer reported at half value (Set TV removed in protocol v5). |
| 1.16.3 | 2026-01-14 | Masimo | IAP protocol fix. |
| 1.14.9 | 2024-10-17 | Fresenius Link+ | Hardware handshaking removed from the Link+ port; dose-rate monitor types added. |
