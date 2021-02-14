# -*- coding: utf-8 -*-

import os

from metalmetrics.printer.printer import Printer, PrinterException
from metalmetrics.proto.proto import Format


def test_exception():
    exception = PrinterException("exception")
    assert str(exception) == "exception"


def test_printer():
    buf = {
        "metrics": {
            Format.CPU: "1 CPU",
            Format.DISK: "10TB HDD",
            Format.IO: "10.0kB_read/s,10.0kB_wrtn/s",
            Format.IP: "127.0.0.1",
            Format.KERNEL: "5.4.0-54-generic",
            Format.MAC: "01:02:03:04:05:06",
            Format.NETWORK: "10Mbps",
            Format.OS: "18.04.1-Ubuntu",
            Format.RAM: "8GB",
            Format.SYSTEM: "System Information",
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
