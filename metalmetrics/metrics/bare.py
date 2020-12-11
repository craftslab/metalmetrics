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
            Spec.RAM: self._ram(),
        }

    def _execution(self):
        return self._exec

    @staticmethod
    def _cpu():
        cmd = "awk -F: '/model name/ {core++} END {print core}' /proc/cpuinfo"
        proc = subprocess.Popen(
            cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, _ = proc.communicate()
        if proc.returncode != 0:
            return "invalid"
        return "%s CPU" % out.strip().decode("utf-8")

    @staticmethod
    def _disk():
        def _helper(cmd, stdin, stdout):
            return subprocess.Popen(
                cmd.split(), stdin=stdin, stdout=stdout, stderr=subprocess.PIPE
            )

        cmd = "df -hPl"
        df = _helper(cmd=cmd, stdin=None, stdout=subprocess.PIPE)
        cmd = (
            "grep -wvE '\\-|none|tmpfs|devtmpfs|by-uuid|chroot|Filesystem|udev|docker'"
        )
        grep = _helper(cmd=cmd, stdin=df.stdout, stdout=subprocess.PIPE)
        cmd = "awk '{print $2}'"
        proc = _helper(cmd=cmd, stdin=grep.stdout, stdout=subprocess.PIPE)
        total, _ = proc.communicate()
        if proc.returncode != 0:
            return "invalid"
        cmd = "awk '{print $3}'"
        proc = _helper(cmd=cmd, stdin=grep.stdout, stdout=subprocess.PIPE)
        used, _ = proc.communicate()
        if proc.returncode != 0:
            return "invalid"
        return "%s GB (%s GB Used)" % (
            total.strip().decode("utf-8"),
            used.strip().decode("utf-8"),
        )

    @staticmethod
    def _io():
        return "10.0kB_read/s,10.0kB_wrtn/s"

    @staticmethod
    def _ip():
        return "127.0.0.1"

    @staticmethod
    def _kernel():
        cmd = "uname -r"
        proc = subprocess.Popen(
            cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, _ = proc.communicate()
        if proc.returncode != 0:
            return "invalid"
        return out.strip().decode("utf-8")

    @staticmethod
    def _mac():
        return "01:02:03:04:05:06"

    @staticmethod
    def _network():
        return "10Mbps"

    @staticmethod
    def _os():
        cmd = """awk -F'[= "]' '/PRETTY_NAME/{print $3,$4,$5}' /etc/os-release"""
        proc = subprocess.Popen(
            cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, _ = proc.communicate()
        if proc.returncode != 0:
            return "invalid"
        return out.strip().decode("utf-8")

    @staticmethod
    def _ram():
        return "8GB"
