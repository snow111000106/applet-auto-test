#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/5/10
# @Author : chenxuehong
# @Version：V 0.1
# @File : test_login.py
# @desc :

import minium
from page.LoginPage import LoginPage
from conf import route, config


class BaseCase(minium.MiniTest):
    """测试用例基类"""

    @classmethod
    def setUpClass(cls) -> None:
        super(BaseCase, cls).setUpClass()
        cls.loginpage = LoginPage(cls)
        cls.loginpage.code_login(user_name=config.default_account, code=config.default_code)

    @classmethod
    def tearDownClass(cls):
        super(BaseCase, cls).tearDownClass()

    def setUp(self):
        super(BaseCase, self).setUp()
        self.homepage.switch_to_tabbar(route.home_page)

    def tearDown(self):
        super(BaseCase, self).tearDown()
        pass
