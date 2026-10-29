"""
C-11.34 | Chapter 11: Search Trees
Type: Creativity
Page: book p.530 (PDF p.552)    ->  python tools/show.py C-11.34
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Problem:
    In Section 11.1.2 we claim that the ﬁnd range method of a binary search tree
    executes in O(s + h) time where s is the number of items found within the range and
    h is the height of the tree. Our implementation, in Code Fragment 11.6 begins by
    searching for the starting key, and then repeat- edly calling theafter method until
    reaching the end of the range. Each call to after is guaranteed to run in O(h) time.
    This suggests a weaker O(sh) bound for ﬁnd range, since it involves O(s) calls to
    after. Prove that this implementation achieves the stronger O(s + h) bound.

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
