#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/6/10
# @Author : chenxuehong
# @Version：V 0.1
# @File : test_home.py
# @desc : 企业版-首页测试用例

import time
import minium
from conf import route
from testcase.vip_6.BaseCase import BaseCase
from common.base import Base
from page.HomePage import HomePage
from page.RankPage import RankPage
from conf import config


@minium.ddt_class
class HomePageTest(BaseCase):

    def __init__(self, methodName='runTest'):
        super(HomePageTest, self).__init__(methodName)
        self.homepage = HomePage(self)
        self.rankpage = RankPage(self)

    def setUp(self):
        self.loginpage.go_to_home()
        time.sleep(1)

    def tearDown(self):
        self.homepage.go_to_home()

    def test_banner(self):
        """
        测试登录后榜单是否存在
        """
        time.sleep(2)
        self.assertTrue(self.homepage.is_banner_exist())

    @minium.skipUnless(condition=config.platform != "ide", reason="仅真机支持人工客服跳转")
    def test_banner_jump(self):
        """
        测试真机点击广告位跳转人工客服
        """

        self.homepage.click_banner()
        time.sleep(2)
        path = self.homepage.current_path
        try:
            self.assertEqual(path, route.home_page)
        finally:
            self.homepage.back_mini()

    @minium.ddt_case('author', 'note', 'brand', 'kind', 'hot_key')
    def test_rank_jump(self, value):
        """
        测试首页点击榜单跳转后的路径是否正确
        """

        self.homepage.click_Rank(rank_type=value)
        time.sleep(2)
        path = self.homepage.current_path
        self.assertEqual(path, route.rank_page)

    @minium.ddt_case(('author', '1'), ('note', '2'), ('brand', '3'))
    def test_my_collect_num(self, value):
        """
        测试我的博主/笔记/品牌收藏数量是否正确
        """
        types, num = value
        re = self.homepage.my_collect_num(rank_type=types)
        self.assertEqual(re, num)

    @minium.ddt_case('author', 'note', 'brand')
    def test_my_collect_jump(self, value):
        """
        测试我的博主/笔记/品牌收藏跳转后path是否正确
        """
        self.homepage.click_collect(types=value)
        time.sleep(5)
        path = self.homepage.current_path
        self.assertEqual(path, route.my_collect_page)

    @minium.ddt_case(('author', '0'), ('note', '0'))
    def test_my_monitor_num(self, value):
        """
        测试我的博主/笔记监控数量是否正确
        """
        types, num = value
        re = self.homepage.my_monitor_num(rank_type=types)
        self.assertEqual(re, num)

    @minium.ddt_case('author', 'note')
    def test_my_monitor_jump(self, value):
        """
        测试我的博主/笔记监控跳转后path是否正确
        """
        self.homepage.click_trace(types=value)
        time.sleep(5)
        path = self.homepage.current_path
        self.assertEqual(path, route.my_trace_page)

    @minium.ddt_case('author_rank', 'note_rank', 'brand_rank', 'hot_key_rank')
    def test_rank_num(self, types):
        """
        测试各个榜单的元素是否为5个
        """

        num = self.homepage.get_rank_num(types=types)
        self.assertEqual(num, 5)
        self.homepage.slide_to_rank(types=types, top=1)

    @minium.ddt_case('author_rank', 'note_rank', 'brand_rank', 'hot_key_rank')
    def test_rank_more_jump(self, types):
        """
        测试点击各个榜单的【查看更多】按钮，是否可以正确跳转到对应榜单tab
        """

        self.homepage.slide_to_rank(types=types)
        self.homepage.click_more(rank_type=types)
        time.sleep(1)
        path = self.homepage.current_path
        self.assertEqual(path, route.rank_page)
        self.homepage.slide_to_rank(types=types, top=1)

    def test_fans_rank_detail_ele(self):
        """
        1，测试博主涨粉榜的元素是否存在
        2，测试博主涨粉榜的榜单时间是否为前一天
        """

        self.homepage.slide_to_rank(types='author_rank')
        num = self.homepage.is_fans_rank_ele_exist()
        self.assertEqual(num, 5)
        self.assertEqual(Base.get_time(1), self.homepage.get_rank_time(types='author_rank'))
        self.homepage.slide_to_rank(types='author_rank', top=1)

    def test_fans_rank_click(self):
        """
        测试博主涨粉榜的跳转是否正确
        """

        self.homepage.slide_to_rank(types='author_rank')
        self.homepage.click_into_detail(rank_type='author')
        time.sleep(2)
        path = self.homepage.current_path
        self.assertEqual(path, route.author_detail_page)
        self.homepage.back()
        self.homepage.slide_to_rank(types='author_rank', top=1)

    def test_note_rank_detail_ele(self):
        """
        1，测试实时笔记榜的元素是否存在
        2，测试实时笔记榜的榜单时间是否为近48小时
        """

        self.homepage.slide_to_rank(types='note_rank')
        num = self.homepage.is_note_rank_ele_exist()
        times = self.homepage.get_rank_time(types='note_rank')
        self.assertEqual(num, 6)
        self.assertEqual(times, '近48小时')
        self.homepage.slide_to_rank(types='note_rank', top=1)

    def test_note_rank_click(self):
        """
        测试实时笔记榜的跳转是否正确
        """

        self.homepage.slide_to_rank(types='note_rank')
        self.homepage.click_into_detail(rank_type='note')
        time.sleep(2)
        path = self.homepage.current_path
        self.assertEqual(path, route.note_detail_page)
        self.homepage.back()
        self.homepage.slide_to_rank(types='note_rank', top=1)

    def test_brand_rank_detail_ele(self):
        """
        1，测试品牌商业投放榜的元素是否存在
        2，测试品牌商业投放榜的榜单时间是否为前一天
        """

        self.homepage.slide_to_rank(types='brand_rank')
        num = self.homepage.is_brand_rank_ele_exist()
        self.assertEqual(num, 4)
        self.assertEqual(Base.get_time(1), self.homepage.get_rank_time(types='brand_rank'))
        self.homepage.slide_to_rank(types='brand_rank', top=1)

    def test_brand_rank_click(self):
        """
        测试品牌商业投放榜的跳转是否正确
        """

        self.homepage.slide_to_rank(types='brand_rank')
        self.homepage.click_into_detail(rank_type='brand')
        time.sleep(2)
        path = self.homepage.current_path
        self.assertEqual(path, route.brand_detail_page)
        self.homepage.back()
        self.homepage.slide_to_rank(types='brand_rank', top=1)

    def test_hot_key_rank_detail_ele(self):
        """
        1，测试热搜词总量榜的元素是否存在
        2，测试热搜词总量榜的榜单时间是否为前一天
        """

        self.homepage.slide_to_rank(types='hot_key_rank')
        num = self.homepage.is_hot_key_rank_ele_exist()
        self.assertEqual(num, 2)
        self.assertEqual(Base.get_time(1), self.homepage.get_rank_time(types='hot_key_rank'))
        self.homepage.slide_to_rank(types='hot_key_rank', top=1)

    def test_hot_key_rank_click(self):
        """
        测试热搜词总量榜的跳转是否正确
        """

        self.homepage.slide_to_rank(types='hot_key_rank')
        self.homepage.click_into_detail(rank_type='hot_key')
        time.sleep(2)
        path = self.homepage.current_path
        self.assertEqual(path, route.hot_key_detail_page)
        self.homepage.back()
        self.homepage.slide_to_rank(types='hot_key_rank', top=1)
