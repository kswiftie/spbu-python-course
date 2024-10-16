import functools
from typing import Generator, Callable, List


def get_prime_number(func: Callable):
    """
    Decorator for prime_seq_gen that counts the nth prime number

    Returns
    -------
    int
        prime number by inputted number
    """

    @functools.wraps(func)
    def inner(n: int) -> int:
        if n < 1:
            raise ValueError("Number of prime number must be greater than 0")
        g = func()
        try:
            for i in range(n - 1):
                next(g)
            return next(g)
        except Exception:
            raise ValueError(
                "Number of prime number must be into generated sequence of prime numbers"
            )

    return inner


def prime_seq_gen() -> Generator:
    """
    A function that generates sequence of prime numbers before inputted number


    Returns
    -------
    Generator
        Sequence of prime numbers
    """
    n = 2
    prime_numbers: List = []

    while True:
        is_prime = True
        for p in prime_numbers:
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(n)
            yield n
        n += 1
