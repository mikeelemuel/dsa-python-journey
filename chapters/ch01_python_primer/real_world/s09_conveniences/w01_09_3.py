"""
W-1.9.3 | Chapter 1: Python Primer
Type: Real-world · ★★ Building up
Section: 1.9 Additional Python Conveniences · book pp.42–45    ->  python tools/show.py W-1.9.3
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Title: Bus trip unpacker
Practices: divmod · returning a tuple · simultaneous assignment
Source: https://claude.ai/artifact/KAfywZC2CWVic2CF1hPfXq

Problem:
    - A Cubao to Baguio bus trip takes 287 minutes. Use
      hours, minutes = divmod(287, 60) and print "4 h 47 min".
    - Write trip_stats(times) that returns the fastest, slowest, and average
      time AS ONE TUPLE. Call it as
      fast, slow, avg = trip_stats([287, 301, 265, 330]).
    - Loop through [("Victory", 287), ("Genesis", 265), ("Solid North", 301)]
      with `for line, mins in …` and print each line's time in h/min.
    - Swap the driver and conductor with driver, conductor = conductor, driver.
      Then rotate three seats a, b, c so each person moves one seat to the left,
      in one line.

Example:
    4 h 47 min
    fast=265 slow=330 avg=295.75
    Victory 4 h 47 min

Hint:
    return a, b, c automatically packs into a tuple (page 44). The right side
    of a simultaneous assignment is evaluated completely before anything on the
    left changes. That's why a swap needs no temporary variable.

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
