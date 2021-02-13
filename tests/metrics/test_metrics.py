# -*- coding: utf-8 -*-

import os

from metalmetrics.config.config import Config
from metalmetrics.metrics.metrics import Metrics, MetricsException
from metalmetrics.proto.proto import Format


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
    config.output_file = "output.json"

    try:
        metrics = Metrics(config)
    except MetricsException as _:
        assert False
    else:
        assert True

    assert metrics._instance() is not None

    try:
        buf = metrics.routine()
    except MetricsException as _:
        assert False
    else:
        assert True

    assert buf is not None

    try:
        buf = metrics.routine(Format.CPU)
    except MetricsException as _:
        assert False
    else:
        assert True

    assert buf is not None
    assert buf["bare"] is not None
    assert buf["bare"][Format.CPU] is not None

    assert os.path.isfile(config.output_file)
    os.remove(config.output_file)
