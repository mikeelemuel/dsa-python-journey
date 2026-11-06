"""
W-1.9.2 | Chapter 1: Python Primer
Type: Real-world · ★★ Building up
Section: 1.9 Additional Python Conveniences · book pp.42–45    ->  python tools/show.py W-1.9.2
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Title: Carinderia menu queries
Practices: list, set, dict, and generator comprehensions
Source: https://claude.ai/artifact/KAfywZC2CWVic2CF1hPfXq

Problem:
    Answer each with ONE comprehension:
    - A list of dish names under ₱60
    - A set of all categories
    - A dict of name -> price with 12% VAT, rounded to 2 decimals
    - The total cost of one of everything, using a generator expression inside
      sum() (no square brackets)

        menu = [("adobo", 90, "ulam"), ("sinigang", 110, "ulam"),
                ("rice", 15, "kanin"), ("halo-halo", 75, "dessert"),
                ("leche flan", 50, "dessert"), ("garlic rice", 25, "kanin")]

Example:
    ['rice', 'leche flan', 'garlic rice']
    {'ulam', 'kanin', 'dessert'}
    {'adobo': 100.8, 'sinigang': 123.2, ...}
    365

Hint:
    You can unpack each tuple right in the comprehension:
    [name for name, price, cat in menu if price < 60]. Page 43 compares all four
    bracket styles side by side.

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
