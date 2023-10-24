#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/9/20
# @Author : chenxuehong
# @Version：V 0.1
# @File : test_my_monitor.py
# @desc : 我的监控页面测试用例-页面不为空
import time
import minium
from common.base import Base
from testcase.vip_6.BaseCase import BaseCase
from page.MyMonitorPage import MonitorPage


@minium.ddt_class
class MonitorPageTest(BaseCase):

    def __init__(self, methodName='runTest'):
        super(MonitorPageTest, self).__init__(methodName)
        self.monitorpage = MonitorPage(self)

    @classmethod
    def setUpClass(cls):
        super(MonitorPageTest, cls).setUpClass()
        cls.monitorpage = MonitorPage(cls)
        cls.monitorpage.into_my_monitor()

    def test_author(self):
        """
        测试我的监控页面-博主页面
        """
        self.monitorpage.select_tab(tab_name='博主')
        info = self.monitorpage.get_info(ids=[1], items=('name', 'red_id', 'monitor_time', 'status', 'monitor_fans_inc'),
                                         card=self.monitorpage.author_completed_card)
        re_info = Base.get_monitor_info(types='author_list', id=1)
        self.assertDictEqual(info[0], re_info)

    def test_note(self):
        """
        测试我的收藏页面-笔记页面
        """
        self.monitorpage.select_tab(tab_name='笔记')
        info = self.monitorpage.get_info(ids=[1], items=('title', 'create_time', 'author_name', 'monitor_time', 'status'),
                                         card=self.monitorpage.note_completed_card)
        re_info = Base.get_monitor_info(types='note_list', id=1)
        self.assertDictEqual(info[0], re_info)

    def test_brand(self):
        """
        测试我的收藏页面-品牌页面
        """
        self.monitorpage.select_tab(tab_name='品牌')
        info = self.monitorpage.get_info(ids=[1], items=('name', 'status', 'monitor_time', 'monitor_note_num', 'monitor_interaction'),
                                         card=self.monitorpage.brand_completed_card)
        re_info = Base.get_monitor_info(types='brand_list', id=1)
        self.assertDictEqual(info[0], re_info)

    def test_author_tend(self):
        """
        测试博主监控的趋势图
        """
        self.monitorpage.select_tab(tab_name='博主')
        info = self.monitorpage.get_tend_info(ids=[1], card=self.monitorpage.author_trends_pop)
        self.assertEqual(info[0], Base.get_monitor_info(types='author_list', id=1)['name'])

    def test_note_tend(self):
        """
        测试笔记监控的趋势图
        """
        self.monitorpage.select_tab(tab_name='笔记')
        info = self.monitorpage.get_tend_info(ids=[1], card=self.monitorpage.note_trends_pop)
        self.assertEqual(info[0], Base.get_monitor_info(types='note_list', id=1)['author_name'])