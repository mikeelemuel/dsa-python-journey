"""
R-1.9 | Chapter 1: Python Primer
Type: Reinforcement
Page: book p.51 (PDF p.73)    ->  python tools/show.py R-1.9
Status: done            # todo | in-progress | done | skipped
Date: 2026-11-11
Time:

Problem:
    What parameters should be sent to the range constructor, to produce a range with
    values 50, 60, 70, 80?

Approach:
    (idea, then time/space complexity)
    Read each parameter off the target sequence:
      start = 50 (first value), step = 10 (gap), stop = 90 (one step past 80).
    Answer: range(50, 90, 10)

    Time:  O(1) to build - a range stores only start/stop/step, not the values.
    Space: O(1).

Notes:
    - stop is a value to stop before, not a count; len(n) was the wrong idea.
    - Any stop from 81 to 90 works; stop = 80 gives only 50, 60, 70.
    - [i * 10 for i in range(5, 9)] gives the same numbers, but as a list, not a range.
    - For a changing evenly spaced list n:
      range(n[0], n[-1] + step, step) with step = n[1] - n[0]
      (needs 2+ items, equal gaps, non-zero step, ints only).
"""


# your solution here
def tens_from_50_to_80():
    return range(50, 90, 10)


if __name__ == "__main__":
    print(list(tens_from_50_to_80()))
