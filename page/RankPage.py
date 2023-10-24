#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/5/10
# @Author : chenxuehong
# @Version：V 0.1
# @File : RankPage.py
# @desc : 榜单页面封装
import time
from page.BasePage import BasePage
from conf import route

class RankPage(BasePage):

    #博主
    author_rank="/page/view/view[1]/view[2]/view/scroll-view/view/view[1]/text"
    #涨粉榜
    author_fans_inc_rank = "/page/view/view[2]/view/author-rank/view/view/view[1]"
    #行业榜
    author_industry_rank='/page/view/view[2]/view/author-rank//view/view/view[2]'
    #地区榜
    author_area_rank='/page/view/view[2]/view/author-rank//view/view/view[3]'
    #MCN榜
    author_mcn_rank='/page/view/view[2]/view/author-rank//view/view/view[4]'


    #笔记
    note_rank="/page/view/view[1]/view[2]/view/scroll-view/view/view[2]/text"    
    #实时笔记榜
    note_realtime_rank = "/page/view/view[2]/view/notes-rank/view/view/view[1]"
    #商业笔记榜
    business_note_rank="/page/view/view[2]/view/notes-rank//view/view/view[2]"
    #低粉爆文榜
    low_fans_note="/page/view/view[2]/view/notes-rank//view/view/view[3]"



    #品牌
    brand_rank="/page/view/view[1]/view[2]/view/scroll-view/view/view[3]/text"
    #商业投放榜
    brand_business_rank="/page/view/view[2]/view/brand-rank//view/view/view[1]"
    #品牌种草榜
    brand_recommend_rank = "/page/view/view[2]/view/brand-rank//view/view/view[2]"
    #投放增长榜
    brand_launch_rank="/page/view/view[2]/view/brand-rank//view/view/view[3]"


    #品类
    kind_rank="/page/view/view[1]/view[2]/view/scroll-view/view/view[4]/text"
    #商业投放榜
    kind_business_rank="/page/view/view[2]/view/category-rank//view/view/view[1]"
    #品类种草榜
    kind_recommend_rank = "/page/view/view[2]/view/category-rank//view/view/view[2]"
    #投放增长榜
    kind_launch_rank="/page/view/view[2]/view/category-rank//view/view/view[3]"


    #热搜词
    hot_key_rank="/page/view/view[1]/view[2]/view/scroll-view/view/view[5]/text"
    #热搜词增量榜
    hot_key_inc_rank = "/page/view/view[2]/view/hot-wordsrank//view/view/view[1]"
    #热搜词总量榜
    hot_key_total_rank="/page/view/view[2]/view/hot-wordsrank//view/view/view[2]"

    


    #博主--类目选择--css选择器
    author_category_choice='.uni-input.flex.align-items-center.data-v-44afd76e'
    #博主--城市选择--css选择器
    author_city_choice=".c646a73.fs26._div.data-v-a54cc9c4"


    #笔记-实时笔记榜打开时间选择弹窗--xpath
    note_realtime_open_time_choice="/page/view/view[2]/view/notes-rank//view/real-time//view/view[1]/view/sort[1]//view/view/view[1]"
    #笔记-低粉爆文榜打开时间选择弹窗--xpath
    note_low_fans="/page/view/view[2]/view/notes-rank//view/low-powder-message//view/view[1]/view/sort[1]//view/view/view[1]"
    #笔记-打开选择排序字段弹窗--css(使用的时候要结合文字过滤)
    note_open_sort_choice=".uni-input.c646a73.fs26.data-v-0255a0d4"
    #笔记-打开类目选择弹窗-css
    note_open_category_choice=".uni-input.c646a73.fs28.data-v-0f1fbb8d"


    #品牌-打开类目选择弹窗-css
    brand_open_category_choice=".uni-input.c646a73.fs28.data-v-6c3cf032"

    #品类-打开类目选择弹窗-css
    kind_open_category_choice=".uni-input.c646a73.fs28.data-v-64200b9c"

    #热搜词-打开类目选择弹窗-css
    hot_key_open_category_choice=".uni-input.c646a73.fs28.data-v-0f1fbb8d"

    ######通用元素######

    #弹窗确认按钮--css选择器(所有榜单通用)
    pop_yes_button=".u-select__header__confirm.u-select__header__btn.data-v-42a2fee4"

    #升级会员按钮--css选择器(所有榜单通用)
    upgrade_vip_button=".contact-btn.data-v-0de29d0e"
    #升级会员提示文案--css选择器(所有榜单通用)
    upgrade_vip_text=".fs28.font-weight-500.c202629.data-v-0de29d0e"

    #所有榜单弹窗选择滑块（左边项或单独一整条）--css选择器
    pop_item_select=".u-select__body__picker-view__item.data-v-42a2fee4"
    
    #打开日周月榜选择弹窗--css选择器
    open_date_choice=".c646a73.fs26._div.data-v-185d6c3d"


    def into_rank_page(self):
        """进入榜单页"""
        self.switch_to_tabbar(route.rank_page)
        time.sleep(1)
        return self


    def switch_rank(self,rank_type):
        """切换到不同的大榜单"""
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
            print('榜单类型输入错误')

        time.sleep(1)
        return self

    def switch_detail_rank(self,rank_type,detail_type):
        """切换到不同榜单下的细分榜"""

        if rank_type == 'author':
            if detail_type=="fans":
                self.get_element(self.author_fans_inc_rank).click()
            elif detail_type=="industry":
                self.get_element(self.author_industry_rank).click()
            elif detail_type=="area":
                self.get_element(self.author_area_rank).click()
            elif detail_type=="mcn":
                self.get_element(self.author_mcn_rank).click()
            else:
                print("榜单输入错误")
        elif rank_type == 'note':
            if detail_type=="realtime":
                self.get_element(self.note_realtime_rank).click()
            elif detail_type=="business":
                self.get_element(self.business_note_rank).click()
            elif detail_type=="low_fans":
                self.get_element(self.low_fans_note).click()
            else:
                print("榜单输入错误")
        elif rank_type == 'brand':
            if detail_type=="business":
                self.get_element(self.brand_business_rank).click()
            elif detail_type=="recommend":
                self.get_element(self.brand_recommend_rank).click()
            elif detail_type=="launch":
                self.get_element(self.brand_launch_rank).click()
            else:
                print("榜单输入错误")
        elif rank_type == 'kind':
            if detail_type=="business":
                self.get_element(self.kind_business_rank).click()
            elif detail_type=='recommend':
                self.get_element(self.kind_recommend_rank).click()
            elif detail_type=="launch":
                self.get_element(self.kind_launch_rank).click()
            else:
                print("榜单输入错误")
        elif rank_type == 'hot_key':
            if detail_type=='inc':
                self.get_element(self.hot_key_inc_rank).click()
            elif detail_type=="total":
                self.get_element(self.hot_key_total_rank).click()
            else:
                print("榜单输入错误")
        else:
            print('榜单类型输入错误')

    def is_have_upgrade(self):
        if self.is_ele_exist(self.upgrade_vip_button,inner_text="升级会员") and self.is_ele_exist(self.upgrade_vip_text,inner_text="升级会员可查看更多数据，"):
            return True
        else:
            return False




