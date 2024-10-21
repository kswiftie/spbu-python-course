import pytest, threading, time
from project.threadpool import Threadpool
from utils import wait_signal, waste_time, remember_inputs


@pytest.mark.parametrize(
    "threadpool_model, funcs, args, tasks_to_end, number_tasks, number_threads",
    [
        (
            Threadpool(5),
            [wait_signal for _ in range(5)],
            [threading.Event() for _ in range(5)],
            [],
            0,
            5,
        ),
        (
            Threadpool(5),
            [wait_signal for _ in range(7)],
            [threading.Event() for _ in range(7)],
            [],
            2,
            5,
        ),
        (Threadpool(6), [], [], [], 0, 6),
        (
            Threadpool(4),
            [wait_signal for _ in range(2)],
            [threading.Event() for _ in range(2)],
            [],
            0,
            4,
        ),
        (
            Threadpool(5),
            [wait_signal for _ in range(7)],
            [threading.Event() for _ in range(7)],
            [3],
            1,
            5,
        ),
        (
            Threadpool(5),
            [wait_signal for _ in range(12)],
            [threading.Event() for _ in range(12)],
            [3],
            6,
            5,
        ),
        (
            Threadpool(5),
            [wait_signal for _ in range(12)],
            [threading.Event() for _ in range(12)],
            list(range(7)),
            0,
            5,
        ),
        (
            Threadpool(5),
            [wait_signal for _ in range(12)],
            [threading.Event() for _ in range(12)],
            list(range(4)),
            3,
            5,
        ),
    ],
)
def test_enqueue(
    threadpool_model, funcs, args, tasks_to_end, number_tasks, number_threads
):
    for i in range(len(funcs)):
        threadpool_model.enqueue(funcs[i], args[i])

    for id in tasks_to_end:
        args[id].set()

    time.sleep(0.05)
    tasks_count = len(threadpool_model.tasks)
    thread_count = len([x for x in threadpool_model.threads if x.is_alive()])
    for i in range(len(funcs)):
        args[i].set()

    threadpool_model.dispose()
    assert thread_count == number_threads and tasks_count == number_tasks


@pytest.mark.parametrize(
    "threadpool_model, funcs, number_tasks, number_threads",
    [
        (Threadpool(5), [waste_time for _ in range(5)], 0, 0),
        (Threadpool(5), [waste_time for _ in range(7)], 0, 0),
        (Threadpool(5), [waste_time for _ in range(3)], 0, 0),
        (Threadpool(5), [waste_time for _ in range(1)], 0, 0),
        (Threadpool(5), [], 0, 0),
    ],
)
def test_dispose(threadpool_model, funcs, number_tasks, number_threads):
    for func in funcs:
        threadpool_model.enqueue(func)

    threadpool_model.dispose()
    time.sleep(0.05)
    tasks_count = len(threadpool_model.tasks)
    thread_count = len([x for x in threadpool_model.threads if x.is_alive()])

    assert thread_count == number_threads and tasks_count == number_tasks


@pytest.mark.parametrize(
    "threadpool_model, func, inputs, expected",
    [
        (Threadpool(1), remember_inputs, [{1}], {1}),
        (Threadpool(3), remember_inputs, [{1}, {2}, {3}], {1, 2, 3}),
        (Threadpool(4), remember_inputs, [{1}, {3}, {5}, {4}, {2}], set(range(1, 6))),
        (
            Threadpool(8),
            remember_inputs,
            [{1, 5, 4}, {3, 2}, {5, 7}, {4, 6, 0}, {3, 9, 8}],
            set(range(10)),
        ),
    ],
)
def test_runner(threadpool_model, func, inputs, expected):
    to_remember = set()
    for inp in inputs:
        threadpool_model.enqueue(func, inp, st=to_remember)

    threadpool_model.dispose()
    assert to_remember == expected


@pytest.mark.parametrize(
    "threadpool_model, func",
    [
        (Threadpool(1), lambda x: x**2),
        (Threadpool(3), print),
        (Threadpool(5), [waste_time for _ in range(3)]),
    ],
)
def test_enquence_after_dispose(threadpool_model, func):
    threadpool_model.dispose()
    try:
        threadpool_model.enqueue(func)
        assert False
    except TypeError:
        assert True
