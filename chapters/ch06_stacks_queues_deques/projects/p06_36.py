"""
P-6.36 | Chapter 6: Stacks, Queues, and Deques
Type: Project
Page: book p.254 (PDF p.276)    ->  python tools/show.py P-6.36
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Problem:
    When a share of common stock of some company is sold, the capital gain (or,
    sometimes, loss) is the difference between the share’s selling price and the price
    originally paid to buy it. This rule is easy to under- stand for a single share, but
    if we sell multiple shares of stock bought over a long period of time, then we must
    identify the shares actually be- ing sold. A standard accounting principle for
    identifying which shares of a stock were sold in such a case is to use a FIFO
    protocol—the shares sold are the ones that have been held the longest (indeed, this
    is the de- fault method built into several personal ﬁnance software packages). For
    example, suppose we buy 100 shares at $20 each on day 1, 20 shares at $24 on day 2,
    200 shares at $36 on day 3, and then sell 150 shares on day 4 at $30 each. Then
    applying the FIFO protocol means that of the 150 shares sold, 100 were bought on day
    1, 20 were bought on day 2, and 30 were bought on day 3. The capital gain in this
    case would therefore be 100 · 10 + 20 · 6 + 30 · (−6), or $940. Write a program that
    takes as input a sequence of transactions of the form “buy x share(s) at y each” or
    “sell x share(s) at y each,” assuming that the transactions oc- cur on consecutive
    days and the values x and y are integers. Given this input sequence, the output
    should be the total capital gain (or loss) for the entire sequence, using the FIFO
    protocol to identify shares.

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
