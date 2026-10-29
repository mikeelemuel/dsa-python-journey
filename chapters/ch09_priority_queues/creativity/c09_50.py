"""
C-9.50 | Chapter 9: Priority Queues
Type: Creativity
Page: book p.399 (PDF p.421)    ->  python tools/show.py C-9.50
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Problem:
    An online computer system for trading stocks needs to process orders of the form
    “buy 100 shares at $ x each” or “sell 100 shares at $ y each.” A buy order for $ x
    can only be processed if there is an existing sell order with price $ y such that y
    ≤ x. Likewise, a sell order for $ y can only be processed if there is an existing
    buy order with price $ x such that y ≤ x. If a buy or sell order is entered but
    cannot be processed, it must wait for a future order that allows it to be processed.
    Describe a scheme that allows buy and sell orders to be entered inO(logn) time,
    independent of whether or not they can be immediately processed.

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
