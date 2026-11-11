"""
C-1.18 | Chapter 1: Python Primer
Type: Creativity
Page: book p.52 (PDF p.74)    ->  python tools/show.py C-1.18
Status: done            # todo | in-progress | done | skipped
Date: 2026-11-12
Time:

Problem:
    Demonstrate how to use Python’s list comprehension syntax to produce the list [0, 2,
    6, 12, 20, 30, 42, 56, 72, 90].

Approach:
    (idea, then time/space complexity)
    Spot the pattern: each value is n times the next number, n * (n + 1):
      0*1, 1*2, 2*3, 3*4, ... 9*10.
    Ten values -> n runs over range(10).
    [n * (n + 1) for n in range(10)]

    Time:  O(n).  Space: O(n) for the list.

Notes:
    (gotchas, what you learned)
    - The gaps grow by 2 each time (2, 4, 6, 8, ...), a hint that the
      values are products of consecutive numbers.
    - range(10) stops at 9, and 9 * 10 = 90 is the last value.
"""


# your solution here
def products_of_consecutive():
    return [n * (n + 1) for n in range(10)]


if __name__ == "__main__":
    print(products_of_consecutive())