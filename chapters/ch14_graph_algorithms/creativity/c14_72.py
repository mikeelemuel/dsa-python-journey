"""
C-14.72 | Chapter 14: Graph Algorithms
Type: Creativity
Page: book p.694 (PDF p.716)    ->  python tools/show.py C-14.72
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Problem:
    Suppose we are given a directed graph ⃗G with n vertices, and let M be the n × n
    adjacency matrix corresponding to ⃗G. a. Let the product of M with itself (M2) be
    deﬁned, for 1 ≤ i, j ≤ n,a s follows: M2(i, j)= M(i,1) ⊙ M(1, j) ⊕···⊕ M(i, n) ⊙
    M(n, j), where “ ⊕” is the Boolean or operator and “ ⊙” is Boolean and. Given this
    deﬁnition, what does M2(i, j)= 1 imply about the ver- tices i and j?W h a ti fM2(i,
    j)= 0? b. Suppose M4 is the product of M2 with itself. What do the entries of M4
    signify? How about the entries of M5 =( M4)(M)? In general, what information is
    contained in the matrix M p? c. Now suppose that ⃗G is weighted and assume the
    following: 1: for 1 ≤ i ≤ n, M(i, i)= 0. 2: for 1 ≤ i, j ≤ n, M(i, j)= weight(i, j)
    if (i, j) is in E. 3: for 1 ≤ i, j ≤ n, M(i, j)= ∞ if (i, j) is not in E. Also, let
    M2 be deﬁned, for 1 ≤ i, j ≤ n, as follows: M2(i, j)= min{M(i,1)+ M(1, j),..., M(i,
    n)+ M(n, j)}. If M2(i, j)= k, what may we conclude about the relationship be- tween
    vertices i and j?

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
