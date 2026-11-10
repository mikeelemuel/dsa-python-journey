import pytest

from chapters.ch01_python_primer.reinforcement.r01_04 import sum_of_squares


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 0),           # no positive integers smaller than 1
        (2, 1),           # 1
        (4, 14),          # 1 + 4 + 9 (n itself excluded)
        (11, 385),        # 1..10
        (101, 338350),    # closed form (n-1)n(2n-1)/6
    ],
)
def test_sum_of_squares(n, expected):
    assert sum_of_squares(n) == expected
