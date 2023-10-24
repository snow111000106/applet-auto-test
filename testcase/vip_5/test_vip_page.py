#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/8/7
# @Author : chenxuehong
# @Version：V 0.1
# @File : test_vip_page.py
# @desc : 个人版-vip页面测试用例

import minium, time
import re
from conf import config
from testcase.vip_5.BaseCase import BaseCase
from page.VipPage import VipPage
from common.base import Base


@minium.skipUnless(condition=config.platform != "ios", reason="仅ios无vip页面")
@minium.ddt_class
class VipPageTest(BaseCase):

    vippage = None

    def __init__(self, methodName='runTest'):
        super(VipPageTest, self).__init__(methodName)
        self.vippage = VipPage(self)

    @classmethod
    def setUpClass(cls):
        super(VipPageTest, cls).setUpClass()
        cls.vippage = VipPage(cls)
        cls.vippage.into_vip_center()

    def test_user_info(self):
        """
        测试个人版用户信息正确
        """
        name, vip_name, vip_time = self.vippage.get_user_info()
        self.assertEqual(vip_name, Base.get_vip_info(5)['vip_name'])
        self.assertEqual(vip_time, Base.get_vip_info(5)['vip_time'])
        self.assertEqual(name, Base.get_vip_info(5)['nickname'])

    @minium.ddt_case(('个人版', '立即续费', ['rgb(245, 101, 137)', 'rgb(255, 92, 92)']),
                     ('企业版', '立即升级', ['rgb(245, 101, 137)', 'rgb(255, 92, 92)']),
                     ('专业版', '立即升级', ['rgb(245, 101, 137)', 'rgb(255, 92, 92)']))
    def test_vip_btn_info(self, value):
        """
        测试个人版用户查看vip续费按钮，文案，背景颜色显示正确
        """
        types, re_text, re_background = value
        self.vippage.switch_vip_tab(tab_name=types)
        time.sleep(2)
        text = self.vippage.get_vip_btn_context()
        bg = self.vippage.get_vip_btn_style(name='background')
        line = []
        for bg in bg:
            # 使用正则表达式匹配 rgb 部分
            linear_gradient_matches = re.findall(r'rgb\([^)]+\)', bg)

            for match in linear_gradient_matches:
                line.append(match)
        color = self.vippage.get_vip_btn_style(name='color')
        self.assertEqual(line, re_background)
        self.assertEqual(text, re_text)
        self.assertEqual(color[0], 'rgb(255, 255, 255)')






