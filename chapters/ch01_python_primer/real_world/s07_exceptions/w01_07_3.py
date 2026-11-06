"""
W-1.7.3 | Chapter 1: Python Primer
Type: Real-world · ★★ Building up
Section: 1.7 Exception Handling · book pp.33–38    ->  python tools/show.py W-1.7.3
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Title: ATM withdrawal guard
Practices: raise · isinstance · type check before value check
Source: https://claude.ai/artifact/SDiTepd5Sp8BBrktSDb1PQ

Problem:
    Write withdraw(balance, amount) that returns the new balance. Before doing
    any math it should:
    - raise TypeError("amount must be a number") if amount isn't an int or float
    - raise ValueError if the amount is not positive, isn't a multiple of 100
      (ATMs only give ₱100 bills and up), or is more than the balance
    Then call it with each test below inside try/except and print the message.

Example:
    withdraw(5000, 2000)    -> 3000
    withdraw(5000, "2000")  -> TypeError: amount must be a number
    withdraw(5000, 250)     -> ValueError: must be a multiple of 100
    withdraw(5000, 9000)    -> ValueError: insufficient balance
    withdraw(5000, -100)    -> ValueError: amount must be positive

Hint:
    Follow the book's sqrt example on page 34: check the type first, then the
    value. Why does that order matter? Try "2000" % 100 and see what happens.

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
