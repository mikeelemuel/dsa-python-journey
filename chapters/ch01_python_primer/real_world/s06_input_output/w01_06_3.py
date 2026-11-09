"""
W-1.6.3 | Chapter 1: Python Primer
Type: Real-world · ★★ Building up
Section: 1.6 Simple Input and Output · book pp.30–32    ->  python tools/show.py W-1.6.3
Status: done            # todo | in-progress | done | skipped
Date: 2026-11-09
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
    To open a file, we will use fp = open('filename')
    We will use the readline() method to read the file line by line

Notes:
    (gotchas, what you learned)
    - `for line in fp` reads one line at a time, which is simpler than calling
      readline() in a loop (the Approach above mentions readline, but the
      for loop is what the solution uses).
    - Each line keeps its trailing "\n", so strip() it before split(",").
      Otherwise the last score is "79\n". int() would still accept it, but the
      blank-line check would not.
    - Skip blank lines (`continue`). A trailing empty line would otherwise
      crash on int() or divide by zero.
    - print(..., file=out) writes to the file and adds the newline for you,
      unlike out.write().
    - One `with` can open two files: `with open(a) as fp, open(b, "w") as out`.
      Both are closed when the block ends.
    - f"{name:<6}" pads the name to 6 characters so the columns line up;
      {average:.2f} gives 2 decimals.
    - Paths are relative to the folder you run from, so run it from
      s06_input_output/.
    - Time O(n) over all scores, space O(1) (one line at a time).
"""


# your solution here
def grade_summarization():
    with open("data/grades.txt") as fp, open("data/summary.txt", "w") as out:
        for line in fp:
            line = line.strip()
            if line == "":
                continue

            parts = line.split(",")
            name = parts[0]

            total = 0
            count = 0
            for s in parts[1:]:
                total += int(s)
                count += 1

            average = total / count

            if average >= 75:
                status = "PASSED"
            else:
                status = "FAILED"

            print(f"{name:<6}{average:.2f}  {status}", file=out)


if __name__ == "__main__":
    grade_summarization()
