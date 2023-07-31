#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/5/10
# @Author : chenxuehong
# @Version：V 0.1
# @File : base.py
# @desc :

import datetime
import yaml


class Base:

    @staticmethod
    def get_time(num):
        """
        :param num: 具体的天数或周数或月数
        :return: 当前日期加上或减去具体的天数
        """

        del_day = datetime.datetime.now() - datetime.timedelta(days=num)
        day = del_day.strftime('%m/%d')
        return day

    @staticmethod
    def calculate_overdue_time(now_time, month_num):
        """
        :param now_time: 当前会员过期时间
        :param month_num: 购买天数
        :return: 预计过期时间
        """
        date_format = '%Y-%m-%d'
        now_time = datetime.datetime.strptime(now_time, date_format)
        days = int(month_num)*31
        del_day = now_time + datetime.timedelta(days=days)
        return del_day.strftime('%Y-%m-%d')

    @staticmethod
    def get_vip_info(vip_level):
        """
        :param vip_level: 会员等级
        :return: 会员账号信息
        """
        with open('./conf/account.yaml', 'r', encoding='utf-8') as f:
            account = yaml.safe_load(f)

        if vip_level == 1:
            return account['vip_1']
        elif vip_level == 4:
            return account['vip_4']
        elif vip_level == 5:
            return account['vip_5']
        elif vip_level == 6:
            return account['vip_6']
        else:
            return account['vip_default']


if __name__ == "__main__":
    a = Base.calculate_overdue_time('2025-07-30', 3)
    print(a)