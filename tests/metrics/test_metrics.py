# -*- coding: utf-8 -*-

import os

from metalmetrics.config.config import Config
from metalmetrics.metrics.metrics import Metrics, MetricsException


def test_exception():
    exception = MetricsException("exception")
    assert str(exception) == "exception"


def test_metrics():
    try:
        _ = Metrics(None)
    except MetricsException as _:
        assert True
    else:
        assert False

    config = Config()
    config.config_file = os.path.join(os.path.dirname(__file__), "../data/config.yml")

    try:
        metrics = Metrics(config)
    except MetricsException as _:
        assert False
    else:
        assert True

    assert metrics._instance() is not None

    try:
        buf = metrics.routine(host=None, spec=None)
    except MetricsException as _:
        assert False
    else:
        assert True

    assert buf is not None

    try:
        buf = metrics.routine(host="foo", spec=None)
    except MetricsException as _:
        assert False
    else:
        assert True

    assert buf is not None
    assert len(buf.keys()) == 0

    try:
        buf = metrics.routine(host="bare", spec=None)
    except MetricsException as _:
        assert False
    else:
        assert True

    assert buf["bare"] is not None

    try:
        buf = metrics.routine(host="bare", spec="foo")
    except MetricsException as _:
        assert False
    else:
        assert True

    assert buf["bare"]["foo"] is None

    try:
        buf = metrics.routine(host="bare", spec="cpu")
    except MetricsException as _:
        assert False
    else:
        assert True

    assert buf["bare"]["cpu"] is not None
