"""
W-1.9.1 | Chapter 1: Python Primer
Type: Real-world · ★ Warm-up
Section: 1.9 Additional Python Conveniences · book pp.42–45    ->  python tools/show.py W-1.9.1
Status: done            # todo | in-progress | done | skipped
Date: 2026-11-12
Time:

Title: One-liner fares
Practices: conditional expressions
Source: https://claude.ai/artifact/KAfywZC2CWVic2CF1hPfXq

Problem:
    Rewrite each block as a single line using `expr1 if condition else expr2`.
    Test each with two inputs that take different branches.

        # a
        if age >= 60:
            fare = base * 0.8
        else:
            fare = base

        # b
        if items == 1:
            label = "item"
        else:
            label = "items"
        print(items, label)

        # c
        if score >= 75:
            print("PASSED")
        else:
            print("FAILED")

Example:
    a) fare = ...
    b) print(...)
    c) print(...)

Hint:
    For (c), put the conditional expression inside print(...), like the
    foo(n if n >= 0 else -n) example on page 42.

Approach:
    (idea, then time/space complexity)
    Use a conditional expression: value_if_true if condition else value_if_false.
    Each block collapses to one line; test each with one input per branch.

    Time:  O(1) per line.  Space: O(1).

Notes:
    (gotchas, what you learned)
    - It picks between two VALUES; an assignment can't go inside it.
      Wrong: fare = base * 0.8 if age >= 60 else fare = base  (SyntaxError)
      Right: fare = base * 0.8 if age >= 60 else base
    - It is a conditional expression, not a comprehension. A comprehension
      builds a collection from a loop: [i*i for i in range(5)].
    - It can sit inside a call: print("PASSED" if score >= 75 else "FAILED").
"""

# your solution here
if __name__ == "__main__":
    base = 100
    for age in (65, 30):
        fare = base * 0.8 if age >= 60 else base
        print(age, fare)                                # 65 80.0 / 30 100

    for items in (1, 3):
        print(items, "item" if items == 1 else "items") # 1 item / 3 items

    for score in (80, 60):
        print("PASSED" if score >= 75 else "FAILED")    # PASSED / FAILED
