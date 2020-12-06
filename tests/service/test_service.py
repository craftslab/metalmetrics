# -*- coding: utf-8 -*-

from metalmetrics.config.config import ConfigFile
from metalmetrics.service.service import Service, ServiceException


def test_exception():
    exception = ServiceException("exception")
    assert str(exception) == "exception"


def test_service():
    assert True
