import pytest
from random import randint
from project.decorators import smart_args, Evaluated, Isolated
from utils import check_isolation, check_evaluation


@pytest.mark.parametrize(
    "function, kwargs, expected_result",
    [
        (smart_args(check_isolation), {'d': {'a': 10}}, {'a': 10}),
    ],
)
def test_smartargs_Isolation(function, kwargs, expected_result):
    inp = [x for x in kwargs.values()][0]
    function(d=inp)
    assert inp == expected_result


@pytest.mark.parametrize(
    "function, inp, expected_result",
    [
        (smart_args(check_evaluation), [{}, {}, {'y': 150}], ""),
    ],
)
def test_smartargs_Evaluation(function, inp, expected_result):
    x, y = [], []
    for kwargs in inp:
        x1, y1 = function(**kwargs)
        x.append(x1)
        y.append(y1)
    assert (len(set(x)) == 1 and len(set(y)) == len(y))
