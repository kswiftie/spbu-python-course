from typing import List, Set
from itertools import product
import concurrent.futures


def sum_of_part(pairlist_part: List[tuple[int]]) -> int:
    """
    This function calculates the sum of an array of pairs of integers
    Parameters
    ----------
    pairlist_part: List[int]
        Inputted list of pairs of integers

    Returns
    -------
    Result: int
        Sum of given list
    """
    return sum(sum(x) for x in pairlist_part)


def cartesian_sum(inp_set: Set[int], cores_number: int) -> int:
    """
    This function receives a set of integers as input and
    calculates the sum of its Cartesian product by itself

    Parameters
    ----------
    inp_set: Set[int]
        The set of integers

    cores_number: int
        The number of cores that can be used.

    Returns
    -------
    Result: int
        Sum of given set
    """

    if cores_number == 0:
        raise ValueError("cores_number cannot be negative")
    cartesian_set = list(product(inp_set, repeat=2))
    pairs_count = len(cartesian_set)

    set_size = max(1, pairs_count // cores_number)

    pairlist_parts = [
        cartesian_set[i : i + set_size] for i in range(0, pairs_count, set_size)
    ]

    with concurrent.futures.ProcessPoolExecutor(max_workers=cores_number) as executor:
        results = list(
            executor.map(sum_of_part, pairlist_parts)
        )  # Используем map для получения результатов

    return sum(results)
