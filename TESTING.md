# Writing tests

How I write a test for an exercise. Run them with `pytest` (see [WORKFLOW.md](WORKFLOW.md)).

## Where it goes

| Exercise | Test file |
|---|---|
| `chapters/ch01_python_primer/reinforcement/r01_02.py` | `chapters/ch01_python_primer/tests/test_r01_02.py` |
| `chapters/ch01_python_primer/real_world/s07_exceptions/w01_07_3.py` | `chapters/ch01_python_primer/tests/real_world/test_w01_07_3.py` |

Real-world imports include the section folder:
`from chapters.ch01_python_primer.real_world.s07_exceptions.w01_07_3 import withdraw`.
Interactive ones (menus, `input()` loops) can skip tests; put the testable logic in a function if you want one.

pytest only finds files named `test_*.py` and functions named `test_*`.

## Template

Copy, rename `r01_02` / `my_function`, keep the parts you need, delete the rest.
Most exercises only need part 1, plus part 2 for edge cases.

```python
import pytest

from chapters.ch01_python_primer.reinforcement.r01_02 import my_function


# 1. Basic: the normal case from the problem statement
def test_basic():
    assert my_function(10) == 20


# 2. Many inputs at once: one row = one test
@pytest.mark.parametrize(
    "value, expected",
    [
        (0, 0),     # zero
        (1, 2),     # smallest positive
        (-3, -6),   # negative
    ],
)
def test_many_inputs(value, expected):
    assert my_function(value) == expected


# 3. Errors: when bad input SHOULD crash
def test_rejects_bad_input():
    with pytest.raises(ValueError):
        my_function("not a number")
```

## What each piece means

- **`from ... import my_function`** loads my solution. The path mirrors the folders, with dots in place of `/` and no `.py`.
- **`assert something`** passes if `something` is true and fails the test if not.
  - `assert f(x) == 5`: the result equals 5
  - `assert f(x) is True`: exactly `True` (use `is` for `True`, `False`, `None`)
  - `assert f(x) == [1, 2, 3]`: lists, dicts and strings compare directly
- **`@pytest.mark.parametrize`** runs the same test once per row, instead of copy-pasting asserts.
- **`pytest.raises(ValueError)`** passes only if the code inside raises that error.

## Picking test cases

1. **Normal:** what does the problem's own example give?
2. **Edges:** 0, 1, negative, empty (`""`, `[]`), one item, very large values.
3. **Wrong answers:** a case where the answer should be `False`, empty, or "not found".
4. **Rules in the problem:** if it bans something (an operator, a built-in), test that too.
   See `test_does_not_use_forbidden_operators` in
   [`test_r01_02.py`](chapters/ch01_python_primer/tests/test_r01_02.py).

## Test first

1. Write the test. 2. Run it: it **fails** (the function doesn't exist yet). 3. Write code until it **passes**.
