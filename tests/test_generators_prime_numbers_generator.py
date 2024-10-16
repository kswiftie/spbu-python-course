import pytest
from project.generators import prime_seq_gen, get_prime_number


@pytest.mark.parametrize(
    "function, args, expected",
    [
        (get_prime_number(prime_seq_gen), [1, 2, 3, 4, 5], [2, 3, 5, 7, 11]),
        (get_prime_number(prime_seq_gen), [12, 13], [37, 41]),
        (
            get_prime_number(prime_seq_gen),
            [x for x in range(30, 41)],
            [113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173],
        ),
    ],
)
def test_(function, args, expected):
    assert [function(x) for x in args] == expected
