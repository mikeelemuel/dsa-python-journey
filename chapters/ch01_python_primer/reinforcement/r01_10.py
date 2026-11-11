"""
R-1.10 | Chapter 1: Python Primer
Type: Reinforcement
Page: book p.51 (PDF p.73)    ->  python tools/show.py R-1.10
Status: done            # todo | in-progress | done | skipped
Date: 2026-11-11
Time:

Problem:
    What parameters should be sent to the range constructor, to produce a range with
    values 8, 6, 4, 2, 0, −2, −4, −6, −8?

Approach:
    (idea, then time/space complexity)
    start = 8 (first value), step = -2 (counting down by 2),
    stop = -10 (one step past -8, going down).
    Answer: range(8, -10, -2)

    Time:  O(1) to build - a range stores only start/stop/step.
    Space: O(1).

Notes:
    - First try was range(8, -8, -2): it stops at -6 because stop is never included.
    - Counting down, stop must be below the last value: any stop from -9 to -10 works.
"""


# your solution here
def evens_from_8_to_minus_8():
    return range(8, -10, -2)


if __name__ == "__main__":
    print(list(evens_from_8_to_minus_8()))
