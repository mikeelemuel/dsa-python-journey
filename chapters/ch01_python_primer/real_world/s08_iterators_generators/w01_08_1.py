"""
W-1.8.1 | Chapter 1: Python Primer
Type: Real-world · ★ Warm-up
Section: 1.8 Iterators and Generators · book pp.39–41    ->  python tools/show.py W-1.8.1
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Title: A for loop without for
Practices: iter · next · StopIteration
Source: https://claude.ai/artifact/BhyrFMkLeHaB9j9CNLUn6e

Problem:
    Print every stop on a jeepney route WITHOUT using a for loop. Create an
    iterator with iter(), call next() inside while True, and stop when
    StopIteration is raised. Print "Para po!" at the end.

        stops = ["Philcoa", "UP Diliman", "Katipunan", "Cubao"]

    Then try next(stops) directly on the list. Read the error and explain in
    one sentence why it fails.

Example:
    Next stop: Philcoa
    Next stop: UP Diliman
    Next stop: Katipunan
    Next stop: Cubao
    Para po!

Hint:
    Page 39: a list is iterable but not an iterator. iter(stops) gives you the
    object that remembers where you are.

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
