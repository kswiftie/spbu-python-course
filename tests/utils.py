from project.decorators import Isolated, Evaluated, smart_args
import time


def mysum(*args):
    return sum(args)


def check_isolation(*, d=Isolated()):
    d["a"] = 0
    return d


def check_evaluation(*, x=time.time(), y=Evaluated(time.time)):
    time.sleep(0.4)
    return (x, y)
