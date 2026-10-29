"""
C-14.73 | Chapter 14: Graph Algorithms
Type: Creativity
Page: book p.694 (PDF p.716)    ->  python tools/show.py C-14.73
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Problem:
    Karen has a new way to do path compression in a tree-based union/ﬁnd partition data
    structure starting at a position p. She puts all the positions that are on the path
    from p to the root in a set S. Then she scans through S and sets the parent pointer
    of each position in S to its parent’s parent pointer (recall that the parent pointer
    of the root points to itself). If this pass changed the value of any position’s
    parent pointer, then she repeats this process, and goes on repeating this process
    until she makes a scan through S that does not change any position’s parent value.
    Show that Karen’s algorithm is correct and analyze its running time for a path of
    length h.

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
