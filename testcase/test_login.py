#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/5/10
# @Author : chenxuehong
# @Version：V 0.1
# @File : test_login.py
# @desc :登录界面测试用例

import time
import minium
from conf import config
from testcase.BaseCase import BaseCase
from page.UserPage import UserPage
from common.base import Base


@minium.ddt_class
class LoginPageTest(BaseCase):

    # 测试登录流程

    def __init__(self, methodName='runTest'):
        super(LoginPageTest, self).__init__(methodName)
        self.userpage = UserPage(self)

    def test_no_login(self):
        """
        测试点击暂不登录后，我的页面没有用户名称
        """

        self.loginpage.no_login()
        time.sleep(1)
        self.assertFalse(self.userpage.is_user_name_exist())

    def test_wechat_login(self):
        """
        测试微信登录后，我的页面有用户名称
        """

        self.loginpage.wechat_login()
        time.sleep(1)
        self.assertTrue(self.userpage.is_user_name_exist())

    @minium.skipUnless(condition=config.env == "debug", reason="测试环境校验验证码登录")
    def test_code_login(self):
        """
        测试【测试环境】验证码登录后，我的页面有用户名称
        """

        self.loginpage.code_login(user_name=Base.get_vip_info(6)['name'], code=config.default_code)
        time.sleep(1)
        self.assertTrue(self.userpage.is_user_name_exist())

    @minium.skipUnless(condition=config.env == "debug", reason="测试环境校验账号登录")
    def test_account_login(self):
        """
        测试【测试环境】账号密码登录后，我的页面有用户名称
        """

        self.loginpage.account_login(user_name=Base.get_vip_info(6)['name'], pwd=Base.get_vip_info(6)['pwd'])
        time.sleep(1)
        self.assertTrue(self.userpage.is_user_name_exist())

    @minium.skipUnless(condition=config.env == "debug", reason="测试登录后账号等级变化")
    @minium.ddt_case((Base.get_vip_info(6)['name'], Base.get_vip_info(6)['pwd'], Base.get_vip_info(6)['vip_name']),
                     (Base.get_vip_info(5)['name'], Base.get_vip_info(5)['pwd'], Base.get_vip_info(5)['vip_name']),
                     (Base.get_vip_info(4)['name'], Base.get_vip_info(4)['pwd'], Base.get_vip_info(4)['vip_name']),
                     (Base.get_vip_info(1)['name'], Base.get_vip_info(1)['pwd'], Base.get_vip_info(1)['vip_name'])
                     )
    def test_login_vip(self, value):
        """
        测试【测试环境】不同账号登录后，会员版本有发生变化
        """

        [name, pwd, vip] = value
        self.loginpage.account_login(user_name=name, pwd=pwd)
        time.sleep(2)
        if vip == '普通会员':
            vip_name, vip_time, user_name = self.userpage.get_user_info(is_common=1)
        else:
            vip_name, vip_time, user_name = self.userpage.get_user_info()
        self.assertEqual(vip, vip_name)

