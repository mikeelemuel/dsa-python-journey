# 1.8 Iterators and Generators (real-world)

Book pp.39–41 · exercise page: https://claude.ai/artifact/BhyrFMkLeHaB9j9CNLUn6e

| ID | Exercise | Tier | Practices |
|---|---|---|---|
| W-1.8.1 | [A for loop without for](w01_08_1.py) | ★ Warm-up | iter · next · StopIteration |
| W-1.8.2 | [Bank queue numbers](w01_08_2.py) | ★★ Building up | infinite generator · independent state |
| W-1.8.3 | [Lazy vs. eager](w01_08_3.py) | ★★ Building up | return a list vs. yield · memory · early stop |
| W-1.8.4 | [Sales log pipeline](w01_08_4.py) | ★★★ Challenge | generators feeding generators · revisit 1.6 and 1.7 |
| W-1.8.5 | [Pandesal tray layouts](w01_08_5.py) | ★★★ Challenge | multiple yields · √n trick · order of results |

## Data files

Input files live in `data/` next to the exercises. Open them relative to the exercise file so it works from any folder:

```python
from pathlib import Path

DATA = Path(__file__).parent / "data"
with open(DATA / "sales.txt") as fp:
    ...
```

## Mental model check

Answer these in your own words after finishing the set.

1. What exactly does a `for` loop do behind the scenes, step by step?
2. What happens if you loop over the same generator object twice?
3. Why can `fibonacci()` on page 41 use `while True` without freezing your program?

-
