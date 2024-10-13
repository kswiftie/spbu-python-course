import pytest
from random import randint
from project.decorators import smart_args, Evaluated, Isolated
from utils import (
    check_isolation,
    check_evaluation,
    check_isolation_posargs,
    check_evaluation_posargs,
)


@pytest.mark.parametrize(
    "function, kwargs, expected_result",
    [
        (smart_args(check_isolation), {"d": {"a": 10}}, {"a": 10}),
    ],
)
def test_smartargs_Isolation(function, kwargs, expected_result):
    inp = [x for x in kwargs.values()][0]
    function(d=inp)
    assert inp == expected_result


@pytest.mark.parametrize(
    "function, inp, lenx, leny, lensetx, lensety",
    [
        (smart_args(check_evaluation), [{}, {}, {"y": 150}], 3, 3, 1, 3),
    ],
)
def test_smartargs_Evaluation(function, inp, lenx, leny, lensetx, lensety):
    x, y = [], []
    for kwargs in inp:
        x1, y1 = function(**kwargs)
        x.append(x1)
        y.append(y1)
    assert (
        len(set(x)) == lensetx
        and len(set(y)) == lensety
        and len(y) == len(y)
        and len(x) == lenx
    )


@pytest.mark.parametrize(
    "function, args, expected",
    [
        (
            smart_args(check_isolation_posargs),
            [[["f"], [1], [3]], [[0], [5], [-4]], [[5], [2], [3]]],
            [[["f"], [1], [3]], [[0], [5], [-4]], [[5], [2], [3]]],
        ),
    ],
)
def test_smartargs_Isolation_posargs(function, args, expected):
    for x in args:
        function(*x)

    assert args == expected


@pytest.mark.parametrize(
    "function, args, kwargs, lenx, leny, lensetx, lensety",
    [
        (
            smart_args(check_evaluation_posargs),
            [[-1], [22, 5, 7], []],
            [{}, {}, {"y": 150}],
            3,
            3,
            1,
            3,
        ),
    ],
)
def test_smartargs_Evaluation_posargs(
    function, args, kwargs, lenx, leny, lensetx, lensety
):
    (
        x,
        y,
    ) = (
        [],
        [],
    )
    for i in range(len(args)):
        *other, x1, y1 = function(*args[i], **kwargs[i])
        x.append(x1)
        y.append(y1)

    assert (
        len(set(x)) == lensetx
        and len(set(y)) == lensety
        and len(y) == len(y)
        and len(x) == lenx
    )
