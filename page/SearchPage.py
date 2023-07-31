#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/7/3
# @Author : chenxuehong
# @Version：V 0.1
# @File : SearchPage.py
# @desc : 搜索页面封装

from page.BasePage import BasePage
from conf import route,config
import time


class SearchPage(BasePage):

    # 搜索框
    search_frame = "input[placeholder='搜索博主/笔记/品牌/品类/热搜词']"
    # 搜索按钮
    search_btn = '/page/view/view[1]/view/u-search/view/view[2]'
    # 全部tab
    all_tab = '//*[@id="u-tab-item-0"]'
    # 博主tab
    author_tab = '//*[@id="u-tab-item-1"]'
    # 笔记tab
    note_tab = '//*[@id="u-tab-item-2"]'
    # 品牌tab
    brand_tab = '//*[@id="u-tab-item-3"]'
    # 品类tab
    kend_tab = '//*[@id="u-tab-item-4"]'
    # 热搜词tab
    hot_key_tab = '//*[@id="u-tab-item-5"]'
    # 全部tab-博主模块
    all_tab_author = {'avatar': '/page/view/view[2]/all-result/view/view/view/view[1]/view[2]/view[{}]/blogger-item'
                                '/view/view[1]/view[1]/img-lazy/u-image/view/image',
                      'name': '/page/view/view[2]/all-result/view/view/view/view[1]/view[2]/view[{}]/blogger-item/view/'
                              'view[1]/view[2]/view[1]',
                      'label': '/page/view/view[2]/all-result/view/view/view/view[1]/view[2]/view[{}]/blogger-item'
                               '/view/view[1]/view[2]/view[2]/view',
                      'liked': '/page/view/view[2]/all-result/view/view/view/view[1]/view[2]/view[{}]'
                               '/blogger-item/view/view[1]/view[2]/view[3]',
                      'fans': '/page/view/view[2]/all-result/view/view/view/view[1]/view[2]/view[{}]'
                              '/blogger-item/view/view[2]/view[1]',
                      'more': '/page/view/view[2]/all-result/view/view/view/view[1]/view[2]/view[4]/view[1]/text',
                      'item': '/page/view/view[2]/all-result/view/view/view/view[1]/view[2]'
                      }

    def into_search(self):
        """
        进入搜索页
        """
        self.navigate_to_open(route.search_page)
        time.sleep(1)
        return self

    def input_key(self, ele, value):
        """
        输入框输入
        """
        try:
            if config.platform != 'ios':
                self.get_element(ele).input("")  # 清空输入
                self.get_element(ele).input(value)
            else:
                self.get_element(ele).trigger("input", {"value": ""})
                self.get_element(ele).trigger("input", {"value": value})
        except:
            print('输入错误，报错元素{}'.format(ele))

    def search(self, value):
        """
        搜索关键字
        """
        try:
            self.input_key(ele=self.search_frame, value=value)
            self.get_element(self.search_btn).click()
            time.sleep(1)
        except Exception as e:
            print(e)

    def is_author_ele_exist(self):
        """判断全部tab下博主模块的元素是否存在"""

        result_1 = self.is_ele_exist(self.all_tab_author['avatar'].format(1))
        result_2 = self.is_ele_exist(self.all_tab_author['name'].format(1))
        result_3 = self.is_ele_exist(self.all_tab_author['label'].format(1))
        result_4 = self.is_ele_exist(self.all_tab_author['liked'].format(1))
        result_5 = self.is_ele_exist(self.all_tab_author['fans'].format(1))

        return result_1+result_2+result_3+result_4+result_5

