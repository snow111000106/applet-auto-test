#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/5/10
# @Author : chenxuehong
# @Version：V 0.1
# @File : test_login.py
# @desc :
import time

import minium
from conf import route, config
from testcase.BaseCase import BaseCase


@minium.ddt_class
class LoginPageTest(BaseCase):

    # 测试登录流程

    def __init__(self, methodName='runTest'):
        super(LoginPageTest, self).__init__(methodName)

    def test_no_login(self):

        self.loginpage.no_login()
        self.loginpage.switch_to_tabbar(route.user_page)
        self.assertFalse(self.userpage.is_user_name_exist())

    def test_wechat_login(self):

        self.loginpage.wechat_login()
        self.loginpage.switch_to_tabbar(route.user_page)
        self.assertTrue(self.userpage.is_user_name_exist())

    @minium.skipUnless(condition=config.env == "debug", reason="测试环境校验验证码登录")
    def test_code_login(self):

        self.loginpage.code_login(user_name=config.default_account, code=config.default_code)
        self.loginpage.switch_to_tabbar(route.user_page)
        self.assertTrue(self.userpage.is_user_name_exist())

    @minium.skipUnless(condition=config.env == "debug", reason="测试环境校验账号登录")
    def test_account_login(self):

        self.loginpage.account_login(user_name=config.default_account, pwd=config.default_pwd)
        self.loginpage.switch_to_tabbar(route.user_page)
        self.assertTrue(self.userpage.is_user_name_exist())
