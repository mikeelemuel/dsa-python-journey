"""
W-1.6.5 | Chapter 1: Python Primer
Type: Real-world · ★★★ Challenge
Section: 1.6 Simple Input and Output · book pp.30–32    ->  python tools/show.py W-1.6.5
Status: done                   # todo | in-progress | done | skipped
Date: 2026-11-09
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
    Loop: show the menu, read a choice, and run the matching function with
    match/case until the user picks Q (break).
    A: ask for name, number, purok; reject a bad number; append
       "name,number,purok\n" with 'a'.
    L: read all lines (empty list if the file doesn't exist); print each
       with enumerate(start=1).
    S: lowercase the search and each name; print lines where search in name.
    D: read all lines, keep those whose name doesn't match, rewrite with 'w'.
    Time: O(n) per command, where n is the number of contacts.
    Space: O(n) for L, S and D, which hold all lines in memory.

Notes:
    (gotchas, what you learned)
    - Tested every command on a scratch copy: L with no file prints "No
      contacts yet.", a bad number is rejected, "NENA" finds "Aling Nena",
      D removes the line and rewrites the file, and an unknown command shows
      the help message.
    - You can't delete one line in place: readlines(), keep the lines you
      want, then writelines() them back in 'w' mode.
    - readlines() keeps each "\n", so writelines(kept) needs no extra
      newlines, but print_contact must strip() before split(",").
    - Lowercase BOTH sides for a case-insensitive match. Search uses `in`
      (partial match); delete uses `!=` (exact name only).
    - Delete removes EVERY contact with that name, not just the first.
    - Delete compares len(kept) with len(contacts) to tell whether anything
      was removed before rewriting the file.
    - match/case with `case _:` handles any unknown command.
    - read_contacts() returns [] when the file is missing, so L, S and D
      all handle the first run.
    - A comma in a name, or a blank line in the file, would break
      split(",") in print_contact (ValueError).
    - `import os` is unused and can go.
"""


# your solution here
import os

FILE = "data/contacts.txt"

def phonebook():
    while True:
        operation = main_menu()

        match operation:
            case 'a':
                add_contact()
            case 'l':
                list_all_contacts()
            case 's':
                search_contact()
            case 'd':
                delete_contact()
            case 'q':
                print('Paalam!')
                break
            case _:
                print('Enter a valid command (A, L, S, D or Q).')


def main_menu():
    print()
    print('[A] Add Contact')
    print('[L] List All')
    print('[S] Search by name')
    print('[D] Delete a contact')
    print('[Q] Quit')
    operation = input("What do you want to do? ").strip().lower()

    return operation


def read_contacts():
    try:
        with open(FILE) as fp:
            return fp.readlines()
    except FileNotFoundError:
        return []

def print_contact(index, line):
    name, number, purok = line.strip().split(',')
    print(f"{index}. {name}  {number}  Purok {purok}")


def add_contact():
    name = input('Name: ').strip()
    number = input('Number: ').strip()
    purok = input('Purok: ').strip()

    if len(number) != 11 or not number.isdigit() or not number.startswith('09'):
        print('Invalid number. It must be 11 digits and start with 09.')
        return

    with open(FILE, 'a') as fp:
        fp.write(f"{name},{number},{purok}\n")

    print(f"Added {name}.")


def list_all_contacts():
    contacts = read_contacts()

    if len(contacts) == 0:
        print('No contacts yet.')
        return

    for index, line in enumerate(contacts, start=1):
        print_contact(index, line)


def search_contact():
    contacts = read_contacts()

    if len(contacts) == 0:
        print('No contacts yet.')
        return

    target = input('Search name: ').strip().lower()
    found = 0

    for line in contacts:
        name = line.split(',')[0]
        if target in name.lower():
            found += 1
            print_contact(found, line)

    if found == 0:
        print('No match found.')


def delete_contact():
    contacts = read_contacts()

    if len(contacts) == 0:
        print('No contacts yet.')
        return

    target = input('Name to delete: ').strip().lower()
    kept = []

    for line in contacts:
        name = line.split(',')[0]
        if name.lower() != target:
            kept.append(line)

    if len(kept) == len(contacts):
        print('No contact with that name.')
        return

    with open(FILE, 'w') as fp:
        fp.writelines(kept)

    print('Contact deleted.')


if __name__ == "__main__":
    phonebook()
