"""
W-1.8.5 | Chapter 1: Python Primer
Type: Real-world · ★★★ Challenge
Section: 1.8 Iterators and Generators · book pp.39–41    ->  python tools/show.py W-1.8.5
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Title: Pandesal tray layouts
Practices: multiple yields · √n trick · order of results
Source: https://claude.ai/artifact/BhyrFMkLeHaB9j9CNLUn6e

Problem:
    A bakery puts n pandesal on a rectangular tray, rows x cols with no gaps.
    Write a generator tray_layouts(n) that yields every (rows, cols) pair IN
    INCREASING ORDER OF ROWS. It should only loop k while k * k <= n, like the
    faster factor generator on page 41.

Example:
    list(tray_layouts(36))
    [(1, 36), (2, 18), (3, 12), (4, 9), (6, 6), (9, 4), (12, 3), (18, 2), (36, 1)]

    list(tray_layouts(13))
    [(1, 13), (13, 1)]

Hint:
    The book's version yields k and n // k right away, which mixes up the
    order. Yield the small rows immediately but save the large partners in a
    list. After the loop, yield them in reverse. Don't yield the perfect-square
    case (6, 6) twice.

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
