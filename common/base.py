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
        计算前N天的日期
        :param num: 具体的天数
        :return: 当前日期加上或减去具体的天数返回格式09/03
        """
        del_day = datetime.datetime.now() - datetime.timedelta(days=num)
        day = del_day.strftime('%m/%d')
        return day

    @staticmethod
    def calculate_overdue_time(now_time, month_num):
        """
        根据购买天数，计算预计过期时间
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
        根据会员等级返回会员信息
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

    @staticmethod
    def get_monitor_info(types, id):
        """
        根据类型,id获取监控列表数据
        :param types: 类型，author_list/note_list/brand_list
        :param id: id
        :return: 监控列表数据
        """
        with open('./conf/monitor_data.yaml', 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)

        info = data[types][id]
        return info

    @staticmethod
    def convert_to_float_with_unit(value):
        """
        将字符串转化为浮点型数值
        :param value: 需要转化的字符串，支持5,222.7w类字符，支持负数，传入为-时输出0
        :return: 浮点型数值
        """
        if value == '-':
            return 0
        unit_multiplier = {'w': 10000, '亿': 100000000}
        is_negative = False
        if value.startswith('-'):
            is_negative = True
            value = value[1:]
        value = value.lower()
        for unit, multiplier in unit_multiplier.items():
            if value.endswith(unit):
                numeric_part = value.replace(',', '').replace(unit, '')
                numeric_value = float(numeric_part) * multiplier
                if is_negative:
                    numeric_value = -numeric_value
                return numeric_value

        numeric_value = float(value.replace(',', ''))
        if is_negative:
            numeric_value = -numeric_value

        return numeric_value

    @staticmethod
    def times_change(relative_time):
        """
        日期转化为时间戳
        """
        # 获取当前日期时间
        now = datetime.datetime.now()

        # 定义相对时间到时间差的映射
        time_mapping = {
            '6小时': datetime.timedelta(hours=6+1),
            '12小时': datetime.timedelta(hours=12+1),
            '24小时': datetime.timedelta(hours=24+1),
            '近3天': datetime.timedelta(days=3+1),
            '近7天': datetime.timedelta(days=7+1),
            '近15天': datetime.timedelta(days=15+1),
            '近30天': datetime.timedelta(days=30+1),
            '近90天': datetime.timedelta(days=90+1)
        }
        if relative_time in time_mapping:
            time_difference = time_mapping[relative_time]
            result_datetime = now - time_difference
            formatted_result = result_datetime.strftime("%m/%d %H:%M")
            return formatted_result
        else:
            raise ValueError("无效的相对时间")


if __name__ == "__main__":
    s = Base.convert_to_float_with_unit('-')
    print(s)