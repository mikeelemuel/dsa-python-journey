"""
C-12.54 | Chapter 12: Sorting and Selection
Type: Creativity
Page: book p.579 (PDF p.601)    ->  python tools/show.py C-12.54
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Problem:
    Show that randomized quick-sort runs in O(nlog n) time with probability at least
    1−1/n, that is, withhigh probability, by answering the following: a. For each input
    element x,d e ﬁ n eCi, j(x) t ob ea0 /1 random variable that is 1 if and only if
    element x is in j + 1 subproblems that belong to size group i. Argue why we need not
    deﬁne Ci, j for j > n. b. Let Xi, j b ea0 /1 random variable that is 1 with
    probability 1 /2 j, independent of any other events, and let L = ⌈log4/3 n⌉. Argue
    why ∑L−1i=0 ∑nj=0 Ci, j(x) ≤ ∑L−1i=0 ∑nj=0 Xi, j. c. Show that the expected value of
    ∑L−1i=0 ∑nj=0 Xi, j is (2 − 1/2n)L. d. Show that the probability that ∑Li=0 ∑nj=0
    Xi, j > 4L is at most 1 /n2, using the Chernoff bound that states that if X is the
    sum of a ﬁnite number of independent 0/1 random variables with expected value μ > 0,
    then Pr(X > 2μ) < (4/e)−μ,w h e r ee = 2.71828128... . e. Argue why the previous
    claim proves randomized quick-sort runs in O(nlog n) time with probability at least
    1 − 1/n.

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
