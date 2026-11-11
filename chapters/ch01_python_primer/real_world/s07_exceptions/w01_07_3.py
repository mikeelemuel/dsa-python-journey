"""
W-1.7.3 | Chapter 1: Python Primer
Type: Real-world · ★★ Building up
Section: 1.7 Exception Handling · book pp.33–38    ->  python tools/show.py W-1.7.3
Status: done            # todo | in-progress | done | skipped
Date: 2026-11-12
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
    define a function that has a signature of withdraw that has a formal parameters of balance and amount both can be float
    Raise a TypeError if the amount or balance is not a numeric
    Raise a ValueError if the balance or amount is not a positive or a multiple of 100
    Raise a ValueError if insufficient balance
    Use try catch

    Time:  O(1).  Space: O(1).

Notes:
    (gotchas, what you learned)
    - withdraw RAISES; the caller CATCHES. My first try put try/except inside
      withdraw and never raised, so withdraw(2000, 3000) printed -1000.
    - balance - amount never raises ValueError on its own; I have to raise it.
    - Check the type first: "2000" % 100 raises a confusing TypeError
      ("not all arguments converted during string formatting").
    - Return the new balance; let the caller decide what to print.
    - except (TypeError, ValueError) as e + type(e).__name__ prints
      "ValueError: insufficient balance" like the example.
"""


# your solution here
def withdraw(balance, amount):
    if not isinstance(amount, (int, float)):
        raise TypeError("amount must be a number")
    if amount <= 0:
        raise ValueError("amount must be positive")
    if amount % 100 != 0:
        raise ValueError("must be a multiple of 100")
    if amount > balance:
        raise ValueError("insufficient balance")
    return balance - amount


if __name__ == "__main__":
    for amount in (2000, "2000", 250, 9000, -100):
        try:
            print(withdraw(5000, amount))
        except (TypeError, ValueError) as e:
            print(f"{type(e).__name__}: {e}")