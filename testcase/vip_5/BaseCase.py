#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/7/26
# @Author : chenxuehong
# @Version：V 0.1
# @File : BaseCase.py
# @desc : 个人版-基础用例封装

import time
from common.base import Base
import minium
from page.LoginPage import LoginPage
from conf import config


class BaseCase(minium.MiniTest):
    """测试用例基类"""

    @classmethod
    def setUpClass(cls) -> None:
        super(BaseCase, cls).setUpClass()
        cls.loginpage = LoginPage(cls)
        cls.loginpage.code_login(user_name=Base.get_vip_info(5)['mobile'], code=config.default_code)
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        super(BaseCase, cls).tearDownClass()

    def setUp(self):
        super(BaseCase, self).setUp()

    def tearDown(self):
        super(BaseCase, self).tearDown()
        pass
