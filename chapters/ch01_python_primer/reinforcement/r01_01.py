"""
R-1.1 | Chapter 1: Python Primer
Type: Reinforcement
Page: book p.51 (PDF p.73)    ->  python tools/show.py R-1.1
Status: done                   # todo | in-progress | done | skipped
Date: 2026-11-06
Time:

Problem:
    Write a short Python function, is multiple(n, m), that takes two integer values and
    returns True if n is a multiple of m, that is ,n = mi for some integer i, and False otherwise.

Approach:
    (idea, then time/space complexity)
    Define a multiple function that has formal parameters of n and m
    Use modulus "%" to identify if n is multiple of m.
    If there is no remainder, return True
    Else False
    Time: O(1), Space: O(1)
Notes:
    m == 0 needs a special case: n % 0 raises ZeroDivisionError, and only 0 is a multiple of 0.
"""


def is_multiple(n, m):
    if m == 0:
        return n == 0  # only 0 is a multiple of 0, and n % 0 would crash
    return n % m == 0


if __name__ == "__main__":
    pass
