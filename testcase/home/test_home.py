#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/5/10
# @Author : chenxuehong
# @Version：V 0.1
# @File : test_login.py
# @desc :
import time

import minium
from page.HomePage import HomePage
from page.RankPage import RankPage
from conf import route
from testcase.home.BaseCase import BaseCase


@minium.ddt_class
class HomePageTest(BaseCase):

    def __init__(self, methodName='runTest'):
        super(HomePageTest, self).__init__(methodName)
        self.homepage = HomePage(self)
        self.rankpage = RankPage(self)

    def test_banner(self):
        self.assertTrue(self.homepage.is_banner_exist())

    @minium.ddt_case('author', 'note', 'brand', 'kind', 'hot_key')
    def test_rank_path(self, value):

        self.homepage.click_Rank(rank_type=value)
        path = self.homepage.current_path
        self.assertEqual(path, route.rank_page)
        self.assertTrue(self.rankpage.is_element_exist(rank_type=value))

    @minium.ddt_case('author', 'note', 'brand')
    def test_my_collect_num(self, value):

        num = self.homepage.my_collect_num(rank_type=value)
        if value == 'author':
            self.assertEqual(num, '50')
        if value == 'note':
            self.assertEqual(num, '8')
        if value == 'brand':
            self.assertEqual(num, '54')

    @minium.ddt_case('author', 'note')
    def test_my_monitor_num(self, value):

        num = self.homepage.my_monitor_num(rank_type=value)
        if value == 'author':
            self.assertEqual(num, '8')
        if value == 'note':
            self.assertEqual(num, '12')

    def test_fans_inc_rank(self):

        num = self.homepage.get_fans_inc_rank_num()
        self.assertEqual(num, 5)
        self.slide_to_fans_inc_rank(types='top')