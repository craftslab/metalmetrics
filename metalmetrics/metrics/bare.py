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

    def _popen(self, cmd, stdin=None):
        return subprocess.Popen(
            cmd, stdin=stdin, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

    def _cpu(self):
        """
        awk -F: '/model name/ {core++} END {print core}' /proc/cpuinfo
        """
        cmd = ["awk", "-F:", "/model name/ {core++} END {print core}", "/proc/cpuinfo"]
        proc = self._popen(cmd)
        out, _ = proc.communicate()
        if proc.returncode != 0:
            return "invalid"
        return "%s CPU" % out.strip().decode("utf-8")

    def _disk(self):
        """
        df -hPl | grep -wvE '\\-|none|tmpfs|devtmpfs|by-uuid|chroot|Filesystem|udev|docker' | awk '{print $2}'
        df -hPl | grep -wvE '\\-|none|tmpfs|devtmpfs|by-uuid|chroot|Filesystem|udev|docker' | awk '{print $3}'
        """

        def _helper(args):
            cmd = ["df", "-hPl"]
            df = self._popen(cmd=cmd)
            cmd = [
                "grep",
                "-wvE",
                "\\-|none|tmpfs|devtmpfs|by-uuid|chroot|Filesystem|udev|docker",
            ]
            grep = self._popen(cmd=cmd, stdin=df.stdout)
            cmd = ["awk", "{print %s}" % args]
            return self._popen(cmd=cmd, stdin=grep.stdout)

        proc = _helper("$2")
        total, _ = proc.communicate()
        if proc.returncode != 0:
            return "invalid"
        proc = _helper("$3")
        used, _ = proc.communicate()
        if proc.returncode != 0:
            return "invalid"
        return "%s GB (%s GB Used)" % (
            total.strip().decode("utf-8"),
            used.strip().decode("utf-8"),
        )

    def _io(self):
        return "10.0kB_read/s,10.0kB_wrtn/s"

    def _ip(self):
        return "127.0.0.1"

    def _kernel(self):
        """
        uname -r
        """
        cmd = ["uname", "-r"]
        proc = self._popen(cmd)
        out, _ = proc.communicate()
        if proc.returncode != 0:
            return "invalid"
        return out.strip().decode("utf-8")

    def _mac(self):
        return "01:02:03:04:05:06"

    def _network(self):
        return "10Mbps"

    def _os(self):
        """
        awk -F'[= "]' '/PRETTY_NAME/{print $3,$4,$5}' /etc/os-release
        """
        cmd = ["awk", '-F[= "]', "/PRETTY_NAME/{print $3,$4,$5}", "/etc/os-release"]
        proc = self._popen(cmd)
        out, _ = proc.communicate()
        if proc.returncode != 0:
            return "invalid"
        return out.strip().decode("utf-8")

    def _ram(self):
        """
        free -m | awk '/Mem/ {print $2}'
        free -m | awk '/Mem/ {print $3}'
        """

        cmd = ["free", "-m"]
        free = self._popen(cmd=cmd)
        cmd = ["awk", "/Mem/ {print $2}"]
        proc = self._popen(cmd=cmd, stdin=free.stdout)
        total, _ = proc.communicate()
        if proc.returncode != 0:
            return "invalid"
        cmd = ["free", "-m"]
        free = self._popen(cmd=cmd)
        cmd = ["awk", "/Mem/ {print $3}"]
        proc = self._popen(cmd=cmd, stdin=free.stdout)
        used, _ = proc.communicate()
        if proc.returncode != 0:
            return "invalid"
        return "%s MB (%s MB Used)" % (
            total.strip().decode("utf-8"),
            used.strip().decode("utf-8"),
        )
