# DSA in Python: Weekday Refresher

Working through every chapter of *Data Structures and Algorithms in Python*
(Goodrich, Tamassia, Goldwasser), one exercise set at a time.

**Schedule:** Monday to Friday, 10:00 to 11:00 PM (Asia/Manila)
**Progress:** see [PROGRESS.md](PROGRESS.md)

## Layout

```
chapters/chNN_topic/
    README.md          my notes for the chapter
    reinforcement/     R-x.y  short drills
    creativity/        C-x.y  harder problems
    projects/          P-x.y  bigger builds
    tests/             pytest tests for my solutions
dsa/                   reusable classes I build (stacks, queues, trees...)
journal/YYYY-MM.md     2-3 lines per session
tools/progress.py      rebuilds PROGRESS.md from each file's Status: line
tools/show.py          prints an exercise's text from my local copy of the PDF
```

File names follow the book: `r05_07.py` is **R-5.7**.

## Pacing plan

| Type | Plan | Per session |
|---|---|---|
| Reinforcement | do all | 3 to 5 |
| Creativity | about half (`Status: skipped` for the rest) | 1 to 2 |
| Projects | 1 to 2 per chapter, on weekends | n/a |

The first session of each chapter is reading only, plus filling in the chapter README.

## Session routine

1. `python tools/progress.py --next` to see where I left off
2. Open those files and read the problem in the docstring (or `python tools/show.py R-5.7`)
3. Solve. In each file set `Status: done`, `Date:`, `Time:`, then write the approach and a test
4. Add 2 to 3 lines to `journal/`
5. Run these and push:

```bash
pytest
python tools/progress.py
git add -A && git commit -m "ch05: R-5.6, R-5.7, C-5.13" && git push
```

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install pytest pypdf
mkdir book && cp /path/to/Data_Structures_and_Algorithms_in_Python.pdf book/
python tools/show.py --fill    # writes each problem into its file's Problem: section
pytest
```

`book/` and `*.pdf` are git-ignored, so the PDF itself never gets pushed.

> **Keep this repo private.** After `--fill`, the files contain the book's exercise text.
