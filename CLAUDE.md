# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

Pure documentation repository for **VitalDB** and **VitalRecorder** — a medical biosignal recording system by Seoul National University VitalLab. No build, test, or lint commands. All content is Markdown with supporting images and archived Word/Excel source files.

## Content Structure

```
README.md                           # Root navigation hub

General/                            # About us, publications, terms
OpenDataset/                        # Open dataset overview
WebMonitoring/                      # Web-based monitoring guide
MyFiles/                            # File download guide

VitalRecorder/                      # Primary docs (converted from docx)
├── README.md                       # Section index
├── Getting_Started*.md             # EN + KO
├── User_Manual*.md                 # EN (Zero variant also here)
├── VitalConnect*.md                # EN + KO
├── Intellivue_Ventilator_Settings*.md  # EN + KO
├── Vital_File_Format.md
├── images/                         # Per-doc image folders (docx-extracted)
└── connection-guide/
    ├── README.md                   # Intro + cable types + troubleshooting
    ├── Hardware_Connection_Guide_Korean.md
    └── devices/
        ├── README.md               # Quick-reference table (all 44 devices)
        ├── anesthesia_machines/
        ├── brain_monitors/
        ├── hemodynamic_monitors/
        ├── patient_monitors/
        ├── syringe_pumps/
        ├── others/
        └── hardware_images/        # Device photos (199 images)

API/                                # Python library + Web API docs
Vitalserver/                        # On-premise server setup

VitalRecorder_v2/                   # Legacy hand-edited docs (keep, do not modify)
googledrive_webdocs/                # Original docx source files (legacy, archive)
scripts/                            # Conversion and cleanup scripts
```

## Converting New docx Files

```bash
# Re-run full conversion (overwrites existing)
bash scripts/convert_docs.sh

# Cleanup pass after conversion
python3 scripts/cleanup_md.py

# Split Hardware Connection Guide into per-device files
python3 scripts/split_hw_guide.py
```

Requirements: `pandoc` (`brew install pandoc`), Python 3.

## Device Guide Format (VitalRecorder)

Each device file in `connection-guide/devices/<category>/<device>.md`:

```markdown
# Manufacturer Model Name

<!-- meta
category: <Patient Monitor|Anesthesia Machine|Hemodynamic Monitor|Syringe Pump|Brain Monitor|Other>
manufacturer: <name>
-->

Content including connection steps, images, device configuration.

Images referenced as: <img src="../hardware_images/imageN.png" width="450">
```

When adding a new device:
- File goes in the appropriate category subdirectory as `manufacturer_model.md` (snake_case)
- Add a row to `connection-guide/devices/README.md` under the correct category table
- Copy device images to `connection-guide/devices/hardware_images/`

## Key Conventions

- **Language suffix**: `_Korean.md`, `_Chinese.md`, `_Spanish.md` (consistent with existing files)
- **Image sizing**: Use `<img src="..." width="450">` for inline images (HTML img tag, not `![]()`)
- **GFM only**: GitHub-Flavored Markdown — no pandoc-specific `{width=...}` attributes
- **Disclaimer** in device README: "not responsible for connection errors; follow manufacturer manual" — preserve in `connection-guide/devices/README.md`
- `VitalRecorder_v2/` is frozen (legacy hand-edited) — do not modify; `VitalRecorder/` is the active folder
