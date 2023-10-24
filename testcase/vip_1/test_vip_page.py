#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/8/7
# @Author : chenxuehong
# @Version：V 0.1
# @File : test_vip_page.py
# @desc : 普通用户-vip页面测试用例

import minium, time
import re
from conf import config
from testcase.vip_1.BaseCase import BaseCase
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
        测试普通用户信息正确
        """
        name, vip_name, vip_time = self.vippage.get_user_info(is_vip=0)
        self.assertEqual(vip_name, Base.get_vip_info(1)['vip_name'])
        self.assertEqual(name, Base.get_vip_info(1)['nickname'])

    @minium.ddt_case(('个人版', '立即升级', ['rgb(245, 101, 137)', 'rgb(255, 92, 92)']),
                     ('企业版', '立即升级', ['rgb(245, 101, 137)', 'rgb(255, 92, 92)']),
                     ('专业版', '立即升级', ['rgb(245, 101, 137)', 'rgb(255, 92, 92)']))
    def test_vip_btn_info(self, value):
        """
        测试普通版用户查看vip续费按钮，文案，背景颜色显示正确
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

    @minium.skipUnless(condition=config.is_activity is True, reason="活动期间有优惠券入口")
    @minium.ddt_case(('个人版', 1, '818特惠 立减100元'), ('个人版', 3, '818特惠 立减200元'),
                     ('专业版', 1, '818特惠 立减800元'), ('专业版', 2, '818特惠 立减250元'),
                     ('专业版', 3, '818特惠 立减100元'), ('专业版', 4, '818特惠 立减3000元'),
                     ('企业版', 1, '818特惠 立减1600元'), ('企业版', 2, '818特惠 立减500元'),
                     ('企业版', 3, '818特惠 立减200元'), ('企业版', 4, '818特惠 立减4500元'))
    def test_coupon_choose(self, value):
        """
        测试各个版本优惠券面额可选中
        """

        types, card_id, re_coupon = value
        self.vippage.choose_vip_version(version=types, card_id=card_id)
        self.vippage.click_ele(types='vip_btn')
        coupon = self.vippage.return_coupon_price()
        self.assertEqual(coupon, '请选择优惠券')
        try:
            self.vippage.click_ele(types='coupon_choose')
            time.sleep(1)
            self.vippage.choose_coupon(types='confirm', value=[1])
            coupon = self.vippage.return_coupon_price()
            self.assertEqual(coupon, re_coupon)
        finally:
            self.vippage.click_ele(types='close_pop')

    @minium.skipUnless(condition=config.is_activity is True, reason="活动期间有优惠券入口")
    @minium.ddt_case(('个人版', 1, ['不使用优惠券', '818特惠 立减100元']), ('个人版', 3, ['不使用优惠券', '818特惠 立减200元']),
                     ('专业版', 1, ['不使用优惠券', '818特惠 立减800元']), ('专业版', 2, ['不使用优惠券', '818特惠 立减250元']),
                     ('专业版', 3, ['不使用优惠券', '818特惠 立减100元']), ('专业版', 4, ['不使用优惠券', '818特惠 立减3000元']),
                     ('企业版', 1, ['不使用优惠券', '818特惠 立减1600元']), ('企业版', 2, ['不使用优惠券', '818特惠 立减500元']),
                     ('企业版', 3, ['不使用优惠券', '818特惠 立减200元']), ('企业版', 4, ['不使用优惠券', '818特惠 立减4500元']))
    def test_coupon(self, value):
        """
        测试各个版本优惠券面额
        """
        types, card_id, re_coupon_list = value
        self.vippage.choose_vip_version(version=types, card_id=card_id)
        time.sleep(1)
        self.vippage.click_ele(types='vip_btn')
        time.sleep(1)
        try:
            self.vippage.click_ele(types='coupon_choose')
            coupon_list = self.vippage.get_coupon_list(num=2)
            self.assertEqual(coupon_list, re_coupon_list)
            self.vippage.click_ele(types='coupon_cancel')
        finally:
            self.vippage.click_ele(types='close_pop')





