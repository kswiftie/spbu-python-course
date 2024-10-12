import functools
from typing import Callable


def curry_explicit(function: Callable, arity: int) -> Callable:
    """
    Decorator for converting a function from multiple parameters into a composition of functions

    Parameters
    ----------
    function: Callable
        Function to be curried

    arity: int
        Arity of function

    Returns
    -------
    function: Callable
        Composition of functions
    """

    if arity < 0:
        raise ValueError("Arity cannot be negative")

    if arity == 0:
        return function

    args = []

    @functools.wraps(function)
    def curried(arg):
        nonlocal args
        args.append(arg)
        if len(args) > arity:
            args = []
            raise ValueError("Too many arguments")
        if len(args) == arity:
            tmp = args
            args = []
            return function(*tmp)
        return lambda more_args: curried(more_args)

    return curried


def uncurry_explicit(function: Callable, arity) -> Callable:
    """
        Decorator for converting a composition of functions into a function of several parameters

        Parameters
        ----------
        function: Callable
            Function to be uncurried

        arity: int
            Arity of function to be maded
            This argument must correspond to the number of compositions

        Returns
        -------
        res: Callable
            Functions of several parameters

        """
    if arity < 0:
        raise ValueError("Arity cannot be negative")

    if arity == 0:
        return function

    @functools.wraps(function)
    def uncurried(*args):
        if len(args) < arity:
            raise ValueError("Not enough arguments passed")

        res = function
        for i in range(len(args)):  # deploying functions
            try:
                res = res(args[i])
            except TypeError:
                raise ValueError("Too many arguments")
        return res

    return uncurried
