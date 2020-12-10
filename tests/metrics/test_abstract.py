# -*- coding: utf-8 -*-

from metalmetrics.config.config import Config
from metalmetrics.metrics.abstract import MetricsAbstract


def test_metricsabstract():
    class MetricsTest(MetricsAbstract):
        def __init__(self, config):
            super().__init__(config)

        def _execution(self):
            return {"cpu": "1CPU"}

    config = Config()
    metrics = MetricsTest(config)

    result = metrics.run("foo")
    assert result is None

    result = metrics.run("cpu")
    assert result is not None
