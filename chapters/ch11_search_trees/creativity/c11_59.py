"""
C-11.59 | Chapter 11: Search Trees
Type: Creativity
Page: book p.533 (PDF p.555)    ->  python tools/show.py C-11.59
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Problem:
    As a positional structure, our TreeMap implementation has a subtle ﬂaw. A position
    instance p associated with an key-value pair (k, v) should re- main valid as long as
    that item remains in the map. In particular, that position should be unaffected by
    calls to insert or delete other items in the collection. Our algorithm for deleting
    an item from a binary search tree may fail to provide such a guarantee, in
    particular because of our rule for using the inorder predecessor of a key as a
    replacement when deleting a key that is located in a node with two children. Given
    an explicit series of Python commands that demonstrates such a ﬂaw.

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
