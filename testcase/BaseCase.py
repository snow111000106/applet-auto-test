#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/5/10
# @Author : chenxuehong
# @Version：V 0.1
# @File : test_login.py
# @desc :

from pathlib import Path
import minium


class BaseCase(minium.MiniTest):
    """测试用例基类"""

    @classmethod
    def setUpClass(cls) -> None:
        super(BaseCase, cls).setUpClass()
        output_dir = Path(cls.CONFIG.outputs)
        if not output_dir.is_dir():
            output_dir.mkdir()

    @classmethod
    def tearDownClass(cls):
        super(BaseCase, cls).tearDownClass()

    def setUp(self):
        super(BaseCase, self).setUp()
        pass

    def tearDown(self):
        super(BaseCase, self).tearDown()
        pass
