# -*- coding: utf-8 -*-

import os

from metalmetrics.config.config import Config
from metalmetrics.service.service import Service, ServiceException


def test_exception():
    exception = ServiceException("exception")
    assert str(exception) == "exception"


def test_service():
    try:
        _ = Service(None)
    except ServiceException as _:
        assert True
    else:
        assert False

    config = Config()
    config.config_file = os.path.join(os.path.dirname(__file__), "../data/config.yml")

    try:
        _ = Service(config)
    except ServiceException as _:
        assert False
    else:
        assert True
