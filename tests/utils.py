from project.decorators import Isolated, Evaluated
import time


def mysum(*args):
    return sum(args)


def check_isolation(*, d=Isolated()):
    d["a"] = 0


def check_evaluation(*, x=time.time(), y=Evaluated(time.time)):
    time.sleep(0.4)
    return (x, y)


def check_isolation_posargs(a=None, s=Isolated(), l=Isolated()):
    s[0] = 2
    l[0] = 2


def check_evaluation_posargs(s=None, x=time.time(), y=Evaluated(time.time)):
    time.sleep(0.1)
    return (s, x, y)
