import pytest
from project.generators import get_rgba_vector, rgba_vector


@pytest.mark.parametrize(
    "function, vector_number, expected",
    [
        (get_rgba_vector(rgba_vector), 0, (0, 0, 0, 0)),
        (get_rgba_vector(rgba_vector), 50, (0, 0, 0, 100)),
        (get_rgba_vector(rgba_vector), 51, (1, 0, 0, 0)),
        (get_rgba_vector(rgba_vector), 256 * 51, (0, 1, 0, 0)),
        (get_rgba_vector(rgba_vector), 256 * 256 * 51, (0, 0, 1, 0)),
    ],
)
def test_(function, vector_number, expected):
    assert function(vector_number) == expected
