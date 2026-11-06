# 1.7 Exception Handling (real-world)

Book pp.33–38 · exercise page: https://claude.ai/artifact/SDiTepd5Sp8BBrktSDb1PQ

| ID | Exercise | Tier | Practices |
|---|---|---|---|
| W-1.7.1 | [GCash top-up that won't crash](w01_07_1.py) | ★ Warm-up | try / except ValueError · while loop |
| W-1.7.2 | [Name that error](w01_07_2.py) | ★★ Building up | common exception types · except … as e |
| W-1.7.3 | [ATM withdrawal guard](w01_07_3.py) | ★★ Building up | raise · isinstance · type check before value check |
| W-1.7.4 | [Bulletproof grades reader](w01_07_4.py) | ★★★ Challenge | multiple excepts · finally · revisit 1.6 |
| W-1.7.5 | [MRT-3 ticket machine](w01_07_5.py) | ★★★ Challenge | several exception types · your own raise · re-raise |

## Data files

Input files live in `data/` next to the exercises. Open them relative to the exercise file so it works from any folder:

```python
from pathlib import Path

DATA = Path(__file__).parent / "data"
with open(DATA / "grades.txt") as fp:
    ...
```

## Mental model check

Answer these in your own words after finishing the set.

1. If line 2 of a 5-line `try` block raises an error, which of the other lines still run?
2. When would you choose `if y != 0:` over `try … except ZeroDivisionError`?
3. Does a `finally` block run if the exception was never caught? What about after a `return`?

-
