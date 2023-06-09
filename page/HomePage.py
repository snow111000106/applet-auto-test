#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/5/10
# @Author : chenxuehong
# @Version：V 0.1
# @File : HomePage.py
# @desc :

from page.BasePage import BasePage
import time


class HomePage(BasePage):

    # 广告位
    banner_picture = "/page/view/view[2]/page-banner/view/swiper/swiper-item/button/image"
    # 博主榜
    author_rank = ("text", '博主榜')
    # 笔记榜
    note_rank = ("text", '笔记榜')
    # 品牌榜
    brand_rank = ("text", '品牌榜')
    # 品类榜
    kind_rank = ("text", '品类榜')
    # 热搜词榜
    hot_key_rank = ("text", '热搜词榜')
    # 我的收藏-博主
    my_collect_author = "/page/view/view[3]/info-count/view/view[1]/view/view[1]/text[1]"
    # 我的收藏-笔记
    my_collect_note = "/page/view/view[3]/info-count/view/view[1]/view/view[2]/text[1]"
    # 我的收藏-品牌
    my_collect_brand = "/page/view/view[3]/info-count/view/view[1]/view/view[3]/text[1]"
    # 我的监控-博主
    my_monitor_author = "/page/view/view[3]/info-count/view/view[2]/view/view[1]/text[1]"
    # 我的监控-笔记
    my_monitor_note = "/page/view/view[3]/info-count/view/view[2]/view/view[2]/text[1]"
    # 博主涨粉榜item
    fans_inc_rank = "author-take-goods-list-item"
    # 实时笔记榜item
    realtime_note_rank = "notes-list-item"
    # 品牌商业投放榜item
    brand_commercial_rank = "brand-commercial-launch-list-item"
    # 热搜词总量榜item
    hot_key_count_rank = "hot-search-term-list-item"
    # 博主涨粉榜-查看更多
    fans_inc_rank_more = "/page/view/view[3]/author-goods/view/view/view[1]/text"
    # 实时笔记榜-查看更多
    realtime_note_rank_more = "/page/view/view[3]/author-fans/view/view/view[1]/text"
    # 品牌商业投放榜-查看更多
    brand_commercial_rank_more = "/page/view/view[3]/douyin-shop/view/view/view[1]/text"
    # 热搜词总量榜-查看更多
    hot_key_count_rank_more = "/page/view/view[3]/popular-products/view/view/view[1]/text"
    # 博主涨粉榜-昵称
    author_rank_nick_name = '/page/view/view[3]/author-goods/view/view/view[2]/view/author-take-goods-list-item[1]/view/view/view[2]/view[1]/view[2]/text[1]'
    # 博主涨粉榜-头像
    author_rank_author_avatar = '/page/view/view[3]/author-goods/view/view/view[2]/view/author-take-goods-list-item[1]/view/view/view[1]'
    # 博主涨粉榜-时间
    author_rank_time = '/page/view/view[3]/author-goods/view/view/view[1]/view/text[2]'
    # 博主涨粉榜-粉丝数
    author_rank_fans = '/page/view/view[3]/author-goods/view/view/view[2]/view/author-take-goods-list-item[1]/view/view/view[2]/view[1]/view[2]/text[2]'
    # 博主涨粉榜-粉丝增量
    author_rank_fans_inc = '/page/view/view[3]/author-goods/view/view/view[2]/view/author-take-goods-list-item[1]/view/view/view[2]/view[2]/text[1]'

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
            print('click_Rank-榜单类型输入错误，仅支持author，note，brand，hot_key')

    def click_more(self, rank_type):
        """ 点击查看更多 """
        if rank_type == 'author_rank':
            self.get_element(self.fans_inc_rank_more).click()
        elif rank_type == 'note_rank':
            self.get_element(self.realtime_note_rank_more).click()
        elif rank_type == 'brand_rank':
            self.get_element(self.brand_commercial_rank_more).click()
        elif rank_type == 'hot_key_rank':
            self.get_element(self.hot_key_count_rank_more).click()
        else:
            print('click_more-榜单类型输入错误，仅支持author_rank，note_rank，brand_rank，hot_key_rank')

    def click_into_detail(self, rank_type):
        """ 点击进入详情页 """
        if rank_type == 'author':
            self.get_element(self.author_rank_author_avatar).click()
        elif rank_type == 'note':
            self.get_elements(self.realtime_note_rank)[0].click()
        elif rank_type == 'brand':
            self.get_elements(self.brand_commercial_rank)[0].click()
        elif rank_type == 'hot_key':
            self.get_elements(self.hot_key_count_rank_more)[0].click()
        else:
            print('click_into_detail-榜单类型输入错误，仅支持author，note，brand，hot_key')

    def click_banner(self):
        """ 点击广告位跳转 """
        try:
            self.get_element(self.banner_picture).click()
        except:
            print('click_banner-广告位不存在')

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
            print('my_collect_num-收藏类型输入错误，仅支持author，note，brand')
        return num

    def my_monitor_num(self, rank_type):
        """ 获取收藏数量 """
        num = 0
        if rank_type == 'author':
            num = self.get_context(self.my_monitor_author)
        elif rank_type == 'note':
            num = self.get_context(self.my_monitor_note)
        else:
            print('my_monitor_num-监控类型输入错误,仅支持author，note')
        return num

    def is_banner_exist(self):
        """ 验证广告位是否存在 """
        result = self.is_ele_exist(self.banner_picture)
        return result

    def is_fans_rank_ele_exist(self):
        """ 验证博主涨粉榜的元素是否存在 """

        result_1 = self.is_ele_exist(self.author_rank_time)
        result_2 = self.is_ele_exist(self.author_rank_nick_name)
        result_3 = self.is_ele_exist(self.author_rank_author_avatar)
        result_4 = self.is_ele_exist(self.author_rank_fans)
        result_5 = self.is_ele_exist(self.author_rank_fans_inc)
        return result_1+result_2+result_3+result_4+result_5

    def slide_to_rank(self, types, top=None):
        """滑动到各个榜单"""
        if types == 'author_rank':
            if top is None:
                self.scroll(high=300)
            else:
                self.scroll(high=-300)
            time.sleep(3)
        elif types == 'note_rank':
            if top is None:
                self.scroll(high=670)
            else:
                self.scroll(high=-670)
            time.sleep(3)
        elif types == 'brand_rank':
            if top is None:
                self.scroll(high=1110)
            else:
                self.scroll(high=-1110)
            time.sleep(3)
        elif types == 'hot_key_rank':
            if top is None:
                self.scroll(high=1560)
            else:
                self.scroll(high=-1560)
            time.sleep(3)
        else:
            print("slide_to_rank-榜单类型输入错误，仅支持author_rank，note_rank，brand_rank，hot_key_rank")

    def get_rank_num(self, types):
        """ 获取榜单个数 """
        num = 0
        if types == 'author_rank':
            self.slide_to_rank(types=types)
            num_list = self.get_elements(self.fans_inc_rank)
            num = len(num_list)
        elif types == 'note_rank':
            self.slide_to_rank(types=types)
            num_list = self.get_elements(self.realtime_note_rank)
            num = len(num_list)
        elif types == 'brand_rank':
            self.slide_to_rank(types=types)
            num_list = self.get_elements(self.brand_commercial_rank)
            num = len(num_list)
        elif types == 'hot_key_rank':
            self.slide_to_rank(types=types)
            num_list = self.get_elements(self.hot_key_count_rank)
            num = len(num_list)
        else:
            print("get_rank_num-榜单类型输入错误，仅支持author_rank，note_rank，brand_rank，hot_key_rank")
        return num