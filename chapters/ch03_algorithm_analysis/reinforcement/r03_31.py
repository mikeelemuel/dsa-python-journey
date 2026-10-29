"""
R-3.31 | Chapter 3: Algorithm Analysis
Type: Reinforcement
Page: book p.142 (PDF p.164)    ->  python tools/show.py R-3.31
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Problem:
    Given an n-element sequence S of integers, Algorithm C executes an O(n)-time
    computation for each even number in S,a n da n O(logn)-time computation for each odd
    number in S. What are the best-case and worst- case running times of Algorithm C? 1
    def example1(S): 2 ”””Return the sum of the elements in sequence S.””” 3 n=l e n ( S
    ) 4 total = 0 5 for j in range(n): #l o o pf r o m0t on - 1 6 total += S[j] 7 return
    total 8 9 def example2(S): 10 ”””Return the sum of the elements with even index in
    sequence S.””” 11 n=l e n ( S ) 12 total = 0 13 for j in range(0, n, 2): # note the
    increment of 2 14 total += S[j] 15 return total 16 17 def example3(S): 18 ”””Return
    the sum of the preﬁx sums of sequence S.””” 19 n=l e n ( S ) 20 total = 0 21 for j
    in range(n): #l o o pf r o m0t on - 1 22 for k in range(1+j): #l o o pf r o m0t oj
    23 total += S[k] 24 return total 25 26 def example4(S): 27 ”””Return the sum of the
    preﬁx sums of sequence S.””” 28 n=l e n ( S ) 29 preﬁx = 0 30 total = 0 31 for j in
    range(n): 32 preﬁx += S[j] 33 total += preﬁx 34 return total 35 36 def example5(A,
    B): # assume that A and B have equal length 37 ”””Return the number of elements in B
    equal to the sum of preﬁx sums in A.””” 38 n=l e n ( A ) 39 count = 0 40 fo r i in
    range(n): #l o o pf r o m0t on - 1 41 total = 0 42 for j in range(n): #l o o pf r o
    m0t on - 1 43 for k in range(1+j): #l o o pf r o m0t oj 44 total += A[k] 45 if B[i]
    == total: 46 count += 1 47 return count Code Fragment 3.10: Some sample algorithms
    for analysis.

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
