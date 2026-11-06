import pytest

from chapters.ch01_python_primer.reinforcement.r01_03 import minmax

def test_minmax_basic():
    assert minmax([1, 2, 3, 4]) == (1, 4)

@pytest.mark.parametrize(
    "data, expected",
    [
        ([0, 1, 2, 3, 4], (0, 4)),       # sorted
        ([5, 8, 3], (3, 8)),             # unsorted
        ([-4, -1, -9], (-9, -1)),        # all negative
        ([7], (7, 7)),                   # single item
        ((2.5, 1.5, 3.5), (1.5, 3.5)),   # tuple of floats
        ([4, 4, 4], (4, 4)),             # duplicates
    ],
)

def test_minmax(data, expected):
    assert minmax(data) == expected