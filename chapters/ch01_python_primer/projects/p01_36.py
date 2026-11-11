"""
P-1.36 | Chapter 1: Python Primer
Type: Project
Page: book p.54 (PDF p.76)    ->  python tools/show.py P-1.36
Status: done            # todo | in-progress | done | skipped
Date: 2026-11-12
Time:

Problem:
    Write a Python program that inputs a list of words, separated by white- space, and
    outputs how many times each word appears in the list. You need not worry about
    efﬁciency at this point, however, as this topic is something that will be addressed
    later in this book.

Approach:
    (idea, then time/space complexity)
    Read a line with input() and split() it on whitespace into a list of words.
    Build a dict comprehension word -> words.count(word); a repeated word just
    rewrites its own entry with the same count, so each word appears once.
    Print each word and its count.

    Time:  O(n^2) - words.count() scans the whole list once per word.
    Space: O(k) for the dict, k = number of distinct words.

Notes:
    (gotchas, what you learned)
    - First try: sum([k+1 for k in words if k in words]) crashed with
      TypeError, because k is a str and "the" + 1 is not allowed.
    - One count per word needs a dict, not a single sum.
    - `if k in words` is always true when k comes from words; it filters nothing.
    - split() with no argument splits on any run of spaces/tabs/newlines.
    - Counting is case-sensitive: "The" and "the" are different words.
    - O(n) version: one loop that adds 1 to counts[word]; hash tables come later.
"""


# your solution here
def list_of_words(words):
    return {w: words.count(w) for w in words}


if __name__ == "__main__":
    words = input("Words: ").split()
    for word, n in list_of_words(words).items():
        print(word, n)
