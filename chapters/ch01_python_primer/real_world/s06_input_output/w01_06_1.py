"""
W-1.6.1 | Chapter 1: Python Primer
Type: Real-world · ★ Warm-up
Section: 1.6 Simple Input and Output · book pp.30–32    ->  python tools/show.py W-1.6.1
Status: done                   # todo | in-progress | done | skipped
Date: 2026-11-07
Time:

Title: Sari-sari store receipt line
Practices: input · float() · print(sep=, end=)
Source: https://claude.ai/artifact/R4zdNBmahtUo7GwysUZkKz

Problem:
    Ask for an item name, its price, and the quantity. Print one receipt line
    using sep to put " | " between the fields. Then use end="" on a second print
    so "Salamat po!" appears on the same line as the total.

Example:
    Item: Lucky Me Pancit Canton
    Price: 16.50
    Qty: 3
    Lucky Me Pancit Canton | 3 | ₱49.50
    TOTAL ₱49.50 — Salamat po!

Hint:
    input() always gives you a string. Wrap it: float(input("Price: ")).
    To keep two decimals, use f"{total:.2f}".

Approach:
    (idea, then time/space complexity)
    Read item (str), price (float) and qty (int) with input().
    Compute total = price * qty.
    Print item, qty and total with sep=" | " for the receipt line.
    Print the total with end=" — " so the next print continues on the same line.
    Time: O(1). Space: O(1), a fixed number of variables.


Notes:
    (gotchas, what you learned)
    - sep goes BETWEEN values; it does nothing with a single value.
    - end goes AFTER the print (default is "\n"). Put it on the print whose
      line you want to continue, not the next one.
    - {x:.2f}, not {x: .2f}; the space adds a leading space.
    - Call the function under if __name__ == "__main__": or nothing runs.
"""


# your solution here
def print_receipt():
    item = input('Item: ')
    price = float(input('Price: '))
    qty = int(input('Qty: '))

    total = price * qty

    print(item, qty, f"₱{total:.2f}", sep=" | ")
    print(f"TOTAL ₱{total:.2f}", end=" — ")
    print("Salamat po!")


if __name__ == "__main__":
    print_receipt()
