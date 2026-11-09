"""
W-1.6.2 | Chapter 1: Python Primer
Type: Real-world · ★★ Building up
Section: 1.6 Simple Input and Output · book pp.30–32    ->  python tools/show.py W-1.6.2
Status: done                   # todo | in-progress | done | skipped
Date: 2026-11-09
Time:

Title: Jeepney dispatcher log
Practices: input().split() · open('a') · write
Source: https://claude.ai/artifact/R4zdNBmahtUo7GwysUZkKz

Problem:
    The dispatcher types one passenger per line as `name destination fare`.
    Split each line, convert the fare to a number, and APPEND it to
    data/jeep_log.txt. A blank line ends input. Print how many passengers were
    logged and the total fare.

    Run the program twice. Then change 'a' to 'w' and run it twice again. Open
    the file each time and describe what changed (write it in Notes).

Example:
    > Ana Cubao 13
    > Ben Fairview 18
    >
    Logged 2 passengers. Total fare: ₱31.00

Hint:
    write does not add a newline for you. End each string with a newline,
    or use print(name, dest, fare, file=fp).

Approach:
    (idea, then time/space complexity)
    The flow for each line:
    line = input() gives you "Juan Cubao 13".
    If line is empty (""), stop the loop.
    line.split() gives you ["Juan", "Cubao", "13"].
    Unpack it: name, destination, fare = line.split(), then fare = float(fare).
    Write the line to the file, add 1 to the count, and add the fare to the total.
Notes:
    (gotchas, what you learned)
    - 'a' (append): each run adds its lines to the END of the file. After two
      runs the file had 4 lines; the first run's lines were still there.
    - 'w' (write): opening the file empties it first. After two runs it had
      only 2 lines, from the last run; the earlier ones were gone.
    - Use 'a' for a log you keep adding to; use 'w' only to start fresh.
    - write() adds no newline, so end each string with "\n".
    - The path data/jeep_log.txt is relative to the folder you run from, not
      to the .py file. Run it from s06_input_output/ or the data/ folder
      won't be found.
"""


# your solution here
def log_passengers():
    count = 0
    total = 0

    with open("data/jeep_log.txt", "a") as fp:
        while True:
            line = input("> ")

            if line == "":
                break

            name, destination, fare = line.split()
            fare = float(fare)

            fp.write(f"{name} {destination} {fare:.2f}\n")
            count += 1
            total += fare

    print(f"Logged {count} passengers. Total fare: ₱{total:.2f}")


if __name__ == "__main__":
    log_passengers()