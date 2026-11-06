"""
W-1.7.5 | Chapter 1: Python Primer
Type: Real-world · ★★★ Challenge
Section: 1.7 Exception Handling · book pp.33–38    ->  python tools/show.py W-1.7.5
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Title: MRT-3 ticket machine
Practices: several exception types · your own raise · re-raise
Source: https://claude.ai/artifact/SDiTepd5Sp8BBrktSDb1PQ

Problem:
    Show a numbered list of stations. Ask for the origin and destination
    numbers and print the fare: ₱13 base plus ₱1 per station traveled, capped
    at ₱28.

        stations = ["North Ave", "Quezon Ave", "GMA Kamuning", "Cubao",
                    "Santolan", "Ortigas", "Shaw", "Boni", "Guadalupe",
                    "Buendia", "Ayala", "Magallanes", "Taft"]

    - A non-number gives "Enter a station number." (ValueError from int).
    - A number outside the list gives "No such station." Catch the IndexError
      rather than checking the range first.
    - The same origin and destination should
      raise ValueError("Origin and destination are the same") from your own
      code and be caught by the same handler as other bad values.
    - On Ctrl-D (EOFError), print "Machine shutting down." and re-raise with a
      bare raise.

Example:
    From: 4   (Cubao)
    To:   11  (Ayala)
    7 stations · Fare ₱20

Hint:
    stations[-1] doesn't raise an error. It quietly gives you "Taft". Decide
    whether negative numbers should be allowed, and raise your own IndexError if
    not. This is the "look before you leap" vs "ask forgiveness" choice from
    page 36.

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
