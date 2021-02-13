# -*- coding: utf-8 -*-

from metalmetrics.config.config import Config
from metalmetrics.metrics.abstract import MetricsAbstract
from metalmetrics.proto.proto import Format


def test_metricsabstract():
    class MetricsTest(MetricsAbstract):
        def __init__(self, config):
            super().__init__(config)

        def _execution(self, _):
            return {Format.CPU: "1 CPU"}

    config = Config()
    metrics = MetricsTest(config)

    result = metrics.run(Format.CPU)
    assert result is not None
