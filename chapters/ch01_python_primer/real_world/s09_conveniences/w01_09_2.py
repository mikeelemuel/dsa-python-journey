"""
W-1.9.2 | Chapter 1: Python Primer
Type: Real-world · ★★ Building up
Section: 1.9 Additional Python Conveniences · book pp.42–45    ->  python tools/show.py W-1.9.2
Status: done            # todo | in-progress | done | skipped
Date: 2026-11-12
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
    Write each query as a for loop first, then fold it into one comprehension.
    Unpack each tuple in the loop header: for dish, price, category in menu.
      list -> [ ... ]   set -> { x ... }   dict -> { k: v ... }   generator -> sum( ... )

    Time:  O(n) each - one pass over the menu.
    Space: O(k) for the list/set/dict results; O(1) for the sum (generator).

Notes:
    (gotchas, what you learned)
    - The comprehension replaces the empty container + append/add/[key]=.
    - "Under ₱60" means price < 60, not <= 60.
    - A set prints in any order, so it may not match the example's order.
    - Check the loop and comprehension print the same thing: the first dict loop
      forgot the VAT and printed plain prices.
    - Reusing `categories` for the VAT dict works but hides the set; a name like
      vat_prices would read better.
"""


# your solution here


if __name__ == "__main__":
    menu = [("adobo", 90, "ulam"), ("sinigang", 110, "ulam"),
            ("rice", 15, "kanin"), ("halo-halo", 75, "dessert"),
            ("leche flan", 50, "dessert"), ("garlic rice", 25, "kanin")]

    # - A list of dish names under ₱60

    cheap_dishes = []
    for dish, price, category in menu:
        if price < 60:
            cheap_dishes.append(dish)

    print(cheap_dishes)
    print([dish for dish, price, category in menu if price < 60])

    # - A set of all categories

    categories = set()
    for dish, price, category in menu:
        categories.add(category)

    print(categories)
    print({category for dish, price, category in menu})

    # - A dict of name -> price with 12% VAT, rounded to 2 decimals

    categories = {}
    for dish, price, category in menu:
        categories[dish] = round(price * 1.12, 2)

    print(categories)
    print({dish: round(price * 1.12, 2) for dish, price, category in menu})

    # - The total cost of one of everything, using a generator expression inside sum() (no square brackets)
    total_cost = 0
    for dish, price, category in menu:
        total_cost += price

    print(total_cost)
    print(sum(price for dish, price, category in menu))