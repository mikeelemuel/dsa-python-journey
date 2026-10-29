"""
C-10.36 | Chapter 10: Maps, Hash Tables, and Skip Lists
Type: Creativity
Page: book p.455 (PDF p.477)    ->  python tools/show.py C-10.36
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Problem:
    The quadratic probing strategy has a clustering problem related to the way it looks
    for open slots. Namely, when a collision occurs at bucket h(k),i t checks buckets
    A[(h(k)+ i2) mod N],f o ri = 1,2,..., N − 1. a. Show that i2 mod N will assume at
    most (N + 1)/2 distinct values, for N prime, as i ranges from 1 to N − 1. As a part
    of this justiﬁca- tion, note that i2 mod N =( N − i)2 mod N for all i. b. A better
    strategy is to choose a prime N such that N mod 4 = 3a n d then to check the buckets
    A[(h(k) ± i2) mod N] as i ranges from 1 to (N − 1)/2, alternating between plus and
    minus. Show that this alternate version is guaranteed to check every bucket in A.

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
