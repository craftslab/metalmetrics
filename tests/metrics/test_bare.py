# -*- coding: utf-8 -*-

import os

from metalmetrics.config.config import Config
from metalmetrics.metrics.bare import Bare, BareException


def test_exception():
    exception = BareException("exception")
    assert str(exception) == "exception"


def test_bare():
    config = Config()
    config.inxi_file = os.path.join(os.path.dirname(__file__), "../data/inxi")
    config.config_file = os.path.join(os.path.dirname(__file__), "../data/config.yml")

    try:
        bare = Bare(config)
        _exec = bare._execution()
    except BareException as _:
        assert False
    else:
        assert True

    assert _exec is not None

    buf = bare._popen(["ls"])
    assert buf is not None

    buf = bare._cpu()
    print(buf)
    assert len(buf) != 0

    buf = bare._disk()
    print(buf)
    assert len(buf) != 0

    buf = bare._io()
    print(buf)
    assert len(buf) != 0

    buf = bare._ip()
    print(buf)
    assert len(buf) != 0

    buf = bare._kernel()
    print(buf)
    assert len(buf) != 0

    buf = bare._mac()
    print(buf)
    assert len(buf) != 0

    buf = bare._network()
    print(buf)
    assert len(buf) != 0

    buf = bare._os()
    print(buf)
    assert len(buf) != 0

    buf = bare._ram()
    print(buf)
    assert len(buf) != 0

    buf = bare._system()
    print(buf)
    assert len(buf) != 0
