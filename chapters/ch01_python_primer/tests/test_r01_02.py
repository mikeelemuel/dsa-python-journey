import ast
import inspect

import pytest

from chapters.ch01_python_primer.reinforcement.r01_02 import is_even

def test_is_even_basic():
    assert is_even(4) is True
    assert is_even(7) is False

@pytest.mark.parametrize(
    "k, expected",
    [
        (0, True),        # zero is even
        (1, False),       # smallest odd
        (2, True),        # smallest even > 0
        (-6, True),       # negative even
        (-3, False),      # negative odd
        (10**18, True),   # very large even
    ],
)
def test_is_even_edge_cases(k, expected):
    assert is_even(k) is expected

def test_does_not_use_forbidden_operators():
    tree = ast.parse(inspect.getsource(is_even))
    forbidden = (ast.Mult, ast.Mod, ast.Div, ast.FloorDiv)
    used = [type(node.op).__name__ for node in ast.walk(tree)
            if isinstance(node, (ast.BinOp, ast.AugAssign)) and isinstance(node.op, forbidden)]
    assert used == [], f"forbidden operators used: {used}"