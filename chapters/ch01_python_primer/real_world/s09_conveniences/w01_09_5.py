"""
W-1.9.5 | Chapter 1: Python Primer
Type: Real-world · ★★★ Challenge
Section: 1.9 Additional Python Conveniences · book pp.42–45    ->  python tools/show.py W-1.9.5
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Title: Barangay election tally
Practices: dict and set comprehensions · unpacking items() · ties
Source: https://claude.ai/artifact/KAfywZC2CWVic2CF1hPfXq

Problem:
    Each vote is a candidate's name. Using comprehensions wherever they fit:
    - Build candidates as a set comprehension, then tally as a dict
      comprehension of name -> vote count.
    - Print the results from highest to lowest, unpacking each (name, count)
      pair in a for loop.
    - Find the top vote count, then make a list of everyone who has it. Print
      "Winner: X" or "Tie between: X, Y, Z" using a conditional expression.
    - Bonus: turn the precinct grid into per-candidate totals using zip(*grid)
      and unpacking.

        votes = ["Reyes", "Santos", "Reyes", "Cruz", "Santos",
                 "Reyes", "Cruz", "Santos", "Bautista", "Cruz"]

        # rows = precincts, columns = Reyes, Santos, Cruz
        grid = [(120, 98, 110), (87, 101, 95), (140, 133, 120)]

Example:
    Tie between: Cruz, Reyes, Santos
    Bonus: Reyes 347 · Santos 332 · Cruz 325

Hint:
    votes.count(name) works inside a dict comprehension. It's slow for a
    million votes, and Chapter 10 shows a better way. To sort by count, use
    sorted(tally.items(), key=lambda pair: pair[1], reverse=True). The key= idea
    comes from page 28.

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
