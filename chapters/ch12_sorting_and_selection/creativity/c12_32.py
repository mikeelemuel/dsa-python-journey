"""
C-12.32 | Chapter 12: Sorting and Selection
Type: Creativity
Page: book p.576 (PDF p.598)    ->  python tools/show.py C-12.32
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Problem:
    Another way to analyze randomized quick-sort is to use a recurrence equation. In
    this case, we let T (n) denote the expected running time of randomized quick-sort,
    and we observe that, because of the worst-case partitions for good and bad splits,
    we can write T (n) ≤ 1 2 (T (3n/4)+ T (n/4)) + 1 2 (T (n − 1)) +bn, where bn is the
    time needed to partition a list for a given pivot and concate- nate the result
    sublists after the recursive calls return. Show, by induction, that T (n) is O(nlog
    n).

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
