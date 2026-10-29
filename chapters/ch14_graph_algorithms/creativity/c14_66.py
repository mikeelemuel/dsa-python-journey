"""
C-14.66 | Chapter 14: Graph Algorithms
Type: Creativity
Page: book p.693 (PDF p.715)    ->  python tools/show.py C-14.66
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Problem:
    An old MST method, called Bar˚uvka’s algorithm, works as follows on a graph G having
    n vertices and m edges with distinct weights: Let T be a subgraph of G initially
    containing just the vertices in V . while T has fewer than n − 1 edges do for each
    connected component Ci of T do Find the lowest-weight edge (u, v) in E with u in Ci
    and v not in Ci. Add (u, v) to T (unless it is already in T ). return T Prove that
    this algorithm is correct and that it runs in O(mlog n) time.

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
