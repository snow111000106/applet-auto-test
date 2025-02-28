#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/8/7
# @Author : chenxuehong
# @Version：V 0.1
# @File : read_config.py
# @desc : 读取配置

from conf import config
import sys
import json

default_config = {
  "project_path": "$project_path_value",
  "dev_tool_path": "$dev_tool_path_value",
  "debug_mode": "debug",
  "enable_app_log": True,
  "platform": "$platform_value",
  "test_port": 9420,
  "close_ide": True,
  "use_push": True,
  "auto_relaunch": False,
  "remote_connect_timeout": 180,
  "outputs": "outputs",
  "assert_capture": True,
  "auto_authorize": True
}


project_path_win = "C:/Users/CDS-DN268/PycharmProjects/rb-wxapp/dist/build/mp-weixin"  # windows下小程序源码编译路径
project_path_mac = "/Users/snow/Desktop/rb-wxapp/dist/build/mp-weixin"  # mac下小程序源码编译路径
dev_tool_path_win = "E:/wx/微信web开发者工具/cli.bat"  # windows下微信开发者工具路径
dev_tool_path_mac = "/Applications/wechatwebdevtools.app/Contents/MacOS/cli"  # mac下微信开发者工具路径
device_desire_android = {
    "serial": "xxxxx",
    "uiautomator_version": 2
  }  # 安卓设备信息，替换serial
device_desire_ios = {
    "wda_bundle": "com.cxh.WebDriverAgent.xctrunner",  # 这个是我自己安装的wda需要替换
    "os_type": "ios",
    "device_info": {
      "udid": "xxxxxx"
    }
}  # ios设备信息，替换uuid


def read_config():
    if config.platform == 'ios':
        platform_value = 'IOS'
        device_desire_value = device_desire_ios
        default_config["device_desire"] = device_desire_value
    elif config.platform == 'android':
        platform_value = 'Android'
        device_desire_value = device_desire_android
        default_config["device_desire"] = device_desire_value
    elif config.platform == 'ide':
        platform_value = config.platform
    else:
        print('配置调试端错误，仅支持配置ide/ios/android，现在使用ide模式启动')
        platform_value = config.platform
    if sys.platform == 'win32':
        project_path_value = project_path_win
        dev_tool_path_value = dev_tool_path_win
    elif sys.platform == 'darwin':
        project_path_value = project_path_mac
        dev_tool_path_value = dev_tool_path_mac
    else:
        print('当前系统不支持小程序自动化')

    default_config["platform"] = platform_value
    default_config["project_path"] = project_path_value
    default_config["dev_tool_path"] = dev_tool_path_value
    print(default_config)

    with open('./conf/config.json', 'w') as f:
        json.dump(default_config, f, indent=4)
