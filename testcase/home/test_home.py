#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/5/10
# @Author : chenxuehong
# @Version：V 0.1
# @File : test_login.py
# @desc :
import time

import minium
from conf import route
from testcase.home.BaseCase import BaseCase
from page.HomePage import HomePage
from page.RankPage import RankPage
from conf import config


@minium.ddt_class
class HomePageTest(BaseCase):

    def __init__(self, methodName='runTest'):
        super(HomePageTest, self).__init__(methodName)
        self.homepage = HomePage(self)
        self.rankpage = RankPage(self)

    def test_banner(self):
        self.assertTrue(self.homepage.is_banner_exist())

    @minium.skipUnless(condition=config.platform != "ide", reason="真机支持人工客服跳转")
    def test_banner_jump(self):
        self.homepage.click_banner()
        time.sleep(2)
        path = self.homepage.current_path
        self.assertEqual(path, route.home_page)
        self.homepage.back_mini()

    @minium.ddt_case('author', 'note', 'brand', 'kind', 'hot_key')
    def test_all_rank_path(self, value):

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

    @minium.ddt_case('author_rank', 'note_rank', 'brand_rank', 'hot_key_rank')
    def test_rank_num(self, types):

        num = self.homepage.get_rank_num(types=types)
        self.assertEqual(num, 5)
        self.homepage.slide_to_rank(types=types, top=1)

    @minium.ddt_case('author_rank', 'note_rank', 'brand_rank', 'hot_key_rank')
    def test_rank_more(self, types):

        self.homepage.slide_to_rank(types=types)
        self.homepage.click_more(rank_type=types)
        path = self.homepage.current_path
        self.assertEqual(path, route.rank_page)
        self.homepage.slide_to_rank(types=types, top=1)

    def test_fans_rank_detail_ele(self):

        self.homepage.slide_to_rank(types='author_rank')
        num = self.homepage.is_fans_rank_ele_exist()
        self.assertEqual(num, 5)
        self.homepage.slide_to_rank(types='author_rank', top=1)

    def test_fans_rank_click(self):

        self.homepage.slide_to_rank(types='author_rank')
        self.homepage.click_into_detail(rank_type='author')
        time.sleep(2)
        path = self.homepage.current_path
        self.assertEqual(path, route.author_detail_page)
        self.homepage.back()
        self.homepage.slide_to_rank(types='author_rank', top=1)
