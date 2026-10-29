"""
C-10.34 | Chapter 10: Maps, Hash Tables, and Skip Lists
Type: Creativity
Page: book p.455 (PDF p.477)    ->  python tools/show.py C-10.34
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Problem:
    Computing a hash code can be expensive, especially for lengthy keys. In our hash
    table implementations, we compute the hash code when ﬁrst in- serting an item, and
    recompute each item’s hash code each time we resize our table. Python’s dict class
    makes an interesting trade-off. The hash code is computed once, when an item is
    inserted, and the hash code is stored as an extra ﬁeld of the item composite, so
    that it need not be recom- puted. Reimplement our HashTableBase class to use such an
    approach.

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
