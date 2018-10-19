#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess
import configParse
import serverInit

apkPath = configParse.get_apk_path()
apk_package = configParse.get_apk_package()

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
    cmd = installCmd % (device, apkPath)
    os.system(cmd)


# def apk_installed(device):
#     p = subprocess.Popen(['adb shell'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     output, err = p.communicate(b'pm list package\n')
#     package_info = output.decode('utf-8')
#     print ('包信息-------')
#     print (package_info)
#     # if(package_info.):
#     #     return True
#     return False


# 安装Apk到所有设备
def install_apk_on_all_devices(ip):
    if ip:
        for conn in serverInit.get_connections():
            conn.app_install(apkPath)
    else:
        for device in get_devices():
            install_apk(device)


if __name__ == '__main__':
    install_apk_on_all_devices(True)

