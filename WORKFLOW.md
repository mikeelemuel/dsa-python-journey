# Development Workflow

Solo repo: work on `main`, commit once per session, and let the tests and tracker keep me honest.

## One-time setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install pytest pypdf
mkdir book && cp /path/to/Data_Structures_and_Algorithms_in_Python.pdf book/
python tools/show.py --fill        # writes each problem into its file (safe to re-run)
```

In VS Code: install the Python extension and select the `.venv` interpreter.

---

## Each session (weekdays, 10:00 to 11:00 PM)

### 1. Pick up where I left off (2 min)

```bash
source .venv/bin/activate
git pull                            # if I worked from another machine
python tools/progress.py --next     # e.g. Next up: R-1.1, R-1.2, R-1.3
```

### 2. Read and plan (about 5 min per exercise)

- Open the file, e.g. `chapters/ch01_python_primer/reinforcement/r01_01.py`
- Set `Status: in-progress`
- Write the idea in `Approach:` **before** coding

### 3. Write the test first

Template and tips: [TESTING.md](TESTING.md)

`chapters/ch01_python_primer/tests/test_r01_01.py`:

```python
from chapters.ch01_python_primer.reinforcement.r01_01 import is_multiple


def test_is_multiple():
    assert is_multiple(10, 5)
    assert not is_multiple(10, 3)
    assert is_multiple(0, 7)        # edge cases!
```

### 4. Solve until green

```bash
pytest chapters/ch01_python_primer -q                        # just this chapter
python chapters/ch01_python_primer/reinforcement/r01_01.py   # print-style exercises
```

### 5. Close out the exercise

```
Status: done
Date: 2026-10-30
Time: 10 min
```

Then add the time/space complexity to `Approach:` and anything surprising to `Notes:`.

### 6. Wrap up (at 10:55)

```bash
pytest                              # whole repo still passes
python tools/progress.py            # refresh PROGRESS.md
# add 2-3 lines to journal/YYYY-MM.md
git add -A
git commit -m "ch01: R-1.1, R-1.2, R-1.3"
git push
```

GitHub Actions re-runs the tests and checks that `PROGRESS.md` is current.
A green check means the session is done.

---

## Non-code exercises

For proofs, explanations, and "describe..." questions:

- Write the answer in `Approach:`, or in a markdown file next to the exercise (e.g. `r03_14.md`)
- No test needed. Mark `Status: done` as usual

## When stuck

| Situation | Do this |
|---|---|
| More than 25 min on one problem | Write what I tried in `Notes:`, leave `in-progress`, move on. It stays at the top of "Up next" |
| Not worth doing | `Status: skipped` plus one line on why (skipped exercises don't count toward the total) |
| Unfinished code at 11 PM | Commit it anyway. Never leave work uncommitted overnight |

## Chapter rhythm

| When | What |
|---|---|
| First session | Read the chapter; fill in its `README.md` (key ideas, complexity table) |
| Sessions 2 to N | Reinforcement first, then creativity |
| Book builds a class (ArrayStack, LinkedQueue...) | Move my version into `dsa/` with its own test; import it in later chapters |
| Weekend (optional) | One project from the chapter |
| Last session | Re-read chapter notes and journal, then `git tag chNN-done && git push --tags` |

## Commit conventions

```
ch05: R-5.6, R-5.7, C-5.13              normal session
ch06: add ArrayStack to dsa/            reusable code
ch05: revisit C-5.20 (O(n) solution)    improving an old answer
chore: update tools/progress.py         repo housekeeping
```

## Cheat sheet

```bash
python tools/progress.py --next   # what's next
python tools/show.py R-5.7        # re-read a problem from the PDF
pytest chapters/ch05_* -q         # test one chapter
pytest                            # test everything
python tools/progress.py          # refresh tracker
```
