#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

configPath = './conf/config.json'


def get_config(config):
    f = open(config,'r')
    string = f.read()
    f.close()
    return string


def get_config_json():
    config_str = get_config(configPath)
    return json.loads(config_str)


def get_apk_path():
    config = get_config_json()
    apk = config['apkPath']
    return apk


def get_apk_package():
    config = get_config_json()
    package = config['packageName']
    return package


if __name__ == '__main__':
    get_apk_path()