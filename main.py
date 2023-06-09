#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/5/10
# @Author : chenxuehong
# @Version：V 0.1
# @File : main.py
# @desc :

import os
from conf import config

if __name__ == "__main__":

    # 运行执行class文件中的指定用例,无法获取当前path，无法运行有ddt装饰的用例
    cmd0 = "minitest -m testcase.home.test_home --case test_rank_num -c {}_config.json -g".format(config.platform)
    # 运行执行testcase文件中的指定用例
    cmd1 = "minitest -m testcase.home.test_home -c {}_config.json -g".format(config.platform)
    # 按照suite配置执行用例
    cmd2 = "minitest -s suite.json -c {}_config.json -g".format(config.platform)

    os.system(cmd2)