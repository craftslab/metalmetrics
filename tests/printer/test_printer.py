# -*- coding: utf-8 -*-

import os

from metalmetrics.config.config import Spec
from metalmetrics.printer.printer import Printer, PrinterException


def test_exception():
    exception = PrinterException("exception")
    assert str(exception) == "exception"


def test_printer():
    buf = {
        "bare": {
            Spec.CPU: "1CPU",
            Spec.DISK: "10TB HDD",
            Spec.IO: "10.0kB_read/s,10.0kB_wrtn/s",
            Spec.IP: "127.0.0.1",
            Spec.KERNEL: "5.4.0-54-generic",
            Spec.MAC: "01:02:03:04:05:06",
            Spec.NETWORK: "10Mbps",
            Spec.OS: "18.04.1-Ubuntu",
            Spec.RAM: "8GB",
            Spec.SYSTEM: "System Information",
        }
    }

    printer = Printer()

    name = "printer.json"
    printer.run(data=buf, name=name, append=False)
    assert os.path.isfile(name)
    os.remove(name)

    name = "printer.txt"
    printer.run(data=buf, name=name, append=False)
    assert os.path.isfile(name)
    os.remove(name)

    name = "printer.xlsx"
    printer.run(data=buf, name=name, append=False)
    assert os.path.isfile(name)
    os.remove(name)
