#!/usr/bin/env python3
"""
cleanup_md.py
Post-processes pandoc-generated markdown files:
  - Strips <u> tags (docx underline → plain text)
  - Strips <span class="mark"> highlight tags
  - Fixes [<u>url</u>](url) → [url](url)
  - Converts simple single-column pipe tables → fenced code blocks
  - Removes <colgroup> sections from HTML tables
  - Removes 3+ consecutive blank lines → 2 blank lines
  - Fixes escaped angle brackets \< \> in text
"""

import re
import sys
import os
from pathlib import Path

def cleanup(content: str) -> str:
    # ── 1. Strip <u> underline tags (keep text) ────────────────────────────
    content = re.sub(r'<u>(.*?)</u>', r'\1', content, flags=re.DOTALL)

    # ── 2. Strip <span class="mark"> highlight tags (keep text) ───────────
    content = re.sub(r'<span[^>]*class="mark"[^>]*>(.*?)</span>', r'\1', content, flags=re.DOTALL)
    content = re.sub(r'<span[^>]*>(.*?)</span>', r'\1', content, flags=re.DOTALL)

    # ── 3. Fix links like [<u>text</u>](url) or [text](url) with <u> ──────
    # Already handled above since we stripped <u> first

    # ── 4. Convert simple single-column pipe tables → code blocks ─────────
    # Pattern: lines like  | code |  followed by  |---|
    # These are docx "Code" style paragraphs
    def pipe_to_code(m):
        # Extract code lines (remove leading/trailing | and whitespace)
        rows_block = m.group(0)
        # Split into lines, filter out separator lines (|---|)
        lines = rows_block.strip().split('\n')
        code_lines = []
        for line in lines:
            line = line.strip()
            if re.match(r'^\|[-|: ]+\|$', line):
                continue  # separator
            if line.startswith('|') and line.endswith('|'):
                # strip leading/trailing |
                inner = line[1:-1].strip()
                code_lines.append(inner)
        if not code_lines:
            return m.group(0)
        return '```\n' + '\n'.join(code_lines) + '\n```'

    # Match single-column pipe tables: all rows have exactly one | on each side
    # Only match "simple" ones (no HTML inside, no bold/italic formatting inside cells)
    simple_pipe_table = re.compile(
        r'(?:^\| [^|\n]+ \|\n)+^\|[-]+\|(?:\n^\| [^|\n]+ \|)*',
        re.MULTILINE
    )
    def try_pipe_to_code(m):
        text = m.group(0)
        # Only convert if content looks like code (not a real data table)
        lines = [l.strip() for l in text.split('\n') if l.strip() and not re.match(r'^\|[-|: ]+\|$', l.strip())]
        cells = [re.sub(r'^\||\|$', '', l).strip() for l in lines]
        # Heuristic: if it's 1-3 lines with no | inside cells and looks like code
        has_pipe_inside = any('|' in c for c in cells)
        looks_like_prose = any(len(c.split()) > 12 for c in cells)  # long prose sentences
        if has_pipe_inside or looks_like_prose:
            return text  # keep as table
        return pipe_to_code(m)

    content = simple_pipe_table.sub(try_pipe_to_code, content)

    # ── 5. Remove <colgroup> sections from HTML tables ─────────────────────
    content = re.sub(r'\n?<colgroup>.*?</colgroup>\n?', '\n', content, flags=re.DOTALL)

    # ── 6. Fix pandoc escape sequences in text and code blocks ───────────
    content = re.sub(r'\\<', '<', content)
    content = re.sub(r'\\>', '>', content)
    # Unescape \* (pandoc escapes literal asterisks in docx text)
    content = re.sub(r'\\\*', '*', content)
    # Unescape \$ (pandoc escapes $ to prevent math parsing)
    content = re.sub(r'\\\$', '$', content)
    # Unescape \[ and \] outside of link syntax
    content = re.sub(r'\\\[', '[', content)
    content = re.sub(r'\\\]', ']', content)

    # ── 7. Remove excessive blank lines (3+ → 2) ──────────────────────────
    content = re.sub(r'\n{4,}', '\n\n\n', content)

    # ── 8. Strip trailing whitespace from lines ────────────────────────────
    lines = content.split('\n')
    lines = [l.rstrip() for l in lines]
    content = '\n'.join(lines)

    # ── 9. Ensure single newline at end of file ────────────────────────────
    content = content.rstrip('\n') + '\n'

    return content


def process_file(path: Path):
    original = path.read_text(encoding='utf-8')
    cleaned = cleanup(original)
    if cleaned != original:
        path.write_text(cleaned, encoding='utf-8')
        return True
    return False


def main():
    repo = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # Directories to process (skip VitalRecorder/ — that's the old v1 folder)
    dirs = [
        repo / "VitalRecorder_v2",
        repo / "API",
        repo / "Vitalserver",
        repo / "WebMonitoring",
        repo / "General",
        repo / "OpenDataset",
        repo / "MyFiles",
    ]

    total = 0
    changed = 0
    for d in dirs:
        for md in sorted(d.rglob("*.md")):
            total += 1
            if process_file(md):
                changed += 1
                print(f"  cleaned  {md.relative_to(repo)}")
            else:
                print(f"  ok       {md.relative_to(repo)}")

    print(f"\n  {changed}/{total} files updated")


if __name__ == "__main__":
    main()
