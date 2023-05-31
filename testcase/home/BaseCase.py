#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/5/10
# @Author : chenxuehong
# @Version：V 0.1
# @File : test_login.py
# @desc :

from pathlib import Path
import minium
from page.LoginPage import LoginPage
from conf import route


class BaseCase(minium.MiniTest):
    """测试用例基类"""

    @classmethod
    def setUpClass(cls) -> None:
        super(BaseCase, cls).setUpClass()
        # cls.loginpage = LoginPage(cls)
        # cls.loginpage.account_login()

    @classmethod
    def tearDownClass(cls):
        super(BaseCase, cls).tearDownClass()

    def setUp(self):
        super(BaseCase, self).setUp()
        self.homepage.switch_to_tabbar(route.home_page)

    def tearDown(self):
        super(BaseCase, self).tearDown()
        pass
