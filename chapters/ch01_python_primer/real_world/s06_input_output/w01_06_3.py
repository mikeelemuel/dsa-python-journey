"""
W-1.6.3 | Chapter 1: Python Primer
Type: Real-world · ★★ Building up
Section: 1.6 Simple Input and Output · book pp.30–32    ->  python tools/show.py W-1.6.3
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Title: Class average from a file
Practices: for line in fp · strip · print(file=)
Source: https://claude.ai/artifact/R4zdNBmahtUo7GwysUZkKz

Problem:
    Read data/grades.txt line by line, compute each student's average, and
    write a summary to data/summary.txt using print(..., file=out). Mark anyone
    below 75 as FAILED.

Example:
    data/grades.txt          data/summary.txt
    Ana,88,92,79             Ana   86.33  PASSED
    Ben,70,65,81             Ben   72.00  FAILED
    Carl,95,90,98            Carl  94.33  PASSED
    Dina,74,76,72            Dina  74.00  FAILED

Hint:
    Each line ends with a newline. Use line.strip().split(","), then convert
    the scores with int(). Left-align names with f"{name:<6}".

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
