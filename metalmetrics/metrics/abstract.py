# -*- coding: utf-8 -*-

import abc


class MetricsAbstractException(Exception):
    def __init__(self, info):
        super().__init__(self)
        self._info = info

    def __str__(self):
        return self._info


class MetricsAbstract(abc.ABC):
    def __init__(self, config):
        self._config = config

    @abc.abstractmethod
    def _execution(self):
        pass

    def run(self):
        try:
            result = self._execution()
        except MetricsAbstractException as _:
            result = None
        return result