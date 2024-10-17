import pytest
from random import randint
from project.decorators import smart_args, Evaluated, Isolated
from utils import check_isolation, check_evaluation, check_evaluation_with_isolation


@pytest.mark.parametrize(
    "function, args, kwargs, expected",
    [
        (
            check_isolation,
            [4, {"a": 10, "b": 11}, [5, 3]],
            {},
            ([4, {"a": "a", "b": "b"}, []], {}),
        ),
        (
            check_isolation,
            [],
            {"d": {"a": 1, "b": 2}, "l": [5]},
            ([], {"d": {"a": "a", "b": "b"}, "l": []}),
        ),
        (
            check_isolation,
            [12],
            {"d": {"a": 1, "b": 2}, "l": [5]},
            ([12], {"d": {"a": "a", "b": "b"}, "l": []}),
        ),
        (
            check_isolation,
            [12, {"a": 10, "b": 11}],
            {"l": [5]},
            ([12, {"a": "a", "b": "b"}], {"l": []}),
        ),
        (
            check_isolation,
            [12, {"a": 10, "b": 11}, [5]],
            {},
            ([12, {"a": "a", "b": "b"}, []], {}),
        ),
        (
            smart_args(check_isolation),
            [],
            {"d": {"a": 1, "b": 2}, "l": [5]},
            ([], {"d": {"a": 1, "b": 2}, "l": [5]}),
        ),
        (
            smart_args(check_isolation),
            [12],
            {"d": {"a": 1, "b": 2}, "l": [5]},
            ([12], {"d": {"a": 1, "b": 2}, "l": [5]}),
        ),
        (
            smart_args(check_isolation),
            [12, {"a": 10, "b": 11}],
            {"l": [5]},
            ([12, {"a": 10, "b": 11}], {"l": [5]}),
        ),
        (
            smart_args(check_isolation),
            [12, {"a": 10, "b": 11}, [5]],
            {},
            ([12, {"a": 10, "b": 11}, [5]], {}),
        ),
    ],
)
def test_smartargs_Isolation(function, args, kwargs, expected):
    function(*args, **kwargs)
    assert (args, kwargs) == expected


@pytest.mark.parametrize(
    "function, args, kwargs, expected",
    [
        (smart_args(check_evaluation), [1, 2, 3], {}, (1, 2, 3)),
        (smart_args(check_evaluation), [1, 2], {"y": 150}, (1, 2, 150)),
        (smart_args(check_evaluation), [1], {"x": -1, "y": 150}, (1, -1, 150)),
        (smart_args(check_evaluation), [], {"x": 2, "y": 3}, (None, 2, 3)),
    ],
)
def test_smartargs_Evaluation_substitutions(function, args, kwargs, expected):
    res = function(*args, **kwargs)
    assert res == expected


@pytest.mark.parametrize(
    "function, args, kwargs, launch_cnt, unique_values_x, unique_values_y",
    [
        (
            smart_args(check_evaluation),
            [],
            {},
            1,
            1,
            1,
        ),
        (smart_args(check_evaluation), [], {}, 3, 1, 3),
        (smart_args(check_evaluation), [], {}, 5, 1, 5),
        (smart_args(check_evaluation), [], {}, 7, 1, 7),
    ],
)
def test_smartargs_Evaluation_uniqueness(
    function, args, kwargs, launch_cnt, unique_values_x, unique_values_y
):
    s, x, y = [], set(), set()
    for _ in range(launch_cnt):
        s, x1, y1 = function(*args, **kwargs)
        x.add(x1)
        y.add(y1)

    assert len(x) == unique_values_x and len(y) == unique_values_y


@pytest.mark.parametrize(
    "function, args, kwargs, expected",
    [
        (
            smart_args(check_evaluation_with_isolation),
            [1, {"a": 10, "b": 11}, 150],
            {},
            ([1, {"a": 10, "b": 11}, 150], {}, 150),
        ),
        (
            smart_args(check_evaluation_with_isolation),
            [1],
            {"d": {"a": 2, "b": 3}, "y": 152},
            ([1], {"d": {"a": 2, "b": 3}, "y": 152}, 152),
        ),
        (
            smart_args(check_evaluation_with_isolation),
            [],
            {"d": {"a": 8.6, "b": -4.2}, "y": 6},
            ([], {"d": {"a": 8.6, "b": -4.2}, "y": 6}, 6),
        ),
    ],
)
def test_smartargs_Evaluation_substitutions_with_Isolation(
    function, args, kwargs, expected
):
    s, y = function(*args, **kwargs)
    assert (args, kwargs, y) == expected


@pytest.mark.parametrize(
    "function, args, kwargs, launch_cnt, expected",
    [
        (
            smart_args(check_evaluation_with_isolation),
            [1, {"a": 10, "b": 11}],
            {},
            3,
            ([1, {"a": 10, "b": 11}], {}, 3),
        ),
        (
            smart_args(check_evaluation_with_isolation),
            [1],
            {"d": {"a": 2, "b": 3}},
            5,
            ([1], {"d": {"a": 2, "b": 3}}, 5),
        ),
        (
            smart_args(check_evaluation_with_isolation),
            [],
            {"d": {"a": 8.6, "b": -4.2}},
            7,
            ([], {"d": {"a": 8.6, "b": -4.2}}, 7),
        ),
    ],
)
def test_smartargs_Evaluation_uniqueness_with_Isolation(
    function, args, kwargs, launch_cnt, expected
):
    y = set()
    for _ in range(launch_cnt):
        s, y1 = function(*args, **kwargs)
        y.add(y1)

    assert (args, kwargs, len(y)) == expected
