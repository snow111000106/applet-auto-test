#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/10/7
# @Author : chenxuehong
# @Version：V 0.1
# @File : test_search.py
# @desc : 专业版-搜索页面测试用例

import time
import minium
from common.base import Base
from testcase.vip_4.BaseCase import BaseCase
from common.CustomAssert import CustomAssert
from page.SearchPage import SearchPage


@minium.ddt_class
class SearchPageTest(BaseCase):

    def __init__(self, methodName='runTest'):
        super(SearchPageTest, self).__init__(methodName)
        self.searchpage = SearchPage(self)
        self.CustomAssert = CustomAssert()

    def setUp(self):
        self.searchpage.into_search()

    def tearDown(self):
        self.searchpage.go_to_home()
        time.sleep(1)

    @minium.ddt_case('粉丝数最多', '涨粉数最多', '赞藏最多')
    def test_authorLib_sort(self, sort_types):
        """
        测试专业版用户的博主库可切换排序
        """
        # 粉丝数最多对应校验粉丝数，粉丝数在get_author_info在第2位置，赞藏数在第3位置，涨粉数在第4位置
        sort_mapping = {
            '粉丝数最多': 2, '赞藏最多': 3, '涨粉数最多': 4,
        }
        value = sort_mapping.get(sort_types, -1)
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_sort(types='博主', sort_types=sort_types)
        info = self.searchpage.get_author_info(num=10)
        for i in range(len(info) - 1):
            self.assertGreaterEqual(info[i][value], info[i + 1][value])

    def test_authorLib_filter_by_one_first_label(self):
        """
        测试专业版用户的博主库可筛选单个博主一级标签
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.authorLib_filter_by_label(first_label='科技数码', second_label='全部')
        time.sleep(2)
        info = self.searchpage.get_author_label(num=10)
        for i in range(len(info)):
            self.assertIn('科技数码', info[i][2])

    def test_authorLib_filter_by_one_second_label(self):
        """
        测试专业版用户的博主库可筛选单个博主二级标签
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.authorLib_filter_by_label(first_label='美妆', second_label='香水')
        time.sleep(2)
        info = self.searchpage.get_author_label(num=10)
        for i in range(len(info)):
            self.assertIn('美妆', info[i][2])

    def test_authorLib_filter_by_multi_first_label(self):
        """
        测试专业版用户的博主库可筛选多个博主一级标签
        """
        self.searchpage.select_tab(tab_name='博主')
        first_label = ['游戏', '运动健身']
        self.searchpage.authorLib_filter_by_mult_first_author_label(first_label=first_label)
        time.sleep(2)
        info = self.searchpage.get_author_label(num=10)
        for i in range(len(info)):
            self.assertMultiIn(first_label, info[i][2])

    def test_authorLib_filter_by_multi_second_label(self):
        """
        测试专业版用户的博主库可筛选多个博主二级标签
        """
        self.searchpage.select_tab(tab_name='博主')
        labels = [['时尚', ['发型', '鞋靴']], ['美妆', ['美甲', '香水']]]
        self.searchpage.authorLib_filter_by_mult_second_author_label(labels=labels)
        time.sleep(2)
        info = self.searchpage.get_author_label(num=10)
        for i in range(len(info)):
            self.assertMultiIn([labels[0][0], labels[1][0]], info[i][2])

    def test_authorLib_filter_by_one_fans_label(self):
        """
        测试专业版用户的博主库可筛选单个粉丝标签
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.authorLib_filter_by_fans_label(fans_labels='旅行达人')
        time.sleep(2)
        info = self.searchpage.get_author_info(num=10)
        self.assertEqual(len(info), 10)

    def test_authorLib_filter_by_multi_fans_label(self):
        """
        测试专业版用户的博主库可筛选多个粉丝标签
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.authorLib_filter_by_fans_label(
            fans_labels=['旅行达人', '爱美少女', '带娃宝妈', '追星族', '二次元萌宅'])
        time.sleep(2)
        info = self.searchpage.get_author_label(num=10)
        self.assertEqual(len(info), 10)

    @minium.ddt_case('图文为主', '视频为主')
    def test_authorLib_filter_by_content_form(self, types):
        """
        测试专业版用户的博主库可筛选内容形式
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.authorLib_filter_by_content_form(types=types)
        time.sleep(2)
        info = self.searchpage.get_author_info(num=10)
        self.assertEqual(len(info), 10)

    def test_authorLib_filter_by_90_note(self):
        """
        测试专业版用户的博主库可筛选近90天爆文数
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.authorLib_filter_by_note(types='1-10', note_types='近90天爆文数')
        time.sleep(2)
        self.searchpage.scroll_filter_item(types='author')
        info = self.searchpage.get_author_info(num=10)
        self.assertEqual(len(info), 10)

    def test_authorLib_filter_by_business_note(self):
        """
        测试专业版用户的博主库可筛选近90天商业笔记数
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.authorLib_filter_by_note(types='11-50', note_types='近90天商业笔记数')
        self.searchpage.scroll_filter_item(types='author')
        time.sleep(2)
        info = self.searchpage.get_author_info(num=10)
        self.assertEqual(len(info), 10)

    def test_authorLib_filter_by_brand_cooperate(self):
        """
        测试专业版用户的博主库可筛选有品牌合作
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.authorLib_filter_by_brand_cooperate()
        self.searchpage.scroll_filter_item(types='author')
        time.sleep(2)
        info = self.searchpage.get_author_info(num=10)
        self.assertEqual(len(info), 10)

    @minium.ddt_case('男', '女')
    def test_authorLib_filter_by_author_gender(self, gender):
        """
        测试专业版用户的博主库可以筛选博主性别
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_author_filter(filter_types='博主信息', types='博主性别', value=gender)
        time.sleep(2)
        info = self.searchpage.get_author_info(num=10)
        self.assertEqual(len(info), 10)

    @minium.ddt_case('企业账号', '个人账号')
    def test_authorLib_filter_by_author_types(self, types):
        """
        测试专业版用户的博主库可以筛选博主属性
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_author_filter(filter_types='博主信息', types='博主属性', value=types)
        time.sleep(2)
        info = self.searchpage.get_author_info(num=10)
        self.assertEqual(len(info), 10)

    def test_authorLib_filter_by_author_area(self):
        """
        测试专业版用户的博主库可以筛选博主地区
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_author_filter(filter_types='博主信息', types='博主地区', value=['福建省', '厦门市'])
        time.sleep(2)
        info = self.searchpage.get_author_info(num=10)
        self.assertEqual(len(info), 10)

    def test_authorLib_filter_by_author_level(self):
        """
        测试专业版用户的博主库可以筛选博主红薯等级
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_author_filter(filter_types='博主信息', types='红薯等级', value='金冠薯')
        time.sleep(2)
        info = self.searchpage.get_author_info(num=10)
        self.assertEqual(len(info), 10)

    def test_authorLib_filter_by_fans_level(self):
        """
        测试专业版用户的博主库可以筛选粉丝量级
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_author_filter(filter_types='粉丝信息', types='粉丝量级', value='0-1000')
        time.sleep(2)
        try:
            info = self.searchpage.get_author_info(num=10)
            for i in range(len(info)):
                self.CustomAssert.assertGreaterEqual(info[i][2], 0)
                self.CustomAssert.assertLessEqual(info[i][2], 1000)
        finally:
            self.capture(name='result')

    @minium.ddt_case('男性居多', '女性居多')
    def test_authorLib_filter_by_fans_gender(self, gender):
        """
        测试专业版用户的博主库可以筛选粉丝性别
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_author_filter(filter_types='粉丝信息', types='粉丝性别', value=gender)
        time.sleep(2)
        info = self.searchpage.get_author_info(num=10)
        self.assertEqual(len(info), 10)

    def test_authorLib_filter_by_fans_area(self):
        """
        测试专业版用户的博主库可以筛选粉丝地区
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_author_filter(filter_types='粉丝信息', types='粉丝地区', value=['辽宁省', '丹东市'])
        time.sleep(2)
        info = self.searchpage.get_author_info(num=10)
        self.assertEqual(len(info), 10)

    def test_authorLib_filter_by_fans_age(self):
        """
        测试专业版用户的博主库可以筛选粉丝年龄
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_author_filter(filter_types='粉丝信息', types='粉丝年龄', value='18-24')
        time.sleep(2)
        info = self.searchpage.get_author_info(num=10)
        self.assertEqual(len(info), 10)

    def test_authorLib_filter_by_liked(self):
        """
        测试专业版用户的博主库可以筛选赞藏总数
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_author_filter(filter_types='内容筛选', types='赞藏总数', value='5W-10W')
        time.sleep(2)

        try:
            info = self.searchpage.get_author_info(num=10)
            for i in range(len(info)):
                self.CustomAssert.assertGreaterEqual(info[i][3], 50000)
                self.CustomAssert.assertLessEqual(info[i][3], 100000)
        finally:
            self.capture(name='result')

    @minium.ddt_case('有MCN机构', '有联系方式', '有直播带货')
    def test_authorLib_filter_by_senior(self, types):
        """
        测试专业版用户的博主库可筛选高级筛选
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_author_filter(filter_types='高级筛选', types=types, value=None)
        time.sleep(2)
        info = self.searchpage.get_author_info(num=10)
        self.assertEqual(len(info), 10)

    def test_authorLib_filter_by_price(self):
        """
        测试专业版用户的博主库可筛选报价区间
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_author_filter(filter_types='高级筛选', types='报价区间', value='0-1000')
        time.sleep(2)
        info = self.searchpage.get_author_info(num=10)
        self.assertEqual(len(info), 10)

    @minium.ddt_case('互动量', '点赞数', '评论数', '收藏数')
    def test_noteLib_sort(self, sort_types):
        """
        测试专业版用户的笔记库可切换排序
        """
        # 互动量排序对应校验互动量，互动量在get_note_info在第4位置，点赞数在第5位置，评论数在第6位置，收藏数在第7位置
        sort_mapping = {
            '互动量': 4, '点赞数': 5, '评论数': 6, '收藏数': 7
        }
        value = sort_mapping.get(sort_types, -1)
        self.searchpage.select_tab(tab_name='笔记')
        self.searchpage.select_sort(types='笔记', sort_types=sort_types)
        info = self.searchpage.get_note_info(num=10)
        for i in range(len(info) - 1):
            self.assertGreaterEqual(info[i][value], info[i + 1][value])

    def test_noteLib_filter_by_first_label(self):
        """
        测试专业版用户的笔记库可筛选单个笔记一级标签
        """
        self.searchpage.select_tab(tab_name='笔记')
        self.searchpage.noteLib_filter_by_label(first_label='时尚', second_label='全部')
        time.sleep(2)
        info = self.searchpage.get_note_label(num=10)
        for i in range(len(info)):
            self.assertIn('时尚', info[i][2])

    def test_noteLib_filter_by_second_label(self):
        """
        测试专业版用户的笔记库可筛选单个笔记二级标签
        """
        self.searchpage.select_tab(tab_name='笔记')
        self.searchpage.noteLib_filter_by_label(first_label='美妆', second_label='香水')
        time.sleep(2)
        info = self.searchpage.get_note_label(num=10)
        for i in range(len(info)):
            self.assertIn('美妆', info[i][2])

    @minium.ddt_case('图文笔记', '视频笔记')
    def test_noteLib_filter_by_note_types(self, types):
        """
        测试专业版用户的笔记库可筛选笔记类型
        """
        self.searchpage.select_tab(tab_name='笔记')
        self.searchpage.noteLib_filter_by_note_types(types=types)
        time.sleep(2)
        info = self.searchpage.get_note_label(num=10)
        self.assertEqual(len(info), 10)

    @minium.ddt_case('6小时', '12小时', '24小时', '近3天', '近7天', '近15天', '近30天', '近90天')
    def test_noteLib_filter_by_create_time(self, create_time):
        """
        测试专业版用户的笔记库可筛选笔记发布时间
        """
        self.searchpage.select_tab(tab_name='笔记')
        self.searchpage.noteLib_filter_by_create_time(create_time=create_time)
        time.sleep(2)
        try:
            info = self.searchpage.get_note_info(num=10)
            re_times = Base.times_change(create_time)
            for i in range(len(info)):
                times = info[i][3]
                self.CustomAssert.assertDatetimeBefore(re_times, times)
        finally:
            self.capture('result')

    @minium.ddt_case('商业笔记', '低粉爆文')
    def test_noteLib_filter_by_note_btn(self, types):
        """
        测试专业版用户的笔记库可筛选商业笔记/低粉爆文
        """
        self.searchpage.select_tab(tab_name='笔记')
        self.searchpage.noteLib_filter_by_types(types=types)
        self.searchpage.scroll_filter_item(types='note')
        time.sleep(2)
        info = self.searchpage.get_note_info(num=10)
        if types == '低粉爆文':
            for i in range(len(info)):
                self.assertGreater(info[i][5], 500)
        else:
            self.assertEqual(len(info), 10)

    def test_noteLib_filter_by_interaction(self):
        """
        测试专业版用户的笔记库可筛选互动量
        """
        self.searchpage.select_tab(tab_name='笔记')
        self.searchpage.select_note_filter(filter_types='笔记筛选', types='互动量', value='1000-5000')
        time.sleep(2)
        try:
            info = self.searchpage.get_note_info(num=10)
            for i in range(len(info)):
                self.assertGreaterEqual(info[i][4], 1000)
                self.assertLessEqual(info[i][4], 5000)
        finally:
            self.capture('result')

    def test_noteLib_filter_by_liked(self):
        """
        测试专业版用户的笔记库可筛选点赞数
        """
        self.searchpage.select_tab(tab_name='笔记')
        self.searchpage.select_note_filter(filter_types='笔记筛选', types='点赞数', value='200-500')
        time.sleep(2)
        try:
            info = self.searchpage.get_note_info(num=10)
            for i in range(len(info)):
                self.assertGreaterEqual(info[i][5], 200)
                self.assertLessEqual(info[i][5], 500)
        finally:
            self.capture('result')

    @minium.ddt_case('男性居多', '女性居多')
    def test_noteLib_filter_by_fans_gender(self, gender):
        """
        测试专业版用户的笔记库可以筛选粉丝性别
        """
        self.searchpage.select_tab(tab_name='笔记')
        self.searchpage.select_note_filter(filter_types='粉丝信息', types='粉丝性别', value=gender)
        time.sleep(2)
        info = self.searchpage.get_note_info(num=10)
        self.assertEqual(len(info), 10)

    def test_noteLib_filter_by_fans_area(self):
        """
        测试专业版用户的笔记库可以筛选粉丝地区
        """
        self.searchpage.select_tab(tab_name='笔记')
        self.searchpage.select_note_filter(filter_types='粉丝信息', types='粉丝地区', value=['福建省', '泉州市'])
        time.sleep(2)
        info = self.searchpage.get_note_info(num=10)
        self.assertEqual(len(info), 10)

    def test_noteLib_filter_by_senior(self):
        """
        测试专业版用户的笔记库可筛选高级筛选-企业博主发文
        """
        self.searchpage.select_tab(tab_name='笔记')
        self.searchpage.select_note_filter(filter_types='高级筛选', types='企业博主发文', value=None)
        time.sleep(2)
        info = self.searchpage.get_note_info(num=10)
        self.assertEqual(len(info), 10)

    @minium.ddt_case('最近投放时间', '昨日互动增量', '总互动量', '总博主数', '总笔记数')
    def test_brandLib_sort(self, sort_types):
        """
        测试专业版用户的品牌库可切换排序
        """
        # 最近投放时间排序对应校验投放时间，投放时间在get_brand_info在第2位置，总互动量在第3位置，总博主数在第4位置，总笔记数在第5位置
        sort_mapping = {
            '最近投放时间': 2, '昨日互动增量': -1, '总互动量': 3, '总博主数': 4, '总笔记数': 5
        }
        value = sort_mapping.get(sort_types, -1)
        self.searchpage.select_tab(tab_name='品牌')
        self.searchpage.select_sort(types='品牌', sort_types=sort_types)
        info = self.searchpage.get_brand_info(num=10)
        for i in range(len(info) - 1):
            if sort_types == '最近投放时间':
                self.CustomAssert.assertDatetimeBefore(info[i + 1][value], info[i][value])
                self.capture('result')
            elif sort_types == '昨日互动增量':
                self.assertEqual(len(info), 10)
            else:
                self.assertLessEqual(info[i + 1][value], info[i][value])

    def test_brandLib_filter_by_first_label(self):
        """
        测试专业版用户的品牌库可筛选一级品牌标签
        """
        self.searchpage.select_tab(tab_name='品牌')
        self.searchpage.brandLib_filter_by_label(first_label='美食/饮食', second_label='全部')
        label = self.searchpage.get_brand_label(num=10)
        for i in range(len(label)):
            self.assertIsNotNone(label[i][2])

    def test_brandLib_filter_by_second_label(self, ):
        """
        测试专业版用户的品牌库可筛选二级品牌标签
        """
        self.searchpage.select_tab(tab_name='品牌')
        self.searchpage.brandLib_filter_by_label(first_label='日用/宠物', second_label='宠物')
        label = self.searchpage.get_brand_label(num=10)
        for i in range(len(label)):
            self.assertIn('宠物', label[i][2])

    def test_brandLib_filter_by_business(self):
        """
        测试专业版用户的品牌库可筛选有商业投放
        """
        self.searchpage.select_tab(tab_name='品牌')
        self.searchpage.brandLib_filter_by_business()
        info = self.searchpage.get_brand_info(num=10)
        self.assertEqual(len(info), 10)

    def test_brandLib_filter_by_other_labels(self):
        """
        测试专业版用户的品牌库可筛选标签按钮
        """
        self.searchpage.select_tab(tab_name='品牌')
        self.searchpage.brandLib_filter_by_other_labels(types='科技/厨电')
        label = self.searchpage.get_brand_label(num=10)
        for i in range(len(label)):
            self.assertIsNotNone(label[i][2])

    def test_brandLib_filter_by_interaction(self):
        """
        测试专业版用户的品牌库可筛选总互动量
        """
        self.searchpage.select_tab(tab_name='品牌')
        self.searchpage.select_brand_filter(filter_types='品牌筛选', types='总互动量', value='1000-5000')
        time.sleep(2)
        try:
            info = self.searchpage.get_brand_info(num=10)
            for i in range(len(info)):
                self.assertGreaterEqual(info[i][3], 1000)
                self.assertLessEqual(info[i][3], 5000)
        finally:
            self.capture('result')

    def test_brandLib_filter_by_author_num(self):
        """
        测试专业版用户的品牌库可筛选种草博主数
        """
        self.searchpage.select_tab(tab_name='品牌')
        self.searchpage.select_brand_filter(filter_types='品牌筛选', types='种草博主数', value='50-100')
        time.sleep(2)
        try:
            info = self.searchpage.get_brand_info(num=10)
            for i in range(len(info)):
                self.assertGreaterEqual(info[i][4], 50)
                self.assertLessEqual(info[i][4], 100)
        finally:
            self.capture('result')

    def test_brandLib_filter_by_note_num(self):
        """
        测试专业版用户的品牌库可筛选总笔记数
        """
        self.searchpage.select_tab(tab_name='品牌')
        self.searchpage.select_brand_filter(filter_types='品牌筛选', types='总笔记数', value='10-30')
        time.sleep(2)
        try:
            info = self.searchpage.get_brand_info(num=10)
            for i in range(len(info)):
                self.assertGreaterEqual(info[i][5], 10)
                self.assertLessEqual(info[i][5], 30)
        finally:
            self.capture('result')

    @minium.ddt_case('男性居多', '女性居多')
    def test_brandLib_filter_by_fans_gender(self, gender):
        """
        测试专业版用户的品牌库可筛选粉丝性别
        """
        self.searchpage.select_tab(tab_name='品牌')
        self.searchpage.select_brand_filter(filter_types='粉丝信息', types='粉丝性别', value=gender)
        time.sleep(2)
        info = self.searchpage.get_brand_info(num=10)
        self.assertEqual(len(info), 10)

    def test_brandLib_filter_by_fans_area(self):
        """
        测试专业版用户的品牌库可筛选粉丝地区
        """
        self.searchpage.select_tab(tab_name='品牌')
        self.searchpage.select_brand_filter(filter_types='粉丝信息', types='粉丝地区', value=['天津市', '不限'])
        time.sleep(2)
        info = self.searchpage.get_brand_info(num=10)
        self.assertEqual(len(info), 10)

    @minium.ddt_case('笔记最多', '互动量最多')
    def test_kindLib_sort(self, sort_types):
        """
        测试专业版用户的品类库可筛选排序
        """
        # 笔记最多排序对应校验笔记数，笔记数在get_kind_info在第2位置，总互动量在第3位置
        sort_mapping = {
            '笔记最多': 2, '互动量最多': 3
        }
        value = sort_mapping.get(sort_types, -1)
        self.searchpage.select_tab(tab_name='品类')
        self.searchpage.select_sort(types='品类', sort_types=sort_types)
        time.sleep(2)
        info = self.searchpage.get_kind_info(num=10)
        for i in range(len(info) - 1):
            self.assertLessEqual(info[i + 1][value], info[i][value])

    @minium.ddt_case('近7天', '近15天', '近30天', '近90天', '近180天', '近360天')
    def test_kindLib_filter_by_times(self, times):
        """
        测试专业版用户的品类库可筛选时间
        """
        self.searchpage.select_tab(tab_name='品类')
        self.searchpage.kindLib_filter_by_times(times=times)
        time.sleep(2)
        if times == '近360天':
            status = self.searchpage.is_vip_have_authority(tab_name='category')
            self.assertTrue(status)
        else:
            info = self.searchpage.get_kind_info(num=10)
            self.assertEqual(len(info), 10)

    def test_kindLib_filter_by_first_label(self):
        """
        测试专业版用户的品类库可筛选一级标签
        """
        self.searchpage.select_tab(tab_name='品类')
        self.searchpage.kindLib_filter_by_label(first_label='日用/宠物', second_label='全部')
        time.sleep(2)
        label = self.searchpage.get_kind_label(num=10)
        for i in range(len(label)):
            self.assertIn('日用/宠物', label[i][2])

    def test_kindLib_filter_by_second_label(self):
        """
        测试专业版用户的品类库可筛选二级品类标签
        """
        self.searchpage.select_tab(tab_name='品类')
        self.searchpage.kindLib_filter_by_label(first_label='日用/宠物', second_label='宠物')
        label = self.searchpage.get_kind_label(num=10)
        for i in range(len(label)):
            self.assertIn('宠物', label[i][2])

    def test_kindLib_filter_by_other_labels(self):
        """
        测试专业版用户的品类库可筛选标签按钮
        """
        self.searchpage.select_tab(tab_name='品类')
        self.searchpage.kindLib_filter_by_other_labels(types='美妆/装扮')
        label = self.searchpage.get_kind_label(num=10)
        for i in range(len(label)):
            self.assertIn('美妆/装扮', label[i][2])

    def test_hotWordLib_sort(self):
        """
        测试专业版用户的热搜词库可筛选排序
        """
        self.searchpage.select_tab(tab_name='热搜词')
        self.searchpage.select_sort(types='热搜词', sort_types='热度值排序')
        time.sleep(2)
        info = self.searchpage.get_hot_word_info(num=10)
        for i in range(len(info) - 1):
            self.assertLessEqual(info[i + 1][4], info[i][4])

    def test_hotWordLib_filter_by_first_label(self):
        """
        测试专业版用户的热搜词库可筛选单个一级标签
        """
        self.searchpage.select_tab(tab_name='热搜词')
        self.searchpage.hotWordLib_filter_by_label(first_label='时尚', second_label='全部')
        time.sleep(2)
        info = self.searchpage.get_hot_word_info(num=10)
        self.assertEqual(len(info), 10)

    def test_hotWordLib_filter_by_second_label(self):
        """
        测试专业版用户的热搜词库可筛选单个二级标签
        """
        self.searchpage.select_tab(tab_name='热搜词')
        self.searchpage.hotWordLib_filter_by_label(first_label='摄影', second_label='摄影器材')
        time.sleep(2)
        info = self.searchpage.get_hot_word_info(num=10)
        self.assertEqual(len(info), 10)

    def test_hotWordLib_filter_by_other_label(self):
        """
        测试专业版用户的热搜词库可筛选标签按钮
        """
        self.searchpage.select_tab(tab_name='热搜词')
        self.searchpage.hotWordLib_filter_by_other_labels(types='摄影')
        time.sleep(2)
        info = self.searchpage.get_hot_word_info(num=10)
        self.assertEqual(len(info), 10)


