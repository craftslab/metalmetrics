# -*- coding: utf-8 -*-

from metalmetrics.config.config import ConfigFile, Spec
from metalmetrics.metrics.abstract import MetricsAbstract, MetricsAbstractException


class BareException(MetricsAbstractException):
    def __init__(self, info):
        super().__init__(self)
        self._info = info

    def __str__(self):
        return self._info


class Bare(MetricsAbstract):
    def __init__(self, config):
        super().__init__(config)
        buf = self._config.config_file.get(ConfigFile.SPEC, None)
        if buf is None:
            raise BareException("spec invalid")
        self._spec = buf.get("bare", [])
        self._impl = {
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

    def _execution(self, spec):
        buf = {}
        if spec is not None and isinstance(spec, str):
            buf = self._impl.get(spec, None)
        else:
            for key in self._impl.keys():
                if key in self._spec:
                    buf[key] = self._impl[key]
        return buf

    @staticmethod
    def _cpu():
        return "1CPU"

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
