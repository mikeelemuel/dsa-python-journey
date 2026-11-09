"""
W-1.6.4 | Chapter 1: Python Primer
Type: Real-world · ★★★ Challenge
Section: 1.6 Simple Input and Output · book pp.30–32    ->  python tools/show.py W-1.6.4
Status: done                   # todo | in-progress | done | skipped
Date: 2026-11-09
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
    1. Load the bookmark.
       Try to open data/bookmark.txt with 'r' and read the number with int().
       If the file doesn't exist yet, use position 0.

    2. Open the story and jump to the bookmark.
       Open data/story.txt with 'r', then fp.seek(position).
       If position > 0, print "Resuming from byte ...".

    3. Show pages in a loop.
       Repeat:
         - Read up to 3 lines with readline(), printing each one.
         - If readline() returns "" at any point, the story is over:
           print "Tapos na!", set position to 0, and stop.
         - Otherwise ask "Continue? (y/n)".
           If the answer is "n", set position = fp.tell() and stop.
           If "y", go back to the top of the loop for the next 3 lines.

    4. Save the bookmark.
       Open data/bookmark.txt with 'w' and write the position (as a string).
       Print "Saved bookmark at byte ...".

    Time: O(k) per run, where k is the number of lines shown, because seek()
    jumps straight to the bookmark without re-reading earlier lines.
    Space: O(1), only one line is held in memory at a time.

Notes:
    (gotchas, what you learned)
    - Tested with a 7-line story: answering "n" after page 1 saved byte 9
      (3 lines of "lN\n" = 3 bytes each). The next run printed "Resuming from
      byte 9" and continued at line 4. Reaching the end printed "Tapos na!"
      and reset the bookmark to 0.
    - tell() and seek() work in bytes, not lines. That is why a bookmark
      can jump straight back to where you stopped without re-reading.
    - Take fp.tell() BEFORE the file closes; after the `with` block it fails.
    - readline() returns "" only at the end of the file. A blank line in the
      story is "\n", so `line == ""` is a safe end check.
    - `break` inside the for loop only leaves the for, not the while. The
      `finished` flag carries "story over" out to the outer loop.
    - try/except FileNotFoundError handles the first run, before
      bookmark.txt exists.
    - write() needs a string: bm.write(str(position)).
    - If bookmark.txt contains junk, int() raises ValueError, which is not
      caught.
    - Paths are relative to the folder you run from, so run it from
      s06_input_output/.
"""


# your solution here
def bookmark_reader():
    # 1. Load the bookmark
    try:
        with open("data/bookmark.txt", "r") as bm:
            position = int(bm.read())
    except FileNotFoundError:
        position = 0

    # 2. Open the story and jump to the bookmark
    with open("data/story.txt", "r") as fp:
        fp.seek(position)
        if position > 0:
            print(f"Resuming from byte {position}")

        # 3. Show pages in a loop
        finished = False
        while True:
            for i in range(3):
                line = fp.readline()
                if line == "":
                    finished = True
                    break
                print(line, end="")

            if finished:
                print("Tapos na!")
                position = 0
                break

            answer = input("Continue? (y/n) ").strip().lower()
            if answer == "n":
                position = fp.tell()
                break

    # 4. Save the bookmark
    with open("data/bookmark.txt", "w") as bm:
        bm.write(str(position))

    if position > 0:
        print(f"Saved bookmark at byte {position}.")


if __name__ == "__main__":
    bookmark_reader()
