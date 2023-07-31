#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/7/26
# @Author : chenxuehong
# @Version：V 0.1
# @File : test_user_center.py
# @desc : 个人版-我的页面测试用例

import minium, time
from common.base import Base
from conf import config, route
from testcase.vip_5.BaseCase import BaseCase
from page.UserPage import UserPage


@minium.ddt_class
class UserPageTest(BaseCase):

    userpage = None

    def __init__(self, methodName='runTest'):
        super(UserPageTest, self).__init__(methodName)
        self.userpage = UserPage(self)

    @classmethod
    def setUpClass(cls):
        super(UserPageTest, cls).setUpClass()
        cls.userpage = UserPage(cls)
        cls.userpage.into_user_center()

    def test_user_info(self):
        """
        测试用户信息元素显示正确
        """
        vip_name, vip_time, user_name = self.userpage.get_user_info()
        self.assertEqual(vip_name, Base.get_vip_info(5)['name'])
        self.assertEqual(vip_time, Base.get_vip_info(5)['vip_time'])
        self.assertEqual(user_name, Base.get_vip_info(5)['mobile'])

    @minium.ddt_case(('my_collect', '博主/笔记/品牌/品类'), ('my_trace', '实时监控数据'))
    def test_my_collect_text(self, value):
        """
        测试我的收藏底部文案
        """
        types, text = value
        re = self.userpage.get_ele_text(types=types)
        self.assertEqual(re, text)

    @minium.skipUnless(condition=config.platform != "ide", reason="仅真机支持人工客服跳转")
    def test_cs_jump(self):
        """
        测试真机点击联系客服跳转人工客服
        """

        self.userpage.click_ele(types='customer_service')
        time.sleep(2)
        path = self.userpage.current_path
        try:
            self.assertEqual(path, route.home_page)
        finally:
            self.userpage.back_mini()

    @minium.ddt_case(('my_collect', route.my_collect_page),
                     ('my_trace', route.my_trace_page), ('my_set', route.my_set_page))
    def test_jump(self, value):
        """
        测试跳转path正确
        """
        types, re_path = value
        self.userpage.click_ele(types=types)
        time.sleep(2)
        try:
            path = self.userpage.current_path
            self.assertEqual(path, re_path)
        finally:
            self.userpage.back(delta=1)

    @minium.skipUnless(condition=config.platform == "ios", reason="ios不支持跳转到vip页面")
    def test_ios_vip_jump(self):
        """
        测试ios点击续费按钮跳转客服页面
        """
        self.userpage.click_ele(types='vip_btn')
        time.sleep(2)
        try:
            path = self.userpage.current_path
            self.assertEqual(path, route.home_page)
        finally:
            self.userpage.back_mini()

    @minium.skipUnless(condition=config.platform != "ios", reason="非ios支持跳转到vip页面")
    def test_vip_jump(self):
        """
        测试点击续费按钮跳转vip页面
        """
        self.userpage.click_ele(types='vip_btn')
        time.sleep(2)
        try:
            path = self.userpage.current_path
            self.assertEqual(path, route.vip_page)
        finally:
            self.userpage.back(delta=1)

    def test_my_set_info(self):
        """
        测试设置页面的用户信息
        """
        self.userpage.click_ele(types='my_set')
        time.sleep(2)
        nick_name, mobil, wechat_status, account_types = self.userpage.get_my_set_info()
        try:
            self.assertEqual(nick_name, Base.get_vip_info(5)['mobile'])
            self.assertEqual(mobil, Base.get_vip_info(5)['mobile'])
            self.assertEqual(wechat_status, '未绑定微信')
            self.assertEqual(account_types, '主账号')
        finally:
            self.userpage.back(delta=1)
