from chapters.ch01_python_primer.reinforcement.r01_10 import evens_from_8_to_minus_8


def test_range_counts_down_from_8_to_minus_8():
    assert list(evens_from_8_to_minus_8()) == [8, 6, 4, 2, 0, -2, -4, -6, -8]


def test_returns_a_range_object():
    assert isinstance(evens_from_8_to_minus_8(), range)
