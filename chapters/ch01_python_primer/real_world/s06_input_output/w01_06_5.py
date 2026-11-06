"""
W-1.6.5 | Chapter 1: Python Primer
Type: Real-world · ★★★ Challenge
Section: 1.6 Simple Input and Output · book pp.30–32    ->  python tools/show.py W-1.6.5
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Title: Barangay contact book
Practices: menu loop · all three modes · rewrite a file
Source: https://claude.ai/artifact/R4zdNBmahtUo7GwysUZkKz

Problem:
    Build a small command-line phonebook stored in data/contacts.txt, one
    contact per line as name,number,purok. Show a menu until the user picks Q:
        [A] Add contact     -> append mode
        [L] List all        -> read mode, numbered list
        [S] Search by name  -> case-insensitive match
        [D] Delete contact  -> read all lines, then rewrite with 'w'
        [Q] Quit
    - Reject a number that isn't 11 digits starting with 09.
    - Listing should still work if the file doesn't exist yet. Print
      "No contacts yet."

Example:
    [A] name: Aling Nena  number: 09171234567  purok: 3
    [L] 1. Aling Nena  09171234567  Purok 3

Hint:
    You can't delete one line from a text file in place. Read every line with
    readlines(), keep the ones you want, and write them all back with
    writelines() in 'w' mode. Exception handling (1.7) makes the missing-file
    case cleaner, so come back and improve this after the next topic.

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
