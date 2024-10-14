import pytest
from project.generators import prime_seq_gen, get_prime_number


@pytest.mark.parametrize(
    "function, prime_number_number, expected",
    [
        (get_prime_number()(prime_seq_gen), 12, 37),
        (get_prime_number()(prime_seq_gen), 13, 41),
        (get_prime_number()(prime_seq_gen), 6, 13),
        (get_prime_number(stopnumber=150000)(prime_seq_gen), 12423, 133103),
    ],
)
def test_(function, prime_number_number, expected):
    assert function(prime_number_number) == expected
