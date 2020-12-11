# -*- coding: utf-8 -*-

import subprocess

from metalmetrics.config.config import Spec
from metalmetrics.metrics.abstract import MetricsAbstract


class BareException(Exception):
    def __init__(self, info):
        super().__init__(self)
        self._info = info

    def __str__(self):
        return self._info


class Bare(MetricsAbstract):
    def __init__(self, config):
        super().__init__(config)
        self._exec = {
            Spec.CPU: self._cpu(),
            Spec.DISK: self._disk(),
            Spec.IO: self._io(),
            Spec.IP: self._ip(),
            Spec.KERNEL: self._kernel(),
            Spec.MAC: self._mac(),
            Spec.NETWORK: self._network(),
            Spec.OS: self._os(),
            Spec.PROCESS: self._process(),
            Spec.RAM: self._ram(),
            Spec.SSH: self._ssh(),
        }

    def _execution(self):
        return self._exec

    @staticmethod
    def _cpu():
        cmd = "awk -F: '/model name/ {core++} END {print core}' /proc/cpuinfo"
        proc = subprocess.Popen(
            cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, err = proc.communicate()
        if proc.returncode != 0:
            return "invalid"
        return "%sCPU" % out.strip().decode("utf-8")

    @staticmethod
    def _disk():
        return "10TB HDD"

    @staticmethod
    def _io():
        return "10.0kB_read/s,10.0kB_wrtn/s"

    @staticmethod
    def _ip():
        return "127.0.0.1"

    @staticmethod
    def _kernel():
        return "5.4.0-54-generic"

    @staticmethod
    def _mac():
        return "01:02:03:04:05:06"

    @staticmethod
    def _network():
        return "10Mbps"

    @staticmethod
    def _os():
        return "18.04.1-Ubuntu"

    @staticmethod
    def _process():
        return "10"

    @staticmethod
    def _ram():
        return "8GB"

    @staticmethod
    def _ssh():
        return "20"
