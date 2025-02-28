#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/8/28
# @Author : chenxuehong
# @Version：V 0.1
# @File : CustomAssert.py
# @desc : 自定义asser类

import minium
import re
from datetime import datetime


class CustomAssert(minium.MiniTest):

    def assertMultiIn(self, first, second, msg=None):
        """
        自定义的断言方法，判断first里面有一个在second里面即通过
        """
        for i in first:
            if i in second:
                # 只要有一个元素在 second 中，断言通过
                return
        # 如果循环完毕都没有通过，则表示所有元素都不在 second 里面，断言失败
        standard_msg = f"列表 {first} 中的所有元素都不在列表 {second} 里面"
        self.fail(self._formatMessage(msg, standard_msg))

    def assertLess(self, a, b, msg=None):
        """Just like self.assertTrue(a < b), but with a nicer default message."""
        if not int(a) < int(b):
            standard_msg = f'{a} 不小于 {b}'
            self.fail(self._formatMessage(msg, standard_msg))

    def assertLessEqual(self, a, b, msg=None):
        """Just like self.assertTrue(a <= b), but with a nicer default message."""
        if not int(a) <= int(b):
            standard_msg = f'{a} 不小于等于 to {b}'
            self.fail(self._formatMessage(msg, standard_msg))

    def assertGreater(self, a, b, msg=None):
        """Just like self.assertTrue(a > b), but with a nicer default message."""
        if not int(a) > int(b):
            standard_msg = f'{a} 不大于 {b}'
            self.fail(self._formatMessage(msg, standard_msg))

    def assertGreaterEqual(self, a, b, msg=None):
        """Just like self.assertTrue(a >= b), but with a nicer default message."""
        if not int(a) >= int(b):
            standard_msg = f'{a} 不大于等于 {b}'
            self.fail(self._formatMessage(msg, standard_msg))

    # def assertDatetimeBefore(self, a, b, msg=None):
    #     """自定义的断言方法，判断a的时间在b之前即通过"""
    #     # 将日期时间字符串解析为datetime对象
    #     datetime_a = datetime.strptime(a, "%m-%d %H:%M")
    #     datetime_b = datetime.strptime(b, "%m-%d %H:%M")
    #
    #     if not datetime_a <= datetime_b:
    #         standard_msg = f"{a} 时间不在 {b} 之前"
    #         self.fail(self._formatMessage(msg, standard_msg))

    def assertDatetimeBefore(self, a, b, msg=None):
        """自定义的断言方法，判断a的时间在b之前即通过"""

        # 使用正则表达式检查日期时间格式并解析
        datetime_a = None
        datetime_b = None

        # 检查a的时间格式
        if re.match(r"\d{2}-\d{2} \d{2}:\d{2}", a):
            datetime_a = datetime.strptime(a, "%m-%d %H:%M")
        elif re.match(r"\d{2}/\d{2} \d{2}:\d{2}", a):
            datetime_a = datetime.strptime(a, "%m/%d %H:%M")
        else:
            raise ValueError(f"不支持的时间格式: {a}")

        # 检查b的时间格式
        if re.match(r"\d{2}-\d{2} \d{2}:\d{2}", b):
            datetime_b = datetime.strptime(b, "%m-%d %H:%M")
        elif re.match(r"\d{2}/\d{2} \d{2}:\d{2}", b):
            datetime_b = datetime.strptime(b, "%m/%d %H:%M")
        else:
            raise ValueError(f"不支持的时间格式: {b}")

        if not datetime_a <= datetime_b:
            standard_msg = f"{a} 时间不在 {b} 之前"
            self.fail(self._formatMessage(msg, standard_msg))


