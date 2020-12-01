# -*- coding: utf-8 -*-

import sys

from metalmetrics.cmd.argument import Argument
from metalmetrics.cmd.banner import BANNER
from metalmetrics.config.config import Config, ConfigException
from metalmetrics.logger.logger import Logger
from metalmetrics.metrics.metrics import Metrics, MetricsException
from metalmetrics.runtime.runtime import Runtime, RuntimeException


def main():
    print(BANNER)

    argument = Argument()
    arg = argument.parse(sys.argv)

    try:
        config = Config()
        config.config_file = arg.config_file
        config.output_file = arg.output_file
    except ConfigException as e:
        Logger.error(str(e))
        return -1

    try:
        metrics = Metrics(config)
    except MetricsException as e:
        Logger.error(str(e))
        return -2

    Logger.info("metalmetrics running")

    try:
        runtime = Runtime(config)
        runtime.run(metrics.routine, [])
    except RuntimeException as e:
        Logger.error(str(e))
        return -3

    Logger.info("metalmetrics exiting")

    return 0
