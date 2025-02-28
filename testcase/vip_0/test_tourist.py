#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/10/7
# @Author : chenxuehong
# @Version：V 0.1
# @File : test_tourist.py
# @desc :游客权限测试用例

import time
import minium
from conf import route
from testcase.vip_0.BaseCase import BaseCase
from page.LoginPage import LoginPage
from page.HomePage import HomePage
from page.UserPage import UserPage
from page.SearchPage import SearchPage


@minium.ddt_class
class TouristTest(BaseCase):

    # 测试游客权限

    def __init__(self, methodName='runTest'):
        super(TouristTest, self).__init__(methodName)
        self.userpage = UserPage(self)
        self.homepage = HomePage(self)
        self.loginpage = LoginPage(self)
        self.searchpage = SearchPage(self)

    def tearDown(self):
        self.homepage.go_to_home()
        time.sleep(1)

    @minium.ddt_case('author', 'note', 'brand')
    def test_my_collect_num(self, rank_type):
        """
        测试游客不显示我的收藏数
        """
        self.homepage.go_to_home()
        time.sleep(1)
        num = self.homepage.my_collect_num(rank_type=rank_type)
        self.assertEqual(num, '-')

    @minium.ddt_case('author', 'note')
    def test_my_monitor_num(self, rank_type):
        """
        测试游客不显示我的监控数
        """
        self.homepage.go_to_home()
        time.sleep(1)
        num = self.homepage.my_monitor_num(rank_type=rank_type)
        self.assertEqual(num, '-')

    @minium.ddt_case('author', 'note', 'brand')
    def test_my_collect_jump(self, value):
        """
        测试游客点击我的博主/笔记/品牌收藏跳转后path是否正确
        """
        self.homepage.go_to_home()
        self.homepage.click_collect(types=value)
        time.sleep(5)
        path = self.homepage.current_path
        self.assertEqual(path, route.login_index_page)

    @minium.ddt_case('author', 'note')
    def test_my_monitor_jump(self, value):
        """
        测试游客点击我的博主/笔记监控跳转后path是否正确
        """
        self.homepage.go_to_home()
        self.homepage.click_trace(types=value)
        time.sleep(5)
        path = self.homepage.current_path
        self.assertEqual(path, route.login_index_page)

    @minium.ddt_case('author', 'note', 'brand', 'hot_key')
    def test_home_rank_jump(self, value):
        """
        测试游客首页点击榜单跳转到登录页
        """
        self.homepage.go_to_home()
        self.homepage.click_into_detail(rank_type=value)
        time.sleep(2)
        path = self.homepage.current_path
        self.assertEqual(path, route.login_index_page)

    @minium.ddt_case('my_collect', 'my_trace', 'my_set', 'vip_btn')
    def test_user_page_jump(self, types):
        """
        测试游客在我的页面点击各个入口跳转登录页
        """
        self.userpage.into_user_center()
        self.userpage.click_ele(types=types)
        time.sleep(2)
        path = self.userpage.current_path
        self.assertEqual(path, route.login_index_page)

    def test_vip_page_jump(self):
        """
        测试游客搜索后跳转登录页面
        """
        self.searchpage.into_search()
        self.searchpage.search(value='测试')
        time.sleep(2)
        path = self.searchpage.current_path
        self.assertEqual(path, route.login_index_page)

    def test_authorLib(self):
        """
        测试游客的博主库无法查看
        """
        self.searchpage.into_search()
        self.searchpage.select_tab(tab_name='博主')
        status = self.searchpage.is_vip_have_login(tab_name='blogger')
        self.assertTrue(status)

    @minium.ddt_case('粉丝数最多', '涨粉数最多', '赞藏最多')
    def test_authorLib_sort(self, sort_types):
        """
        测试游客的博主库无法切换排序
        """
        self.searchpage.into_search()
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_sort(types='博主', sort_types=sort_types)
        status = self.searchpage.is_vip_have_login(tab_name='blogger')
        self.assertTrue(status)

    def test_authorLib_filter_by_one_first_label(self):
        """
        测试游客的博主库无法筛选单个博主一级标签
        """
        self.searchpage.into_search()
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.authorLib_filter_by_label(first_label='时尚', second_label='全部')
        status = self.searchpage.is_vip_have_login(tab_name='blogger')
        self.assertTrue(status)

    def test_authorLib_filter_by_one_fans_label(self):
        """
        测试游客的博主库无法筛选单个粉丝标签
        """
        self.searchpage.into_search()
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.authorLib_filter_by_fans_label(fans_labels='旅行达人')
        status = self.searchpage.is_vip_have_login(tab_name='blogger')
        self.assertTrue(status)

    def test_authorLib_filter_by_brand_cooperate(self):
        """
        测试游客的博主库无法筛选有品牌合作
        """
        self.searchpage.into_search()
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.authorLib_filter_by_brand_cooperate()
        self.searchpage.scroll_filter_item(types='author')
        status = self.searchpage.is_vip_have_login(tab_name='blogger')
        self.assertTrue(status)

    def test_authorLib_filter_by_author_types(self):
        """
        测试游客的博主库无法筛选博主属性
        """
        self.searchpage.into_search()
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_author_filter(filter_types='博主信息', types='博主属性', value='企业账号')
        status = self.searchpage.is_vip_have_login(tab_name='blogger')
        self.assertTrue(status)

    def test_noteLib(self):
        """
        测试游客可查看笔记库前10条数据
        """
        self.searchpage.into_search()
        self.searchpage.select_tab(tab_name='笔记')
        self.searchpage.check_scroll(page=1)
        status = self.searchpage.is_vip_have_login(tab_name='note', ids='12')
        self.assertTrue(status)

    @minium.ddt_case('互动量', '点赞数', '评论数', '收藏数')
    def test_noteLib_sort(self, sort_types):
        """
        测试游客的笔记库可以切换排序
        """
        self.searchpage.into_search()
        self.searchpage.select_tab(tab_name='笔记')
        self.searchpage.select_sort(types='笔记', sort_types=sort_types)
        status = self.searchpage.is_vip_have_login(tab_name='note', ids='12')
        self.assertTrue(status)

    def test_noteLib_filter_by_first_label(self):
        """
        测试游客的笔记库无法筛选单个笔记一级标签
        """
        self.searchpage.into_search()
        self.searchpage.select_tab(tab_name='笔记')
        self.searchpage.noteLib_filter_by_label(first_label='时尚', second_label='全部')
        status = self.searchpage.is_vip_have_login(tab_name='note')
        self.assertTrue(status)

    @minium.ddt_case('6小时', '近30天', '近90天')
    def test_noteLib_filter_by_create_time(self, create_time):
        """
        测试游客的笔记库无法筛选笔记发布时间
        """
        self.searchpage.into_search()
        self.searchpage.select_tab(tab_name='笔记')
        self.searchpage.noteLib_filter_by_create_time(create_time=create_time)
        status = self.searchpage.is_vip_have_login(tab_name='note')
        if create_time == '近30天':
            self.assertFalse(status)
        else:
            self.assertTrue(status)

    def test_brandLib(self):
        """
        测试游客的品牌库可查看前10条
        """
        self.searchpage.into_search()
        self.searchpage.select_tab(tab_name='品牌')
        self.searchpage.check_scroll(page=1)
        status = self.searchpage.is_vip_have_login(tab_name='brand', ids='12')
        self.assertTrue(status)

    @minium.ddt_case('最近投放时间', '昨日互动增量', '总互动量', '总博主数', '总笔记数')
    def test_brandLib_sort(self, sort_types):
        """
        测试游客的品牌库无法切换排序
        """
        self.searchpage.into_search()
        self.searchpage.select_tab(tab_name='品牌')
        self.searchpage.select_sort(types='品牌', sort_types=sort_types)
        status = self.searchpage.is_vip_have_login(tab_name='brand')
        if sort_types == '最近投放时间':
            self.assertFalse(status)
        else:
            self.assertTrue(status)

    def test_brandLib_filter_by_first_label(self):
        """
        测试游客的品牌库无法筛选一级品牌标签
        """
        self.searchpage.into_search()
        self.searchpage.select_tab(tab_name='品牌')
        self.searchpage.brandLib_filter_by_label(first_label='日用/宠物', second_label='全部')
        status = self.searchpage.is_vip_have_login(tab_name='brand')
        self.assertTrue(status)

    def test_kindLib(self):
        """
        测试游客的品类库可查看前10条
        """
        self.searchpage.into_search()
        self.searchpage.select_tab(tab_name='品类')
        self.searchpage.check_scroll(page=1)
        status = self.searchpage.is_vip_have_login(tab_name='category', ids='12')
        self.assertTrue(status)

    @minium.ddt_case('笔记最多', '互动量最多')
    def test_kindLib_sort(self, sort_types):
        """
        测试游客的品类库无法筛选排序
        """
        self.searchpage.into_search()
        self.searchpage.select_tab(tab_name='品类')
        self.searchpage.select_sort(types='品类', sort_types=sort_types)
        if sort_types == '笔记最多':
            status = self.searchpage.is_vip_have_login(tab_name='category', ids='12')
            self.assertTrue(status)
        else:
            status = self.searchpage.is_vip_have_login(tab_name='category')
            self.assertTrue(status)

    @minium.ddt_case('近7天', '近15天', '近30天')
    def test_kindLib_filter_by_times(self, times):
        """
        测试游客的品类库可筛选30天以内的数据
        """
        self.searchpage.into_search()
        self.searchpage.select_tab(tab_name='品类')
        self.searchpage.kindLib_filter_by_times(times=times)
        self.searchpage.check_scroll(page=1)
        status = self.searchpage.is_vip_have_login(tab_name='category', ids='12')
        self.assertTrue(status)

    @minium.ddt_case('近90天', '近180天', '近360天')
    def test_kindLib_filter_by_times2(self, times):
        """
        测试游客的品类库无法筛选超过30天的数据
        """
        self.searchpage.into_search()
        self.searchpage.select_tab(tab_name='品类')
        self.searchpage.kindLib_filter_by_times(times=times)
        status = self.searchpage.is_vip_have_login(tab_name='category')
        self.assertTrue(status)

    def test_kindLib_filter_by_first_label(self):
        """
        测试游客的品类库无法筛选一级标签
        """
        self.searchpage.into_search()
        self.searchpage.select_tab(tab_name='品类')
        self.searchpage.kindLib_filter_by_label(first_label='美食/饮食', second_label='全部')
        status = self.searchpage.is_vip_have_login(tab_name='category')
        self.assertTrue(status)

    def test_hotWordLib(self):
        """
        测试游客的热搜词库可查看前10条
        """
        self.searchpage.into_search()
        self.searchpage.select_tab(tab_name='热搜词')
        self.searchpage.check_scroll(page=5)
        status = self.searchpage.is_vip_have_login(tab_name='hot-word', ids='3')
        self.assertTrue(status)

    def test_hotWordLib_filter_by_first_label(self):
        """
        测试游客的热搜词库无法筛选单个一级标签
        """
        self.searchpage.into_search()
        self.searchpage.select_tab(tab_name='热搜词')
        self.searchpage.hotWordLib_filter_by_label(first_label='体育赛事', second_label='全部')
        status = self.searchpage.is_vip_have_login(tab_name='hot-word')
        self.assertTrue(status)
