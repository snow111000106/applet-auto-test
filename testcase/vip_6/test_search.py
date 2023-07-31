#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/7/3
# @Author : chenxuehong
# @Version：V 0.1
# @File : test_search.py
# @desc : 企业版-搜索页面测试用例

import minium
from testcase.vip_6.BaseCase import BaseCase
from page.SearchPage import SearchPage


@minium.ddt_class
class SearchPageTest(BaseCase):

    def __init__(self, methodName='runTest'):
        super(SearchPageTest, self).__init__(methodName)
        self.searchpage = SearchPage(self)

    def setUp(self):
        self.searchpage.into_search()

    def tearDown(self):
        self.searchpage.go_to_home()

    @minium.ddt_case('测试', '福利', 'baby', '美妆')
    def test_search_author_keyword(self, value):
        """
        测试搜索后，博主模块的元素存在
        """
        self.searchpage.search(value=value)
        self.assertEqual(self.searchpage.is_author_ele_exist(), 5)