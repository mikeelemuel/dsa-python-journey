"""
P-9.56 | Chapter 9: Priority Queues
Type: Project
Page: book p.400 (PDF p.422)    ->  python tools/show.py P-9.56
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Problem:
    Let S be a set of n points in the plane with distinct integer x-a n d y-
    coordinates. Let T be a complete binary tree storing the points from S at its
    external nodes, such that the points are ordered left to right by in- creasing
    x-coordinates. For each node v in T ,l e tS(v) denote the subset of S consisting of
    points stored in the subtree rooted at v. For the root r of T ,d e ﬁ n etop (r) to
    be the point in S = S(r) with maximum y-coordinate. For every other node v,d e ﬁ n
    etop (r) to be the point in S with highest y- coordinate in S(v) that is not also
    the highest y-coordinate in S(u),w h e r e u is the parent of v in T (if such a
    point exists). Such labeling turns T into a priority search tree. Describe a linear-
    time algorithm for turning T into a priority search tree. Implement this approach.

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
