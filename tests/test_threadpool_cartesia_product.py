import pytest
from project.threadpool import cartesian_sum
from utils import get_function_execution_time


@pytest.mark.parametrize(
    "function, inp_set, cores_number, expected",
    [
        (cartesian_sum, {1, 2}, 6, 12),
        (cartesian_sum, {}, 12, 0),
        (cartesian_sum, set(range(1, 5)), 8, 80),
        (cartesian_sum, set(range(1, 6)), 12, 150),
    ],
)
def test_cartesian_sum_value(function, inp_set, cores_number, expected):
    assert function(inp_set, cores_number) == expected


@pytest.mark.parametrize(
    "function, args, expected_time",
    [
        (get_function_execution_time, [cartesian_sum, {1, 2}, 6], 0.5),
        (get_function_execution_time, [cartesian_sum, {}, 12], 0.5),
        (get_function_execution_time, [cartesian_sum, set(range(1, 5)), 8], 0.5),
        (get_function_execution_time, [cartesian_sum, set(range(1, 6)), 12], 0.5),
    ],
)
def test_cartesian_sum_time(function, args, expected_time):
    assert function(*args) <= expected_time
