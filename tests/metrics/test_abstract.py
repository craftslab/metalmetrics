# -*- coding: utf-8 -*-

from metalmetrics.config.config import Config
from metalmetrics.metrics.abstract import MetricsAbstract, MetricsAbstractException


def test_exception():
    exception = MetricsAbstractException("exception")
    assert str(exception) == "exception"


def test_metricsabstract():
    class MetricsTest1(MetricsAbstract):
        def __init__(self, config):
            super().__init__(config)

        def _execution(self):
            return "_execution"

    config = Config()

    metrics = MetricsTest1(config)
    result = metrics.run()
    assert result is not None

    class MetricsTest2(MetricsAbstract):
        def __init__(self, config):
            super().__init__(config)

        def _execution(self):
            raise MetricsAbstractException("exception")

    metrics = MetricsTest2(config)
    result = metrics.run()
    assert result is None
