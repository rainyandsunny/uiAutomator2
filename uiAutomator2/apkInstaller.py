#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess
import configParse

apkPath = configParse.get_apk_path()

installCmd = 'adb -s %s install %s'


# 得到连接的所有设备
def get_devices():
    devices_str = subprocess.Popen(['adb devices',''], stdout=subprocess.PIPE, shell=True).communicate()
    devices = devices_str[0].lstrip("List of devices attached\n").splitlines()
    device_names = []
    for device in devices:
        if device:
            device_names.append(device.rstrip("\tdevice\n"))
    return device_names


# 得到连接的设备数目
def get_device_num():
    return len(get_devices())


# 安装Apk到目标设备
def install_apk(device):
    cmd = installCmd % (device,apkPath)
    os.system(cmd)


# 安装Apk到所有设备
def install_apk_on_all_devices():
    for device in get_devices():
        install_apk(device)




if __name__ == '__main__':
    install_apk_on_all_devices()

