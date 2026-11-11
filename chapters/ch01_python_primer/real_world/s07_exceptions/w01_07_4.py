"""
W-1.7.4 | Chapter 1: Python Primer
Type: Real-world · ★★★ Challenge
Section: 1.7 Exception Handling · book pp.33–38    ->  python tools/show.py W-1.7.4
Status: done            # todo | in-progress | done | skipped
Date: 2026-11-12
Time:

Title: Bulletproof grades reader
Practices: multiple excepts · finally · revisit 1.6
Source: https://claude.ai/artifact/SDiTepd5Sp8BBrktSDb1PQ

Problem:
    Upgrade your class average program from W-1.6.3 so it survives the messy
    data/grades.txt in this folder.
    - If the file is missing, print "grades.txt not found" and stop gracefully.
    - Skip any line that can't be parsed. Keep a list of the skipped line
      numbers and the reason for each.
    - A student may have any number of scores. Only a name with zero scores
      counts as bad.
    - Use finally to close the file and print "Finished reading." no matter
      what happened.

Example:
    Ana   86.33
    Carl  94.33
    Eli   88.00
    Skipped: line 2 (invalid literal for int(): 'sixty'), line 4 (no scores), line 5 (blank)
    Finished reading.

Hint:
    Wrap the open in one try and each line's parsing in a smaller inner try.
    Opening a missing file raises FileNotFoundError in modern Python, which is a
    subclass of the book's IOError (now called OSError), so catching either
    works.

Approach:
    (idea, then time/space complexity)
    Outer try: open the file; except FileNotFoundError prints "not found";
    finally closes the file (if it opened) and prints "Finished reading.".
    Inner try per line (numbered with enumerate): split on commas, int() each
    score, raise ValueError("no scores") if there are none. On ValueError,
    record "line N (reason)" and move on. Blank lines are recorded as skipped too.

    Time:  O(total characters in the file) - one pass.
    Space: O(skipped lines) - only the skip list is kept.

Notes:
    (gotchas, what you learned)
    - My first try had one outer `except ValueError`: it caught 'sixty' but
      that jumped OUT of the loop, so Carl and Eli were never read.
      Catch per-line errors inside the loop so the loop keeps going.
    - A name with no scores means count == 0 -> ZeroDivisionError; raising
      ValueError("no scores") routes it to the same skip handler.
    - str(e) gives the reason; Python's real text is
      "invalid literal for int() with base 10: 'sixty'" (the example shortens it).
    - fp = None before the try, so finally can tell whether open() succeeded.
    - The path is built from __file__ so it works from any working directory.
"""

from pathlib import Path

GRADES_FILE = Path(__file__).parent / "data" / "grades.txt"


# your solution here
def parse_line(line):
    """Return (name, average) or raise ValueError with the reason."""
    name, *scores = line.split(",")
    if not scores:
        raise ValueError("no scores")
    numbers = [int(s) for s in scores]
    return name, sum(numbers) / len(numbers)


def grade_summarization(path=GRADES_FILE):
    skipped = []
    fp = None
    try:
        fp = open(path)
        for line_no, line in enumerate(fp, start=1):
            line = line.strip()
            if line == "":
                skipped.append(f"line {line_no} (blank)")
                continue
            try:
                name, average = parse_line(line)
            except ValueError as e:
                skipped.append(f"line {line_no} ({e})")
                continue
            print(f"{name:<6}{average:.2f}")
        if skipped:
            print("Skipped: " + ", ".join(skipped))
    except FileNotFoundError:
        print(f"{path.name} not found")
    finally:
        if fp is not None:
            fp.close()
        print("Finished reading.")


if __name__ == "__main__":
    grade_summarization()
    grade_summarization(GRADES_FILE.with_name("missing.txt"))
