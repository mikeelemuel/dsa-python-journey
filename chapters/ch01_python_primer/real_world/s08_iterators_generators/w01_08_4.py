"""
W-1.8.4 | Chapter 1: Python Primer
Type: Real-world · ★★★ Challenge
Section: 1.8 Iterators and Generators · book pp.39–41    ->  python tools/show.py W-1.8.4
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Title: Sales log pipeline
Practices: generators feeding generators · revisit 1.6 and 1.7
Source: https://claude.ai/artifact/BhyrFMkLeHaB9j9CNLUn6e

Problem:
    Imagine data/sales.txt has a million lines, so you can't load it into a
    list. Build three small generators and connect them like pipes:
    - read_lines(path) yields each stripped line, skipping blanks and lines
      starting with #.
    - parse(lines) yields (date, item, amount) tuples and silently skips lines
      that raise ValueError.
    - only(item, rows) yields just the rows for one item.
    Then compute the total taho sales in one line.

Example:
    sum(r[2] for r in only("taho", parse(read_lines("data/sales.txt"))))
    -> 55

Hint:
    Each generator takes the previous one as its input and loops over it with
    for. Only one line is in memory at any moment. Put a print in each stage to
    watch a single line travel through all three.

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
