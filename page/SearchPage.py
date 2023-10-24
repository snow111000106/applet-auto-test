#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/7/3
# @Author : chenxuehong
# @Version：V 0.1
# @File : SearchPage.py
# @desc : 搜索页面封装

from page.BasePage import BasePage
from conf import route, config
from common.base import Base
import time, math


class SearchPage(BasePage):

    # 搜索框
    search_frame = "input[placeholder='搜索博主/笔记/品牌/品类/热搜词']"
    # 搜索按钮
    search_btn = '/page/view/view[1]/view/u-search/view/view[2]'
    # tab切换
    tab = '/page/view/view[1]/u-tabs/view/view/scroll-view/view/view[{}]'
    # 全部tab-博主模块
    all_tab_author = {'avatar': '/page/view/view[2]/all-result/view/view/view/view[1]/view[2]/view[{}]/blogger-item'
                                '/view/view[1]/view[1]/img-lazy/u-image/view/image',
                      'name': '/page/view/view[2]/all-result/view/view/view/view[1]/view[2]/view[{}]/blogger-item/view'
                              '/view[1]/view[2]/view[1]',
                      'label': '/page/view/view[2]/all-result/view/view/view/view[1]/view[2]/view[{}]/blogger-item'
                               '/view/view[1]/view[2]/view[2]/view',
                      'liked_and_collect': '/page/view/view[2]/all-result/view/view/view/view[1]/view[2]/view[{}]'
                               '/blogger-item/view/view[1]/view[2]/view[3]',
                      'fans': '/page/view/view[2]/all-result/view/view/view/view[1]/view[2]/view[{}]'
                              '/blogger-item/view/view[2]/view[1]'
                      }
    # 全部tab-笔记模块
    all_tab_note = {
        'avatar': '/page/view/view[2]/all-result/view/view/view/view[2]/view[2]/view[{}]/note-item/view/view[1]'
                  '/view[1]/img-lazy/u-image/view/image',
        'title': '/page/view/view[2]/all-result/view/view/view/view[2]/view[2]/view[{}]/note-item/view/view[1]/view[2]'
                 '/view[1]/view[1]',
        'create_time': '/page/view/view[2]/all-result/view/view/view/view[2]/view[2]/view[{}]/note-item/view/view[1]'
                       '/view[2]/view[1]/view[2]',
        'author_avatar': '/page/view/view[2]/all-result/view/view/view/view[2]/view[2]/view[{}]/note-item/view/view[1]'
                         '/view[2]/view[2]/view/img-lazy/u-image/view/image',
        'author_nickname': '/page/view/view[2]/all-result/view/view/view/view[2]/view[2]/view[{}]/note-item/view'
                           '/view[1]/view[2]/view[2]/view/view',
        'liked': '/page/view/view[2]/all-result/view/view/view/view[2]/view[2]/view[{}]/note-item/view/view[2]'
                 '/view[1]/view[2]',
        'comment': '/page/view/view[2]/all-result/view/view/view/view[2]/view[2]/view[{}]/note-item/view/view[2]'
                   '/view[2]/view[2]',
        'collect': '/page/view/view[2]/all-result/view/view/view/view[2]/view[2]/view[{}]/note-item/view/view[2]'
                   '/view[3]/view[2]',
        'share': '/page/view/view[2]/all-result/view/view/view/view[2]/view[2]/view[{}]/note-item/view/view[2]'
                 '/view[4]/view[2]'
    }
    # 全部tab-品牌模块
    all_tab_brand = {
        'avatar': '/page/view/view[2]/all-result/view/view/view/view[3]/view[2]/view[{}]/brand-item/view/view[1]'
                  '/view[1]/img-lazy/u-image/view/image',
        'name': '/page/view/view[2]/all-result/view/view/view/view[3]/view[2]/view[{}]/brand-item/view/view[1]'
                '/view[2]/view[1]',
        'note_num': '/page/view/view[2]/all-result/view/view/view/view[3]/view[2]/view[{}]/brand-item/view'
                    '/view[2]/view[1]/view[1]',
        'interact': '/page/view/view[2]/all-result/view/view/view/view[3]/view[2]/view[{}]/brand-item/view'
                    '/view[2]/view[2]/view[1]'
    }
    # 全部tab-品类模块
    all_tab_kind = {
        'name': '/page/view/view[2]/all-result/view/view/view/view[4]/view[2]/view[{}]/category-item'
                '/view/view[1]/view[1]',
        'tab': '/page/view/view[2]/all-result/view/view/view/view[4]/view[2]/view[{}]/category-item'
               '/view/view[1]/view[2]',
        'note_num': '/page/view/view[2]/all-result/view/view/view/view[4]/view[2]/view[{}]/category-item'
                    '/view/view[2]/view[1]/view[1]',
        'interact': '/page/view/view[2]/all-result/view/view/view/view[4]/view[2]/view[{}]/category-item'
                    '/view/view[2]/view[2]/view[1]'
    }
    # 全部tab-热搜词模块
    all_tab_hot_keyword = {
        'name': '/page/view/view[2]/all-result/view/view/view/view[5]/view[2]/view[{}]/hot-word-item'
                '/view/view[1]/view[1]',
        'note_num': '/page/view/view[2]/all-result/view/view/view/view[5]/view[2]/view[{}]/hot-word-item'
                    '/view/view[1]/view[2]/view[1]',
        'interact': '/page/view/view[2]/all-result/view/view/view/view[5]/view[2]/view[{}]/hot-word-item'
                    '/view/view[1]/view[2]/view[2]',
        'hot_value': '/page/view/view[2]/all-result/view/view/view/view[5]/view[2]/view[{}]/hot-word-item'
                     '/view/view[2]/view[1]'
    }
    # 查看更多相关入口
    more = '/page/view/view[2]/all-result/view/view/view/view[{}]/view[2]/view[4]/view[1]/text'
    # 各个模块item
    item = '/page/view/view[2]/all-result/view/view/view/view[{}]/view[2]'
    # 历史搜索标题
    history_word_item = '/page/view/view[2]/all-result/view/view/view[1]/view/view[1]/view'
    # 历史搜索词
    history_word = '/page/view/view[2]/all-result/view/view/view[1]/view/view[2]{}'
    # 清空历史搜索
    clear_history = '/page/view/view[2]/all-result/view/view/view[1]/view/view[1]/image'
    # 热门搜索
    hot_search = '/page/view/view[2]/all-result/view/view/view/view[2]/view[{}]'
    # 热门搜索列表
    hot_search_list = '.search-tag'

    # 排序弹窗，博主blogger-list，笔记note-list，品牌brand-list，品类category-list，热搜词hot-word-list
    sort_pop = {
        'enter': '/page/view/view[2]/{}/view/view[1]/view[1]/sort/view/view/view[1]',
        'sort_name': '/page/view/view[2]/{}/view/view[1]/view[1]/sort/view/u-select'
                     '/view/u-popup/view/view/scroll-view/view/view[2]/picker-view',
        'confirm': '/page/view/view[2]/{}/view/view[1]/view[1]/sort/view/u-select/view/u-popup'
                   '/view/view/scroll-view/view/view[1]/view[3]',
        'cancel': '/page/view/view[2]/{}/view/view[1]/view[1]/sort/view/u-select/view/u-popup'
                  '/view/view/scroll-view/view/view[1]/view[1]'
                }
    # 地区选择弹窗，博主blogger，笔记note，品牌brand
    area_pop = {
        'area_select_confirm': '/page/view/view[2]/{}-list/view/view[1]/view[1]/{}-filtrate/view/u-select'
                               '/view/u-popup/view/view/scroll-view/view/view[1]/view[3]',
        'area_select_cancel': '/page/view/view[2]/{}-list/view/view[1]/view[1]/{}-filtrate/view/u-select'
                              '/view/u-popup/view/view/scroll-view/view/view[1]/view[1]',
        'area_select_area': '/page/view/view[2]/{}-list/view/view[1]/view[1]/{}-filtrate/view/u-select/view'
                            '/u-popup/view/view/scroll-view/view/view[2]/picker-view'
    }
    # 筛选项item
    filter_item = {
        'author': '/page/view/view[2]/blogger-list/view/view[1]/view[2]/view',
        'note': '/page/view/view[2]/note-list/view/view[1]/view[2]/view',
        'brand': '/page/view/view[2]/brand-list/view/view[1]/view[2]/view',
        'kind': '/page/view/view[2]/category-list/view/view[1]/view[2]/view'
    }

    # 博主tab页
    # 全部筛选弹窗
    author_filter_pop = {
        'enter': '/page/view/view[2]/blogger-list/view/view[1]/view[1]/blogger-filtrate/view/view[1]/text',
        'confirm': '/page/view/view[2]/blogger-list/view/view[1]/view[1]/blogger-filtrate'
                   '/view/view[2]/view/view[2]/view[2]/view[2]',
        'close': '/page/view/view[2]/blogger-list/view/view[1]/view[1]/blogger-filtrate'
                 '/view/view[2]/view/view[1]/image',
        'reset': '/page/view/view[2]/blogger-list/view/view[1]/view[1]/blogger-filtrate'
                 '/view/view[2]/view/view[2]/view[2]/view[1]',
        'filter_types': '/page/view/view[2]/blogger-list/view/view[1]/view[1]/blogger-filtrate'
                        '/view/view[2]/view/view[2]/view[1]/scroll-view[1]/view[{}]/view/text',
        'author_gender': '/page/view/view[2]/blogger-list/view/view[1]/view[1]/blogger-filtrate/view/view[2]/view'
                         '/view[2]/view[1]/scroll-view[2]/view/view[1]/view[2]/view[2]/view[{}]',
        'author_area_enter': '/page/view/view[2]/blogger-list/view/view[1]/view[1]/blogger-filtrate/view/view[2]'
                             '/view/view[2]/view[1]/scroll-view[2]/view/view[1]/view[3]/view[2]/view/text',
        'author_type': '/page/view/view[2]/blogger-list/view/view[1]/view[1]/blogger-filtrate/view/view[2]/view/view[2]'
                       '/view[1]/scroll-view[2]/view/view[1]/view[4]/view[2]/view[{}]',
        'author_level': '/page/view/view[2]/blogger-list/view/view[1]/view[1]/blogger-filtrate/view/view[2]/view'
                        '/view[2]/view[1]/scroll-view[2]/view/view[1]/view[5]/view[2]/view[{}]',
        'author_level_extend': '/page/view/view[2]/blogger-list/view/view[1]/view[1]/blogger-filtrate/view/view[2]'
                               '/view/view[2]/view[1]/scroll-view[2]/view/view[1]/view[5]/view[1]/view[2]',
        'fans_level': '/page/view/view[2]/blogger-list/view/view[1]/view[1]/blogger-filtrate/view/view[2]/view/view[2]'
                      '/view[1]/scroll-view[2]/view/view[2]/view[2]/view[3]/view[{}]',
        'fans_level_input': '/page/view/view[2]/blogger-list/view/view[1]/view[1]/blogger-filtrate/view/view[2]/view'
                            '/view[2]/view[1]/scroll-view[2]/view/view[2]/view[2]/view[2]/view[{}]/input',
        'fans_gender': '/page/view/view[2]/blogger-list/view/view[1]/view[1]/blogger-filtrate/view/view[2]/view/view[2]'
                       '/view[1]/scroll-view[2]/view/view[2]/view[3]/view[2]/view[{}]',
        'fans_age': '/page/view/view[2]/blogger-list/view/view[1]/view[1]/blogger-filtrate/view/view[2]/view/view[2]'
                    '/view[1]/scroll-view[2]/view/view[2]/view[4]/view[2]/view[{}]',
        'fans_area_enter': '/page/view/view[2]/blogger-list/view/view[1]/view[1]/blogger-filtrate/view/view[2]'
                           '/view/view[2]/view[1]/scroll-view[2]/view/view[2]/view[5]/view[2]/view/text',
        'liked_and_collect': '/page/view/view[2]/blogger-list/view/view[1]/view[1]/blogger-filtrate/view/view[2]/view'
                             '/view[2]/view[1]/scroll-view[2]/view/view[3]/view[2]/view[3]/view[{}]',
        'liked_and_collect_input': '/page/view/view[2]/blogger-list/view/view[1]/view[1]/blogger-filtrate/view/view[2]'
                                   '/view/view[2]/view[1]/scroll-view[2]/view/view[3]/view[2]/view[2]/view[{}]/input',
        'senior_filter_btn': '/page/view/view[2]/blogger-list/view/view[1]/view[1]/blogger-filtrate/view/view[2]/view'
                             '/view[2]/view[1]/scroll-view[2]/view/view[4]/view[2]/view[2]/view[{}]',
        'have_price': '/page/view/view[2]/blogger-list/view/view[1]/view[1]/blogger-filtrate/view/view[2]/view/view[2]'
                      '/view[1]/scroll-view[2]/view/view[4]/view[3]/view[3]/view[{}]',
        'have_price_input': '/page/view/view[2]/blogger-list/view/view[1]/view[1]/blogger-filtrate/view/view[2]/view'
                            '/view[2]/view[1]/scroll-view[2]/view/view[4]/view[3]/view[2]/view[{}]/input'
    }
    # 博主标签弹窗
    author_label_pop = {
        'enter': '/page/view/view[2]/blogger-list/view/view[1]/view[2]/view/view/blogger-second-category'
                 '/view/view[1]/text[1]',
        'confirm': '/page/view/view[2]/blogger-list/view/view[1]/view[2]/view/view/blogger-second-category'
                   '/view/view[2]/view/view[3]/view[2]',
        'close': '/page/view/view[2]/blogger-list/view/view[1]/view[2]/view/view/blogger-second-category'
                 '/view/view[2]/view/view[1]/image',
        'reset': '/page/view/view[2]/blogger-list/view/view[1]/view[2]/view/view/blogger-second-category'
                 '/view/view[2]/view/view[3]/view[1]',
        'first_label': '/page/view/view[2]/blogger-list/view/view[1]/view[2]/view/view/blogger-second-category'
                       '/view/view[2]/view/view[2]/scroll-view[1]/view[{}]/view/text',
        'second_label': '/page/view/view[2]/blogger-list/view/view[1]/view[2]/view/view/blogger-second-category'
                        '/view/view[2]/view/view[2]/scroll-view[2]/view[{}]/view/text[1]'
    }
    # 粉丝标签弹窗
    author_fans_label_pop = {
        'enter': '/page/view/view[2]/blogger-list/view/view[1]/view[2]/view/view/fan-one-category/view/view[1]/view',
        'confirm': '/page/view/view[2]/blogger-list/view/view[1]/view[2]/view/view/fan-one-category'
                   '/view/view[2]/view/view[2]/view[2]/view[2]',
        'close': '/page/view/view[2]/blogger-list/view/view[1]/view[2]/view/view/fan-one-category'
                 '/view/view[2]/view/view[1]/image',
        'reset': '/page/view/view[2]/blogger-list/view/view[1]/view[2]/view/view/fan-one-category'
                 '/view/view[2]/view/view[2]/view[2]/view[1]',
        'label': '/page/view/view[2]/blogger-list/view/view[1]/view[2]/view/view/fan-one-category'
                 '/view/view[2]/view/view[2]/view[1]/scroll-view/view[{}]/view/text[1]',
    }
    # 内容形式弹窗
    author_content_form_pop = {
        'enter': '/page/view/view[2]/blogger-list/view/view[1]/view[2]/view/view/blogger-sort[1]/view/view/view[1]',
        'confirm': '/page/view/view[2]/blogger-list/view/view[1]/view[2]/view/view/blogger-sort[1]'
                   '/view/u-select/view/u-popup/view/view/scroll-view/view/view[1]/view[3]',
        'cancel': '/page/view/view[2]/blogger-list/view/view[1]/view[2]/view/view/blogger-sort[1]'
                  '/view/u-select/view/u-popup/view/view/scroll-view/view/view[1]/view[1]',
        'types': '/page/view/view[2]/blogger-list/view/view[1]/view[2]/view/view/blogger-sort[1]/view/u-select'
                 '/view/u-popup/view/view/scroll-view/view/view[2]/picker-view',
    }
    # 近90天爆文数弹窗
    author_90_note_pop = {
        'enter': '/page/view/view[2]/blogger-list/view/view[1]/view[2]/view/view/blogger-sort[2]/view/view/view[1]',
        'confirm': '/page/view/view[2]/blogger-list/view/view[1]/view[2]/view/view/blogger-sort[2]'
                   '/view/u-select/view/u-popup/view/view/scroll-view/view/view[1]/view[3]',
        'cancel': '/page/view/view[2]/blogger-list/view/view[1]/view[2]/view/view/blogger-sort[2]'
                  '/view/u-select/view/u-popup/view/view/scroll-view/view/view[1]/view[1]',
        'types': '/page/view/view[2]/blogger-list/view/view[1]/view[2]/view/view/blogger-sort[2]/view/u-select/view'
                 '/u-popup/view/view/scroll-view/view/view[2]/picker-view',
    }
    # 近90天商业笔记数弹窗
    author_90_business_pop = {
        'enter': '/page/view/view[2]/blogger-list/view/view[1]/view[2]/view/view/blogger-sort[3]/view/view/view[1]',
        'confirm': '/page/view/view[2]/blogger-list/view/view[1]/view[2]/view/view/blogger-sort[3]'
                   '/view/u-select/view/u-popup/view/view/scroll-view/view/view[1]/view[3]',
        'cancel': '/page/view/view[2]/blogger-list/view/view[1]/view[2]/view/view/blogger-sort[3]'
                  '/view/u-select/view/u-popup/view/view/scroll-view/view/view[1]/view[1]',
        'types': '/page/view/view[2]/blogger-list/view/view[1]/view[2]/view/view/blogger-sort[3]/view/u-select/view'
                 '/u-popup/view/view/scroll-view/view/view[2]/picker-view',
    }
    # 有品牌合作筛选按钮
    author_brand_cooperate = '/page/view/view[2]/blogger-list/view/view[1]/view[2]/view/view/view'
    # 博主卡片
    author_card = {
        'avatar': '/page/view/view[2]/blogger-list/view/view[{}]/blogger-list-item/view/view/view[1]'
                  '/img-lazy/u-image/view/image',
        'nickname': '/page/view/view[2]/blogger-list/view/view[{}]/blogger-list-item/view/view/view[2]/view[1]',
        'label': '/page/view/view[2]/blogger-list/view/view[{}]/blogger-list-item/view/view/view[2]/view[2]/view[{}]',
        'fans': '/page/view/view[2]/blogger-list/view/view[{}]/blogger-list-item'
                '/view/view/view[2]/view[3]/view[1]/view[2]',
        'liked_and_collect': '/page/view/view[2]/blogger-list/view/view[{}]/blogger-list-item/view'
                             '/view/view[2]/view[3]/view[2]/view/view[2]',
        'fans_inc': '/page/view/view[2]/blogger-list/view/view[{}]/blogger-list-item'
                    '/view/view/view[2]/view[3]/view[3]/view/view[2]'
    }

    # 笔记tab页
    # 全部筛选弹窗
    note_filter_pop = {
        'enter': '/page/view/view[2]/note-list/view/view[1]/view[1]/note-filtrate/view/view[1]/text',
        'confirm': '/page/view/view[2]/note-list/view/view[1]/view[1]/note-filtrate'
                   '/view/view[2]/view/view[2]/view[2]/view[2]',
        'close': '/page/view/view[2]/note-list/view/view[1]/view[1]/note-filtrate/view/view[2]/view/view[1]/image',
        'reset': '/page/view/view[2]/note-list/view/view[1]/view[1]/note-filtrate'
                 '/view/view[2]/view/view[2]/view[2]/view[1]',
        'filter_types': '/page/view/view[2]/note-list/view/view[1]/view[1]/note-filtrate/view/view[2]/view/view[2]'
                        '/view[1]/scroll-view[1]/view[{}]/view/text',
        'interaction': '/page/view/view[2]/note-list/view/view[1]/view[1]/note-filtrate/view/view[2]/view/view[2]'
                       '/view[1]/scroll-view[2]/view/view[1]/view[2]/view[2]/view[{}]',
        'likes': '/page/view/view[2]/note-list/view/view[1]/view[1]/note-filtrate/view/view[2]/view/view[2]/view[1]'
                 '/scroll-view[2]/view/view[1]/view[3]/view[2]/view[{}]',
        'fans_gender': '/page/view/view[2]/note-list/view/view[1]/view[1]/note-filtrate/view/view[2]/view/view[2]'
                       '/view[1]/scroll-view[2]/view/view[2]/view[2]/view[2]/view[{}]',
        'fans_area_enter': '/page/view/view[2]/note-list/view/view[1]/view[1]/note-filtrate/view/view[2]/view/view[2]'
                           '/view[1]/scroll-view[2]/view/view[2]/view[3]/view[2]/view/text',
        'senior_filter_btn': '/page/view/view[2]/note-list/view/view[1]/view[1]/note-filtrate/view/view[2]/view/view[2]'
                             '/view[1]/scroll-view[2]/view/view[3]/view[2]/view[2]/view'
    }
    # 笔记标签弹窗
    note_label_pop = {
        'enter': '/page/view/view[2]/note-list/view/view[1]/view[2]/view/view/note-second-category/view/view[1]/text[1]',
        'confirm': '/page/view/view[2]/note-list/view/view[1]/view[2]/view/view/note-second-category'
                   '/view/view[2]/view/view[1]/view[2]',
        'cancel': '/page/view/view[2]/note-list/view/view[1]/view[2]/view/view/note-second-category'
                  '/view/view[2]/view/view[1]/view[1]',
        'first_label': '/page/view/view[2]/note-list/view/view[1]/view[2]/view/view/note-second-category'
                       '/view/view[2]/view/view[2]/scroll-view[1]/view[{}]/view/text',
        'second_label': '/page/view/view[2]/note-list/view/view[1]/view[2]/view/view/note-second-category/view/view[2]'
                        '/view/view[2]/scroll-view[2]/view[{}]/view/text[1]'
    }
    # 笔记类型弹窗
    note_types_pop = {
        'enter': '/page/view/view[2]/note-list/view/view[1]/view[2]/view/view/note-sort[1]/view/view/view[1]',
        'confirm': '/page/view/view[2]/note-list/view/view[1]/view[2]/view/view/note-sort[1]/view/u-select'
                   '/view/u-popup/view/view/scroll-view/view/view[1]/view[3]',
        'cancel': '/page/view/view[2]/note-list/view/view[1]/view[2]/view/view/note-sort[1]/view/u-select'
                  '/view/u-popup/view/view/scroll-view/view/view[1]/view[1]',
        'types_name': '/page/view/view[2]/note-list/view/view[1]/view[2]/view/view/note-sort[1]/view/u-select'
                      '/view/u-popup/view/view/scroll-view/view/view[2]/picker-view'
    }
    # 笔记发布时间弹窗
    note_create_time_pop = {
        'enter': '/page/view/view[2]/note-list/view/view[1]/view[2]/view/view/note-sort[2]/view/view/view[1]',
        'confirm': '/page/view/view[2]/note-list/view/view[1]/view[2]/view/view/note-sort[2]/view/u-select'
                   '/view/u-popup/view/view/scroll-view/view/view[1]/view[3]',
        'cancel': '/page/view/view[2]/note-list/view/view[1]/view[2]/view/view/note-sort[2]/view/u-select'
                  '/view/u-popup/view/view/scroll-view/view/view[1]/view[1]',
        'times_types': '/page/view/view[2]/note-list/view/view[1]/view[2]/view/view/note-sort[2]/view/u-select'
                       '/view/u-popup/view/view/scroll-view/view/view[2]/picker-view'
    }
    # 商业笔记/低粉爆文筛选按钮
    note_business = '/page/view/view[2]/note-list/view/view[1]/view[2]/view/view/view[{}]'
    # 笔记卡片
    note_card = {
        'avatar': '/page/view/view[2]/note-list/view/view[{}]/note-list-item/view/view[1]/view[1]/img-lazy'
                  '/u-image/view/image',
        'title': '/page/view/view[2]/note-list/view/view[{}]/note-list-item/view/view[1]/view[2]/view[1]/view[1]',
        'label': '/page/view/view[2]/note-list/view/view[{}]/note-list-item/view/view[1]/view[2]/'
                 'view[1]/view[2]/view[{}]',
        'author_avatar': '/page/view/view[2]/note-list/view/view[{}]/note-list-item/view/view[1]/view[2]/view[2]'
                         '/view[1]/img-lazy/u-image/view/image',
        'author_nickname': '/page/view/view[2]/note-list/view/view[{}]/note-list-item'
                           '/view/view[1]/view[2]/view[2]/view[1]/view',
        'create_time': '/page/view/view[2]/note-list/view/view[{}]/note-list-item/view/view[1]/view[2]/view[2]/view[2]',
        'interact': '/page/view/view[2]/note-list/view/view[{}]/note-list-item/view/view[2]/view[1]/view[2]',
        'liked': '/page/view/view[2]/note-list/view/view[{}]/note-list-item/view/view[2]/view[2]/view[2]',
        'comment': '/page/view/view[2]/note-list/view/view[{}]/note-list-item/view/view[2]/view[3]/view[2]',
        'collect': '/page/view/view[2]/note-list/view/view[{}]/note-list-item/view/view[2]/view[4]/view[2]'
    }

    # 品牌tab
    # 全部筛选弹窗
    brand_filter_pop = {
        'enter': '/page/view/view[2]/brand-list/view/view[1]/view[1]/brand-filtrate/view/view[1]/text',
        'reset': '/page/view/view[2]/brand-list/view/view[1]/view[1]/brand-filtrate'
                 '/view/view[2]/view/view[2]/view[2]/view[1]',
        'confirm': '/page/view/view[2]/brand-list/view/view[1]/view[1]/brand-filtrate'
                   '/view/view[2]/view/view[2]/view[2]/view[2]',
        'close': '/page/view/view[2]/brand-list/view/view[1]/view[1]/brand-filtrate/view/view[2]/view/view[1]/image',
        'brand_info': '/page/view/view[2]/brand-list/view/view[1]/view[1]/brand-filtrate/view/view[2]/view/view[2]'
                      '/view[1]/scroll-view[1]/view[1]/view/text',
        'fans_info': '/page/view/view[2]/brand-list/view/view[1]/view[1]/brand-filtrate/view/view[2]/view/view[2]'
                     '/view[1]/scroll-view[1]/view[2]/view/text',
        'interaction': '/page/view/view[2]/brand-list/view/view[1]/view[1]/brand-filtrate/view/view[2]/view/view[2]'
                      '/view[1]/scroll-view[2]/view/view[1]/view[2]/view[2]/view[{}]',
        'author_num': '/page/view/view[2]/brand-list/view/view[1]/view[1]/brand-filtrate/view/view[2]/view/view[2]'
                      '/view[1]/scroll-view[2]/view/view[1]/view[3]/view[2]/view[{}]',
        'note_num': '/page/view/view[2]/brand-list/view/view[1]/view[1]/brand-filtrate/view/view[2]/view/view[2]'
                    '/view[1]/scroll-view[2]/view/view[1]/view[4]/view[2]/view[{}]',
        'fans_gender': '/page/view/view[2]/brand-list/view/view[1]/view[1]/brand-filtrate/view/view[2]/view/view[2]'
                       '/view[1]/scroll-view[2]/view/view[2]/view[2]/view[2]/view[{}]',
        'fans_area_enter': '/page/view/view[2]/brand-list/view/view[1]/view[1]/brand-filtrate/view/view[2]/view/view[2]'
                           '/view[1]/scroll-view[2]/view/view[2]/view[3]/view[2]/view/text'
    }
    # 品牌标签弹窗
    brand_label_pop = {
        'enter': '/page/view/view[2]/brand-list/view/view[1]/view[2]/view/view/brand-second-category'
                 '/view/view[1]/text[1]',
        'confirm': '/page/view/view[2]/brand-list/view/view[1]/view[2]/view/view/brand-second-category'
                   '/view/view[2]/view/view[1]/view[2]',
        'cancel': '/page/view/view[2]/brand-list/view/view[1]/view[2]/view/view/brand-second-category'
                  '/view/view[2]/view/view[1]/view[1]',
        'first_label': '/page/view/view[2]/brand-list/view/view[1]/view[2]/view/view/brand-second-category'
                       '/view/view[2]/view/view[2]/scroll-view[1]/view[{}]/view/text',
        'second_label': '/page/view/view[2]/brand-list/view/view[1]/view[2]/view/view/brand-second-category'
                        '/view/view[2]/view/view[2]/scroll-view[2]/view[{}]/view/text[1]'
    }
    # 有商业投放筛选按钮/其他标签按钮
    brand_label_btn = '/page/view/view[2]/brand-list/view/view[1]/view[2]/view/view/view[{}]'
    # 品牌卡片
    brand_card = {
        'avatar': '/page/view/view[2]/brand-list/view/view[{}]/brand-list-item'
                  '/view/view[1]/view/img-lazy/u-image/view/image',
        'name': '/page/view/view[2]/brand-list/view/view[{}]/brand-list-item/view/view[2]/view[1]/view[1]',
        'category': '/page/view/view[2]/brand-list/view/view[{}]/brand-list-item/view/view[2]/view[2]{}',
        'times': '/page/view/view[2]/brand-list/view/view[{}]/brand-list-item/view/view[2]/view[1]/view[2]',
        'interact': '/page/view/view[2]/brand-list/view/view[{}]/brand-list-item/view/view[2]/view[{}]/view[1]/view[2]',
        'author_num': '/page/view/view[2]/brand-list/view/view[{}]/brand-list-item/view/view[2]/view[{}]/view[2]/view[2]',
        'note_num': '/page/view/view[2]/brand-list/view/view[{}]/brand-list-item/view/view[2]/view[{}]/view[3]/view[2]'
    }

    # 品类tab
    # 时间筛选弹窗
    kind_times_pop = {
        'enter': '/page/view/view[2]/category-list/view/view[1]/view[1]/time-sort/view/view/view[1]',
        'confirm': '/page/view/view[2]/category-list/view/view[1]/view[1]/time-sort/view/u-select/view/u-popup'
                   '/view/view/scroll-view/view/view[1]/view[3]',
        'cancel': '/page/view/view[2]/category-list/view/view[1]/view[1]/time-sort/view/u-select/view/u-popup'
                  '/view/view/scroll-view/view/view[1]/view[1]',
        'times': '/page/view/view[2]/category-list/view/view[1]/view[1]/time-sort/view/u-select/view/u-popup'
                 '/view/view/scroll-view/view/view[2]/picker-view'
    }
    # 品类标签弹窗
    kind_label_pop = {
        'enter': '/page/view/view[2]/category-list/view/view[1]/view[2]/view/view/category-second-category'
                 '/view/view[1]/text[1]',
        'confirm': '/page/view/view[2]/category-list/view/view[1]/view[2]/view/view/category-second-category'
                   '/view/view[2]/view/view[1]/view[2]',
        'cancel': '/page/view/view[2]/category-list/view/view[1]/view[2]/view/view/category-second-category'
                  '/view/view[2]/view/view[1]/view[1]',
        'first_label': '/page/view/view[2]/category-list/view/view[1]/view[2]/view/view/category-second-category'
                       '/view/view[2]/view/view[2]/scroll-view[1]/view[{}]/view/text',
        'second_label': '/page/view/view[2]/category-list/view/view[1]/view[2]/view/view/category-second-category'
                        '/view/view[2]/view/view[2]/scroll-view[2]/view[{}]/view/text[1]'
    }
    # 品类标签筛选按钮
    kind_label_btn = '/page/view/view[2]/category-list/view/view[1]/view[2]/view/view/view[{}]'
    # 品类卡片
    kind_card = {
        'name': '/page/view/view[2]/category-list/view/view[{}]/category-list-item/view/view[1]/view[1]',
        'category': '/page/view/view[2]/category-list/view/view[{}]/category-list-item/view/view[1]/view[2]/view[{}]',
        'note_num': '/page/view/view[2]/category-list/view/view[{}]/category-list-item/view/view[2]/view[1]/view[1]',
        'interact': '/page/view/view[2]/category-list/view/view[{}]/category-list-item/view/view[2]/view[2]/view[1]'
    }

    # 热搜词tab
    # 分类弹窗
    hot_keyword_label_pop = {
        'enter': '/page/view/view[2]/hot-word-list/view/view[1]/view[2]/view/view/hot-word-second-category'
                 '/view/view[1]/text[1]',
        'confirm': '/page/view/view[2]/hot-word-list/view/view[1]/view[2]/view/view/hot-word-second-category'
                   '/view/view[2]/view/view[1]/view[2]',
        'cancel': '/page/view/view[2]/hot-word-list/view/view[1]/view[2]/view/view/hot-word-second-category'
                  '/view/view[2]/view/view[1]/view[1]',
        'first_label': '/page/view/view[2]/hot-word-list/view/view[1]/view[2]/view/view/hot-word-second-category'
                       '/view/view[2]/view/view[2]/scroll-view[1]/view[{}]/view/text',
        'second_label': '/page/view/view[2]/hot-word-list/view/view[1]/view[2]/view/view/hot-word-second-category'
                        '/view/view[2]/view/view[2]/scroll-view[2]/view[{}]/view/text[1]'
    }
    # 标签筛选按钮
    hot_keyword_label_btn = '/page/view/view[2]/hot-word-list/view/view[1]/view[2]/view/view/view[{}]'
    # 热搜词卡片
    hot_keyword_card = {
        'name': '/page/view/view[2]/hot-word-list/view/view[2]/view/view/view[{}]/view[1]/text',
        'note_num': '/page/view/view[2]/hot-word-list/view/view[2]/view/view/view[{}]/view[2]',
        'interact': '/page/view/view[2]/hot-word-list/view/view[2]/view/view/view[{}]/view[3]',
        'hot_value': '/page/view/view[2]/hot-word-list/view/view[2]/view/view/view[{}]/view[4]/text'
    }
    # 会员权限不足升级提示
    vip_upgrade_tips = '/page/view/view[2]/{}-list/view/view[{}]/list-auth/view/view/text[1]'
    # 会员权限不足升级按钮
    vip_upgrade_btn = '/page/view/view[2]/{}-list/view/view[{}]/list-auth/view/view/button'
    # 游客登录提示
    tourist_tips = '/page/view/view[2]/{}-list/view/view[{}]/list-auth/view/view/text'
    # 游客登录按钮
    tourist_login_btn = '/page/view/view[2]/{}-list/view/view[{}]/list-auth/view/view/text'

    def into_search(self):
        """
        进入搜索页
        """
        self.navigate_to_open(route.search_page)
        time.sleep(1)
        return self

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

    def input_value(self, types, value):
        """输入自定义数值"""
        input_value = value.split('-')
        if input_value[0].isdigit() and input_value[1].isdigit():
            start_fans = int(input_value[0])
            end_fans = int(input_value[1])
            if start_fans <= end_fans:
                self.get_element(self.author_filter_pop[types].format(1)).input(input_value[0])
                self.get_element(self.author_filter_pop[types].format(3)).input(input_value[1])
            else:
                print('自定义区间输入错误：起始值大于结束值')
        else:
            print('自定义区间输入错误：请输入整数值，并以-链接')

    def click_clear_history(self):
        """清空历史搜索"""
        self.get_element(self.clear_history).click()

    def is_vip_have_authority(self, tab_name, ids='2'):
        """判断是否有会员权限"""
        return self.is_ele_exist(self.vip_upgrade_tips.format(tab_name, ids))

    def is_vip_have_login(self, tab_name, ids='2'):
        """判断是否有登录入口"""
        return self.is_ele_exist(self.tourist_tips.format(tab_name, ids))

    def click_into_detail(self, types):
        """点击进入详情页"""
        if types == '博主':
            self.get_element(self.author_card['avatar'].format(2)).click()
        elif types == '笔记':
            self.get_element(self.note_card['avatar'].format(2)).click()
        elif types == '品牌':
            self.get_element(self.brand_card['avatar'].format(2)).click()
        elif types == '品类':
            self.get_element(self.kind_card['name'].format(2)).click()
        elif types == '热搜词':
            self.get_element(self.hot_keyword_card['name'].format(2)).click()
        else:
            print('click_into_detail-库类型输入错误,仅支持博主/笔记/品牌/品类/热搜词')
        return self

    def scroll_to_item(self, types, top=None):
        """滑动到各个模块，适配iphone5"""

        scroll_positions = {
            '博主': 0,
            '笔记': 300,
            '品牌': 600,
            '品类': 900,
            '热搜词': 1200
        }

        scroll_position = scroll_positions.get(types)

        if scroll_position is not None:
            if top is None:
                self.scroll_page(high=scroll_position)
            else:
                self.scroll_page(high=-scroll_position)
        else:
            print("slide_to_item-榜单类型输入错误，仅支持博主/笔记/品牌/品类/热搜词")

        time.sleep(2)

    def select_tab(self, tab_name):
        """选择tab"""
        tab_mapping = {
            '全部': 1,
            '博主': 2,
            '笔记': 3,
            '品牌': 4,
            '品类': 5,
            '热搜词': 6
        }

        tab_index = tab_mapping.get(tab_name)

        if tab_index is not None:
            self.get_element(self.tab.format(tab_index)).click()
            time.sleep(1)
        else:
            print('select_tab-榜单类型输入错误，仅支持全部/博主/笔记/品牌/品类/热搜词')

        return self

    def sure_into_tab(self, tab_name):
        """确认是否进入各个tab页面"""

        if tab_name == '博主':
            re = self.is_ele_exist(self.sort_pop['enter'].format('blogger-list'))
        elif tab_name == '笔记':
            re = self.is_ele_exist(self.sort_pop['enter'].format('note-list'))
        elif tab_name == '品牌':
            re = self.is_ele_exist(self.sort_pop['enter'].format('brand-list'))
        elif tab_name == '品类':
            re = self.is_ele_exist(self.sort_pop['enter'].format('category-list'))
        elif tab_name == '热搜词':
            re = self.is_ele_exist(self.sort_pop['enter'].format('hot-word-list'))
        else:
            re = None
            print('sure_into_tab-榜单类型输入错误，仅支持博主/笔记/品牌/品类/热搜词')

        return re

    def scroll_filter_item(self, types):
        """左滑显示筛选项"""
        self.get_element(self.filter_item[types]).scroll_to(top=0, left=300)
        return self

    def is_tab_ele_exist(self, tab_name):
        """判断全部tab下xx模块的元素是否存在"""

        total_result = 0
        if tab_name == '博主':
            item = self.all_tab_author.items()
        elif tab_name == '笔记':
            item = self.all_tab_note.items()
        elif tab_name == '品牌':
            item = self.all_tab_brand.items()
        elif tab_name == '品类':
            item = self.all_tab_kind.items()
        elif tab_name == '热搜词':
            item = self.all_tab_hot_keyword.items()
        else:
            print('tab_name输入错误，仅支持博主/笔记/品牌/品类/热搜词')
            item = None
        for key, value in item:
            result = self.is_ele_exist(value.format(1))
            total_result += result

        return total_result

    def click_more(self, tab_name):
        """点击全部tab下，不同模块的查看更多相关"""

        more_buttons = {
            '博主': 1,
            '笔记': 2,
            '品牌': 3,
            '品类': 4,
            '热搜词': 5
        }

        button_index = more_buttons.get(tab_name)

        if button_index is not None:
            self.get_element(self.more.format(button_index)).click()
        else:
            print('模块名输入错误，仅支持博主/笔记/品牌/品类/热搜词')

        return self

    def is_history_word_exist(self):
        """判断历史搜索是否有数据"""
        if self.is_ele_exist(self.history_word_item):
            return True
        else:
            return False

    def get_history_word(self):
        """获取历史搜索记录"""
        text = []
        if self.is_ele_exist(self.history_word.format('/view')):
            context = self.get_context(self.history_word.format('/view'))
            text.append(context)
        else:
            for i in range(len(self.history_word.format(''))):
                context = self.get_context(self.history_word.format('/view[{}]').format(i))
                text.append(context)
        return text

    def get_hot_search_word(self):
        """获取热门搜索词"""
        text = []
        for i in range(len(self.get_elements(self.hot_search_list))-1):
            ele = self.is_ele_exist(self.hot_search.format(i+1))
            if ele:
                context = self.get_context(self.hot_search.format(i+1))
                text.append(context)
            else:
                break
        return text

    def get_author_info(self, num):
        """获取博主库列表博主信息，返回格式[id, 博主名称，粉丝数，赞藏总数，粉丝增量]"""
        page = math.ceil(num/20)
        author_list = []
        if num > 100:
            print('暂不支持超过100条数据')
        else:
            self.check_scroll(page)
            for i in range(num):
                name = self.get_context(self.author_card['nickname'].format(i+2))
                fans = self.get_context(self.author_card['fans'].format(i+2))
                liked_and_collect = self.get_context(self.author_card['liked_and_collect'].format(i+2))
                fans_inc = self.get_context(self.author_card['fans_inc'].format(i+2))
                author_list.append([i + 1, name, Base.convert_to_float_with_unit(fans),
                                    Base.convert_to_float_with_unit(liked_and_collect),
                                    Base.convert_to_float_with_unit(fans_inc)])
            self.check_scroll(page, top=True)
        return author_list

    def get_note_info(self, num):
        """获取笔记库列表笔记信息,返回格式[id, 标题，博主名称，创建时间，互动量，点赞数，评论数，收藏数]"""
        page = math.ceil(num/20)
        note_list = []
        if num > 100:
            print('暂不支持超过100条数据')
        else:
            self.check_scroll(page)
            for i in range(num):
                title = self.get_context(self.note_card['title'].format(i+2))
                author_name = self.get_context(self.note_card['author_nickname'].format(i+2))
                create_time = self.get_context(self.note_card['create_time'].format(i+2))
                format_create_time = create_time[3:]
                interact = self.get_context(self.note_card['interact'].format(i+2))
                liked = self.get_context(self.note_card['liked'].format(i+2))
                comment = self.get_context(self.note_card['comment'].format(i+2))
                collect = self.get_context(self.note_card['collect'].format(i + 2))
                note_list.append([i + 1, title, author_name, format_create_time,
                                  Base.convert_to_float_with_unit(interact), Base.convert_to_float_with_unit(liked),
                                  Base.convert_to_float_with_unit(comment), Base.convert_to_float_with_unit(collect)])
            self.check_scroll(page, top=True)
        return note_list

    def get_brand_info(self, num):
        """获取品牌库列表品牌信息,返回格式[id, 品牌名称，投放时间，总互动量，总博主数，总笔记数]"""
        page = math.ceil(num/20)
        brand_list = []
        if num > 100:
            print('暂不支持超过100条数据')
        else:
            self.check_scroll(page)
            for i in range(num):
                brand_name = self.get_context(self.brand_card['name'].format(i+2))
                times = self.get_context(self.brand_card['times'].format(i+2))
                format_times = times[7:]
                # 判断是否有标签
                ele = self.is_ele_exist(self.brand_card['interact'].format(i+2, 2))
                if ele:
                    interact = self.get_context(self.brand_card['interact'].format(i+2, 2))
                    author_num = self.get_context(self.brand_card['author_num'].format(i+2, 2))
                    note_num = self.get_context(self.brand_card['note_num'].format(i+2, 2))
                else:
                    interact = self.get_context(self.brand_card['interact'].format(i + 2, 3))
                    author_num = self.get_context(self.brand_card['author_num'].format(i + 2, 3))
                    note_num = self.get_context(self.brand_card['note_num'].format(i + 2, 3))
                brand_list.append([i + 1, brand_name, format_times, Base.convert_to_float_with_unit(interact),
                                   Base.convert_to_float_with_unit(author_num),
                                   Base.convert_to_float_with_unit(note_num)])
            self.check_scroll(page, top=True)
        return brand_list

    def get_kind_info(self, num):
        """获取品类库列表品类信息,返回格式[id, 品类名称，相关笔记数，总互动量]"""
        page = math.ceil(num/20)
        kind_list = []
        if num > 100:
            print('暂不支持超过100条数据')
        else:
            self.check_scroll(page)
            for i in range(num):
                kind_name = self.get_context(self.kind_card['name'].format(i+2))
                note_num = self.get_context(self.kind_card['note_num'].format(i+2))
                interact = self.get_context(self.kind_card['interact'].format(i+2))
                kind_list.append([i + 1, kind_name, Base.convert_to_float_with_unit(note_num),
                                  Base.convert_to_float_with_unit(interact)])
            self.check_scroll(page, top=True)
        return kind_list

    def get_hot_word_info(self, num):
        """获取热搜词库列表热搜词信息,返回格式[id, 热搜词，新增笔记数，新增互动量，热度值]"""
        page = math.ceil(num/20)
        hot_word_list = []
        if num > 100:
            print('暂不支持超过100条数据')
        else:
            self.check_scroll(page)
            for i in range(num):
                hot_word_name = self.get_context(self.hot_keyword_card['name'].format(i+2))
                note_num = self.get_context(self.hot_keyword_card['note_num'].format(i+2))
                interact = self.get_context(self.hot_keyword_card['interact'].format(i+2))
                hot_value = self.get_context(self.hot_keyword_card['hot_value'].format(i+2))
                hot_word_list.append([i + 1, hot_word_name, Base.convert_to_float_with_unit(note_num),
                                      Base.convert_to_float_with_unit(interact),
                                      Base.convert_to_float_with_unit(hot_value)])
            self.check_scroll(page, top=True)
        return hot_word_list

    def get_item_labels(self, num, name_selector, label_selector, card_selector=None, kind_types=False):
        """获取各个库的标签"""
        page = math.ceil(num / 20)
        label_list = []
        if num > 100:
            print('暂不支持超过100条数据')
        else:
            self.check_scroll(page)
            for i in range(num):
                name = self.get_context(name_selector.format(i + 2))

                labels = []
                ele1 = self.is_ele_exist(card_selector.format(i + 2, 3)) if card_selector else 'no_brand'
                if ele1 == 'no_brand':
                    value = 2 if kind_types else 3
                    for j in range(value):
                        ele = self.is_ele_exist(label_selector.format(i+2, j+1))
                        if ele:
                            label = self.get_context(label_selector.format(i+2, j+1))
                            labels.append(label)
                        else:
                            break
                elif ele1:
                    for j in range(3):
                        ids = f'/view[{j + 1}]'
                        ele = self.is_ele_exist(label_selector.format(i + 2, ids))
                        if ele:
                            label = self.get_context(label_selector.format(i + 2, ids))
                            labels.append(label)
                        else:
                            break
                else:
                    print('{}标签不存在'.format(name))
                label_list.append([i + 1, name, labels])
            self.check_scroll(page, top=True)
        return label_list

    def get_author_label(self, num):
        """获取博主库列表博主标签"""
        return self.get_item_labels(num, self.author_card['nickname'], self.author_card['label'])

    def get_note_label(self, num):
        """获取笔记库列表笔记标签"""
        return self.get_item_labels(num, self.note_card['title'], self.note_card['label'])

    def get_brand_label(self, num):
        return self.get_item_labels(num, self.brand_card['name'], self.brand_card['category'], card_selector=self.brand_card['interact'])

    def get_kind_label(self, num):
        """获取品类库列表品类标签"""
        return self.get_item_labels(num, self.kind_card['name'], self.kind_card['category'], kind_types=True)

    def select_area(self, types, value):
        """选择地区省份通用方法"""
        # value格式为['福建省', '厦门市']
        province = config.province_mapping.get(value[0], -1)
        city = config.city_mapping.get(value[1], -1)
        if province == -1 or city == -1:
            print('不存在的省或者市{}-{}'.format(value[0], value[1]))
        else:
            try:
                self.get_element(self.area_pop['area_select_area'].format(types, types)).trigger("change", {"value": [province-1, 0]})
                time.sleep(2)
                self.get_element(self.area_pop['area_select_area'].format(types, types)).trigger("change", {"value": [province-1, city]})
            finally:
                self.get_element(self.area_pop['area_select_confirm'].format(types, types)).click()

    def select_sort(self, types, sort_types):
        """选择不同库的不同排序"""
        sort_mapping = {
            '粉丝数最多': [0], '涨粉数最多': [1], '赞藏最多': [2],
            '互动量': [0], '点赞数': [1], '评论数': [2], '收藏数': [3],
            '最近投放时间': [0], '昨日互动增量': [1], '总互动量': [2], '总博主数': [3], '总笔记数': [4],
            '笔记最多': [0], '互动量最多': [1],
            '热度值排序': [0]
        }
        # 博主blogger - list，笔记note - list，品牌brand - list，品类category - list，热搜词hot - word - list
        types_mapping = {
            '博主': 'blogger-list',
            '笔记': 'note-list',
            '品牌': 'brand-list',
            '品类': 'category-list',
            '热搜词': 'hot-word-list'
        }
        value = sort_mapping.get(sort_types, -1)
        type_value = types_mapping.get(types)
        if value == -1:
            print('排序类型错误')
        else:
            self.get_element(self.sort_pop['enter'].format(type_value)).click()
            time.sleep(1)
            self.get_element(self.sort_pop['sort_name'].format(type_value)).trigger("change", {"value": value})
            self.get_element(self.sort_pop['confirm'].format(type_value)).click()

    def filter_by_labels(self, label_pop, first_label, second_label):
        """"博主/笔记/热搜词库选择单个一级/二级标签通用方法"""
        first_label_value = config.first_label_mapping.get(first_label, -1)  # 使用get方法获取对应的值，不存在时返回-1
        second_label_value = config.second_label_mapping.get(second_label, -1)
        if first_label_value == -1 or second_label_value == -1:
            print(f"未找到标签：{first_label, second_label}")
        else:
            self.get_element(label_pop['enter']).click()
            self.get_element(label_pop['first_label'].format(first_label_value + 1)).click()
            self.get_element(label_pop['second_label'].format(second_label_value + 1)).click()
            self.get_element(label_pop['confirm']).click()

    def filter_by_category(self, category_pop, first_category, second_category):
        """"品牌/品类库选择单个一级/二级分类通用方法"""
        first_category_value = config.category_mapping.get(first_category, -1)['id']  # 使用get方法获取对应的值，不存在时返回-1
        if second_category == '全部':
            second_category_value = config.category_mapping.get(second_category, -1)
        else:
            second_category_list = config.category_mapping.get(first_category, -1)['sub_label']
            second_category_value = second_category_list.get(second_category, -1)
        if first_category_value == -1 or second_category_value == -1:
            print(f"未找到分类：{first_category, second_category}")
        else:
            self.get_element(category_pop['enter']).click()
            self.get_element(category_pop['first_label'].format(first_category_value + 1)).click()
            self.get_element(category_pop['second_label'].format(second_category_value + 1)).click()
            self.get_element(category_pop['confirm']).click()

    def authorLib_filter_by_label(self, first_label, second_label):
        """博主库选择单个的一级/二级博主标签"""
        self.filter_by_labels(self.author_label_pop, first_label, second_label)

    def noteLib_filter_by_label(self, first_label, second_label):
        """笔记库选择单个的一级/二级笔记标签"""
        self.filter_by_labels(self.note_label_pop, first_label, second_label)

    def brandLib_filter_by_label(self, first_label, second_label):
        """品牌库选择单个的一级/二级品牌标签"""
        self.filter_by_category(self.brand_label_pop, first_label, second_label)

    def kindLib_filter_by_label(self, first_label, second_label):
        """品类库选择单个的一级/二级品类标签"""
        self.filter_by_category(self.kind_label_pop, first_label, second_label)

    def hotWordLib_filter_by_label(self, first_label, second_label):
        """热搜词库选择单个的一级/二级分类标签"""
        self.filter_by_labels(self.hot_keyword_label_pop, first_label, second_label)

    def filter_by_fan_info(self, filter_types, value, filter_pop, types):
        """"筛选粉丝信息通用方法"""
        if filter_types == '粉丝性别':
            gender_value = config.fans_gender_mapping.get(value, -1)
            if gender_value == -1:
                print('粉丝性别输入错误')
            else:
                self.get_element(filter_pop['fans_gender'].format(gender_value)).click()

        elif filter_types == '粉丝地区':
            self.get_element(filter_pop['fans_area_enter']).click()
            self.select_area(value=value, types=types)

        elif filter_types == '粉丝年龄':
            age_value = config.fans_age_mapping.get(value, -1)
            if age_value != -1:
                self.get_element(filter_pop['fans_age'].format(age_value)).click()
            else:
                print('粉丝年龄区间输入错误')
        else:
            print('粉丝信息筛选类型输入错误，仅支持粉丝年龄/粉丝性别/粉丝地区')

    def authorLib_filter_by_fans_info(self, types, value):
        """博主库粉丝信息筛选"""

        if types == '粉丝量级':
            fans_value = config.fans_mapping.get(value, -1)
            if fans_value != -1:
                self.get_element(self.author_filter_pop['fans_level'].format(fans_value)).click()
            else:
                self.input_value(types='fans_level_input', value=value)
        else:
            self.filter_by_fan_info(filter_types=types, value=value, types='blogger', filter_pop=self.author_filter_pop)

    def noteLib_filter_by_fans_info(self, types, value):
        """笔记库粉丝信息筛选"""
        self.filter_by_fan_info(filter_types=types, value=value, types='note', filter_pop=self.note_filter_pop)

    def brandLib_filter_by_fans_info(self, types, value):
        """品牌库粉丝信息筛选"""
        self.filter_by_fan_info(filter_types=types, value=value, types='brand', filter_pop=self.brand_filter_pop)

    def filter_by_btn(self, element, types):
        """点击筛选按钮通用方法"""
        color = self.get_styles(ele=element, names='color')
        if color == config.color['default']:
            self.get_element(element).click()
        elif color == config.color['red']:
            print('已选中{}'.format(types))

    def authorLib_filter_by_brand_cooperate(self):
        """博主库选择有品牌合作的"""
        self.filter_by_btn(element=self.author_brand_cooperate, types='有品牌合作')

    def noteLib_filter_by_types(self, types):
        """笔记库选择商业笔记/低粉爆文"""
        if types == '商业笔记':
            self.filter_by_btn(element=self.note_business.format(1), types=types)
        elif types == '低粉爆文':
            self.filter_by_btn(element=self.note_business.format(2), types=types)
        else:
            print('noteLib_filter_by_types-筛选类型输入错误，仅支持商业笔记/低粉爆文')

    def brandLib_filter_by_business(self):
        """品牌库筛选有商业投放"""
        self.filter_by_btn(element=self.brand_label_btn.format(1), types='有商业投放')

    def brandLib_filter_by_other_labels(self, types):
        """品牌库筛选标签按钮"""
        value = config.other_label_mapping.get(types, -1)
        if value == -1:
            print('brandLib_filter_by_other_labels-标签按钮名称输入错误')
        else:
            self.filter_by_btn(element=self.brand_label_btn.format(value), types=types)

    def kindLib_filter_by_other_labels(self, types):
        """品类库筛选标签按钮"""
        value = config.other_label_mapping.get(types, -1)
        if value == -1:
            print('kindLib_filter_by_other_labels-标签按钮名称输入错误')
        else:
            self.filter_by_btn(element=self.kind_label_btn.format(value-1), types=types)

    def hotWordLib_filter_by_other_labels(self, types):
        """热搜词库筛选标签按钮"""
        value = config.hot_keyword_category_mapping.get(types, -1)
        if value == -1:
            print('hotWordLib_filter_by_other_labels-标签按钮名称输入错误')
        else:
            self.filter_by_btn(element=self.hot_keyword_label_btn.format(value), types=types)

    def select_author_filter(self, filter_types, types, value):
        """选择博主库的全部筛选类型"""
        try:
            self.get_element(self.author_filter_pop['enter']).click()
            self.get_element(self.author_filter_pop['reset']).click()
            if filter_types == '博主信息':
                self.authorLib_filter_by_author_info(types=types, value=value)

            elif filter_types == '粉丝信息':
                self.get_element(self.author_filter_pop['filter_types'].format(2)).click()
                self.authorLib_filter_by_fans_info(types=types, value=value)

            elif filter_types == '内容筛选':
                self.get_element(self.author_filter_pop['filter_types'].format(3)).click()
                self.authorLib_filter_by_content_type(types=types, value=value)

            elif filter_types == '高级筛选':
                self.get_element(self.author_filter_pop['filter_types'].format(4)).click()
                self.authorLib_filter_by_senior_filter(types=types, value=value)
        finally:
            time.sleep(2)
            self.get_element(self.author_filter_pop['confirm']).click()

    def select_note_filter(self, filter_types, types, value):
        """选择笔记库的全部筛选类型"""
        try:
            self.get_element(self.note_filter_pop['enter']).click()
            self.get_element(self.note_filter_pop['reset']).click()
            if filter_types == '笔记筛选':
                self.noteLib_filter_by_note_info(types=types, value=value)

            elif filter_types == '粉丝信息':
                self.get_element(self.note_filter_pop['filter_types'].format(2)).click()
                self.noteLib_filter_by_fans_info(types=types, value=value)

            elif filter_types == '高级筛选':
                self.get_element(self.note_filter_pop['filter_types'].format(3)).click()
                self.noteLib_filter_by_senior_filter(types=types)
        finally:
            time.sleep(2)
            self.get_element(self.note_filter_pop['confirm']).click()

    def select_brand_filter(self, filter_types, types, value):
        """选择品牌库的全部筛选类型"""
        try:
            self.get_element(self.brand_filter_pop['enter']).click()
            self.get_element(self.brand_filter_pop['reset']).click()
            if filter_types == '品牌筛选':
                self.get_element(self.brand_filter_pop['brand_info']).click()
                self.brandLib_filter_by_brand_info(types=types, value=value)

            elif filter_types == '粉丝信息':
                self.get_element(self.brand_filter_pop['fans_info']).click()
                self.brandLib_filter_by_fans_info(types=types, value=value)
        finally:
            time.sleep(2)
            self.get_element(self.brand_filter_pop['confirm']).click()

    def authorLib_filter_by_mult_first_author_label(self, first_label):
        """博主库选择多个一级博主标签"""
        self.get_element(self.author_label_pop['enter']).click()
        self.get_element(self.author_label_pop['reset']).click()
        for i in first_label:
            first_label_value = config.first_label_mapping.get(i, -1)  # 使用get方法获取对应的值，不存在时返回-1
            if first_label_value == -1:
                print(f"未找到标签：{first_label}")
            else:
                self.get_element(self.author_label_pop['first_label'].format(first_label_value+1)).click()
                self.get_element(self.author_label_pop['second_label'].format(1)).click()
        self.get_element(self.author_label_pop['confirm']).click()

    def authorLib_filter_by_mult_second_author_label(self, labels):
        """博主库选择多个二级博主标签"""
        self.get_element(self.author_label_pop['enter']).click()
        self.get_element(self.author_label_pop['reset']).click()
        for i in range(len(labels)):
            first_label = labels[i][0]
            second_label = labels[i][1]
            first_label_value = config.first_label_mapping.get(first_label, -1)
            for j in second_label:
                second_label_value = config.second_label_mapping.get(j, -1)  # 使用get方法获取对应的值，不存在时返回-1
                if second_label_value == -1:
                    print(f"未找到标签：{first_label}")
                else:
                    self.get_element(self.author_label_pop['first_label'].format(first_label_value+1)).click()
                    self.get_element(self.author_label_pop['second_label'].format(second_label_value+1)).click()

        self.get_element(self.author_label_pop['confirm']).click()

    def authorLib_filter_by_fans_label(self, fans_labels):
        """博主库选择粉丝标签"""
        self.get_element(self.author_fans_label_pop['enter']).click()
        self.get_element(self.author_fans_label_pop['reset']).click()
        if isinstance(fans_labels, str):
            fans_labels = [fans_labels]
        for label in fans_labels:
            label_value = config.fans_label_mapping.get(label, -1)
            if label_value == -1:
                print(f"未找到粉丝标签：{label}")
            else:
                self.get_element(self.author_fans_label_pop['label'].format(label_value + 1)).click()
        self.get_element(self.author_fans_label_pop['confirm']).click()

    def authorLib_filter_by_content_form(self, types):
        """博主库选择不同内容形式"""
        self.get_element(self.author_content_form_pop['enter']).click()
        type_value_mapping = {
            '不限': [0],
            '图文为主': [1],
            '视频为主': [2],
        }
        value = type_value_mapping.get(types, -1)
        if value == -1:
            print('authorLib_filter_by_content_form-内容形式输入错误，仅支持不限/图文为主/视频为主')
        else:
            self.get_element(self.author_content_form_pop['types']).trigger("change", {"value": value})
            self.get_element(self.author_content_form_pop['confirm']).click()

    def authorLib_filter_by_note(self, types, note_types):
        """博主库选择近90天爆文数/近90天商业笔记数"""
        value = config.note_num_mapping.get(types, -1)
        if value == -1:
            print('authorLib_filter_by_note-笔记数筛选条件输入错误，仅支持近90天爆文数/近90天商业笔记数')
        else:
            if note_types == '近90天爆文数':
                self.get_element(self.author_90_note_pop['enter']).click()
                self.get_element(self.author_90_note_pop['types']).trigger("change", {"value": value})
                self.get_element(self.author_90_note_pop['confirm']).click()
            elif note_types == '近90天商业笔记数':
                self.get_element(self.author_90_business_pop['enter']).click()
                self.get_element(self.author_90_business_pop['types']).trigger("change", {"value": value})
                self.get_element(self.author_90_business_pop['confirm']).click()

    def authorLib_filter_by_author_info(self, types, value):
        """博主库博主信息筛选"""
        if types == '博主性别':
            gender_value = config.gender_mapping.get(value, -1)
            if gender_value == -1:
                print('博主性别输入错误')
            else:
                self.get_element(self.author_filter_pop['author_gender'].format(gender_value)).click()

        elif types == '博主属性':
            if value == '企业账号':
                self.get_element(self.author_filter_pop['author_type'].format(1)).click()
            elif value == '个人账号':
                self.get_element(self.author_filter_pop['author_type'].format(2)).click()
            else:
                print('博主账号类型输入错误')

        elif types == '博主地区':
            self.get_element(self.author_filter_pop['author_area_enter']).click()
            self.select_area(value=value, types='blogger')

        elif types == '红薯等级':
            level = config.author_level_mapping.get(value, -1)
            if level == -1:
                print('未找到对应的红薯等级：{}'.format(value))
            else:
                self.get_element(self.author_filter_pop['author_level_extend']).click()
                self.get_element(self.author_filter_pop['author_level'].format(level)).click()
        else:
            print('authorLib_filter_by_author_info-博主信息筛选类型错误，仅支持博主性别/博主地区/博主属性/红薯等级')

    def authorLib_filter_by_content_type(self, types, value):
        """博主库内容形式筛选"""
        if types == '赞藏总数':
            liked_value = config.liked_and_collect_mapping.get(value, -1)
            if liked_value != -1:
                self.get_element(self.author_filter_pop['liked_and_collect'].format(liked_value)).click()
            else:
                self.input_value(types='liked_and_collect_input', value=value)
        else:
            print('authorLib_filter_by_content_type-内容筛选类型输入错误，仅支持赞藏总数')

    def authorLib_filter_by_senior_filter(self, types, value):
        """博主库高级筛选"""
        if types == '有MCN机构':
            self.get_element(self.author_filter_pop['senior_filter_btn'].format(1)).click()
        elif types == '有联系方式':
            self.get_element(self.author_filter_pop['senior_filter_btn'].format(2)).click()
        elif types == '有直播带货':
            self.get_element(self.author_filter_pop['senior_filter_btn'].format(3)).click()
        elif types == '报价区间':
            price_value = config.price_mapping.get(value, -1)
            if price_value != -1:
                self.get_element(self.author_filter_pop['have_price'].format(price_value)).click()
            else:
                self.input_value(types='have_price_input', value=value)
        else:
            print('authorLib_filter_by_senior_filter-高级筛选类型输入错误，请输入：有MCN机构/有联系方式/有直播带货/报价区间')

    def noteLib_filter_by_note_types(self, types):
        """笔记库选择不同笔记类型"""
        self.get_element(self.note_types_pop['enter']).click()
        type_value_mapping = {
            '不限': [0],
            '图文笔记': [1],
            '视频笔记': [2],
        }
        value = type_value_mapping.get(types, -1)
        if value == -1:
            print('noteLib_filter_by_note_types-笔记类型输入错误')
        else:
            self.get_element(self.note_types_pop['types_name']).trigger("change", {"value": value})
            self.get_element(self.note_types_pop['confirm']).click()

    def noteLib_filter_by_create_time(self, create_time):
        """笔记库选择不同笔记创建时间"""
        self.get_element(self.note_create_time_pop['enter']).click()
        value = config.note_create_time_mapping.get(create_time, -1)
        if value == -1:
            print('noteLib_filter_by_create_time-笔记创建时间输入错误')
        else:
            self.get_element(self.note_create_time_pop['times_types']).trigger("change", {"value": value})
            self.get_element(self.note_create_time_pop['confirm']).click()

    def noteLib_filter_by_note_info(self, types, value):
        """笔记库笔记信息筛选"""
        if types == '互动量':
            interaction_value = config.interaction_mapping.get(value, -1)
            if interaction_value == -1:
                print('互动量筛选输入错误')
            else:
                self.get_element(self.note_filter_pop['interaction'].format(interaction_value)).click()

        elif types == '点赞数':
            liked_value = config.liked_mapping.get(value, -1)
            if liked_value == -1:
                print('点赞数筛选输入错误')
            else:
                self.get_element(self.note_filter_pop['likes'].format(liked_value)).click()
        else:
            print('noteLib_filter_by_note_info-笔记信息筛选类型错误，仅支持互动量/点赞数')

    def noteLib_filter_by_senior_filter(self, types):
        """笔记库高级筛选"""
        if types == '企业博主发文':
            self.get_element(self.note_filter_pop['senior_filter_btn'].format(1)).click()
        else:
            print('noteLib_filter_by_senior_filter-高级筛选类型输入错误，仅支持企业博主发文')

    def brandLib_filter_by_brand_info(self, types, value):
        """品牌库品牌筛选"""
        if types == '总互动量':
            interaction_value = config.interaction_mapping.get(value, -1)
            if interaction_value == -1:
                print('总互动量筛选输入错误')
            else:
                self.get_element(self.brand_filter_pop['interaction'].format(interaction_value)).click()
        elif types == '种草博主数':
            num_value = config.author_num_mapping.get(value, -1)
            if num_value == -1:
                print('种草博主数输入错误')
            else:
                self.get_element(self.brand_filter_pop['author_num'].format(num_value)).click()
        elif types == '总笔记数':
            num_value = config.author_num_mapping.get(value, -1)
            if num_value == -1:
                print('总笔记数输入错误')
            else:
                self.get_element(self.brand_filter_pop['note_num'].format(num_value)).click()
        else:
            print('brandLib_filter_by_brand_info-筛选类型输入错误，仅支持总互动量/种草博主数/总笔记数')

    def kindLib_filter_by_times(self, times):
        """品类库筛选不同时间"""
        self.get_element(self.kind_times_pop['enter']).click()
        value = config.kindLib_times_mapping.get(times, -1)
        if value == -1:
            print('kindLib_filter_by_times-品类周期时间输入错误')
        else:
            self.get_element(self.kind_times_pop['times']).trigger("change", {"value": value})
            self.get_element(self.kind_times_pop['confirm']).click()















