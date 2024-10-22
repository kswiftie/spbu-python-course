from ast import Index

import numpy as np
from collections import deque
from threading import Thread, Event
from typing import Callable, List, Dict, Any

DEQTYPE = deque[Any]


class Threadpool:
    """
    A class for working with threads.
    """

    def __init__(self, num_threads: int) -> None:
        """
        The initializer of the class.
        num_threads is accepted as input, which
        will tell the class how many threads to create for processing tasks

        Parameters
        ----------
        num_threads: int
            Function to be curried
        """
        self.num_threads = num_threads
        self.threads = np.empty(num_threads, dtype=object)
        self.tasks: DEQTYPE = deque()
        self.event = Event()  # To signal the arrival of tasks
        self.is_threads_closed = False
        for i in range(num_threads):  # Run threads
            self.threads[i] = Thread(target=self.runner)
            self.threads[i].start()

    def runner(self) -> None:
        """
        A function for performing tasks in different threads.
        When initializing the class, it runs in a separate thread and
        waits for self.event to become True and
        for tasks to appear in self.tasks


        """
        self.event.wait()
        while self.tasks:
            task, args, kwargs = self.tasks.popleft()
            result = task(*args, **kwargs)
        self.event.clear()

    def enqueue(
        self, task: Callable, *args: List[Any], **kwargs: Dict[Any, Any]
    ) -> None:
        """
        The function of adding tasks for processing

        Parameters
        ----------
        task: Callable
            A function that needs to be executed in a separate thread

        args: List
            Function args

        kwargs: Dict
            function kwargs

        """
        if self.is_threads_closed:
            raise TypeError("Pool is closed")
        self.tasks.append((task, args, kwargs))
        self.event.set()

    def dispose(self) -> None:
        """
        The function of stopping processes.
        After starting, new processes stop being added, and
        waiting for the completion of already running tasks begins
        """
        self.is_threads_closed = True
        self.event.set()
        for thread in self.threads:
            thread.join()
