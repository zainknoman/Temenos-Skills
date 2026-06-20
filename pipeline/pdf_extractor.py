"""
PDF Extractor for Temenos Learning Library
Scans E:\Learning, categorizes PDFs by domain, extracts text using pymupdf,
and saves structured output to cache/pdf_extracts/ for skill enhancement.
"""

import os
import json
import re
import fitz  # pymupdf
from pathlib import Path

SOURCE_DIR = Path(r"E:\Learning")
OUTPUT_DIR = Path(r"E:\Projects\Temenos-Skills\cache\pdf_extracts")

# Domain keyword rules — order matters, first match wins
DOMAIN_RULES = [
    ("programming",  [
        "infobasic", "jbase", "jbc", "programming", "coding standard",
        "tam coding", "t24 programming", "dbtools", "db tools",
        "programmers reference", "component", "subroutine", "function",
        "version routine", "validation", "nofile", "enquiry",
    ]),
    ("tafj", [
        "tafj", "tafj-as", "java system", "jdk", "jboss", "eclipse plugin",
        "tafj runtime", "tafj installation", "tafj configuration",
        "tafj technical", "tafj kick start",
    ]),
    ("aa_framework", [
        "aact", "aa common", "aa retail", "aa and ofs", "aa framework",
        "arrangement", "activity", "property class", "named activities",
        "simulation engine", "product tracker", "aa framework",
        "building blocks",
    ]),
    ("ofs_api", [
        "ofs", "soap api", "message format", "ofs transaction",
    ]),
    ("rest_api", [
        "rest api", "rest endpoint", "api lab", "application program interface",
        "apis in limited", "api behavior",
    ]),
    ("architecture", [
        "enterprise framework", "extensibility framework", "extending transact",
        "data hub", "data lake", "database platform", "architecture",
        "process orchestration", "workflow", "stack 6",
        "content packages", "add-on modules", "overview dev",
    ]),
    ("cob_batch", [
        "cob", "end of day", "eod", "batch", "commit capture",
    ]),
    ("de_documents", [
        "document engine", "de handoff", "delivery engine", "printer",
        "ear file builder", "artefact",
    ]),
    ("accounts_product", [
        "account processes", "accounts_ac", "accounts.pdf", "account statement",
        "balance check", "posting restriction", "overdraft",
    ]),
    ("deposits_product", [
        "deposit", "term deposit", "mudaraba", "wakala",
    ]),
    ("loans_product", [
        "loan", "lending", "facility", "repayment", "interest on loan",
        "amend loan", "syndicate", "preclose",
    ]),
    ("payments_product", [
        "payment", "funds transfer", "transfer", "swift", "ach", "payment order",
        "payment holiday",
    ]),
    ("customer_product", [
        "customer", "kyc", "party", "corporate customer", "retail customer",
        "person or entity",
    ]),
    ("trade_finance", [
        "import lc", "export lc", "guarantee", "standby lc", "trade",
        "collection", "letter of credit", "documentary",
    ]),
    ("analytics", [
        "analytics", "data lake", "reporting", "loan approval", "chatbot", "nlp",
    ]),
]

# Filenames to skip (non-Temenos or generic)
SKIP_PATTERNS = [
    "schaum", "software engineering",
]


def categorize(name_lower: str) -> str | None:
    for skip in SKIP_PATTERNS:
        if skip in name_lower:
            return None
    for domain, keywords in DOMAIN_RULES:
        for kw in keywords:
            if kw in name_lower:
                return domain
    return "misc"


def extract_text(pdf_path: Path, max_pages: int = 60) -> str:
    try:
        doc = fitz.open(str(pdf_path))
        pages = min(len(doc), max_pages)
        parts = []
        for i in range(pages):
            text = doc[i].get_text()
            if text.strip():
                parts.append(text)
        doc.close()
        return "\n".join(parts)
    except Exception as e:
        return f"[EXTRACT ERROR: {e}]"


def sanitize_filename(name: str) -> str:
    return re.sub(r'[<>:"/\\|?*]', '_', name)


def run():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    index = {}  # domain -> list of {file, source, pages, chars}

    pdfs = list(SOURCE_DIR.rglob("*.pdf"))
    total = len(pdfs)
    seen_names = set()
    skipped_dup = 0
    skipped_irrelevant = 0
    processed = 0

    print(f"Found {total} PDFs in {SOURCE_DIR}")

    for i, pdf_path in enumerate(pdfs, 1):
        name = pdf_path.name
        name_lower = name.lower()

        # Skip duplicates by filename
        if name_lower in seen_names:
            skipped_dup += 1
            continue
        seen_names.add(name_lower)

        domain = categorize(name_lower)
        if domain is None:
            skipped_irrelevant += 1
            continue

        domain_dir = OUTPUT_DIR / domain
        domain_dir.mkdir(exist_ok=True)

        out_name = sanitize_filename(pdf_path.stem) + ".txt"
        out_path = domain_dir / out_name

        # Skip if already extracted
        if out_path.exists():
            index.setdefault(domain, []).append({"file": out_name, "source": name, "cached": True})
            processed += 1
            if i % 50 == 0:
                print(f"  [{i}/{total}] (cached) {name}")
            continue

        text = extract_text(pdf_path)
        out_path.write_text(text, encoding="utf-8", errors="replace")

        entry = {"file": out_name, "source": name, "chars": len(text), "cached": False}
        index.setdefault(domain, []).append(entry)
        processed += 1

        if i % 25 == 0 or i <= 5:
            print(f"  [{i}/{total}] {domain:20s} | {name[:60]}")

    # Write index
    index_path = OUTPUT_DIR / "index.json"
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2)

    print(f"\nDone.")
    print(f"  Processed : {processed}")
    print(f"  Duplicates: {skipped_dup}")
    print(f"  Irrelevant: {skipped_irrelevant}")
    print(f"  Output    : {OUTPUT_DIR}")
    print(f"  Index     : {index_path}")

    # Print domain summary
    print("\nDomain summary:")
    for domain, entries in sorted(index.items()):
        print(f"  {domain:25s} {len(entries):4d} files")


if __name__ == "__main__":
    run()
