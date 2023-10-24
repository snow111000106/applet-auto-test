#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/9/18
# @Author : chenxuehong
# @Version：V 0.1
# @File : MyCollectPage.py
# @desc : 我的收藏页面封装

from page.BasePage import BasePage
from conf import route, config
from common.base import Base
import time, math


class CollectPage(BasePage):

    # 顶部tab
    tab_name = "/page/view/view/u-tabs-swiper/view/scroll-view/view/view[{}]/u-badge"
    # 搜索按钮
    group_pop = {
        'enter': '/page/view/{}/view/view[1]/sort/view/view/view[1]',
        'confirm': '/page/view/{}/view/view[1]/sort/view/u-select/view/u-popup/view/view/scroll-view'
                   '/view/view[1]/view[3]',
        'cancel': '/page/view/{}/view/view[1]/sort/view/u-select/view/u-popup/view/view/scroll-view'
                  '/view/view[1]/view[1]',
        'group_name': '/page/view/{}/view/view[1]/sort/view/u-select/view/u-popup/view/view/scroll-view'
                      '/view/view[2]/picker-view'
    }
    # 博主卡片 从id2开始
    author_card = {
        'avatar': '/page/view/blogger/view/view[{}]/blogger-list-item/view/view/view[1]/img-lazy/u-image/view/image',
        'nickname': '/page/view/blogger/view/view[{}]/blogger-list-item/view/view/view[2]/view[1]',
        'label': '/page/view/blogger/view/view[{}]/blogger-list-item/view/view/view[2]/view[2]/view[{}]',
        'interaction': '/page/view/blogger/view/view[{}]/blogger-list-item/view/view/view[2]/view[3]/view[1]/view[2]',
        'liked_and_collect': '/page/view/blogger/view/view[{}]/blogger-list-item/view/view/view[2]/view[3]'
                             '/view[2]/view/view[2]',
        'fans_inc': '/page/view/blogger/view/view[{}]/blogger-list-item/view/view/view[2]/view[3]/view[3]/view/view[2]'
    }
    # 笔记卡片 从id2开始
    note_card = {
        'avatar': '/page/view/note/view/view[{}]/note-list-item/view/view[1]/view[1]/img-lazy/u-image/view/image',
        'title': '/page/view/note/view/view[{}]/note-list-item/view/view[1]/view[2]/view[1]/view[1]',
        'create_time': '/page/view/note/view/view[{}]/note-list-item/view/view[1]/view[2]/view[1]/view[2]/view',
        'author_name': '/page/view/note/view/view[{}]/note-list-item/view/view[1]/view[2]/view[2]/view[2]',
        'author_avatar': '/page/view/note/view/view[{}]/note-list-item/view/view[1]/view[2]/view[2]/view[1]/img-lazy'
                         '/u-image/view/image',
        'interaction': '/page/view/note/view/view[{}]/note-list-item/view/view[2]/view[1]/view[2]',
        'comment': '/page/view/note/view/view[{}]/note-list-item/view/view[2]/view[2]/view[2]',
        'collect': '/page/view/note/view/view[{}]/note-list-item/view/view[2]/view[3]/view[2]',
        'share': '/page/view/note/view/view[{}]/note-list-item/view/view[2]/view[4]/view[2]'
    }
    # 品牌卡片
    brand_card = {
        'avatar': '/page/view/brand/view/view[{}]/brand-list-item/view/view[1]/view[1]/view/img-lazy/u-image/view/image',
        'name': '/page/view/brand/view/view[{}]/brand-list-item/view/view[1]/view[2]/view[1]',
        'label': '/page/view/brand/view/view[{}]/brand-list-item/view/view[1]/view[2]/view[2]/view[{}]',
        'interaction': '/page/view/brand/view/view[{}]/brand-list-item/view/view[2]/view[1]/view/view[2]/label[1]',
        'author_num': '/page/view/brand/view/view[{}]/brand-list-item/view/view[2]/view[2]/view/view[2]/label[1]',
        'note_num': '/page/view/brand/view/view[{}]/brand-list-item/view/view[2]/view[3]/view/view[2]/label[1]',
        'interaction_inc': '/page/view/brand/view/view[{}]/brand-list-item/view/view[2]/view[3]/view/view[2]/label[1]',
        'author_num_inc': '/page/view/brand/view/view[{}]/brand-list-item/view/view[2]/view[2]/view/view[2]/label[3]',
        'note_num_inc': '/page/view/brand/view/view[{}]/brand-list-item/view/view[2]/view[3]/view/view[2]/label[3]'
    }
    # 品类卡片
    kind_card = {
        'name': '/page/view/category/view/view[1]/view[{}]/category-list-item/view/view[1]/view[1]',
        'label': '/page/view/category/view/view[1]/view[{}]/category-list-item/view/view[1]/view[2]/view[{}]',
        'note_num': '/page/view/category/view/view[1]/view[{}]/category-list-item/view/view[2]/view[1]/view[1]',
        'interaction': '/page/view/category/view/view[1]/view[{}]/category-list-item/view/view[2]/view[2]/view[1]'
    }
    # 热搜词卡片
    hot_keyword_card = {
        'name': '/page/view/hot-word/view/view/view[{}]/view[1]/text',  # 从id2开始
        'note_num': '/page/view/hot-word/view/view/view[{}]/view[2]',   # 从id2开始
        'interaction': '/page/view/hot-word/view/view/view[{}]/view[3]',  # 从id2开始
        'hot_value': '/page/view/hot-word/view/view/view[{}]/view[4]/text'  # 从id2开始
    }
    # 页面为空提示
    empty_tips = '/page/view/{}/view/view{}/no-collect/view/view[1]/text'
    # 去看看
    jump = '/page/view/{}/view/view{}/no-collect/view/view[2]/view'

    def into_my_collect(self):
        """
        进入我的收藏页
        """
        self.navigate_to_open(route.my_collect_page)
        time.sleep(1)
        return self

    def select_tab(self, tab_name):
        """选择tab"""
        tab_mapping = {
            '博主': 1,
            '笔记': 2,
            '品牌': 3,
            '品类': 4,
            '热搜词': 5
        }

        tab_index = tab_mapping.get(tab_name)

        if tab_index is not None:
            self.get_element(self.tab_name.format(tab_index)).click()
            time.sleep(1)
        else:
            print('select_tab-榜单类型输入错误，仅支持博主/笔记/品牌/品类/热搜词')

        return self

    def click_into_detail(self, types):
        """点击进入详情页"""
        if types == '博主':
            self.get_element(self.author_card['avatar'].format(2)).click()
        elif types == '笔记':
            self.get_element(self.note_card['avatar'].format(2)).click()
        elif types == '品牌':
            self.get_element(self.brand_card['avatar'].format(1)).click()
        elif types == '品类':
            self.get_element(self.kind_card['name'].format(1)).click()
        elif types == '热搜词':
            self.get_element(self.hot_keyword_card['name'].format(2)).click()
        else:
            print('click_into_detail-库类型输入错误,仅支持博主/笔记/品牌/品类/热搜词')
        return self

    def switch_group(self, types, value):
        """切换分组"""
        if types == '博主':
            self.get_element(self.group_pop['enter'].format('blogger')).click()
            self.get_element(self.group_pop['group_name'].format('blogger')).trigger("change", {"value": value})
            self.get_element(self.group_pop['confirm'].format('blogger')).click()
        elif types == '笔记':
            self.get_element(self.group_pop['enter'].format('note')).click()
            self.get_element(self.group_pop['group_name'].format('note')).trigger("change", {"value": value})
            self.get_element(self.group_pop['confirm'].format('note')).click()
        else:
            print('switch_group-分组类型输入错误，仅支持博主/笔记')

    def get_author_info(self, group_id=False):
        """获取博主列表数据"""
        page = math.ceil(config.author_collect / 20)
        author_list = []
        if group_id == 1:
            num = config.author_collect_group1
        else:
            num = config.author_collect

        self.check_scroll(page)
        for i in range(num):
            nickname = self.get_context(self.author_card['nickname'].format(i + 2))
            interaction = self.get_context(self.author_card['interaction'].format(i + 2))
            liked_and_collect = self.get_context(self.author_card['liked_and_collect'].format(i + 2))
            fans_inc = self.get_context(self.author_card['fans_inc'].format(i + 2))
            author_list.append([i + 1, nickname, Base.convert_to_float_with_unit(interaction),
                                Base.convert_to_float_with_unit(liked_and_collect),
                                Base.convert_to_float_with_unit(fans_inc)])
        self.check_scroll(page, top=True)
        return author_list

    def get_note_info(self, group_id=False):
        """获取笔记列表数据"""
        page = math.ceil(config.note_collect / 20)
        note_list = []
        if group_id == 1:
            num = config.note_collect_group1
        else:
            num = config.note_collect

        self.check_scroll(page)
        for i in range(num):
            title = self.get_context(self.note_card['title'].format(i + 2))
            create_time = self.get_context(self.note_card['create_time'].format(i + 2))
            author_name = self.get_context(self.note_card['author_name'].format(i + 2))
            interaction = self.get_context(self.note_card['interaction'].format(i + 2))
            comment = self.get_context(self.note_card['comment'].format(i + 2))
            collect = self.get_context(self.note_card['collect'].format(i + 2))
            share = self.get_context(self.note_card['share'].format(i + 2))
            note_list.append([i + 1, title, create_time, author_name, Base.convert_to_float_with_unit(interaction),
                              Base.convert_to_float_with_unit(comment), Base.convert_to_float_with_unit(collect),
                              Base.convert_to_float_with_unit(share)])
        self.check_scroll(page, top=True)
        return note_list

    def get_brand_info(self):
        """获取品牌列表数据"""
        page = math.ceil(config.brand_collect / 20)
        brand_list = []

        self.check_scroll(page)
        for i in range(config.brand_collect):
            name = self.get_context(self.brand_card['name'].format(i + 1))
            interaction = self.get_context(self.brand_card['interaction'].format(i + 1))
            author_num = self.get_context(self.brand_card['author_num'].format(i + 1))
            note_num = self.get_context(self.brand_card['note_num'].format(i + 1))
            brand_list.append([i + 1, name, Base.convert_to_float_with_unit(interaction),
                              Base.convert_to_float_with_unit(author_num), Base.convert_to_float_with_unit(note_num)])
        self.check_scroll(page, top=True)
        return brand_list

    def get_kind_info(self):
        """获取品类列表数据"""
        page = math.ceil(config.kind_collect / 20)
        kind_list = []

        self.check_scroll(page)
        for i in range(config.kind_collect):
            name = self.get_context(self.kind_card['name'].format(i + 1))
            interaction = self.get_context(self.kind_card['interaction'].format(i + 1))
            note_num = self.get_context(self.kind_card['note_num'].format(i + 1))
            kind_list.append([i + 1, name, Base.convert_to_float_with_unit(interaction),
                              Base.convert_to_float_with_unit(note_num)])
        self.check_scroll(page, top=True)
        return kind_list

    def get_hot_keyword_info(self):
        """获取热搜词列表数据"""
        page = math.ceil(config.hot_keyword_collect / 20)
        hot_keyword_list = []

        self.check_scroll(page)
        for i in range(config.hot_keyword_collect):
            name = self.get_context(self.hot_keyword_card['name'].format(i + 2))
            interaction = self.get_context(self.hot_keyword_card['interaction'].format(i + 2))
            note_num = self.get_context(self.hot_keyword_card['note_num'].format(i + 2))
            hot_value = self.get_context(self.hot_keyword_card['hot_value'].format(i + 2))
            hot_keyword_list.append([i + 1, name, Base.convert_to_float_with_unit(interaction),
                                     Base.convert_to_float_with_unit(note_num),
                                     Base.convert_to_float_with_unit(hot_value)])
        self.check_scroll(page, top=True)
        return hot_keyword_list

    def get_empty_tips(self, types):
        """获取页面为空提示"""
        content = None
        if types == '博主':
            content = self.get_context(self.empty_tips.format('blogger', '[2]'))
        elif types == '笔记':
            content = self.get_context(self.empty_tips.format('note', '[2]'))
        elif types == '品牌':
            content = self.get_context(self.empty_tips.format('brand', ''))
        elif types == '品类':
            content = self.get_context(self.empty_tips.format('category', ''))
        elif types == '热搜词':
            content = self.get_context(self.empty_tips.format('hot-word', ''))
        else:
            print('get_empty_tips-类型输入错误，仅支持博主/笔记/品牌/品类/热搜词')
        return content

    def click_jump(self, types):
        """点击去看看"""
        if types == '博主':
            self.get_element(self.jump.format('blogger', '[2]')).click()
        elif types == '笔记':
            self.get_element(self.jump.format('note', '[2]')).click()
        elif types == '品牌':
            self.get_element(self.jump.format('brand', '')).click()
        elif types == '品类':
            self.get_element(self.jump.format('category', '')).click()
        elif types == '热搜词':
            self.get_element(self.jump.format('hot-word', '')).click()
        else:
            print('get_empty_tips-类型输入错误，仅支持博主/笔记/品牌/品类/热搜词')