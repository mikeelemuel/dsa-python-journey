"""
W-1.7.4 | Chapter 1: Python Primer
Type: Real-world · ★★★ Challenge
Section: 1.7 Exception Handling · book pp.33–38    ->  python tools/show.py W-1.7.4
Status: todo            # todo | in-progress | done | skipped
Date:
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

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
