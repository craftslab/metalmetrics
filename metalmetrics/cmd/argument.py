# -*- coding: utf-8 -*-

import argparse

from ..__version__ import __version__


class Argument(object):
    def __init__(self):
        self._parser = argparse.ArgumentParser(description="Metal Metrics")
        self._add()

    def _add(self):
        self._parser.add_argument(
            "-c",
            "--config-file",
            action="store",
            dest="config_file",
            help="config file",
            required=True,
        )
        self._parser.add_argument(
            "-o",
            "--output-file",
            action="store",
            default="",
            dest="output_file",
            help="output file (.json|.txt|.xlsx)",
            required=False,
        )
        self._parser.add_argument(
            "-v", "--version", action="version", version=__version__
        )

    def parse(self, argv):
        return self._parser.parse_args(argv[1:])