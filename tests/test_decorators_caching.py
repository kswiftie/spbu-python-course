import pytest
from project.decorators import memoize

sum = memoize(max_cached_args=3, show_cache=True)(sum)


@pytest.mark.parametrize(
    "function, function_inputs, expected_result",
    [
        (sum, [1, 2, 3], [6]),
        (sum, [5, -1, -3, -1, -3], [6, -3]),
        (
            sum,
            [
                3.5783645163013524,
                4.7957585177990865,
                -2.360007025295503,
                2.084946450180979,
                4.7400573122482506,
                -3.1304113865913905,
            ],
            [6, -3, 9.708708384642776],
        ),
        (sum, [-2, -1, -4, -3], [-3, 9.708708384642776, -10]),
        (sum, [5, -1, -3, -1, -3], [9.708708384642776, -10, -3]),
    ],
)
def test_memoize(function, function_inputs, expected_result):
    assert function(function_inputs) == expected_result
