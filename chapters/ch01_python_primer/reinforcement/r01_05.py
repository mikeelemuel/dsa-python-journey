"""
R-1.5 | Chapter 1: Python Primer
Type: Reinforcement
Page: book p.51 (PDF p.73)    ->  python tools/show.py R-1.5
Status: done            # todo | in-progress | done | skipped
Date: 2026-11-11
Time:

Problem:
    Give a single command that computes the sum from Exercise R-1.4, rely- ing on
    Python’s comprehension syntax and the built-in sum function.

Approach:
    (idea, then time/space complexity)
    Use the sum() built in function
    Use the formula i**2 to  get the squares of the integer
    Use the for loop range to get the positive less than n

    Time:  O(n) - one square per number in 1 .. n-1.
    Space: O(1) - a generator expression yields one value at a time.

Notes:
    - The bare expression at module level raised NameError (n undefined);
      it needs to live inside a function that takes n.
    - sum(i**2 for i in ...) is a generator expression: no list is built.
      sum([i**2 for i in ...]) would allocate an O(n) list first.
"""


# your solution here
def sum_of_squares(n):
    return sum(i**2 for i in range(1, n))

if __name__ == "__main__":
    pass
