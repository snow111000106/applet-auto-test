#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/10/7
# @Author : chenxuehong
# @Version：V 0.1
# @File : BaseCase.py
# @desc : 游客页面基础用例封装

import minium
from page.UserPage import UserPage
from conf import route


class BaseCase(minium.MiniTest):
    """测试用例基类"""

    @classmethod
    def setUpClass(cls):
        super(BaseCase, cls).setUpClass()
        cls.userpage = UserPage(cls)
        cls.userpage.into_user_center()
        user = cls.userpage.is_user_name_exist()
        if user:
            cls.userpage.logout()
        else:
            print("已退出登录")

    @classmethod
    def tearDownClass(cls):
        super(BaseCase, cls).tearDownClass()
        pass

    def setUp(self):
        super(BaseCase, self).setUp()
        pass

    def tearDown(self):
        super(BaseCase, self).tearDown()
        pass
