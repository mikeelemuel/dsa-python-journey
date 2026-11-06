"""
W-1.7.2 | Chapter 1: Python Primer
Type: Real-world · ★★ Building up
Section: 1.7 Exception Handling · book pp.33–38    ->  python tools/show.py W-1.7.2
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Title: Name that error
Practices: common exception types · except … as e
Source: https://claude.ai/artifact/SDiTepd5Sp8BBrktSDb1PQ

Problem:
    Before running anything, write down which exception each line raises.
    Then put each line in its own try block, catch it with
    `except Exception as e`, and print type(e).__name__ and e to check your
    guesses. For each one, write one sentence on how you'd fix the code so the
    error can't happen.

        load = {"GoSURF50": 50, "GIGA99": 99}
        fares = [13, 15, 18]

        load["UNLI20"]           # a
        fares[3]                 # b
        int("₱13")               # c
        "Fare: " + 13            # d
        1000 / len([])           # e
        fares.pop().upper()      # f
        print(total_fare)        # g

Example:
    a) my guess: ...   actual: ...
    b) my guess: ...   actual: ...

Hint:
    Table 1.6 on page 33 lists every type you need. Two of these are
    TypeError-like but only one actually is. Check what fares.pop() gives back
    before .upper() runs on it.

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
