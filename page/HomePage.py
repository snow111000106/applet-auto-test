#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/5/10
# @Author : chenxuehong
# @Version：V 0.1
# @File : HomePage.py
# @desc :

from page.BasePage import BasePage


class HomePage(BasePage):

    banner_picture = "/page/view/view[2]/page-banner/view/swiper/swiper-item/button/image"
    author_rank = ("text", '博主榜')
    note_rank = ("text", '笔记榜')
    brand_rank = ("text", '品牌榜')
    kind_rank = ("text", '品类榜')
    hot_key_rank = ("text", '热搜词榜')
    my_collect_author = "/page/view/view[3]/info-count/view/view[1]/view/view[1]/text[1]"
    my_collect_note = "/page/view/view[3]/info-count/view/view[1]/view/view[2]/text[1]"
    my_collect_brand = "/page/view/view[3]/info-count/view/view[1]/view/view[3]/text[1]"
    my_monitor_author = "/page/view/view[3]/info-count/view/view[2]/view/view[1]/text[1]"
    my_monitor_note = "/page/view/view[3]/info-count/view/view[2]/view/view[2]/text[1]"
    fans_inc_rank = "author-take-goods-list-item"

    def click_Rank(self, rank_type):
        """ 点击跳转榜单 """
        if rank_type == 'author':
            self.get_element(self.author_rank[0], inner_text=self.author_rank[1]).click()
        elif rank_type == 'note':
            self.get_element(self.note_rank[0], inner_text=self.note_rank[1]).click()
        elif rank_type == 'brand':
            self.get_element(self.brand_rank[0], inner_text=self.brand_rank[1]).click()
        elif rank_type == 'kind':
            self.get_element(self.kind_rank[0], inner_text=self.kind_rank[1]).click()
        elif rank_type == 'hot_key':
            self.get_element(self.hot_key_rank[0], inner_text=self.hot_key_rank[1]).click()
        else:
            print('榜单类型输入错误')

    def my_collect_num(self, rank_type):
        """ 获取收藏数量 """
        num = 0
        if rank_type == 'author':
            num = self.get_context(self.my_collect_author)
        elif rank_type == 'note':
            num = self.get_context(self.my_collect_note)
        elif rank_type == 'brand':
            num = self.get_context(self.my_collect_brand)
        else:
            print('收藏类型输入错误')
        return num

    def my_monitor_num(self, rank_type):
        """ 获取收藏数量 """
        num = 0
        if rank_type == 'author':
            num = self.get_context(self.my_monitor_author)
        elif rank_type == 'note':
            num = self.get_context(self.my_monitor_note)
        else:
            print('监控类型输入错误')
        return num

    def is_banner_exist(self):
        """ 验证广告位是否存在 """
        result = self.is_ele_exist(self.banner_picture)
        return result

    def slide_to_fans_inc_rank(self, types='fans_inc_rank'):
        """滑动到涨粉榜"""
        if types == 'fans_inc_rank':
            self.scroll(high=256)
            self.sleep()
        else:
            self.scroll(high=-256)
            self.sleep()

    def get_fans_inc_rank_num(self):
        """ 获取博主涨粉榜个数 """
        self.slide_to_fans_inc_rank()
        num_list = self.get_elements(self.fans_inc_rank)
        num = len(num_list)
        return num