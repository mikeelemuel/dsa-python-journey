import pytest

from chapters.ch01_python_primer.reinforcement.r01_01 import is_multiple


def test_is_multiple():
    assert is_multiple(10, 5) is True
    assert is_multiple(10, 3) is False


@pytest.mark.parametrize(
    "n, m, expected",
    [
        (5, 5, True),     # n equals m (i = 1)
        (5, 1, True),     # everything is a multiple of 1
        (0, 7, True),     # 0 is a multiple of everything (i = 0)
        (3, 10, False),   # n smaller than m
        (-10, 5, True),   # negative n
        (10, -5, True),   # negative m
        (-10, -5, True),  # both negative
        (-7, 5, False),   # negative, not a multiple
    ],
)
def test_is_multiple_edge_cases(n, m, expected):
    assert is_multiple(n, m) is expected


def test_zero_is_only_multiple_of_zero():
    assert is_multiple(0, 0) is True
    assert is_multiple(5, 0) is False
