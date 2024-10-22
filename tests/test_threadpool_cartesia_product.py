import pytest
from project.threadpool import cartesian_sum
from utils import onethread_cartesian_sum


@pytest.mark.parametrize(
    "function, inp_set, cores_number",
    [
        (cartesian_sum, {1, 2}, 6),
        (cartesian_sum, {}, 12),
        (cartesian_sum, set(range(1, 5)), 8),
        (cartesian_sum, set(range(1, 6)), 12),
        (cartesian_sum, set(range(1, 500, 2)), 8),
        (cartesian_sum, set(range(1, 10**3, 3)), 12),
    ],
)
def test_cartesian_sum_value(function, inp_set, cores_number):
    assert function(inp_set, cores_number) == onethread_cartesian_sum(inp_set)
