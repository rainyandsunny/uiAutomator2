#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uiautomator2 as u2

appUrl = 'http://pgqdsy3oa.bkt.clouddn.com/qianjie.apk'
d = u2.connect('172.90.15.216')


#print(d.device_info)

# 安装app
#d.app_install(appUrl)

# 启动app
# d.app_start("com.qianlizhangdan.app")

# 停掉app
# d.app_stop("com.qianlizhangdan.app")

# 退出app
# d.app_clear('com.qianlizhangdan.app')

# 停止所有app
# d.app_stop_all()

# 推送文件到设备
# d.push("./file/1.txt", "/sdcard/")

# 从设备取文件
# d.pull("/sdcard/1.txt","tep.txt")

# 启动app
# sess = d.session("com.qianlizhangdan.app")

# 打印window信息
# print(d.window_size())

# 打印当前app信息
# print(d.current_app())

# Attach to the running app7
# sess = d.session("com.qianlizhangdan.app", attach=True)

# 打印当前设备名
# print(d.serial)

# 打开屏幕
# d.screen_on()

# 关闭屏幕
# d.screen_off()

# 得到当前屏幕状态
# d.info.get('screenOn')

# 响应按键
# d.press("camera")

# Freeze/Un-freeze rotation(是否竖屏锁定)
# d.freeze_rotation(False)

# 截屏
# d.screenshot("home.jpg")

# xml = d.dump_hierarchy()

# 打开通知栏
#d.open_notification()
# d.open_quick_settings()

# 设置设备方向
# d.set_orientation('n')


# 获取方向
# d.orientation