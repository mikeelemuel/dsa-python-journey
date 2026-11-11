from chapters.ch01_python_primer.reinforcement.r01_09 import tens_from_50_to_80


def test_range_produces_50_to_80():
    assert list(tens_from_50_to_80()) == [50, 60, 70, 80]


def test_returns_a_range_object():
    assert isinstance(tens_from_50_to_80(), range)
