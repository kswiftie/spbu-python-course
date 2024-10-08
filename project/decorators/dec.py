import functools, random, inspect, copy
from collections import OrderedDict
from logging import exception


def curry_explicit(function, arity: int):
    """
    Decorator for converting a function from multiple parameters into a composition of functions

    Parameters
    ----------
    function
        Function to be curried

    arity: int
        Arity of function

    Returns
    -------
    function
        Composition of functions

    """

    if arity < 0:
        raise ValueError("Arity cannot be negative")

    args_seen = 1  # count of args we`ve already got

    @functools.wraps(function)
    def curried(*args):
        nonlocal args_seen
        if len(args) > args_seen or len(args) > arity:
            raise ValueError("Too many arguments")

        if len(args) == arity:
            args_seen = 0
            try:
                return function(*args)
            except TypeError: # if arity < function required args
                raise ValueError("Incorrect arity entered")

        args_seen += 1
        return lambda *more_args: curried(*(args + more_args))

    return curried


def uncurry_explicit(function, arity):
    """
        Decorator for converting a composition of functions into a function of several parameters

        Parameters
        ----------
        function
            Function to be uncurried

        arity: int
            Arity of function to be maded
            This argument must correspond to the number of compositions

        Returns
        -------
        function
            Functions of several parameters

        """
    if arity < 0:
        raise ValueError("Arity cannot be negative")

    @functools.wraps(function)
    def uncurried(*args):
        res = function()
        for i in range(len(args)):
            try:
                res = res(args[i])
            except TypeError:
                raise ValueError("Too many arguments")
        return res

    return uncurried


def memoize(max_cashed_args: int = 0):
    # todo: add description and exceptions and rename variables
    # todo: stop store duplicate results
    # todo: i think this dec isnt supposed to return all last values so fix it
    def decorator(func):
        cashe = OrderedDict()

        @functools.wraps(func)
        def cash_function(*args, **kwargs):
            if max_cashed_args == 0:  # maybe this have written bad
                return func(*args, **kwargs)
            key = str(args) + str(kwargs)  # unique key for input values
            cashe[key] = func(*args, **kwargs)
            if key in cashe:
                cashe.move_to_end(key)
            if len(cashe) > max_cashed_args:  # elif should be here i guess
                cashe.popitem(last=False)
            return cashe[key]

        return cash_function

    return decorator


def smart_args(func):
    def wrapper(*args, **kwargs):
        func_signature = inspect.signature(func)  # function signature
        for name, param in func_signature.parameters.items():
            if isinstance(param.default, Evaluated):
                kwargs[name] = param.default.evaluate()
            elif isinstance(param.default, Isolated):
                if name in kwargs:
                    kwargs[name] = copy.deepcopy(kwargs[name])
                else:
                    raise ValueError(
                        f"Argument '{name}' must be provided when using Isolated."
                    )
        return func(*args, **kwargs)

    return wrapper
