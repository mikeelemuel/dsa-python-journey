"""
C-1.15 | Chapter 1: Python Primer
Type: Creativity
Page: book p.52 (PDF p.74)    ->  python tools/show.py C-1.15
Status: done            # todo | in-progress | done | skipped
Date: 2026-11-12
Time:

Problem:
    Write a Python function that takes a sequence of numbers and determines if all the
    numbers are different from each other (that is, they are distinct).

Approach:
    (idea, then time/space complexity)
    A set keeps one copy of each value, so duplicates collapse.
    If the set is as long as the sequence, nothing was dropped -> all distinct.

    Time:  O(n) average - one pass to build the set.
    Space: O(n) - the set can hold every value.

Notes:
    (gotchas, what you learned)
    - First try (commented out) used copies.pop(i) with i as a VALUE, but pop()
      takes a POSITION: [1, 2, 3] gave False and [5, 6, 7] raised IndexError.
      Loop with enumerate(numbers) to get (position, value) pairs.
    - True if x else False is just x.
    - A function needs to be called; return only works inside a def.
    - Dict keys and set items can't repeat; list and tuple items can.
    - Tuples can go in a set (hashable); lists can't.
"""


# your solution here
def is_distinct(numbers):
    # for i in numbers:
    #     copies = numbers.copy()
    #     copies.pop(i)
    #
    #     if i in copies:
    #         return False
    # return True
    return len(set(numbers)) == len(numbers)


if __name__ == "__main__":
    numbers = [1, 2, 4, 8, 6, 7, 8]
    print(is_distinct(numbers))


