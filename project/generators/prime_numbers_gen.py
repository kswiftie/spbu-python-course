import functools
from typing import Generator, Callable


def get_prime_number(*, stopnumber: int = 1000):
    """
    Decorator for prime_seq_gen that counts the nth prime number

    Parameters
    ----------
    stopnumber: int
        The number limiting the sequence of prime numbers

    Returns
    -------
    int
        prime number by inputted number
    """

    def wrapper(func: Callable):
        @functools.wraps(func)
        def inner(n: int) -> int:
            if n < 1:
                raise ValueError("Number of prime number must be greater than 0")
            g = func(stopnumber)
            try:
                for i in range(n - 1):
                    next(g)
                return next(g)
            except Exception:
                raise ValueError(
                    "Number of prime number must be into generated sequence of prime numbers"
                )

        return inner

    return wrapper


def prime_seq_gen(stopnumber: int) -> Generator:
    """
    A function that generates sequence of prime numbers before inputted number

    Parameters
    ----------
    stopnumber: int
        The number limiting the sequence of prime numbers

    Returns
    -------
    Generator
        Sequence of prime numbers
    """
    if stopnumber < 2:
        raise ValueError("stopnumber must be greater than 1")
    prime_numbers = [2]
    yield 2
    for n in range(3, stopnumber + 1):
        is_prime = True
        for p in prime_numbers:
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(n)
            yield n
