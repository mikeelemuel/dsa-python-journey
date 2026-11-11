import pytest

from chapters.ch01_python_primer.creativity.c01_15 import is_distinct


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1, 2, 4, 8, 6, 7, 8], False),   # 8 appears twice
        ([1, 2, 3], True),
        ([5, 6, 7], True),                # values larger than the length
        ([], True),                       # nothing to compare
        ([4], True),
        ([3, 3], False),
        ((1, 2, 1), False),               # any sequence, not just lists
    ],
)
def test_is_distinct(numbers, expected):
    assert is_distinct(numbers) is expected
