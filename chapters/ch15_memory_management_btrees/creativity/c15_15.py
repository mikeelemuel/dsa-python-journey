"""
C-15.15 | Chapter 15: Memory Management and B-Trees
Type: Creativity
Page: book p.718 (PDF p.740)    ->  python tools/show.py C-15.15
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Problem:
    Another possible external-memory map implementation is to use a skip list, but to
    collect consecutive groups ofO(B) nodes, in individual blocks, on any level in the
    skip list. In particular, we deﬁne an order-d B-skip list to be such a
    representation of a skip list structure, where each block contains at least ⌈d/2⌉
    list nodes and at most d list nodes. Let us also choose d in this case to be the
    maximum number of list nodes from a level of a skip list that can ﬁt into one block.
    Describe how we should modify the skip-list insertion and removal algorithms for a
    B-skip list so that the expected height of the structure is O(log n/log B).

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
