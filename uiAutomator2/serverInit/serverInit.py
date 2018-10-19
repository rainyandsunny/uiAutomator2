#!/usr/bin/env python
# -*- coding: utf-8 -*-

import apkInstaller
import os
import configParse
import uiautomator2 as u2


startCmd = "python -m uiautomator2 init"

conns = []


def server_start():
    os.system(startCmd)


def __connect_devices():
    global conns
    ips = configParse.get_devices_ip()
    for ip in ips:
        conns.append(u2.connect(ip))


def get_connections():
    if len(conns) == 0:
        __connect_devices()
    return conns


def init():
    server_start()
    get_connections()
    apkInstaller.install_apk_on_all_devices(True)
