# -*- coding: utf-8 -*-

from metalmetrics.metrics.container import ContainerException


def test_exception():
    exception = ContainerException("exception")
    assert str(exception) == "exception"


def test_container():
    assert True
