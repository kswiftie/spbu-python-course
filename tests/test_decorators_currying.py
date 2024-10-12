import pytest, io, sys
from project.decorators import curry_explicit, uncurry_explicit
from utils import mysum


@pytest.mark.parametrize(
    "function, function_arity, function_inputs, expected_result",
    [
        (lambda x, y, z: f'<{x},{y},{z}>', 3, [123, 456, 562], "<123,456,562>"),
        (mysum, 5, [1, 2, 3, 4, 5], 15),
        (mysum, 0, [], 0),
    ],
)
def test_curried_functions(function, function_arity, function_inputs, expected_result):
    f2 = curry_explicit(function, function_arity)
    tmp = f2 if function_arity else f2()
    for x in function_inputs:
        tmp = tmp(x)
    assert tmp == expected_result


@pytest.mark.parametrize(
    "function, function_arity, function_inputs, expected_result",
    [
        (print, 2, ["inp1", 12], "inp1 12\n"),
        (print, 0, [], "\n"),
    ],
)
def test_curried_print(function, function_arity, function_inputs, expected_result):
    f2 = curry_explicit(function, function_arity)
    sys.stdout = io.StringIO()  # Redirect output

    tmp = f2 if function_arity else f2()
    for x in function_inputs:
        tmp = tmp(x)

    output = sys.stdout.getvalue()
    sys.stdout = sys.__stdout__  # Recovery output
    assert output == expected_result


@pytest.mark.parametrize(
    "curried_function, function_arity, function_inputs, expected_result",
    [
        (curry_explicit(lambda x, y, z: f'<{x},{y},{z}>', 3), 3, [123, 456, 562], "<123,456,562>"),
        (curry_explicit(mysum, 5), 5, [1, 2, 3, 4, 5], 15),
        (curry_explicit(mysum, 0), 0, [], 0),
    ],
)
def test_uncurried_functions(curried_function, function_arity, function_inputs, expected_result):
    assert uncurry_explicit(curried_function, function_arity)(*function_inputs) == expected_result
