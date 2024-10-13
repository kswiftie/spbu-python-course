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
    argsinfo = inspect.getfullargspec(func)

    argsln = len(argsinfo.args) if argsinfo.args else 0
    defaultsln = len(argsinfo.defaults) if argsinfo.defaults else 0
    po = argsln - defaultsln

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        cur_arg, argsln = 0, len(args)
        for name, param in func_signature.parameters.items():
            if isinstance(param.default, Evaluated):
                if name not in kwargs:
                    if param.default.func is Isolated:
                        raise ValueError("Isolated cannot be passed to Evaluated")
                    elif argsln > cur_arg:
                        kwargs[name] = args[cur_arg]
                    else:
                        kwargs[name] = param.default.evaluate()

            elif isinstance(param.default, Isolated):
                if name in kwargs:
                    kwargs[name] = copy.deepcopy(kwargs[name])
                elif argsln > cur_arg:
                    kwargs[name] = copy.deepcopy(args[cur_arg])
                else:
                    raise ValueError(
                        f"Argument '{name}' must be inputed when using Isolated."
                    )
            cur_arg += 1
        return func(*args[:po], **kwargs)

    return wrapper
