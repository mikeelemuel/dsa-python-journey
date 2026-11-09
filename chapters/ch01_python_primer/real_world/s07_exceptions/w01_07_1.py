"""
W-1.7.1 | Chapter 1: Python Primer
Type: Real-world · ★ Warm-up
Section: 1.7 Exception Handling · book pp.33–38    ->  python tools/show.py W-1.7.1
Status: done                   # todo | in-progress | done | skipped
Date: 2026-11-09
Time:

Title: GCash top-up that won't crash
Practices: try / except ValueError · while loop
Source: https://claude.ai/artifact/SDiTepd5Sp8BBrktSDb1PQ

Problem:
    Ask for a top-up amount. Keep asking until the user gives a valid positive
    number. Typing letters should print "Numbers only, please." instead of
    crashing. Zero or a negative amount should print
    "Amount must be more than ₱0."

Example:
    Top-up amount: limang daan
    Numbers only, please.
    Top-up amount: -50
    Amount must be more than ₱0.
    Top-up amount: 500
    Topped up ₱500.00

Hint:
    This is the age example from page 37 in a different outfit. Start with an
    invalid value (amount = -1) so the while loop runs at least once.

Approach:
    (idea, then time/space complexity)
    Start with amount = -1 so the while loop runs at least once.
    While amount <= 0: try float(input(...)). If it raises ValueError, print
    "Numbers only, please.". If it converts but is <= 0, print
    "Amount must be more than ₱0.". The loop ends on the first positive
    number; then print it with :.2f.
    Time: O(k) for k attempts. Space: O(1).

Notes:
    (gotchas, what you learned)
    - Tested: "limang daan" -> Numbers only, -50 and 0 -> must be more than
      ₱0, 500 -> Topped up ₱500.00.
    - No isinstance() needed: input() always returns a str. float() either
      converts it or raises ValueError, and except catches that.
    - When float() fails, amount keeps its old value (-1), so the loop
      runs again by itself.
    - The sentinel start value (-1) is what makes a while loop act like
      "do at least once".
    - Gotcha: float("nan") and float("inf") are valid floats. "nan" slips
      through (nan <= 0 is False) and prints "Topped up ₱nan". Use
      math.isfinite(amount) to block it.
"""


# your solution here
def top_up():
    amount = -1

    while amount <= 0:
        try:
            amount = float(input("Top-up amount: "))
            if amount <= 0:
                print("Amount must be more than ₱0.")
        except ValueError:
            print("Numbers only, please.")

    print(f"Topped up ₱{amount:.2f}")


if __name__ == "__main__":
    top_up()
