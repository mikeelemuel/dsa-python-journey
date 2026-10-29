"""
C-9.33 | Chapter 9: Priority Queues
Type: Creativity
Page: book p.397 (PDF p.419)    ->  python tools/show.py C-9.33
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Problem:
    When using a linked-tree representation for a heap, an alternative method for ﬁnding
    the last node during an insertion in a heap T is to store, in the last node and each
    leaf node of T , a reference to the leaf node immedi- ately to its right (wrapping
    to the ﬁrst node in the next lower level for the rightmost leaf node). Show how to
    maintain such references in O(1) time per operation of the priority queue ADT
    assuming that T is implemented with a linked structure. (11,S) (2,B) (5,A) (4,C)
    (6,Z)(9,F)(15,K) (25,J) (12,H)(14,E)(16,X) (7,Q) (8,W) (10,L)(20,B) z w (5,A) (6,Z)
    (20,B)(9,F)(15,K) (25,J) (14,E)(16,X) (7,Q) (12,H) (4,C) wz (a) (b) Figure 9.12:
    Updating the last node in a complete binary tree after operationadd or remove. Node
    w is the last node before operation add or after operation remove. Node z is the
    last node after operation add or before operation remove.

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
