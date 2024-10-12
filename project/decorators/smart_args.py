import functools, inspect, copy
from typing import Callable
from project.decorators.Evaluated import Evaluated
from project.decorators.Isolated import Isolated


def smart_args(func: Callable) -> Callable:
    """
    A decorator that allows you to work with variables by default of the Evaluate and Isolated types

    Parameters
    ----------
    func: Callable
        The function to be processed

    Returns
    -------
    function_result: Any
        The result of processed function
    """

    func_signature = inspect.signature(func)  # function signature

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for name, param in func_signature.parameters.items():
            if isinstance(param.default, Evaluated):
                if name not in kwargs:
                    if param.default.func == Isolated:
                        raise ValueError("Isolated cannot be passed to Evaluated")
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
