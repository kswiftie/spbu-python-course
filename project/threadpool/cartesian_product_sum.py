from typing import List, Set
import concurrent.futures, itertools


def sum_pairs(pairs_list: List[tuple[int, ...]], start: int, end: int) -> int:
    """
    This function calculates the sum of an array of pairs of integers
    Parameters
    ----------
    pairlist_part: List[int]
        Inputted list of pairs of integers
    start: int
        start of interval to be added to sum
    end: int
        end of interval to be added to sum
    Returns
    -------
    Result: int
        Sum of given list
    """
    res = 0
    for i in range(start, end):
        res += pairs_list[i][0] + pairs_list[i][1]
    return res


def cartesian_sum(inp_set: Set[int], num_threads: int) -> int:
    """
    This function receives a set of integers as input and
    calculates the sum of its Cartesian product by itself
    Parameters
    ----------
    inp_set: Set[int]
        The set of integers
    num_threads: int
        The number of threads that can be used.
    Returns
    -------
    Result: int
        Sum of cartesian product of given set
    """

    if num_threads == 0:
        raise ValueError("num_threads cannot be negative")

    if not inp_set:
        return 0

    pairs = list(itertools.product(inp_set, repeat=2))
    n = len(pairs)

    num_threads = min(n, num_threads)

    step = (n + num_threads - 1) // num_threads

    results = []

    with concurrent.futures.ProcessPoolExecutor(max_workers=num_threads) as executor:
        futures = []
        for i in range(num_threads):
            start = i * step
            end = min(start + step, n)
            futures.append(executor.submit(sum_pairs, pairs, start, end))

        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())

    return sum(results)
