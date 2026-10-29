"""
P-8.67 | Chapter 8: Trees
Type: Project
Page: book p.359 (PDF p.381)    ->  python tools/show.py P-8.67
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Problem:
    A slicing ﬂoor plan divides a rectangle with horizontal and vertical sides using
    horizontal and vertical cuts. (See Figure 8.25a.) A slicing ﬂoor plan can be
    represented by a proper binary tree, called a slicing tree, whose internal nodes
    represent the cuts, and whose external nodes represent the basic rectangles into
    which the ﬂoor plan is decomposed by the cuts. (See Figure 8.25b.) The compaction
    problem for a slicing ﬂoor plan is deﬁned as follows. Assume that each basic
    rectangle of a slicing ﬂoor plan is assigned a minimum width w and a minimum height
    h. The compaction problem is to ﬁnd the smallest possible height and width for each
    rectangle of the slicing ﬂoor plan that is compatible with the minimum dimensions A
    B CD EF D E F B C A (a) (b) Figure 8.25: (a) Slicing ﬂoor plan; (b) slicing tree
    associated with the ﬂoor plan. of the basic rectangles. Namely, this problem
    requires the assignment of values h(p) and w(p) to each position p of the slicing
    tree such that: w(p)= ⎧ ⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨ ⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎩ w if p is a leaf whose basic
    rectangle hasminimum width w max(w(𝓁),w(r)) if p is an internal position, associated
    with a horizontal cut, with left child 𝓁 and right child r w(𝓁)+ w(r) if p is an
    internal position, associated with a vertical cut, with left child 𝓁 and right child
    r h(p)= ⎧ ⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨ ⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎩ h if p is a leaf node whose basic
    rectanglehas minimum height h h(𝓁)+ h(r) if p is an internal position, associated
    with a horizontal cut, with left child 𝓁 and right child r max(h(𝓁),h(r)) if p is an
    internal position, associated with a vertical cut, with left child 𝓁 and right child
    r Design a data structure for slicing ﬂoor plans that supports the operations: •
    Create a ﬂoor plan consisting of a single basic rectangle. • Decompose a basic
    rectangle by means of a horizontal cut. • Decompose a basic rectangle by means of a
    vertical cut. • Assign minimum height and width to a basic rectangle. • Draw the
    slicing tree associated with the ﬂoor plan. • Compact and draw the ﬂoor plan.

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
