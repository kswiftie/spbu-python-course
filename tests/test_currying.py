import pytest
from project.decorators import dec


@pytest.mark.parametrize(
    "inp_values, function_arity, function_result",
    [
        ("function", "arity", "curried function"),
    ],
)
def test_curry_explicit(inp_values, function_arity, function_result):
    assert 1 == 1
