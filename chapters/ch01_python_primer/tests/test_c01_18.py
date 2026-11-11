from chapters.ch01_python_primer.creativity.c01_18 import products_of_consecutive


def test_produces_the_target_list():
    assert products_of_consecutive() == [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
