import pytest

from chapters.ch01_python_primer.reinforcement.r01_06 import sum_of_all_odd


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 0),           # no positive integers smaller than 1
        (2, 1),           # 1
        (3, 1),           # 1 (2 is even)
        (4, 10),          # 1 + 9
        (7, 35),          # 1 + 9 + 25 (odd n itself excluded)
        (11, 165),        # 1 + 9 + 25 + 49 + 81
    ],
)
def test_sum_of_all_odd(n, expected):
    assert sum_of_all_odd(n) == expected
