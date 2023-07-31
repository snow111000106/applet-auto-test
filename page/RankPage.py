#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/5/10
# @Author : chenxuehong
# @Version：V 0.1
# @File : RankPage.py
# @desc : 榜单页面封装

from page.BasePage import BasePage


class RankPage(BasePage):

    # 涨粉榜
    fans_inc_rank = "/page/view/view[2]/view/author-rank/view/view/view[1]"
    # 实时笔记榜
    note_realtime_rank = "/page/view/view[2]/view/notes-rank/view/view/view[1]"
    # 品牌种草榜
    brand_recommend_rank = "/page/view/view[2]/view/notes-rank/view/view/view[1]"
    # 品类种草榜
    kind_recommend_rank = "/page/view/view[2]/view/notes-rank/view/view/view[1]"
    # 热搜词增量榜
    hot_key_inc_rank = "/page/view/view[2]/view/hot-wordsrank/view/view/view[1]"

    def is_element_exist(self, rank_type):
        """ 判断榜单存在 """

        result = False
        if rank_type == 'author':
            result = self.is_ele_exist(self.fans_inc_rank)
        elif rank_type == 'note':
            result = self.is_ele_exist(self.note_realtime_rank)
        elif rank_type == 'brand':
            result = self.is_ele_exist(self.brand_recommend_rank)
        elif rank_type == 'kind':
            result = self.is_ele_exist(self.kind_recommend_rank)
        elif rank_type == 'hot_key':
            result = self.is_ele_exist(self.hot_key_inc_rank)
        else:
            print('榜单类型输入错误')
        return result




