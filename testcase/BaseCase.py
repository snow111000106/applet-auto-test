#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/5/10
# @Author : chenxuehong
# @Version：V 0.1
# @File : BaseCase.py
# @desc : 登录页面基础用例封装

import minium
from pathlib import Path
from page.UserPage import UserPage
from page.LoginPage import LoginPage
from page.HomePage import HomePage
from conf import route


class BaseCase(minium.MiniTest):
    """测试用例基类"""

    @classmethod
    def setUpClass(cls):
        super(BaseCase, cls).setUpClass()
        output_dir = Path(cls.CONFIG.outputs)
        if not output_dir.is_dir():
            output_dir.mkdir()
        cls.userpage = UserPage(cls)
        cls.homepage = HomePage(cls)
        cls.loginpage = LoginPage(cls)

    @classmethod
    def tearDownClass(cls):
        super(BaseCase, cls).tearDownClass()
        pass

    def setUp(self):
        super(BaseCase, self).setUp()
        self.loginpage.switch_to_tabbar(route.user_page)
        user = self.userpage.is_user_name_exist()
        if user:
            self.userpage.logout()
        else:
            print("已退出登录")

    def tearDown(self):
        super(BaseCase, self).tearDown()
        self.loginpage.switch_to_tabbar(route.user_page)
