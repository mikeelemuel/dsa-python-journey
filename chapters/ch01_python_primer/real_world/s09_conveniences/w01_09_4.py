"""
W-1.9.4 | Chapter 1: Python Primer
Type: Real-world · ★★★ Challenge
Section: 1.9 Additional Python Conveniences · book pp.42–45    ->  python tools/show.py W-1.9.4
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Title: Shrink this code
Practices: combine everything · same output, fewer lines
Source: https://claude.ai/artifact/KAfywZC2CWVic2CF1hPfXq

Problem:
    Rewrite this in 5 lines or fewer (not counting the data) with the exact
    same output. Use comprehensions, unpacking, and conditional expressions.

        scores = {"Ana": 88, "Ben": 72, "Carl": 95, "Dina": 74, "Eli": 81}

        passed = []
        for name in scores:
            if scores[name] >= 75:
                passed.append(name)
        passed.sort()

        remarks = {}
        for name in scores:
            if scores[name] >= 90:
                remarks[name] = "with honors"
            else:
                if scores[name] >= 75:
                    remarks[name] = "passed"
                else:
                    remarks[name] = "failed"

        total = 0
        for name in scores:
            total = total + scores[name]
        average = total / len(scores)

        print(passed)
        print(remarks)
        print(round(average, 2))

Example:
    ['Ana', 'Carl', 'Eli']
    {'Ana': 'passed', 'Ben': 'failed', 'Carl': 'with honors', 'Dina': 'failed', 'Eli': 'passed'}
    82.0

Hint:
    Conditional expressions can be chained: "a" if x else "b" if y else "c".
    Use sorted() around a comprehension, and `for name, s in scores.items()` to
    unpack each pair.

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
