"""
R-1.6 | Chapter 1: Python Primer
Type: Reinforcement
Page: book p.51 (PDF p.73)    ->  python tools/show.py R-1.6
Status: done            # todo | in-progress | done | skipped
Date: 2026-11-11
Time:

Problem:
    Write a short Python function that takes a positive integer n and returns the sum of
    the squares of all the odd positive integers smaller than n.

Approach:
    (idea, then time/space complexity)
    Write a function that has a signature of sum_of_all_odd that has a formal parameter of n
    Define a variable that holds the sum oof all odd
    Use the for loop range(1, n) to iterate the positive integer smaller than n
    Use condition i % 2 != 0 to find the integer is odd
    if it's odd, make a square expression of the i
    return the sum

    Time:  O(n) - one pass over 1 .. n-1, constant work per number.
    Space: O(1) - only the running total and the loop variable.

Notes:
    - range(1, n) stops before n, so an odd n is not included (n=7 -> 1+9+25).
    - n = 1 gives an empty range, so the result is 0.
    - range(1, n, 2) visits only the odd numbers and drops the % check.
    - The __main__ block must pass a real value; sum_of_all_odd(n) raised
      NameError because n was never defined at module level.
"""


# your solution here
def sum_of_all_odd(n):
    total = 0

    for i in range(1, n):
        if i % 2 != 0:
            total += i*i

    return total

if __name__ == "__main__":
    print(sum_of_all_odd(10))
