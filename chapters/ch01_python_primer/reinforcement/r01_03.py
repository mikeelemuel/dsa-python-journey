"""
R-1.3 | Chapter 1: Python Primer
Type: Reinforcement
Page: book p.51 (PDF p.73)    ->  python tools/show.py R-1.3
Status: done                   # todo | in-progress | done | skipped
Date: 2026-11-07
Time:

Problem:
    Write a short Python function, minmax(data), that takes a sequence of one or more
    numbers, and returns the smallest and largest numbers, in the form of a tuple of
    length two. Do not use the built-in functions min or max in implementing your
    solution.

Approach:
    (idea, then time/space complexity)
    Define minmax(data), where data is any sequence of numbers (list, tuple, ...).
    Start both smallest and biggest at data[0], so they begin as real values from the input.
    Loop over every value in data:
        - if the value is less than smallest, it becomes the new smallest
        - otherwise, if it is greater than biggest, it becomes the new biggest
    Return (smallest, biggest) as a tuple.

    Time:  O(n) - one pass over the n items, constant work per item.
    Space: O(1) - only two extra variables (smallest, biggest), no matter how big n is.

Notes:
    - data[0] works because the input has at least one number; an empty sequence
      would raise IndexError.
    - Initializing to 0 fails for lists like [5, 8, 3] or all-negative lists.
    - "return a, b" returns the tuple (a, b).
"""

def minmax(data):
    smallest = biggest = data[0]

    for value in data:
        if value < smallest:
            smallest = value
        elif value > biggest:
            biggest = value

    return smallest, biggest


if __name__ == "__main__":
    pass
