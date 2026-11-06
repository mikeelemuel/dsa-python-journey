"""
W-1.8.2 | Chapter 1: Python Primer
Type: Real-world · ★★ Building up
Section: 1.8 Iterators and Generators · book pp.39–41    ->  python tools/show.py W-1.8.2
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Title: Bank queue numbers
Practices: infinite generator · independent state
Source: https://claude.ai/artifact/BhyrFMkLeHaB9j9CNLUn6e

Problem:
    Write a generator queue_numbers(prefix) that yields "A-001", "A-002", and
    so on forever. Make two counters, one for the regular window "A" and one for
    seniors and PWDs "P". Hand out tickets in this order of arrivals:

        arrivals = ["regular", "senior", "regular", "regular", "senior"]

Example:
    regular -> A-001
    senior  -> P-001
    regular -> A-002
    regular -> A-003
    senior  -> P-002

Hint:
    Use while True: and yield f"{prefix}-{n:03}". Each call to
    queue_numbers(...) creates a separate generator with its own n. That's why
    the two windows don't mix up their numbers.

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
