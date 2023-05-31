#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/5/10
# @Author : chenxuehong
# @Version：V 0.1
# @File : main.py
# @desc :

import unittest
from testcase.test_login import LoginPageTest


if __name__ == "__main__":

    # 单个执行
    # suite = unittest.TestSuite()
    # suite.addTest(HomePageTest('test_author_path')
    # 多个执行
    loader_suite = unittest.TestLoader().discover('.', 'test_*.py')

    runner = unittest.TextTestRunner()
    runner.run(loader_suite)