"""Example test. Delete the skip marker once you've solved R-1.1."""
import pytest

pytestmark = pytest.mark.skip(reason="R-1.1 not solved yet")


def test_is_multiple():
    from chapters.ch01_python_primer.reinforcement.r01_01 import is_multiple

    assert is_multiple(10, 5) is True
    assert is_multiple(10, 3) is False
