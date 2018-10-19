#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 读取配置文件

import json

config_path = './../conf/config.json'


def get_config(config):
    f = open(config, 'r')
    string = f.read()
    f.close()
    return string


def get_config_json():
    config_str = get_config(config_path)
    return json.loads(config_str)


def get_apk_path():
    config = get_config_json()
    apk = config['apkPath']
    return apk


def get_apk_package():
    config = get_config_json()
    package = config['packageName']
    return package


# 得到连接设备的Ip
def get_devices_ip():
    config = get_config_json()
    ips = config['deviceIp']
    return ips


if __name__ == '__main__':
    get_devices_ip()