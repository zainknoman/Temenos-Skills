#!/usr/bin/env python3
"""Turn a Word document into a searchable PDF for Layer B (pdf_extract.py).

Some training material arrives as .docx files whose content is almost all
slide screenshots (e.g. the Temenos COB Foundation / Implementation courses:
88 and 188 images, no body text). pdfplumber reads only a text layer, so
those slides would index as nothing. This step:

  1. Reads word/document.xml in reading order and takes every paragraph's
     text plus every embedded image (a:blip), in the order they appear.
  2. OCRs each image offline with the Windows OCR engine
     (pipeline/ocr_windows.ps1 -- Windows.Media.Ocr, no install, no network).
  3. Writes one PDF page per image: the slide picture on top, its OCR text
     (and any Word text that preceded it) as a real text layer below.
     Page N of the PDF is slide N, so query_docs.py hits cite the slide.

The PDF lands under docs/<topic>/, then pdf_extract.py indexes it like any
other PDF (topic = the docs/ folder name). OCR text per slide is also kept
next to the PDF as <name>.ocr/NNN.txt for review.

Usage (Windows only, because of the OCR engine):
  py -3 pipeline/docx_extract.py --docx "D:/Learning/COB/COB Foundation.docx" --topic COB --transcript claude-project/COB/knowledge/cob-foundation-transcript.md
  py -3 pipeline/pdf_extract.py --pdfs docs --vectordb vectordb --cache cache/pdf_extracts
"""
import argparse
import math
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

import fitz  # PyMuPDF

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
A_BLIP = "{http://schemas.openxmlformats.org/drawingml/2006/main}blip"
R_EMBED = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed"
OCR_PS1 = Path(__file__).with_name("ocr_windows.ps1")

PAGE_W = 960
MARGIN = 30
FONT_SIZE = 9
LINE_H = FONT_SIZE * 1.35
CHARS_PER_LINE = 165  # helv at 9pt across PAGE_W - 2*MARGIN, conservative


def read_docx(path: Path):
    """Yield ('text', str) and ('image', bytes, ext) items in document order."""
    z = zipfile.ZipFile(path)
    root = ET.fromstring(z.read("word/document.xml"))
    rels = {r.get("Id"): r.get("Target") for r in ET.fromstring(z.read("word/_rels/document.xml.rels"))}
    for p in root.iter(W + "p"):
        text = "".join(t.text or "" for t in p.iter(W + "t")).strip()
        if text:
            yield ("text", text)
        for blip in p.iter(A_BLIP):
            target = rels.get(blip.get(R_EMBED))
            if target:
                name = target if target.startswith("word/") else "word/" + target.lstrip("/")
                yield ("image", z.read(name), Path(target).suffix.lower())


def ocr_images(img_dir: Path, out_dir: Path):
    subprocess.run(
        ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(OCR_PS1),
         "-InDir", str(img_dir), "-OutDir", str(out_dir)],
        check=True,
    )


def clean(text: str) -> str:
    """Keep what the PDF base-14 font can encode (Latin-1)."""
    text = text.replace("\ufeff", "").replace("\u2022", "-").replace("\u2014", "-").replace("\u2013", "-")
    text = unicodedata.normalize("NFKC", text)
    return text.encode("latin-1", "replace").decode("latin-1")


def text_height(text: str) -> float:
    lines = sum(max(1, math.ceil(len(line) / CHARS_PER_LINE)) for line in text.splitlines() or [""])
    return lines * LINE_H + 2 * MARGIN


def add_slide(doc, img_bytes: bytes, text: str):
    pix = fitz.Pixmap(img_bytes)
    img_w = PAGE_W - 2 * MARGIN
    img_h = pix.height * img_w / pix.width
    height = MARGIN + img_h + text_height(text)
    while True:
        page = doc.new_page(width=PAGE_W, height=height)
        page.insert_image(fitz.Rect(MARGIN, MARGIN, MARGIN + img_w, MARGIN + img_h), stream=img_bytes)
        box = fitz.Rect(MARGIN, MARGIN + img_h + 10, PAGE_W - MARGIN, height - MARGIN)
        if page.insert_textbox(box, text, fontsize=FONT_SIZE, fontname="helv") >= 0:
            return
        doc.delete_page(-1)
        height *= 1.3


def write_transcript(ocr_dir: Path, out: Path, title: str):
    """Narration-only Markdown: each slide's text up to its first bullet line.
    Screenshot OCR (field dumps, shell output) is dropped because it is mostly noise.
    A slide that starts 'Concept - <name> ... Welcome' opens a new '## <name>' section."""
    lines = [f"# {title} course transcript", "",
             "Narration of each slide, OCR'd from slide screenshots by pipeline/docx_extract.py.",
             "Slide N here = page N of the source PDF.", ""]
    for f in sorted(ocr_dir.glob("*.txt")):
        narr = []
        for line in f.read_text(encoding="utf-8-sig").splitlines():
            if line.lstrip().startswith(("•", "- ")):
                break
            narr.append(line.strip())
        text = re.sub(r"\s+", " ", " ".join(narr)).strip()
        m = re.match(r"Concept\s*[-—]\s*(.+?) Welcome", text)
        if m:
            lines += [f"## {m.group(1).strip()}", ""]
        lines += [f"**Slide {int(f.stem)}.** {text}", ""]
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote transcript {out}")


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser()
    ap.add_argument("--docx", required=True)
    ap.add_argument("--topic", required=True, help="docs/ sub-folder = Layer B topic")
    ap.add_argument("--docs", default="docs")
    ap.add_argument("--name", help="PDF base name (default: the .docx name)")
    ap.add_argument("--transcript", help="also write a narration-only Markdown transcript here")
    args = ap.parse_args()

    src = Path(args.docx)
    out_dir = Path(args.docs) / args.topic
    out_dir.mkdir(parents=True, exist_ok=True)
    name = args.name or src.stem
    pdf_path = out_dir / f"{name}.pdf"
    ocr_keep = out_dir / f"{name}.ocr"

    items = list(read_docx(src))
    images = [i for i in items if i[0] == "image"]
    print(f"{src.name}: {len(images)} images, {sum(1 for i in items if i[0] == 'text')} text paragraphs")

    with tempfile.TemporaryDirectory() as tmp:
        img_dir, txt_dir = Path(tmp) / "img", Path(tmp) / "txt"
        img_dir.mkdir()
        n = 0
        for item in items:
            if item[0] == "image":
                n += 1
                (img_dir / f"{n:03d}.png").write_bytes(
                    item[1] if item[2] == ".png" else fitz.Pixmap(item[1]).tobytes("png"))
        ocr_images(img_dir, txt_dir)

        doc = fitz.open()
        pending, n = [], 0
        for item in items:
            if item[0] == "text":
                pending.append(item[1])
                continue
            n += 1
            png = (img_dir / f"{n:03d}.png").read_bytes()
            ocr = (txt_dir / f"{n:03d}.txt").read_text(encoding="utf-8-sig") if (txt_dir / f"{n:03d}.txt").exists() else ""
            add_slide(doc, png, clean("\n".join(pending + [ocr]).strip()))
            pending = []
        if pending and doc.page_count:
            doc[-1].insert_text((MARGIN, MARGIN), clean("\n".join(pending)), fontsize=FONT_SIZE)
        doc.set_metadata({"title": name, "subject": f"OCR of {src.name}", "creator": "pipeline/docx_extract.py"})
        doc.save(pdf_path, garbage=3, deflate=True)

        if ocr_keep.exists():
            shutil.rmtree(ocr_keep)
        shutil.copytree(txt_dir, ocr_keep)

    print(f"Wrote {pdf_path} ({n} pages) and OCR text in {ocr_keep}")
    if args.transcript:
        write_transcript(ocr_keep, Path(args.transcript), name)


if __name__ == "__main__":
    main()
