# -*- coding: utf-8 -*-

import queue

from metalmetrics.runtime.runtime import Runtime, RuntimeException
from metalmetrics.runtime.runtime import Worker, WorkerException


def routine():
    pass


def test_runtimeexception():
    exception = RuntimeException("exception")
    assert str(exception) == "exception"


def test_runtime():
    try:
        runtime = Runtime(None)
    except RuntimeException as _:
        assert False
    else:
        assert True

    args = "event"

    try:
        runtime.run(routine, args)
    except RuntimeException as _:
        assert False
    else:
        assert True


def test_workerexception():
    exception = WorkerException("exception")
    assert str(exception) == "exception"


def test_worker():
    _queue = queue.Queue(1)
    _queue.put((routine, "routine"))

    try:
        _ = Worker(_queue=_queue)
    except WorkerException as _:
        assert False
    else:
        assert True
