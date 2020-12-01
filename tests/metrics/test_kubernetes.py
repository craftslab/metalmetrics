# -*- coding: utf-8 -*-

from metalmetrics.metrics.kubernetes import KubernetesException


def test_exception():
    exception = KubernetesException("exception")
    assert str(exception) == "exception"


def test_kubernetes():
    assert True
