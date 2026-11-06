"""Print an exercise's text from YOUR copy of the book (the PDF stays on your machine).

Setup (once):
    pip install pypdf
    mkdir book && cp /path/to/Data_Structures_and_Algorithms_in_Python.pdf book/
    # book/ is in .gitignore, so the PDF never gets pushed

Usage:
    python tools/show.py R-5.7
    python tools/show.py r05_07          # file-name style works too
    python tools/show.py W-1.6.3         # real-world exercise (read from its file, no PDF needed)
    python tools/show.py --next          # show your next 3 todo exercises
    python tools/show.py --fill          # write every problem into its file's Problem: section
                                         # (only fills untouched placeholders; safe to re-run)
"""
import json
import os
import re
import sys
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = json.loads((ROOT / "tools" / "exercise_pages.json").read_text())
ID_RE = re.compile(r"(?m)^\s*([RCP])\s*-\s*(\d{1,2})\s*\.\s*(\d{1,2})\b")
STOP_RE = re.compile(r"(?m)^\s*(Creativity|Projects|Chapter Notes)\s*$")


def find_pdf():
    env = os.environ.get("DSA_BOOK_PDF")
    if env:
        return Path(env)
    pdfs = sorted((ROOT / "book").glob("*.pdf"))
    if not pdfs:
        sys.exit("No PDF found. Put the book in book/ or set DSA_BOOK_PDF=/path/to/book.pdf")
    return pdfs[0]


def normalize(arg):
    m = re.fullmatch(r"([rcpRCP])-?0*(\d{1,2})[._]0*(\d{1,2})(\.py)?", Path(arg).name)
    if not m:
        sys.exit(f"Can't read exercise id: {arg!r} (try R-5.7 or r05_07)")
    return f"{m.group(1).upper()}-{int(m.group(2))}.{int(m.group(3))}"


def extract(reader, ex):
    if ex not in PAGES:
        return f"{ex}: not an exercise in this book."
    pdf_page = PAGES[ex]["pdf_page"] - 1
    # drop each page's running header (first line) so it doesn't leak into the text
    text = "\n".join(
        (reader.pages[i].extract_text() or "").split("\n", 1)[-1]
        for i in range(pdf_page, min(pdf_page + 2, len(reader.pages)))
    )
    starts = [m for m in ID_RE.finditer(text)]
    for i, m in enumerate(starts):
        if f"{m.group(1)}-{int(m.group(2))}.{int(m.group(3))}" == ex:
            end = starts[i + 1].start() if i + 1 < len(starts) else len(text)
            stop = STOP_RE.search(text, m.end(), end)
            body = text[m.end(): stop.start() if stop else end]
            body = re.sub(r"\s+", " ", body).strip()
            return (f"{ex}  (book p.{PAGES[ex]['book_page']}, PDF p.{PAGES[ex]['pdf_page']})\n\n"
                    + textwrap.fill(body, 88)
                    + "\n\n(PDF text extraction can drop underscores or mangle math spacing."
                    " Check the page if something looks off.)")
    return f"{ex}: couldn't parse the text. Open the PDF at page {PAGES[ex]['pdf_page']}."


W_RE = re.compile(r"[wW]-?0*(\d{1,2})[._]0*(\d{1,2})[._](\d{1,2})(\.py)?")
ORDER = {"w": 0, "r": 1, "c": 2, "p": 3}  # real-world first within a chapter


def exercise_files():
    files = list((ROOT / "chapters").rglob("[rcp][0-9][0-9]_[0-9][0-9].py"))
    files += (ROOT / "chapters").rglob("w[0-9][0-9]_[0-9][0-9]_[0-9]*.py")
    return sorted(files, key=lambda p: (p.name[1:3], ORDER[p.name[0]], p.name[4:6],
                                        int(p.stem.split("_")[2]) if p.name[0] == "w" else 0))


def show_real_world(arg):
    """Real-world exercises aren't in the book: print the problem from the file itself."""
    m = W_RE.fullmatch(Path(arg).name)
    name = f"w{int(m.group(1)):02}_{int(m.group(2)):02}_{int(m.group(3))}.py"
    found = list((ROOT / "chapters").rglob(name))
    if not found:
        return f"W-{int(m.group(1))}.{int(m.group(2))}.{int(m.group(3))}: no file named {name}"
    doc = found[0].read_text(encoding="utf-8").split('"""')[1]
    return doc.split("\nApproach:")[0].strip()


def next_todo(n=3):
    out = []
    for f in exercise_files():
        head = f.read_text(encoding="utf-8")[:600]
        if re.search(r"^Status:\s*(todo|in-progress)", head, re.M):
            out.append(f.name)
        if len(out) == n:
            break
    return out


PLACEHOLDER = "    (paraphrase the exercise in your own words)"


def problem_text(reader, ex):
    """The problem body, wrapped and indented to sit inside the file's docstring."""
    out = extract(reader, ex)
    parts = out.split("\n\n")
    if len(parts) < 3:
        return None
    body = " ".join(parts[1].split())
    body = body.replace("\\", "\\\\").replace('"""', "'''")  # keep the docstring valid
    return textwrap.indent(textwrap.fill(body, 84), "    ")


def fill(reader):
    files = sorted((ROOT / "chapters").rglob("[rcp][0-9][0-9]_[0-9][0-9].py"))
    filled = 0
    for f in files:
        src = f.read_text(encoding="utf-8")
        if PLACEHOLDER not in src:
            continue  # already filled, or you wrote your own; never overwrite
        text = problem_text(reader, normalize(f.name))
        if text:
            f.write_text(src.replace(PLACEHOLDER, text, 1), encoding="utf-8")
            filled += 1
    print(f"Filled {filled} file(s); {len(files) - filled} already had text and were left alone.")


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    ids = next_todo() if sys.argv[1] == "--next" else sys.argv[1:]
    if all(W_RE.fullmatch(Path(a).name) for a in ids):  # real-world only: no PDF needed
        return print(("\n" + "-" * 60 + "\n\n").join(show_real_world(a) for a in ids))
    try:
        from pypdf import PdfReader
    except ImportError:
        sys.exit("Install pypdf first: pip install pypdf")
    reader = PdfReader(str(find_pdf()))
    if sys.argv[1] == "--fill":
        return fill(reader)
    for i, arg in enumerate(ids):
        if i:
            print("\n" + "-" * 60 + "\n")
        print(show_real_world(arg) if W_RE.fullmatch(Path(arg).name) else extract(reader, normalize(arg)))


if __name__ == "__main__":
    main()
