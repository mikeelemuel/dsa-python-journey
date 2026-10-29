"""
P-11.70 | Chapter 11: Search Trees
Type: Project
Page: book p.534 (PDF p.556)    ->  python tools/show.py P-11.70
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Problem:
    Write a program that performs a simple n-body simulation, called “Jump- ing
    Leprechauns.” This simulation involves n leprechauns, numbered 1 to n. It maintains
    a gold value gi for each leprechaun i, which begins with each leprechaun starting
    out with a million dollars worth of gold, that is, gi = 1000000 for each i =
    1,2,..., n. In addition, the simulation also maintains, for each leprechaun, i, a
    place on the horizon, which is repre- sented as a double-precision ﬂoating-point
    number, xi. In each iteration of the simulation, the simulation processes the
    leprechauns in order. Pro- cessing a leprechaun i during this iteration begins by
    computing a new place on the horizon for i, which is determined by the assignment xi
    = xi + rgi, where r is a random ﬂoating-point number between −1 and 1. The lep-
    rechaun i then steals half the gold from the nearest leprechauns on either side of
    him and adds this gold to his gold value, gi. Write a program that can perform a
    series of iterations in this simulation for a given number, n, of leprechauns. You
    must maintain the set of horizon positions using a sorted map data structure
    described in this chapter.

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
