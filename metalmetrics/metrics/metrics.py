# -*- coding: utf-8 -*-

from metalmetrics.config.config import ConfigFile
from metalmetrics.metrics.bare import Bare
from metalmetrics.metrics.container import Container
from metalmetrics.metrics.kubernetes import Kubernetes
from metalmetrics.printer.printer import Printer


class MetricsException(Exception):
    def __init__(self, info):
        super().__init__(self)
        self._info = info

    def __str__(self):
        return self._info


class Metrics(object):
    def __init__(self, config):
        if config is None:
            raise MetricsException("config invalid")
        self._config = config

    def _dump(self, data):
        printer = Printer()
        printer.run(data=data, name=self._config.output_file, append=False)

    def _spec(self):
        spec = self._config.config_file.get(ConfigFile.SPEC, None)
        if spec is None:
            raise MetricsException("spec invalid")
        buf = {}
        if Bare.__name__.lower() in spec.keys():
            buf[Bare.__name__.lower()] = Bare(self._config)
        if Container.__name__.lower() in spec.keys():
            buf[Container.__name__.lower()] = Container(self._config)
        if Kubernetes.__name__.lower() in spec.keys():
            buf[Kubernetes.__name__.lower()] = Kubernetes(self._config)
        return buf

    def routine(self):
        result = {}
        for key, val in self._spec().items():
            buf = val.run()
            if buf is None:
                continue
            result[key] = buf
        if len(self._config.output_file) != 0:
            self._dump(result)
