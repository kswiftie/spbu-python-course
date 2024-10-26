import random
from typing import Tuple


def get_random_seq(n: int, a: int, b: int) -> tuple[int, ...]:
    """
    A function that generates a random sequence on a specified segment

    Parameters
    ----------
    n: int
        The length of the generated sequence

    a: int
        Min value in sequence

    b: int
        Max value in sequence


    Returns
    -------
    tuple[...]
        The requested sequence

    """

    if n > b - a:
        raise ValueError("the length of the sequence cannot be"
                         "longer than the length of the specified segment")

    root_number = random.randint(a, b)
    to_add_left = (n - 1) // 2
    to_add_right = n // 2
    if root_number - to_add_left < a:
        tmp = a - root_number + to_add_left
        to_add_right += tmp
        to_add_left -= tmp
    elif root_number + to_add_right > b:
        tmp = root_number + to_add_right - b
        to_add_left += tmp
        to_add_right -= tmp

    return tuple([x for x in range(root_number - to_add_left, root_number)] + [x for x in range(root_number,
                                                                                                root_number + to_add_right + 1)])
