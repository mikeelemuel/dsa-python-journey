"""
R-1.2 | Chapter 1: Python Primer
Type: Reinforcement
Page: book p.51 (PDF p.73)    ->  python tools/show.py R-1.2
Status: done                   # todo | in-progress | done | skipped
Date: 2026-11-06
Time:

Problem:
    Write a short Python function, is even(k), that takes an integer value and returns
    True if k is even, and False otherwise. However, your function cannot use the
    multiplication, modulo, or division operators.

Approach:
    (idea, then time/space complexity)
    Idea: is_even function has a formal parameter of k, it is a int
    The caller will get a boolean True or False response from the function

    Without the multiplication, modulo or division operators, we can use the BITWISE
    This approach examines the binary representation of the integer.
    k & 1 keeps the last bit: 0 = even, 1 = odd.
    Time: O(1), Space: O(1)
Notes:
    & binds tighter than ==, so k & 1 == 0 means (k & 1) == 0.
    Works for negatives: -3 & 1 == 1.
    A leftover stub below __main__ silently overrode my function (last def wins).
"""


def is_even(k):
    return k & 1 == 0  # last bit 0 = even; works for negatives too


if __name__ == "__main__":
    pass
