"""
R-1.4 | Chapter 1: Python Primer
Type: Reinforcement
Page: book p.51 (PDF p.73)    ->  python tools/show.py R-1.4
Status: done            # todo | in-progress | done | skipped
Date: 2026-11-11
Time:

Problem:
    Write a short Python function that takes a positive integer n and returns the sum of
    the squares of all the positive integers smaller than n.

Approach:
    (idea, then time/space complexity)
    Start a running total all_squares at 0.
    Loop i over range(1, n), i.e. 1 .. n-1, and add i*i to the total.
    Return the total.

    Time:  O(n) - one pass over n-1 numbers, constant work per number.
    Space: O(1) - only the running total and the loop variable.

Notes:
    - range(1, n) stops before n, which is exactly "smaller than n".
    - n = 1 gives an empty range, so the result is 0.
    - Closed form (n-1)n(2n-1)/6 would make it O(1).
"""


# your solution here
def sum_of_squares(n):
    all_squares = 0

    for i in range(1, n):
        all_squares += i*i

    return all_squares

if __name__ == "__main__":
    pass
