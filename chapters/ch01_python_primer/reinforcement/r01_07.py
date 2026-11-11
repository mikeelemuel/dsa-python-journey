"""
R-1.7 | Chapter 1: Python Primer
Type: Reinforcement
Page: book p.51 (PDF p.73)    ->  python tools/show.py R-1.7
Status: done            # todo | in-progress | done | skipped
Date: 2026-11-11
Time:

Problem:
    Give a single command that computes the sum from Exercise R-1.6, rely- ing on
    Python’s comprehension syntax and the built-in sum function.

Approach:
    (idea, then time/space complexity)
    Use range(1, n, 2) to visit only the odd numbers below n.
    Square each one with a generator expression (i*i for i in ...).
    Pass the generator straight to sum().

    Time:  O(n) - about n/2 numbers, constant work each.
    Space: O(1) - the generator yields one value at a time.

Notes:
    - range(start, stop, step): the 3rd argument is the step; stop is never included.
    - Start at 1, step 2 -> odds only, so no % 2 check is needed.
    - Positive evens would be range(2, n, 2); start at 2 because 0 is not positive.
    - A negative step counts down; step 0 raises ValueError.
"""


# your solution here
def sum_of_all_odd(n):
    return sum(i*i for i in range(1, n, 2))


if __name__ == "__main__":
    print(sum_of_all_odd(10))
