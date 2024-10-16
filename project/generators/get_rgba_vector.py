import functools
from typing import Generator, Callable


def rgba_vector() -> Generator:
    """
    Function that returns an RGBA vector generator

    Returns
    -------
    Generator
        Generator of RGBA vectors
    """
    for b in range(256):
        for g in range(256):
            for r in range(256):
                for a in range(0, 101, 2):
                    yield (r, g, b, a)


def get_rgba_vector(func: Callable):
    """
    A decorator that returns a vector by its number

    Parameters
    ----------
    func: Callable
        RGBA vector Generator

    Returns
    -------
    tuple[int, int, int, int]
        RGBA vector
    """

    @functools.wraps(func)
    def generator_handler(i: int) -> tuple[int, int, int, int]:
        generator = func()
        try:
            for _ in range(i):
                next(generator)
            return next(generator)
        except Exception:
            raise ValueError("RGBA vector with such number does not exist")

    return generator_handler
