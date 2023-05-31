#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/5/10
# @Author : chenxuehong
# @Version：V 0.1
# @File : test_login.py
# @desc :
import time

import minium
from page.LoginPage import LoginPage
from conf import route, config
from testcase.BaseCase import BaseCase


@minium.ddt_class
class LoginPageTest(BaseCase):

    # 测试登录流程

    def __init__(self, methodName='runTest'):
        super(LoginPageTest, self).__init__(methodName)
        self.loginpage = LoginPage(self)

    def test_no_login(self):

        self.loginpage.no_login()
        path = self.loginpage.current_path
        self.assertEqual(path, route.home_page)

    def test_wechat_login(self):

        self.loginpage.wechat_login()
        path = self.loginpage.current_path
        self.assertEqual(path, route.user_page)

    @minium.skipUnless(condition=config.env == "debug", reason="测试环境校验验证码登录")
    def test_code_login(self):

        self.loginpage.code_login()
        path = self.loginpage.current_path
        self.assertEqual(path, route.user_page)

    @minium.skipUnless(condition=config.env == "debug", reason="测试环境校验账号登录")
    def test_account_login(self):

        self.loginpage.account_login()
        path = self.loginpage.current_path
        self.assertEqual(path, route.user_page)