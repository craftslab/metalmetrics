# -*- coding: utf-8 -*-

from metalmetrics.config.config import ConfigFile


class ServiceException(Exception):
    def __init__(self, info):
        super().__init__(self)
        self._info = info

    def __str__(self):
        return self._info


class Service(object):
    def __init__(self, config):
        if config is None:
            raise ServiceException("config invalid")
        self._config = config
