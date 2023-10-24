#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/9/19
# @Author : chenxuehong
# @Version：V 0.1
# @File : test_my_collection.py
# @desc : 我的收藏页面测试用例-页面不为空

import time
import minium
from testcase.vip_6.BaseCase import BaseCase
from page.MyCollectPage import CollectPage
from conf import config
from conf import route


@minium.ddt_class
class CollectPageTest(BaseCase):

    def __init__(self, methodName='runTest'):
        super(CollectPageTest, self).__init__(methodName)
        self.collectpage = CollectPage(self)

    def setUp(self):
        self.collectpage.into_my_collect()

    def tearDown(self):
        self.collectpage.go_to_home()
        time.sleep(1)

    @minium.ddt_case(('博主', route.author_detail_page), ('笔记', route.note_detail_page), ('品牌', route.brand_detail_page),
                     ('品类', route.kind_detail_page), ('热搜词', route.hot_key_detail_page))
    def test_into_detail(self, value):
        """
        测试我的收藏页面跳转详情页
        """
        try:
            types, re_route = value
            self.collectpage.select_tab(tab_name=types)
            self.collectpage.click_into_detail(types=types)
            routes = self.collectpage.current_path
            time.sleep(2)
            self.assertEqual(routes, re_route)
        finally:
            self.collectpage.back(delta=1)

    def test_author(self):
        """
        测试我的收藏页面-博主页面
        """
        self.collectpage.select_tab(tab_name='博主')
        info = self.collectpage.get_author_info()
        print(info)
        self.assertEqual(len(info), config.author_collect)

    def test_note(self):
        """
        测试我的收藏页面-笔记页面
        """
        self.collectpage.select_tab(tab_name='笔记')
        info = self.collectpage.get_note_info()
        self.assertEqual(len(info), config.note_collect)

    def test_brand(self):
        """
        测试我的收藏页面-品牌页面
        """
        self.collectpage.select_tab(tab_name='品牌')
        info = self.collectpage.get_brand_info()
        self.assertEqual(len(info), config.brand_collect)

    def test_kind(self):
        """
        测试我的收藏页面-品类页面
        """
        self.collectpage.select_tab(tab_name='品类')
        info = self.collectpage.get_kind_info()
        self.assertEqual(len(info), config.kind_collect)

    def test_hot_keyword(self):
        """
        测试我的收藏页面-热搜词页面
        """
        self.collectpage.select_tab(tab_name='热搜词')
        info = self.collectpage.get_hot_keyword_info()
        self.assertEqual(len(info), config.hot_keyword_collect)

    def test_author_group(self):
        """
        测试我的收藏页面-博主列表切换分组
        """
        self.collectpage.select_tab(tab_name='博主')
        self.collectpage.switch_group(types='博主', value=[1])
        info = self.collectpage.get_author_info(group_id=1)
        time.sleep(2)
        self.assertEqual(len(info), config.author_collect_group1)

    def test_note_group(self):
        """
        测试我的收藏页面-笔记列表切换分组
        """
        self.collectpage.select_tab(tab_name='笔记')
        self.collectpage.switch_group(types='笔记', value=[1])
        info = self.collectpage.get_note_info(group_id=1)
        time.sleep(2)
        self.assertEqual(len(info), config.note_collect_group1)

