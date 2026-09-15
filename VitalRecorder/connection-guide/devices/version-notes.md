# Vital Recorder Version Notes (device-related)

**Policy: run the latest Vital Recorder.** As of 2026-09-05 that is **1.19.27**. The authoritative list is the official version history — <https://vitaldb.net/vital-recorder/?action=versions> — check it before quoting a version to a site. Device pages no longer state minimum versions; the device-relevant entries are collected here so they can be re-checked in one place.

**Source column:** ✓ = wording confirmed in the official version history · *field* = from installation records only, not (yet) in the official notes · *older* = version predates the detailed notes on the site.

## Dräger (MEDIBUS / MEDIBUS.X — Apollo, Primus, Fabius, Perseus, Atlan, EVITA)

| Version | Date | Change | Source |
|---|---|---|---|
| 1.19.22 | 2026-08-30 | Dräger machines selectable **by model** (`Fabius` added) plus a generic **`Medibus`** entry; `Primus`, `Fabius`, `Medibus` behave identically. Auto-detection now identifies Dräger machines by protocol name, not model. | ✓ |
| 1.19.21 | 2026-08-29 | Logs the model name the machine reports. Notes that **Fabius has AWP/AWF but no CO2 waveform**. | ✓ |
| 1.19.20 | 2026-08-29 | Machines **without waveform capability** (e.g. **Fabius GS**, which has none by specification) collected nothing — connection looked up, no values. Fixed: numerics start immediately; absence of waveforms is logged once. | ✓ |
| 1.19.19 | 2026-08-27 | Records ventilation phase (`VENT_PHASE`), mode (`VENT_MODE`) and device messages (`VENT_MSG`). | ✓ |
| 1.19.18 | 2026-08-27 | Y-cable taps: waveform type auto-detected when the other device's requests are visible on the line. | ✓ |
| 1.19.17 | 2026-08-27 | Y-cable taps: `wavs=` fixes the waveform order manually. Unknown frame types logged once for diagnosis. | ✓ |
| 1.19.16 | 2026-08-27 | Fixes 1.19.15, which dropped all waveforms on Y-cable (observe-only) connections. **Sites on 1.19.15 must upgrade.** | ✓ |
| 1.19.15 | 2026-08-27 | Waveforms were filed under the wrong names (AWP recorded as CO2 on an Evita V600). Fixed; requests the device's available waveforms; **`wavs=` selects up to 4** (AWP AWF PLETH VOL O2 CO2 … ); warns when above 80 % of 9600 bps. | ✓ |
| 1.19.12 | 2026-08-27 | Auto-detection no longer mistakes serial noise for data. | ✓ |
| 1.19.11 | 2026-08-27 | **`COM1 failure` alarms and missing waveforms fixed** — three causes: no keep-alive (NOP now every 2 s), interleaved device commands discarded the waveform-config reply, one device request went unanswered. | ✓ |
| 1.18.40 | 2026-05-12 | Medibus beds crashed in a SIGSEGV restart loop since 1.15.11 (waveform tracks created lazily). Fixed. | ✓ |
| 1.9.1 | — | MEDIBUS.X protocol support (`MedibusX`, 19200 baud). | *older* |

## Philips Intellivue

| Version | Date | Change | Source |
|---|---|---|---|
| 1.19.3 | 2026-08-04 | Repeated SIGSEGV on multi-bed Intellivue installations (two use-after-free bugs) fixed. | ✓ |
| 1.19.9 | 2026-08-14 | Official note: large-file upload out-of-memory loop fixed. Field records also credit this build with improved waveform delivery on Intellivue; not in the official note. | ✓ / *field* |
| 1.16.4 | 2026-01-20 | "Serial communication" bug fix — the Intellivue reception failure seen on 1.16.3. | ✓ |

## GE (S/5, Corometrics)

| Version | Date | Change | Source |
|---|---|---|---|
| 1.19.7 | 2026-08-12 | Corometrics: **maternal SpO2 / PR / NIBP** recorded alongside fetal HR1/HR2 and UACT. | ✓ |
| 1.13.4 | 2024-05-23 | Fetal heart rate and uterine activity added (Corometrics support begins). | ✓ |
| 1.12.4 | — | Intellivue and S/5 waveform tracks selectable by name (`IABP1`, `PLETH`, `CO2` …). | *field* |
| 1.12.7 | — | Nihon Kohden HL7 gateway (central server) support. | *field* |

## Fresenius Kabi Link+ / Agilia

| Version | Date | Change | Source |
|---|---|---|---|
| 1.19.5 | 2026-08-06 | Link+/Agilia parser crashed (`std::length_error`) on serial noise. Fixed. | ✓ |
| 1.19.4 | 2026-08-05 | Reopening a Link+ serial port crashed the process (`terminate called…`). Fixed. | ✓ |
| 1.18.50 | 2026-07-30 | Devices that disconnected once never reconnected (Link+ rack rebooted, Intellivue powered on late). Fixed for all protocol-initiating devices (Link+, Intellivue, S5, Datex, Hamilton). | ✓ |
| 1.19.0 → 1.19.9 | 2026-08 | 1.19.0 retried a dead Link+ port without delay and blocked recording; resolved by 1.19.9. | *field* |
| 1.14.9 | 2024-10-17 | Official note: dose-rate monitor types. Field record: hardware handshaking removed from the Link+ port in this build. | ✓ / *field* |

## Others

| Version | Date | Change | Source |
|---|---|---|---|
| 1.19.27 | 2026-09-05 | Auto-detection listens long enough for **TwitchView / TOFscan**, which report every ~5 min and were never detected before. | ✓ |
| 1.18.49 | 2026-07-29 | **Flow-i**: 11 set-parameters added; TV reported at half value fixed (Set TV removed in protocol v5). **Mindray HL7** `readonly` blocked reception — fixed. | ✓ |
| 1.16.3 | 2026-01-14 | Masimo IAP protocol fix. | ✓ |
| 1.13.9 | 2024-06-27 | Official note: file-loading fix. Field record: NIRSIT-ON+ 32 Hz recording. | ✓ / *field* |
| 1.11.4 | — | NIRSIT-ON+ link moved from 9600 to 115200 baud. | *field* |
| 1.10.2 / 1.10.8 | — | Hamilton G5 support / protocol bug fix. | *older* |
| 1.8.16.x | — | Flow-i (1.8.16.0), Nihon Kohden BSM (1.8.16.2), HemoSphere (1.8.16.4) first supported. | *older* |
| 1.8.15 | — | MEKICS MP1300 present. | *older* |

## Behaviour that depends on version and is easy to miss

- **`AUTO_DETECT=1`** (serial device auto-identification) exists from **1.19.0**; from 1.19.22 it names Dräger machines by protocol (`Medibus`), and from 1.19.27 it waits long enough for slow-talking neuromuscular monitors.
- **`wavs=`** for MEDIBUS devices exists from **1.19.15**; on Y-cable taps it is the only way to fix names (1.19.17) unless the other device's requests are visible (1.19.18).
- **Anything on 1.19.15 exactly** should move to 1.19.16 or later.
