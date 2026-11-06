"""
W-1.8.3 | Chapter 1: Python Primer
Type: Real-world · ★★ Building up
Section: 1.8 Iterators and Generators · book pp.39–41    ->  python tools/show.py W-1.8.3
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Title: Lazy vs. eager
Practices: return a list vs. yield · memory · early stop
Source: https://claude.ai/artifact/BhyrFMkLeHaB9j9CNLUn6e

Problem:
    Write two versions of a function that produces the multiples of 7 up to n:
    multiples_list(n) returns a list, and multiples_gen(n) yields one at a time.
    Add print("computing", k) inside each loop so you can see the work being
    done.
    - Loop over each version with n = 50 but break after the first 3 values.
      Count how many "computing" lines each one prints.
    - Compare sys.getsizeof(list(range(10_000_000))) with
      sys.getsizeof(range(10_000_000)).
    - Make d = {"adobo": 90, "sinigang": 110} and v = d.values(), add a dish to
      d, then print list(v). Explain what you see.

Example:
    multiples_list: computing ... (how many lines?)
    multiples_gen:  computing ... (how many lines?)

Hint:
    The list version computes everything before you get the first value. The
    generator pauses at each yield until you ask for more. Page 40 explains why
    dict views behave the way they do.

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
