from project.decorators import Isolated, Evaluated
from threading import Event
import time


def mysum(*args):
    return sum(args)


def check_isolation(a=None, d=Isolated(), l=Isolated()):
    a = 2
    for x in d:
        d[x] = x
    l.clear()


def check_evaluation(s=None, x=time.time(), y=Evaluated(time.time)):
    time.sleep(0.1)
    return (s, x, y)


def check_evaluation_with_isolation(s=None, d=Isolated(), y=Evaluated(time.time)):
    time.sleep(0.1)
    for x in d:
        d[x] = x
    return (s, y)


def waste_time():
    time.sleep(0.01)


def wait_signal(event):
    event.wait()
    time.sleep(0.01)


def remember_inputs(inp, st=set()):
    for x in inp:
        st.add(x)


def get_function_execution_time(function, *args, **kwargs):
    start = time.time()
    function(*args, **kwargs)
    end = time.time()
    return end - start