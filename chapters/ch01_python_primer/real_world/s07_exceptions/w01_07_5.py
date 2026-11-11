"""
W-1.7.5 | Chapter 1: Python Primer
Type: Real-world · ★★★ Challenge
Section: 1.7 Exception Handling · book pp.33–38    ->  python tools/show.py W-1.7.5
Status: done            # todo | in-progress | done | skipped
Date: 2026-11-12
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
    ask_station(): only int(input(...)) sits in a try; a bad number is re-raised
    as ValueError("Enter a station number."). Then raise IndexError for numbers
    below 1 and ValueError for the same station.
    main(): STATIONS[n - 1] raises IndexError by itself for 14+ (ask forgiveness).
    except ValueError -> print(e); except IndexError -> "No such station.";
    except EOFError -> "Machine shutting down." + bare raise.
    else: stops = abs(destination - origin), fare = min(13 + stops, 28).

    Time:  O(n) to print the n stations; the fare itself is O(1).
    Space: O(1).

Notes:
    (gotchas, what you learned)
    - finally runs even after an error: it printed a fake "0 stations · Fare P0"
      ticket after every error message. else runs only when nothing failed.
    - A try around my own raise caught it: "same station" came out as
      "Enter a station number." Keep the try around int() only.
    - STATIONS[-1] is "Taft", not an error, so numbers below 1 need my own raise.
    - range(1, len(STATIONS)) and len(STATIONS) + 1 were both off by one; letting
      the list raise IndexError for 14+ avoids the bound entirely.
    - abs() makes backwards trips count the same (11 -> 4 is 7 stations).
    - The ₱28 cap never triggers here: the longest trip is 12 stations = ₱25.
    - from None hides int()'s original error if the new one is ever uncaught.
    - input() always returns a str, so int(input()) can't raise TypeError.
    - Ctrl-D (Control, not Command) only ends input on an empty prompt line.
    - sum(1 for _ in range(stops)) just rebuilds stops; a comprehension only
      pays off when each segment has its own price.
"""


# your solution here
STATIONS = ["North Ave", "Quezon Ave", "GMA Kamuning", "Cubao",
            "Santolan", "Ortigas", "Shaw", "Boni", "Guadalupe",
            "Buendia", "Ayala", "Magallanes", "Taft"]
BASE_FARE = 13
MAX_FARE = 28


def stations():
    for index, station in enumerate(STATIONS, start=1):
        print(f"{index:>2}. {station}")


def ask_station():
    try:
        origin = int(input("From: "))
        destination = int(input("To:   "))
    except ValueError:
        raise ValueError("Enter a station number.") from None

    if origin < 1 or destination < 1:
        raise IndexError                    # STATIONS[-1] would quietly give "Taft"
    if origin == destination:
        raise ValueError("Origin and destination are the same")

    return origin, destination


def main():
    stations()
    try:
        origin, destination = ask_station()
        origin_name = STATIONS[origin - 1]
        destination_name = STATIONS[destination - 1]
    except ValueError as e:
        print(e)
    except IndexError:
        print("No such station.")
    except EOFError:
        print("Machine shutting down.")
        raise
    else:
        stops = abs(destination - origin)
        total_fare = min(BASE_FARE + stops, MAX_FARE)
        print(f"{origin_name} -> {destination_name}")
        print(f"{stops} stations · Fare ₱{total_fare}")


if __name__ == "__main__":
    main()
