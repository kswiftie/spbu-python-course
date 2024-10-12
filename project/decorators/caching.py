import functools
from collections import OrderedDict
from typing import Callable, Any


def memoize(*, max_cached_args: int = 0, show_cache: bool = False) -> Any:
    """
    A decorator that allows you to remember the latest results of the function

    Parameters
    ----------
    max_cached_args: int
        Count of args to be memorized

    show_cache: bool
        If True, the function will return all cached results

    Returns
    -------
    Result(s) of function: Any
        The result or cached results of the function
    """
    if max_cached_args < 0:
        raise ValueError("max_cachehd_args cannot be negative")

    def cache_decorator(func):
        cache = OrderedDict()

        @functools.wraps(func)
        def cache_function(*args, **kwargs):
            if max_cached_args == 0:  # maybe this have written bad
                return func(*args, **kwargs)

            key = str(args) + str(kwargs)  # unique key for input values
            if key in cache:
                cache.move_to_end(key)
            else:
                cache[key] = func(*args, **kwargs)
                if len(cache) > max_cached_args:
                    cache.popitem(last=False)

            return cache[key] if not show_cache else [x for x in cache.values()]

        return cache_function

    return cache_decorator
