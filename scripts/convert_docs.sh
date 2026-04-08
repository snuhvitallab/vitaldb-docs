#!/usr/bin/env bash
# convert_docs.sh
# Converts all docx files from googledrive_webdocs/ to Markdown.
# Usage: bash scripts/convert_docs.sh
# Requires: pandoc (brew install pandoc)

set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
GDRIVE="$REPO/googledrive_webdocs"

# ── helpers ──────────────────────────────────────────────────────────────────

# convert_docx <src_relative_to_GDRIVE> <dst_relative_to_REPO> <img_dir_relative_to_REPO>
convert_docx() {
    local src="$GDRIVE/$1"
    local dst="$REPO/$2"
    local img_dir="$REPO/$3"     # final image directory
    local tmp_extract="$img_dir/.pandoc_extract"

    mkdir -p "$(dirname "$dst")" "$img_dir"

    # Convert with pandoc (GFM = GitHub-Flavored Markdown)
    pandoc "$src" -o "$dst" -t gfm --wrap=none --extract-media="$tmp_extract"

    # Move extracted images up one level (remove the /media/ subdir)
    if [ -d "$tmp_extract/media" ]; then
        mv "$tmp_extract/media/"* "$img_dir/" 2>/dev/null || true
        rm -rf "$tmp_extract"
    fi

    # Fix image paths in the markdown:
    # pandoc writes "$tmp_extract/media/imageN.ext" → replace with correct relative path
    # We need the path from $dst's directory to $img_dir
    local dst_dir
    dst_dir="$(dirname "$dst")"
    local rel_img
    rel_img="$(python3 -c "import os; print(os.path.relpath('$img_dir', '$dst_dir'))")"

    # Replace the full tmp_extract/media path with the relative images path
    sed -i '' "s|${tmp_extract}/media/|${rel_img}/|g" "$dst"

    # Clean up pandoc {width="..." height="..."} image attributes (not GFM-standard)
    # Convert: ![alt](path){width="..." height="..."} → <img src="path" width="450">
    # and:     ![](path){width="..." height="..."}   → <img src="path" width="450">
    python3 - "$dst" <<'PYEOF'
import re, sys

path = sys.argv[1]
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace markdown image syntax with size attributes → <img> tag
# Matches: ![alt](src){width="Xin" height="Yin"} or ![alt](src){width="Xpx" ...}
content = re.sub(
    r'!\[([^\]]*)\]\(([^)]+)\)\{[^}]*\}',
    lambda m: f'<img src="{m.group(2)}" alt="{m.group(1)}" width="500">',
    content
)

# Also handle bare markdown images without size attrs → wrap in <img> for consistency
# (Only standalone image lines — i.e. lines that are just an image)
content = re.sub(
    r'^!\[([^\]]*)\]\(([^)]+)\)$',
    lambda m: f'<img src="{m.group(2)}" alt="{m.group(1)}" width="500">',
    content,
    flags=re.MULTILINE
)

# Fix <img> tags inside HTML tables that already have style= attribute
# style="width:Xin;height:Yin" → width="450"
content = re.sub(
    r'(<img\s[^>]*?)style="width:[^"]*"(\s[^>]*>)',
    r'\1width="450"\2',
    content
)
content = re.sub(
    r'(<img\s[^>]*?)style="width:[^"]*"(/>)',
    r'\1width="450"\2',
    content
)
content = re.sub(
    r'(<img\s[^>]*?)style="width:[^"]*"(\s*/>)',
    r'\1width="450"\2',
    content
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
PYEOF

    echo "  ✓  $2"
}

# ── create directory structure ────────────────────────────────────────────────

echo "Creating directory structure..."
mkdir -p "$REPO/VitalRecorder_v2/connection-guide"
mkdir -p "$REPO/API"
mkdir -p "$REPO/Vitalserver"
mkdir -p "$REPO/WebMonitoring"
mkdir -p "$REPO/General"
mkdir -p "$REPO/OpenDataset"
mkdir -p "$REPO/MyFiles"

# ── conversions ───────────────────────────────────────────────────────────────

echo ""
echo "==> General"
convert_docx "1. General Information/About us.docx" \
    "General/About_Us.md" \
    "General/images/about_us"

convert_docx "1. General Information/!Publications.docx" \
    "General/Publications.md" \
    "General/images/publications"

convert_docx "1. General Information/Terms and Conditions.docx" \
    "General/Terms_and_Conditions.md" \
    "General/images/terms"

echo ""
echo "==> Open Dataset"
convert_docx "2. Open Dataset/VitalDB Overview.docx" \
    "OpenDataset/Overview.md" \
    "OpenDataset/images/overview"

echo ""
echo "==> Web Monitoring"
convert_docx "3. Web Monitoring/Web Monitoring User Guide.docx" \
    "WebMonitoring/User_Guide.md" \
    "WebMonitoring/images/user_guide"

convert_docx "3. Web Monitoring/Web Monitoring User Guide (Korean).docx" \
    "WebMonitoring/User_Guide_Korean.md" \
    "WebMonitoring/images/user_guide_ko"

echo ""
echo "==> VitalRecorder_v2"
convert_docx "4. VitalRecorder/!Getting Started.docx" \
    "VitalRecorder_v2/Getting_Started.md" \
    "VitalRecorder_v2/images/getting_started"

convert_docx "4. VitalRecorder/!Getting Started (Korean).docx" \
    "VitalRecorder_v2/Getting_Started_Korean.md" \
    "VitalRecorder_v2/images/getting_started_ko"

convert_docx "4. VitalRecorder/!Vital Recorder User Manual.docx" \
    "VitalRecorder_v2/User_Manual.md" \
    "VitalRecorder_v2/images/user_manual"

convert_docx "4. VitalRecorder/Vital Recorder Zero User Manual.docx" \
    "VitalRecorder_v2/User_Manual_Zero.md" \
    "VitalRecorder_v2/images/user_manual_zero"

convert_docx "4. VitalRecorder/VitalConnect.docx" \
    "VitalRecorder_v2/VitalConnect.md" \
    "VitalRecorder_v2/images/vitalconnect"

convert_docx "4. VitalRecorder/VitalConnect (Korean).docx" \
    "VitalRecorder_v2/VitalConnect_Korean.md" \
    "VitalRecorder_v2/images/vitalconnect_ko"

convert_docx "4. VitalRecorder/Intellivue Settings to Collect Ventilator Data.docx" \
    "VitalRecorder_v2/Intellivue_Ventilator_Settings.md" \
    "VitalRecorder_v2/images/intellivue"

convert_docx "4. VitalRecorder/Intellivue Settings to Collect Ventilator Data (Korean).docx" \
    "VitalRecorder_v2/Intellivue_Ventilator_Settings_Korean.md" \
    "VitalRecorder_v2/images/intellivue_ko"

convert_docx "4. VitalRecorder/Vital File Format.docx" \
    "VitalRecorder_v2/Vital_File_Format.md" \
    "VitalRecorder_v2/images/vital_file_format"

convert_docx "4. VitalRecorder/!Hardware Connection Guide.docx" \
    "VitalRecorder_v2/connection-guide/Hardware_Connection_Guide.md" \
    "VitalRecorder_v2/connection-guide/images/hw_guide"

convert_docx "4. VitalRecorder/!Hardware Connection Guide (Korean).docx" \
    "VitalRecorder_v2/connection-guide/Hardware_Connection_Guide_Korean.md" \
    "VitalRecorder_v2/connection-guide/images/hw_guide_ko"

echo ""
echo "==> My Files"
convert_docx "5. My Files/File Download Guide.docx" \
    "MyFiles/File_Download_Guide.md" \
    "MyFiles/images/file_download"

echo ""
echo "==> API"
convert_docx "6. API/!VitalDB Python Library.docx" \
    "API/Python_Library.md" \
    "API/images/python_library"

convert_docx "6. API/!VitalDB Web API.docx" \
    "API/Web_API.md" \
    "API/images/web_api"

convert_docx "6. API/!VitalDB Web API for Open Dataset.docx" \
    "API/Web_API_OpenDataset.md" \
    "API/images/web_api_open_dataset"

convert_docx "6. API/IntraNet VitalDB API.docx" \
    "API/IntraNet_API.md" \
    "API/images/intranet_api"

convert_docx "6. API/VitalDB Oauth2 API.docx" \
    "API/OAuth2_API.md" \
    "API/images/oauth2"

echo ""
echo "==> Vitalserver"
convert_docx "7. Vitalserver/User Manual of Vitalserver (On-premise VitalDB Server).docx" \
    "Vitalserver/User_Manual.md" \
    "Vitalserver/images/user_manual"

convert_docx "7. Vitalserver/User Manual of Vitalserver (On-premise VitalDB Server) (Korean).docx" \
    "Vitalserver/User_Manual_Korean.md" \
    "Vitalserver/images/user_manual_ko"

convert_docx "7. Vitalserver/How to Set up Vital Recorder for Vitalserver.docx" \
    "Vitalserver/VR_Setup_for_Vitalserver.md" \
    "Vitalserver/images/vr_setup"

convert_docx "7. Vitalserver/Step-by-Step Guide for Setting up Vitalserver and VitalRecorder Test.docx" \
    "Vitalserver/Setup_Step_by_Step.md" \
    "Vitalserver/images/setup_step_by_step"

# ── remove empty image dirs ───────────────────────────────────────────────────
# (for docx files that contained no images)
find "$REPO" -path "*/images/*" -type d -empty -delete 2>/dev/null || true
find "$REPO" -name "images" -type d -empty -delete 2>/dev/null || true

echo ""
echo "Done. All docx files converted."
