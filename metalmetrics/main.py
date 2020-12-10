# -*- coding: utf-8 -*-

import sys

from metalmetrics.cmd.argument import Argument
from metalmetrics.cmd.banner import BANNER
from metalmetrics.config.config import Config, ConfigException
from metalmetrics.logger.logger import Logger
from metalmetrics.metrics.metrics import Metrics, MetricsException
from metalmetrics.queue.queue import Queue, QueueException
from metalmetrics.service.service import Service, ServiceException


def main():
    print(BANNER)

    argument = Argument()
    arg = argument.parse(sys.argv)

    try:
        config = Config()
        config.config_file = arg.config_file
        config.grpc_host = arg.grpc_host
        config.grpc_port = arg.grpc_port
        config.output_file = arg.output_file
    except ConfigException as e:
        Logger.error(str(e))
        return -1

    try:
        metrics = Metrics(config)
    except MetricsException as e:
        Logger.error(str(e))
        return -2

    Logger.info("metrics running")

    try:
        queue = Queue(config)
        queue.run(metrics.routine, [])
    except QueueException as e:
        Logger.error(str(e))
        return -3

    Logger.info("metrics exiting")

    return 0
