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
    Define a function that has a signature of minmax and has formal parameter of data.
    A data could be a list which is a mutable class.
    To find the smallest number, declare a variable to store a default value of smallest and biggest value
    Use for loop to iterate the sequence of numbers
    Make a condition that would check if the current smallest value is smallest than the current value of the current index,
    if not, replace the current smallest value with the value of the current index
    Same thing with the biggest value


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
