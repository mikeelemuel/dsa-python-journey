# 1.6 Simple Input and Output (real-world)

Book pp.30–32 · exercise page: https://claude.ai/artifact/R4zdNBmahtUo7GwysUZkKz

| ID | Exercise | Tier | Practices |
|---|---|---|---|
| W-1.6.1 | [Sari-sari store receipt line](w01_06_1.py) | ★ Warm-up | input · float() · print(sep=, end=) |
| W-1.6.2 | [Jeepney dispatcher log](w01_06_2.py) | ★★ Building up | input().split() · open('a') · write |
| W-1.6.3 | [Class average from a file](w01_06_3.py) | ★★ Building up | for line in fp · strip · print(file=) |
| W-1.6.4 | [Bookmark reader](w01_06_4.py) | ★★★ Challenge | readline · tell · seek · 'r' and 'w' together |
| W-1.6.5 | [Barangay contact book](w01_06_5.py) | ★★★ Challenge | menu loop · all three modes · rewrite a file |

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

1. Why does `age = input("Age: ")` followed by `age + 1` crash?
2. What's the difference between opening a file with `'w'` and with `'a'`?
3. After `fp.read()`, what does a second `fp.read()` return, and why?

-
