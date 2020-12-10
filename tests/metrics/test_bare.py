# -*- coding: utf-8 -*-

import os

from metalmetrics.config.config import Config, Spec
from metalmetrics.metrics.bare import Bare, BareException


def test_exception():
    exception = BareException("exception")
    assert str(exception) == "exception"


def test_bare():
    config = Config()
    config.config_file = os.path.join(os.path.dirname(__file__), "../data/config.yml")

    try:
        bare = Bare(config)
        bare._impl = {Spec.CPU: bare._cpu()}
        ret = bare._execution("foo")
    except BareException as _:
        assert False
    else:
        assert True

    assert ret is None

    try:
        bare = Bare(config)
        bare._impl = {Spec.CPU: bare._cpu()}
        ret = bare._execution(Spec.CPU)
    except BareException as _:
        assert False
    else:
        assert True

    assert ret is not None

    try:
        bare = Bare(config)
        bare._impl = {Spec.CPU: bare._cpu()}
        bare._execution(None)
    except BareException as _:
        assert False
    else:
        assert True
