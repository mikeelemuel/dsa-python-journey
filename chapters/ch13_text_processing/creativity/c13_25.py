"""
C-13.25 | Chapter 13: Text Processing
Type: Creativity
Page: book p.614 (PDF p.636)    ->  python tools/show.py C-13.25
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Problem:
    The Knuth-Morris-Pratt pattern-matching algorithm can be modiﬁed to run faster on
    binary strings by redeﬁning the failure function as: f (k)= the largest j < k such
    that P[0: j] ˆp j is a sufﬁx of P[1: k + 1], where ˆp j denotes the complement of
    the jth bit of P. Describe how to modify the KMP algorithm to be able to take
    advantage of this new failure function and also give a method for computing this
    failure function. Show that this method makes at most n comparisons between the text
    and the pattern (as opposed to the 2 n comparisons needed by the standard KMP
    algorithm given in Section 13.2.3).

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
