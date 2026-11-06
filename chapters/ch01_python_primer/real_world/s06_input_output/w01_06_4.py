"""
W-1.6.4 | Chapter 1: Python Primer
Type: Real-world · ★★★ Challenge
Section: 1.6 Simple Input and Output · book pp.30–32    ->  python tools/show.py W-1.6.4
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Title: Bookmark reader
Practices: readline · tell · seek · 'r' and 'w' together
Source: https://claude.ai/artifact/R4zdNBmahtUo7GwysUZkKz

Problem:
    Write a reader for a long text file (put any story in data/story.txt).
    Each time the program runs it shows the next 3 lines, then asks
    "Continue? (y/n)". When the user quits, save the current position with
    fp.tell() into data/bookmark.txt. On the next run, read the bookmark and
    fp.seek() to it so reading continues where it stopped.
    - If bookmark.txt doesn't exist yet, start at byte 0.
    - When the story ends, print "Tapos na!" and reset the bookmark to 0.

Example:
    Run 1: lines 1–3 … Continue? y … lines 4–6 … Continue? n
    Saved bookmark at byte 412.
    Run 2: Resuming from byte 412 … lines 7–9 …

Hint:
    readline() returns "" (an empty string) at the end of the file. That's
    your stop signal. Remember that tell() counts bytes, not lines.

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
