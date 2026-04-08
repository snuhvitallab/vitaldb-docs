#!/usr/bin/env python3
"""
split_hw_guide.py
Splits VitalRecorder_v2/connection-guide/Hardware_Connection_Guide.md
into per-device files under VitalRecorder_v2/connection-guide/devices/
"""

import re
import os
import shutil

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GUIDE = os.path.join(REPO, "VitalRecorder_v2/connection-guide/Hardware_Connection_Guide.md")
DEVICES_DIR = os.path.join(REPO, "VitalRecorder_v2/connection-guide/devices")
IMG_SRC = os.path.join(REPO, "VitalRecorder_v2/connection-guide/images/hw_guide")
IMG_DST = os.path.join(DEVICES_DIR, "hardware_images")

# ── Category mapping: H1 heading → subdirectory name ─────────────────────────
CATEGORY_MAP = {
    "patient monitors":         "patient_monitors",
    "anesthesia machines":       "anesthesia_machines",
    "cardiac monitors":          "hemodynamic_monitors",
    "infusion pumps":            "syringe_pumps",
    "cerebral monitors":         "brain_monitors",
    "multifunction monitors":    "others",
    "neuromuscular monitors":    "others",
}

# ── Device name → filename mapping ───────────────────────────────────────────
# Derived automatically but some need manual override
FILENAME_OVERRIDES = {
    "ge carescape b850, b650, b450":                  "ge_carescape",
    "ge s/5 am":                                       "ge_s5am",
    "ge b40, b20":                                     "ge_b40_b20",
    "ge b105m, b125m, b155m":                          "ge_b105m",
    "ge solar 8000m, 8000i":                           "ge_solar8000",
    "ge dash 2000/3000/4000":                          "ge_dash2000",
    "ge dash 2500":                                    "ge_dash2500",
    "ge tram-rac 4a":                                  "ge_tram_rac",
    "ge defib connectors":                             "ge_defib",
    "philips intellivue mp/mx series":                 "philips_intellivue",
    "drager infinity kappa":                           "drager_infinity_kappa",
    "drager infinity c500/c700":                       "drager_infinity_c500",
    "mekics mp1300":                                   "mekics_mp1300",
    "nihon kohden bsm":                                "nihon_kohden_bsm",
    "drager apollo, cicero em color, julian, primus, vamos": "drager_apollo",
    "drager fabius, zeus, infinity":                   "drager_fabius",
    "drager perseus":                                  "drager_perseus",
    "ge datex-ohmeda anesthesia machine":              "ge_datex_ohmeda",
    "maquet flow-i":                                   "maquet_flow_i",
    "maquet servo-i ventilator":                       "maquet_servo_i",
    "hamilton g5 ventilator":                          "hamilton_g5",
    "edwards lifesciences ev-1000":                    "edwards_ev1000",
    "edwards lifesciences vigilance":                  "edwards_vigilance",
    "edwards lifesciences vigilance ii":               "edwards_vigilance2",
    "edwards lifesciences vigileo":                    "edwards_vigileo",
    "edwards lifesciences hemosphere":                 "edwards_hemosphere",
    "deltex cardioq":                                  "deltex_cardioq",
    "lidco":                                           "lidco",
    "fresenius vial orchestra (base primea with module dps)": "fresenius_orchestra",
    "fresenius kabi agilia":                           "fresenius_agilia",
    "bbraun spacecom":                                 "bbraun_spacecom",
    "bionet pion tci":                                 "bionet_pion",
    "belmont fms (ri-2)":                              "belmont_fms",
    "medtronic bis vista":                             "medtronic_bis_vista",
    "medtronic bis a2000":                             "medtronic_bis_a2000",
    "medtronic invos cerebral/somatic oximetry":       "medtronic_invos",
    "masimo radical7":                                 "masimo_radical7",
    "masimo root":                                     "masimo_root",
    "sentec: sdm":                                     "sentec_sdm",
    "mdms ani monitor v2":                             "mdms_ani_monitor",
    "ge: corometrics 170":                             "ge_corometrics",
    "blinkdc: twitchview":                             "blink_twitchview",
    "idmed tofscan":                                   "idmed_tofscan",
}

def slugify(title):
    key = title.lower().strip()
    if key in FILENAME_OVERRIDES:
        return FILENAME_OVERRIDES[key]
    # fallback: lowercase, replace non-alphanumeric with _
    slug = re.sub(r'[^a-z0-9]+', '_', key).strip('_')
    return slug

def fix_image_path(content, category):
    """Replace images/hw_guide/ references with ../hardware_images/"""
    content = content.replace("images/hw_guide/", "../hardware_images/")
    return content

def make_device_md(title, category_h1, content):
    """Wrap device content with metadata comment block."""
    # Map category H1 → display name
    cat_display = {
        "patient_monitors":    "Patient Monitor",
        "anesthesia_machines": "Anesthesia Machine",
        "hemodynamic_monitors":"Hemodynamic Monitor",
        "syringe_pumps":       "Syringe Pump",
        "brain_monitors":      "Brain Monitor",
        "others":              "Other",
    }.get(category_h1, "Other")

    # Try to extract manufacturer from title
    mfr_map = {
        "GE": "GE", "Philips": "Philips", "Drager": "Draeger", "Drager": "Draeger",
        "MEKICS": "MEKICS", "Nihon": "Nihon Kohden", "Edwards": "Edwards Lifesciences",
        "Deltex": "Deltex", "LiDCO": "LiDCO", "Fresenius": "Fresenius",
        "BBraun": "BBraun", "Bionet": "Bionet", "Belmont": "Belmont",
        "Medtronic": "Medtronic", "Masimo": "Masimo", "Sentec": "Sentec",
        "MDMS": "MDMS", "BlinkDC": "BlinkDC", "IDMed": "IDMed",
        "Maquet": "Maquet", "Hamilton": "Hamilton",
    }
    manufacturer = "Unknown"
    for key, val in mfr_map.items():
        if key.lower() in title.lower():
            manufacturer = val
            break

    header = f"""<!-- meta
category: {cat_display}
manufacturer: {manufacturer}
-->
"""
    return f"# {title}\n\n{header}\n{content.strip()}\n"


def main():
    with open(GUIDE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Copy images to hardware_images/
    os.makedirs(IMG_DST, exist_ok=True)
    if os.path.isdir(IMG_SRC):
        for fname in os.listdir(IMG_SRC):
            shutil.copy2(os.path.join(IMG_SRC, fname), os.path.join(IMG_DST, fname))
        print(f"  Copied {len(os.listdir(IMG_SRC))} images → devices/hardware_images/")

    # Parse the document into sections
    # We track current H1 category and collect H2 device blocks
    intro_lines = []       # lines before first device section
    troubleshooting_lines = []
    current_category = None
    current_device = None
    device_lines = []
    devices = []           # list of (category, device_title, lines)

    in_troubleshooting = False

    i = 0
    while i < len(lines):
        line = lines[i]

        # H1 category heading
        if line.startswith("# ") and not line.startswith("## "):
            h1 = line[2:].strip()
            cat_key = h1.lower()

            if cat_key == "solutions to common problems":
                # Save current device if any
                if current_device:
                    devices.append((current_category, current_device, device_lines[:]))
                    device_lines = []
                    current_device = None
                in_troubleshooting = True
                current_category = None
                troubleshooting_lines.append(line)
            elif cat_key in CATEGORY_MAP:
                # Save current device if any
                if current_device:
                    devices.append((current_category, current_device, device_lines[:]))
                    device_lines = []
                    current_device = None
                current_category = CATEGORY_MAP[cat_key]
            elif current_category is None and not in_troubleshooting:
                # Intro section (first H1 = Getting Started)
                intro_lines.append(line)
            else:
                if in_troubleshooting:
                    troubleshooting_lines.append(line)
                elif current_device:
                    device_lines.append(line)

        # H2 device heading
        elif line.startswith("## ") and current_category is not None and not in_troubleshooting:
            # Save previous device
            if current_device:
                devices.append((current_category, current_device, device_lines[:]))
            current_device = line[3:].strip()
            device_lines = [line]  # start new device block (include H2 heading)

        else:
            if in_troubleshooting:
                troubleshooting_lines.append(line)
            elif current_device:
                device_lines.append(line)
            elif current_category is None:
                intro_lines.append(line)

        i += 1

    # Save last device
    if current_device and device_lines:
        devices.append((current_category, current_device, device_lines[:]))

    print(f"  Found {len(devices)} device sections")

    # Write intro as README.md
    os.makedirs(DEVICES_DIR, exist_ok=True)
    intro_content = "".join(intro_lines)
    # Append troubleshooting
    if troubleshooting_lines:
        intro_content += "\n---\n\n" + "".join(troubleshooting_lines)

    readme_path = os.path.join(os.path.dirname(DEVICES_DIR), "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(intro_content)
    print(f"  ✓ connection-guide/README.md (intro + troubleshooting)")

    # Write per-device files
    written = 0
    skipped = 0
    for (category, title, dev_lines) in devices:
        if not title.strip():
            skipped += 1
            continue

        cat_dir = os.path.join(DEVICES_DIR, category)
        os.makedirs(cat_dir, exist_ok=True)

        filename = slugify(title) + ".md"
        filepath = os.path.join(cat_dir, filename)

        # Build content: remove the ## heading line (we'll add # in wrapper)
        content_lines = dev_lines[1:] if dev_lines and dev_lines[0].startswith("## ") else dev_lines
        content = "".join(content_lines)
        content = fix_image_path(content, category)
        full_content = make_device_md(title, category, content)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(full_content)
        written += 1

    print(f"  ✓ {written} device files written ({skipped} empty sections skipped)")

    # Print summary
    print("\n  Device files by category:")
    from collections import Counter
    counts = Counter(cat for (cat, _, __) in devices if _.strip())
    for cat, cnt in sorted(counts.items()):
        print(f"    {cat}: {cnt}")


if __name__ == "__main__":
    main()
