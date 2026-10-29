"""
C-10.31 | Chapter 10: Maps, Hash Tables, and Skip Lists
Type: Creativity
Page: book p.454 (PDF p.476)    ->  python tools/show.py C-10.31
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Problem:
    For an ideal compression function, the capacity of the bucket array for a hash table
    should be a prime number. Therefore, we consider the problem of locating a prime
    number in a range [M,2M]. Implement a method for ﬁnding such a prime by using the
    sieve algorithm. In this algorithm, we allocate a 2M cell Boolean array A, such that
    cell i is associated with the integer i. We then initialize the array cells to all
    be “true” and we “mark off” all the cells that are multiples of 2, 3, 5, 7, and so
    on. This process can stop after it reaches a number larger than √ 2M. (Hint:
    Consider a bootstrapping method for ﬁnding the primes up to √ 2M.)

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
