"""
C-12.33 | Chapter 12: Sorting and Selection
Type: Creativity
Page: book p.577 (PDF p.599)    ->  python tools/show.py C-12.33
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Problem:
    Our high-level description of quick-sort describes partitioning the ele- ments into
    three sets L, E,a n d G, having keys less than, equal to, or greater than the pivot,
    respectively. However, our in-place quick-sort im- plementation of Code Fragment
    12.6 does not gather all elements equal to the pivot into a set E. An alternative
    strategy for an in-place, three- way partition is as follows. Loop through the
    elements from left to right maintaining indices i, j,a n dk and the invariant that
    all elements of slice S[0:i] are strictly less than the pivot, all elements of slice
    S[i:j] are equal to the pivot, and all elements of slice S[j:k] are strictly greater
    than the pivot; elements of S[k:n] are yet unclassiﬁed. In each pass of the loop,
    classify one additional element, performing a constant number of swaps as needed.
    Implement an in-place quick-sort using this strategy.

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
