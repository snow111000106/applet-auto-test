#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/5/10
# @Author : chenxuehong
# @Version：V 0.1
# @File : HomePage.py
# @desc : 主页封装

from page.BasePage import BasePage
import time


class HomePage(BasePage):

    # 广告位
    banner_picture = "/page/view/view[2]/page-banner/view/swiper/swiper-item/button/image"
    # 博主榜
    author_rank = "/page/view/view[2]/view[3]/ranking-list-item/view/view/view[1]/view/image"
    # 笔记榜
    note_rank = "/page/view/view[2]/view[3]/ranking-list-item/view/view/view[2]/view/image"
    # 品牌榜
    brand_rank = "/page/view/view[2]/view[3]/ranking-list-item/view/view/view[3]/view/image"
    # 品类榜
    kind_rank = "/page/view/view[2]/view[3]/ranking-list-item/view/view/view[4]/view/image"
    # 热搜词榜
    hot_key_rank = "/page/view/view[2]/view[3]/ranking-list-item/view/view/view[5]/view/image"
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
    author_rank_nick_name = '/page/view/view[3]/author-goods/view/view/view[2]/view/author-take-goods-list-item[1]/' \
                            'view/view/view[2]/view[1]/view[2]/text[1]'
    # 博主涨粉榜-头像
    author_rank_avatar = '/page/view/view[3]/author-goods/view/view/view[2]/view/author-take-goods-list-item[1]/view/' \
                         'view/view[1]'
    # 博主涨粉榜-榜单时间
    author_rank_time = '/page/view/view[3]/author-goods/view/view/view[1]/view/text[2]'
    # 博主涨粉榜-粉丝数
    author_rank_fans = '/page/view/view[3]/author-goods/view/view/view[2]/view/author-take-goods-list-item[1]' \
                       '/view/view/view[2]/view[1]/view[2]/text[2]'
    # 博主涨粉榜-粉丝增量
    author_rank_fans_inc = '/page/view/view[3]/author-goods/view/view/view[2]/view/author-take-goods-list-item[1]' \
                           '/view/view/view[2]/view[2]/text[1]'
    # 实时笔记榜-封面
    note_rank_picture = '/page/view/view[3]/author-fans/view/view/view[2]/view/notes-list-item[1]/view/view/view[1]' \
                        '/img-lazy/u-image/view/image'
    # 实时笔记榜-标题
    note_rank_title = '/page/view/view[3]/author-fans/view/view/view[2]/view/notes-list-item[1]/view/view/view[2]' \
                      '/view[2]/text'
    # 实时笔记榜-榜单时间
    note_rank_time = '/page/view/view[3]/author-fans/view/view/view[1]/view/text[2]'
    # 实时笔记榜-笔记创建时间
    note_rank_create_time = '/page/view/view[3]/author-fans/view/view/view[2]/view/notes-list-item[1]/view' \
                            '/view/view[2]/view[2]/view[1]/text'
    # 实时笔记榜-博主头像
    note_rank_avatar = '/page/view/view[3]/author-fans/view/view/view[2]/view/notes-list-item[1]/view/view/view[2]' \
                       '/view[2]/view[2]/view[1]/img-lazy/u-image/view/image'
    # 实时笔记榜-博主名称
    note_rank_name = '/page/view/view[3]/author-fans/view/view/view[2]/view/notes-list-item[1]/view/view/view[2]' \
                     '/view[2]/view[2]/view[1]/text'
    # 实时笔记榜-互动量
    note_rank_interact = '/page/view/view[3]/author-fans/view/view/view[2]/view/notes-list-item[1]/view/view/view[2]' \
                         '/view[2]/view[2]/view[2]/text[1]'
    # 品牌商业投放榜-榜单时间
    brand_rank_time = '/page/view/view[3]/douyin-shop/view/view/view[1]/view/text[2]'
    # 品牌商业投放榜-品牌名称
    brand_rank_name = '/page/view/view[3]/douyin-shop/view/view/view[2]/view/brand-commercial-launch-list-item[1]/view' \
                      '/view/view[2]/view[1]/view[2]/text[1]'
    # 品牌商业投放榜-商业笔记数
    brand_rank_business_note_num = '/page/view/view[3]/douyin-shop/view/view/view[2]/view' \
                                   '/brand-commercial-launch-list-item[1]/view/view/view[2]/view[1]/view[2]/text[1]'
    # 品牌商业投放榜-商业互动量
    brand_rank_business_note_interact = '/page/view/view[3]/douyin-shop/view/view/view[2]/view/' \
                                        'brand-commercial-launch-list-item[1]/view/view/view[2]/view[2]/text[1]'
    # 品牌商业投放榜-品牌头像
    brand_rank_avatar = '/page/view/view[3]/douyin-shop/view/view/view[2]/view/brand-commercial-launch-list-item[1]' \
                        '/view/view/view[1]/img-lazy/u-image/view/image'
    # 热搜词总量榜-时间
    hot_key_rank_time = '/page/view/view[3]/popular-products/view/view/view[1]/view/text[2]'
    # 热搜词总量榜-名称
    hot_key_rank_name = '/page/view/view[3]/popular-products/view/view/view[2]/view/hot-search-term-list-item[1]/' \
                        'view/view/view/text'
    # 热搜词总量榜-热度值
    hot_key_rank_value = '/page/view/view[3]/popular-products/view/view/view[2]/view/hot-search-term-list-item[1]/' \
                         'view/view/view/view/text[1]'

    def click_Rank(self, rank_type):
        """ 点击跳转榜单 """

        if rank_type == 'author':
            self.get_element(self.author_rank).click()
        elif rank_type == 'note':
            self.get_element(self.note_rank).click()
        elif rank_type == 'brand':
            self.get_element(self.brand_rank).click()
        elif rank_type == 'kind':
            self.get_element(self.kind_rank).click()
        elif rank_type == 'hot_key':
            self.get_element(self.hot_key_rank).click()
        else:
            print('click_Rank-榜单类型输入错误，仅支持author，note，brand，hot_key')
        return self

    def click_collect(self, types):
        """点击跳转收藏"""
        if types == 'author':
            self.get_element(self.my_collect_author).click()
        elif types == 'note':
            self.get_element(self.my_collect_note).click()
        elif types == 'brand':
            self.get_element(self.my_collect_brand).click()
        else:
            print('click_collect-类型输入错误，仅支持author，note，brand')
        return self

    def click_trace(self, types):
        """点击跳转收藏"""
        if types == 'author':
            self.get_element(self.my_monitor_author).click()
        elif types == 'note':
            self.get_element(self.my_monitor_note).click()
        else:
            print('click_collect-类型输入错误，仅支持author，note')
        return self

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
        return self

    def click_into_detail(self, rank_type):
        """ 点击进入详情页 """

        if rank_type == 'author':
            self.get_element(self.author_rank_avatar).click()
        elif rank_type == 'note':
            self.get_element(self.note_rank_picture).click()
        elif rank_type == 'brand':
            self.get_element(self.brand_rank_avatar).click()
        elif rank_type == 'hot_key':
            self.get_element(self.hot_key_rank_name).click()
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

    def get_rank_time(self, types):
        """ 获取各个榜单的榜单时间 """
        if types == 'author_rank':
            times = self.get_context(ele=self.author_rank_time)
        elif types == 'note_rank':
            times = self.get_context(ele=self.note_rank_time)
        elif types == 'brand_rank':
            times = self.get_context(ele=self.brand_rank_time)
        elif types == 'hot_key_rank':
            times = self.get_context(ele=self.hot_key_rank_time)
        else:
            print('get_rank_time-榜单类型输入错误，仅支持author_rank，note_rank，brand_rank，hot_key_rank')
        return times

    def is_hot_key_rank_ele_exist(self):
        """ 验证热搜词总量榜的元素是否存在 """

        result_1 = self.is_ele_exist(self.hot_key_rank_name)
        result_2 = self.is_ele_exist(self.hot_key_rank_value)

        return result_1+result_2

    def is_brand_rank_ele_exist(self):
        """ 验证品牌商业投放榜的元素是否存在 """

        result_1 = self.is_ele_exist(self.brand_rank_avatar)
        result_2 = self.is_ele_exist(self.brand_rank_name)
        result_3 = self.is_ele_exist(self.brand_rank_business_note_num)
        result_4 = self.is_ele_exist(self.brand_rank_business_note_interact)

        return result_1+result_2+result_3+result_4

    def is_note_rank_ele_exist(self):
        """ 验证实时笔记榜的元素是否存在 """

        result_1 = self.is_ele_exist(self.note_rank_name)
        result_2 = self.is_ele_exist(self.note_rank_title)
        result_3 = self.is_ele_exist(self.note_rank_avatar)
        result_4 = self.is_ele_exist(self.note_rank_create_time)
        result_5 = self.is_ele_exist(self.note_rank_picture)
        result_6 = self.is_ele_exist(self.note_rank_interact)
        return result_1+result_2+result_3+result_4+result_5+result_6

    def is_fans_rank_ele_exist(self):
        """ 验证博主涨粉榜的元素是否存在 """

        result_1 = self.is_ele_exist(self.author_rank_time)
        result_2 = self.is_ele_exist(self.author_rank_nick_name)
        result_3 = self.is_ele_exist(self.author_rank_avatar)
        result_4 = self.is_ele_exist(self.author_rank_fans)
        result_5 = self.is_ele_exist(self.author_rank_fans_inc)
        return result_1+result_2+result_3+result_4+result_5

    def slide_to_rank(self, types, top=None):
        """滑动到各个榜单，适配iphone5"""

        if types == 'author_rank':
            if top is None:
                self.scroll_page(high=300)
            else:
                self.scroll_page(high=-300)
        elif types == 'note_rank':
            if top is None:
                self.scroll_page(high=670)
            else:
                self.scroll_page(high=-670)
        elif types == 'brand_rank':
            if top is None:
                self.scroll_page(high=1110)
            else:
                self.scroll_page(high=-1110)
        elif types == 'hot_key_rank':
            if top is None:
                self.scroll_page(high=1560)
            else:
                self.scroll_page(high=-1560)
        else:
            print("slide_to_rank-榜单类型输入错误，仅支持author_rank，note_rank，brand_rank，hot_key_rank")
        time.sleep(2)

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
