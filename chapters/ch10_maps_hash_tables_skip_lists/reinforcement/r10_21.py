"""
R-10.21 | Chapter 10: Maps, Hash Tables, and Skip Lists
Type: Reinforcement
Page: book p.453 (PDF p.475)    ->  python tools/show.py R-10.21
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Problem:
    Consider the following variant of the ﬁnd index method from Code Frag- ment 10.8, in
    the context of the SortedTableMap class: def ﬁnd index(self,k ,l o w ,h i g h ) : if
    high < low: return high + 1 else: mid = (low + high) // 2 if self. table[mid]. key <
    k: return self. ﬁnd index(k, mid + 1, high) else: return self. ﬁnd index(k, low, mid
    − 1) Does this always produce the same result as the original version? Justify your
    answer.

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
