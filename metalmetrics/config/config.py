# -*- coding: utf-8 -*-

import os
import yaml


class ConfigFile:
    METADATA = "metadata"
    SPEC = "spec"


class MetaData:
    NAME = "name"


class Spec:
    CPU = "cpu"
    DISK = "disk"
    IO = "io"
    IP = "ip"
    KERNEL = "kernel"
    MAC = "mac"
    NETWORK = "network"
    OS = "os"
    PROCESS = "process"
    RAM = "ram"
    SSH = "ssh"


class ConfigException(Exception):
    def __init__(self, info):
        super().__init__(self)
        self._info = info

    def __str__(self):
        return self._info


class Config(object):
    def __init__(self):
        self._config_file = None
        self._grpc_host = ""
        self._grpc_port = 0
        self._output_file = ""

    @property
    def config_file(self):
        return self._config_file

    @config_file.setter
    def config_file(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ConfigException("name invalid")
        if not name.endswith(".yml") and not name.endswith(".yaml"):
            raise ConfigException("suffix invalid")
        if not os.path.exists(name):
            raise ConfigException("%s not found" % name)
        with open(name) as file:
            self._config_file = yaml.load(file, Loader=yaml.FullLoader)
        if self._config_file is None:
            raise ConfigException("config invalid")

    @property
    def grpc_host(self):
        return self._grpc_host

    @grpc_host.setter
    def grpc_host(self, host):
        if not isinstance(host, str):
            raise ConfigException("host invalid")
        self._grpc_host = host.strip()

    @property
    def grpc_port(self):
        return self._grpc_port

    @grpc_port.setter
    def grpc_port(self, port):
        if not isinstance(port, int):
            raise ConfigException("port invalid")
        self._grpc_port = port

    @property
    def output_file(self):
        return self._output_file

    @output_file.setter
    def output_file(self, name):
        if not isinstance(name, str):
            raise ConfigException("name invalid")
        if len(name.strip()) != 0:
            if (
                not name.endswith(".json")
                and not name.endswith(".txt")
                and not name.endswith(".xlsx")
            ):
                raise ConfigException("suffix invalid")
            if os.path.exists(name):
                raise ConfigException("%s already exist" % name)
        self._output_file = name.strip()
