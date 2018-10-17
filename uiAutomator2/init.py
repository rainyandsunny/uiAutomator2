#!/usr/bin/env python
# -*- coding: utf-8 -*-

import apkInstaller
import os
import uiautomator2 as u2


startCmd = "python -m uiautomator2 init"

conns = []


def server_start():
    os.system(startCmd)


def __connect_devices():
    global conns
    devices = apkInstaller.get_devices()
    for device in devices:
        conns.append(u2.connect(device))


def get_connections():
    if len(conns) == 0:
        __connect_devices()
    return conns


def init():
    apkInstaller.install_apk_on_all_devices()
    server_start()
    get_connections()
