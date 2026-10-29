"""
P-8.68 | Chapter 8: Trees
Type: Project
Page: book p.361 (PDF p.383)    ->  python tools/show.py P-8.68
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Problem:
    Write a program that can play Tic-Tac-Toe effectively. (See Section 5.6.) To do
    this, you will need to create a game tree T , which is a tree where each position
    corresponds to a game conﬁguration, which, in this case, is a representation of the
    Tic-Tac-Toe board. (See Section 8.4.2.) The root corresponds to the initial
    conﬁguration. For each internal position p in T , the children of p correspond to
    the game states we can reach from p’s game state in a single legal move for the
    appropriate player, A (the ﬁrst player) or B (the second player). Positions at even
    depths correspond to moves for A and positions at odd depths correspond to moves for
    B. Leaves are either ﬁnal game states or are at a depth beyond which we do not want
    to explore. We score each leaf with a value that indicates how good this state is
    for player A. In large games, like chess, we have to use a heuristic scoring
    function, but for small games, like Tic-Tac-Toe, we can construct the entire game
    tree and score leaves as +1, 0, −1, indicating whether player A has a win, draw, or
    lose in that conﬁguration. A good algorithm for choosing moves is minimax. In this
    algorithm, we assign a score to each internal position p in T , such that if p
    represents A’s turn, we compute p’s score as the maximum of the scores of p’s
    children (which corresponds to A’s optimal play from p). If an internal node p
    represents B’s turn, then we compute p’s score as the minimum of the scores of p’s
    children (which corresponds to B’s optimal play from p).

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
