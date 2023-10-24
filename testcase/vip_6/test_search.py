#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/7/3
# @Author : chenxuehong
# @Version：V 0.1
# @File : test_search.py
# @desc : 企业版-搜索页面测试用例
import time
import minium
from common.base import Base
from testcase.vip_6.BaseCase import BaseCase
from common.CustomAssert import CustomAssert
from page.SearchPage import SearchPage
from conf import route


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

    @minium.ddt_case(('博主', '美妆', 5), ('笔记', '测试', 9), ('品牌', '华为', 4),
                     ('品类', '手机', 4), ('热搜词', '分享', 4))
    def test_element_is_exist(self, value):
        """
        测试搜索关键字后，各个模块的元素存在
        """
        tab_name, key, num = value
        self.searchpage.search(value=key)
        time.sleep(1)
        self.searchpage.scroll_to_item(types=tab_name)
        self.searchpage.scroll_to_item(types=tab_name, top=True)
        self.assertEqual(self.searchpage.is_tab_ele_exist(tab_name=tab_name), num)

    @minium.ddt_case('博主', '笔记', '品牌', '品类', '热搜词')
    def test_click_more(self, value):
        """
        测试点击查看更多相关，跳转到相应的模块
        """
        self.searchpage.search(value='小')
        self.searchpage.click_more(tab_name=value)
        self.assertTrue(self.searchpage.sure_into_tab(tab_name=value))
        time.sleep(2)
        self.searchpage.select_tab(tab_name='全部')

    def test_history_search(self):
        """
        测试搜索关键词后，历史搜索有记录
        """
        if self.searchpage.is_history_word_exist():
            self.searchpage.click_clear_history()
        else:
            print('历史搜索已清空')
        self.searchpage.search(value='美')
        self.searchpage.back()
        time.sleep(0.5)
        self.searchpage.into_search()
        time.sleep(0.5)
        word = self.searchpage.get_history_word()
        self.assertEqual(word, ['美'])

    def test_hot_word(self):
        """
        测试热门搜索有数据
        """
        word = self.searchpage.get_hot_search_word()
        self.assertNotEqual(len(word), 0)

    @minium.ddt_case(('博主', route.author_detail_page), ('笔记', route.note_detail_page), ('品牌', route.brand_detail_page),
                     ('品类', route.kind_detail_page), ('热搜词', route.hot_key_detail_page))
    def test_into_detail(self, value):
        """
        测试各个库跳转详情页
        """
        try:
            types, re_route = value
            self.searchpage.select_tab(tab_name=types)
            self.searchpage.click_into_detail(types=types)
            routes = self.searchpage.current_path
            time.sleep(2)
            self.assertEqual(routes, re_route)
        finally:
            self.searchpage.back(delta=1)

    @minium.ddt_case('粉丝数最多', '涨粉数最多', '赞藏最多')
    def test_authorLib_sort(self, sort_types):
        """
        测试企业版用户的博主库可切换排序
        """
        # 粉丝数最多对应校验粉丝数，粉丝数在get_author_info在第2位置，赞藏数在第3位置，涨粉数在第4位置
        sort_mapping = {
            '粉丝数最多': 2, '赞藏最多': 3, '涨粉数最多': 4,
        }
        value = sort_mapping.get(sort_types, -1)
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_sort(types='博主', sort_types=sort_types)
        info = self.searchpage.get_author_info(num=10)
        for i in range(len(info)-1):
            self.assertGreaterEqual(info[i][value], info[i+1][value])

    @minium.ddt_case('时尚', '体育赛事', '科技数码', '美妆', '出行')
    def test_authorLib_filter_by_one_first_label(self, label):
        """
        测试企业版用户的博主库可筛选单个博主一级标签
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.authorLib_filter_by_label(first_label=label, second_label='全部')
        time.sleep(2)
        info = self.searchpage.get_author_label(num=10)
        for i in range(len(info)):
            self.assertIn(label, info[i][2])

    @minium.ddt_case(('美妆', '香水'), ('宠物', '狗'), ('摄影', '摄影器材'), ('母婴', '育儿经验'), ('美食', '美食VLOG'))
    def test_authorLib_filter_by_one_second_label(self, labels):
        """
        测试企业版用户的博主库可筛选单个博主二级标签
        """
        first, second = labels
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.authorLib_filter_by_label(first_label=first, second_label=second)
        time.sleep(2)
        info = self.searchpage.get_author_label(num=10)
        for i in range(len(info)):
            self.assertIn(first, info[i][2])

    def test_authorLib_filter_by_multi_first_label(self):
        """
        测试企业版用户的博主库可筛选多个博主一级标签
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
        测试企业版用户的博主库可筛选多个博主二级标签
        """
        self.searchpage.select_tab(tab_name='博主')
        labels = [['时尚', ['发型', '鞋靴']], ['美妆', ['美甲', '香水']]]
        self.searchpage.authorLib_filter_by_mult_second_author_label(labels=labels)
        time.sleep(2)
        info = self.searchpage.get_author_label(num=10)
        for i in range(len(info)):
            self.assertMultiIn([labels[0][0], labels[1][0]], info[i][2])

    @minium.ddt_case('旅行达人', '爱美少女', '带娃宝妈', '追星族', '二次元萌宅')
    def test_authorLib_filter_by_one_fans_label(self, label):
        """
        测试企业版用户的博主库可筛选单个粉丝标签
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.authorLib_filter_by_fans_label(fans_labels=label)
        time.sleep(2)
        info = self.searchpage.get_author_info(num=10)
        self.assertEqual(len(info), 10)

    def test_authorLib_filter_by_multi_fans_label(self):
        """
        测试企业版用户的博主库可筛选多个粉丝标签
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.authorLib_filter_by_fans_label(fans_labels=['旅行达人', '爱美少女', '带娃宝妈', '追星族', '二次元萌宅'])
        time.sleep(2)
        info = self.searchpage.get_author_label(num=10)
        self.assertEqual(len(info), 10)

    @minium.ddt_case('图文为主', '视频为主')
    def test_authorLib_filter_by_content_form(self, types):
        """
        测试企业版用户的博主库可筛选内容形式
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.authorLib_filter_by_content_form(types=types)
        time.sleep(2)
        info = self.searchpage.get_author_info(num=10)
        self.assertEqual(len(info), 10)

    @minium.ddt_case('0', '1-10', '11-50', '50+')
    def test_authorLib_filter_by_90_note(self, types):
        """
        测试企业版用户的博主库可筛选近90天爆文数
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.authorLib_filter_by_note(types=types, note_types='近90天爆文数')
        time.sleep(2)
        self.searchpage.scroll_filter_item(types='author')
        info = self.searchpage.get_author_info(num=10)
        self.assertEqual(len(info), 10)

    @minium.ddt_case('0', '1-10', '11-50', '50+')
    def test_authorLib_filter_by_business_note(self, types):
        """
        测试企业版用户的博主库可筛选近90天商业笔记数
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.authorLib_filter_by_note(types=types, note_types='近90天商业笔记数')
        self.searchpage.scroll_filter_item(types='author')
        time.sleep(2)
        info = self.searchpage.get_author_info(num=10)
        self.assertEqual(len(info), 10)

    def test_authorLib_filter_by_brand_cooperate(self):
        """
        测试企业版用户的博主库可筛选有品牌合作
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
        测试企业版用户的博主库可以筛选博主性别
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_author_filter(filter_types='博主信息', types='博主性别', value=gender)
        time.sleep(2)
        info = self.searchpage.get_author_info(num=10)
        self.assertEqual(len(info), 10)

    @minium.ddt_case('企业账号', '个人账号')
    def test_authorLib_filter_by_author_types(self, types):
        """
        测试企业版用户的博主库可以筛选博主属性
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_author_filter(filter_types='博主信息', types='博主属性', value=types)
        time.sleep(2)
        info = self.searchpage.get_author_info(num=10)
        self.assertEqual(len(info), 10)

    @minium.ddt_case(['福建省', '厦门市'], ['广东省', '汕头市'], ['四川省', '成都市'], ['上海市', '不限'], ['河北省', '廊坊市'])
    def test_authorLib_filter_by_author_area(self, area):
        """
        测试企业版用户的博主库可以筛选博主地区
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_author_filter(filter_types='博主信息', types='博主地区', value=area)
        time.sleep(2)
        info = self.searchpage.get_author_info(num=10)
        self.assertEqual(len(info), 10)

    @minium.ddt_case('金冠薯', '银冠薯', '泡泡薯')
    def test_authorLib_filter_by_author_level(self, level):
        """
        测试企业版用户的博主库可以筛选博主红薯等级
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_author_filter(filter_types='博主信息', types='红薯等级', value=level)
        time.sleep(2)
        info = self.searchpage.get_author_info(num=10)
        self.assertEqual(len(info), 10)

    @minium.ddt_case('5-1005', '0-1000', '1000-1W', '1W-10W', '10W-50W', '50W-100W', '100W+')
    def test_authorLib_filter_by_fans_level(self, level):
        """
        测试企业版用户的博主库可以筛选粉丝量级
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_author_filter(filter_types='粉丝信息', types='粉丝量级', value=level)
        time.sleep(2)
        try:
            info = self.searchpage.get_author_info(num=10)
            if level == '100W+':
                for i in range(len(info)):
                    self.CustomAssert.assertGreaterEqual(info[i][2], 1000000)
            else:
                level_list = level.split('-')
                for i in range(len(info)):
                    self.CustomAssert.assertGreaterEqual(info[i][2], Base.convert_to_float_with_unit(level_list[0]))
                    self.CustomAssert.assertLessEqual(info[i][2], Base.convert_to_float_with_unit(level_list[1]))
        finally:
            self.capture(name='result')

    @minium.ddt_case('男性居多', '女性居多')
    def test_authorLib_filter_by_fans_gender(self, gender):
        """
        测试企业版用户的博主库可以筛选粉丝性别
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_author_filter(filter_types='粉丝信息', types='粉丝性别', value=gender)
        time.sleep(2)
        info = self.searchpage.get_author_info(num=10)
        self.assertEqual(len(info), 10)

    @minium.ddt_case(['辽宁省', '丹东市'], ['天津市', '不限'], ['福建省', '泉州市'], ['山西省', '太原市'], ['江苏省', '苏州市'])
    def test_authorLib_filter_by_fans_area(self, area):
        """
        测试企业版用户的博主库可以筛选粉丝地区
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_author_filter(filter_types='粉丝信息', types='粉丝地区', value=area)
        time.sleep(2)
        info = self.searchpage.get_author_info(num=10)
        self.assertEqual(len(info), 10)

    @minium.ddt_case('0-17', '18-24', '25-34', '35-44', '44+')
    def test_authorLib_filter_by_fans_age(self, age):
        """
        测试企业版用户的博主库可以筛选粉丝年龄
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_author_filter(filter_types='粉丝信息', types='粉丝年龄', value=age)
        time.sleep(2)
        info = self.searchpage.get_author_info(num=10)
        self.assertEqual(len(info), 10)

    @minium.ddt_case('500-6000', '0-1W', '1W-5W', '5W-10W', '10W-30W', '30W-50W', '50W+')
    def test_authorLib_filter_by_liked(self, value):
        """
        测试企业版用户的博主库可以筛选赞藏总数
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_author_filter(filter_types='内容筛选', types='赞藏总数', value=value)
        time.sleep(2)

        try:
            info = self.searchpage.get_author_info(num=10)
            if value == '50W+':
                for i in range(len(info)):
                    self.CustomAssert.assertGreaterEqual(info[i][3], 500000)
            else:
                level_list = value.split('-')
                for i in range(len(info)):
                    self.CustomAssert.assertGreaterEqual(info[i][3], Base.convert_to_float_with_unit(level_list[0]))
                    self.CustomAssert.assertLessEqual(info[i][3], Base.convert_to_float_with_unit(level_list[1]))
        finally:
            self.capture(name='result')

    @minium.ddt_case('有MCN机构', '有联系方式', '有直播带货')
    def test_authorLib_filter_by_senior(self, types):
        """
        测试企业版用户的博主库可筛选高级筛选
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_author_filter(filter_types='高级筛选', types=types, value=None)
        time.sleep(2)
        info = self.searchpage.get_author_info(num=10)
        self.assertEqual(len(info), 10)

    @minium.ddt_case('800-8000', '0-1000', '1000-5000', '5000-1W', '1W-2W', '2W+')
    def test_authorLib_filter_by_price(self, value):
        """
        测试企业版用户的博主库可筛选报价区间
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_author_filter(filter_types='高级筛选', types='报价区间', value=value)
        time.sleep(2)
        info = self.searchpage.get_author_info(num=10)
        self.assertEqual(len(info), 10)
            
    @minium.ddt_case('互动量', '点赞数', '评论数', '收藏数')
    def test_noteLib_sort(self, sort_types):
        """
        测试企业版用户的笔记库可切换排序
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

    @minium.ddt_case('时尚', '体育赛事', '科技数码', '美妆', '出行')
    def test_noteLib_filter_by_first_label(self, label):
        """
        测试企业版用户的笔记库可筛选单个笔记一级标签
        """
        self.searchpage.select_tab(tab_name='笔记')
        self.searchpage.noteLib_filter_by_label(first_label=label, second_label='全部')
        time.sleep(2)
        info = self.searchpage.get_note_label(num=10)
        for i in range(len(info)):
            self.assertIn(label, info[i][2])

    @minium.ddt_case(('美妆', '香水'), ('宠物', '狗'), ('摄影', '摄影器材'), ('母婴', '育儿经验'), ('美食', '美食VLOG'))
    def test_noteLib_filter_by_second_label(self, labels):
        """
        测试企业版用户的笔记库可筛选单个笔记二级标签
        """
        first, second = labels
        self.searchpage.select_tab(tab_name='笔记')
        self.searchpage.noteLib_filter_by_label(first_label=first, second_label=second)
        time.sleep(2)
        info = self.searchpage.get_note_label(num=10)
        for i in range(len(info)):
            self.assertIn(first, info[i][2])

    @minium.ddt_case('图文笔记', '视频笔记')
    def test_noteLib_filter_by_note_types(self, types):
        """
        测试企业版用户的笔记库可筛选笔记类型
        """
        self.searchpage.select_tab(tab_name='笔记')
        self.searchpage.noteLib_filter_by_note_types(types=types)
        time.sleep(2)
        info = self.searchpage.get_note_label(num=10)
        self.assertEqual(len(info), 10)

    @minium.ddt_case('6小时', '12小时', '24小时', '近3天', '近7天', '近15天', '近30天', '近90天')
    def test_noteLib_filter_by_create_time(self, create_time):
        """
        测试企业版用户的笔记库可筛选笔记发布时间
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
        测试企业版用户的笔记库可筛选商业笔记/低粉爆文
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

    @minium.ddt_case('0-1000', '1000-5000', '5000-1W', '1W-3W', '3W-5W', '5W+')
    def test_noteLib_filter_by_interaction(self, interaction):
        """
        测试企业版用户的笔记库可筛选互动量
        """
        self.searchpage.select_tab(tab_name='笔记')
        self.searchpage.select_note_filter(filter_types='笔记筛选', types='互动量', value=interaction)
        time.sleep(2)
        try:
            info = self.searchpage.get_note_info(num=10)
            if interaction == '5W+':
                for i in range(len(info)):
                    self.assertGreaterEqual(info[i][4], 50000)
            else:
                inter_list = interaction.split('-')
                for i in range(len(info)):
                    self.assertGreaterEqual(info[i][4], Base.convert_to_float_with_unit(inter_list[0]))
                    self.assertLessEqual(info[i][4], Base.convert_to_float_with_unit(inter_list[1]))
        finally:
            self.capture('result')

    @minium.ddt_case('0-200', '200-500', '500-1000', '1000-5000', '5000-1W', '1W+')
    def test_noteLib_filter_by_liked(self, liked):
        """
        测试企业版用户的笔记库可筛选点赞数
        """
        self.searchpage.select_tab(tab_name='笔记')
        self.searchpage.select_note_filter(filter_types='笔记筛选', types='点赞数', value=liked)
        time.sleep(2)
        try:
            info = self.searchpage.get_note_info(num=10)
            if liked == '1W+':
                for i in range(len(info)):
                    self.assertGreaterEqual(info[i][5], 10000)
            else:
                liked_list = liked.split('-')
                for i in range(len(info)):
                    self.assertGreaterEqual(info[i][5], Base.convert_to_float_with_unit(liked_list[0]))
                    self.assertLessEqual(info[i][5], Base.convert_to_float_with_unit(liked_list[1]))
        finally:
            self.capture('result')

    @minium.ddt_case('男性居多', '女性居多')
    def test_noteLib_filter_by_fans_gender(self, gender):
        """
        测试企业版用户的笔记库可以筛选粉丝性别
        """
        self.searchpage.select_tab(tab_name='笔记')
        self.searchpage.select_note_filter(filter_types='粉丝信息', types='粉丝性别', value=gender)
        time.sleep(2)
        info = self.searchpage.get_note_info(num=10)
        self.assertEqual(len(info), 10)

    @minium.ddt_case(['辽宁省', '丹东市'], ['天津市', '不限'], ['福建省', '泉州市'], ['山西省', '太原市'], ['江苏省', '苏州市'])
    def test_noteLib_filter_by_fans_area(self, area):
        """
        测试企业版用户的笔记库可以筛选粉丝地区
        """
        self.searchpage.select_tab(tab_name='笔记')
        self.searchpage.select_note_filter(filter_types='粉丝信息', types='粉丝地区', value=area)
        time.sleep(2)
        info = self.searchpage.get_note_info(num=10)
        self.assertEqual(len(info), 10)

    def test_noteLib_filter_by_senior(self):
        """
        测试企业版用户的笔记库可筛选高级筛选-企业博主发文
        """
        self.searchpage.select_tab(tab_name='笔记')
        self.searchpage.select_note_filter(filter_types='高级筛选', types='企业博主发文', value=None)
        time.sleep(2)
        info = self.searchpage.get_note_info(num=10)
        self.assertEqual(len(info), 10)

    @minium.ddt_case('最近投放时间', '昨日互动增量', '总互动量', '总博主数', '总笔记数')
    def test_brandLib_sort(self, sort_types):
        """
        测试企业版用户的品牌库可切换排序
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
                self.CustomAssert.assertDatetimeBefore(info[i+1][value], info[i][value])
                self.capture('result')
            elif sort_types == '昨日互动增量':
                self.assertEqual(len(info), 10)
            else:
                self.assertLessEqual(info[i + 1][value], info[i][value])

    @minium.ddt_case('日用/宠物', '美食/饮食', '汽车/工具', '游戏', '互联网')
    def test_brandLib_filter_by_first_label(self, labels):
        """
        测试企业版用户的品牌库可筛选一级品牌标签
        """
        self.searchpage.select_tab(tab_name='品牌')
        self.searchpage.brandLib_filter_by_label(first_label=labels, second_label='全部')
        label = self.searchpage.get_brand_label(num=10)
        for i in range(len(label)):
            self.assertIsNotNone(label[i][2])

    @minium.ddt_case(('日用/宠物', '宠物'), ('美食/饮食', '乳品冲饮'), ('汽车/工具', '汽车'), ('游戏', '手游'), ('互联网', '电子商务'))
    def test_brandLib_filter_by_second_label(self, labels):
        """
        测试企业版用户的品牌库可筛选二级品牌标签
        """
        first_label, second_label = labels
        self.searchpage.select_tab(tab_name='品牌')
        self.searchpage.brandLib_filter_by_label(first_label=first_label, second_label=second_label)
        label = self.searchpage.get_brand_label(num=10)
        for i in range(len(label)):
            self.assertIn(second_label, label[i][2])

    def test_brandLib_filter_by_business(self):
        """
        测试企业版用户的品牌库可筛选有商业投放
        """
        self.searchpage.select_tab(tab_name='品牌')
        self.searchpage.brandLib_filter_by_business()
        info = self.searchpage.get_brand_info(num=10)
        self.assertEqual(len(info), 10)

    @minium.ddt_case('美妆/装扮', '科技/厨电', '日用/宠物', '美食/饮食', '教育/母婴')
    def test_brandLib_filter_by_other_labels(self, types):
        """
        测试企业版用户的品牌库可筛选标签按钮
        """
        self.searchpage.select_tab(tab_name='品牌')
        self.searchpage.brandLib_filter_by_other_labels(types=types)
        if types == '美妆/装扮' or types == '科技/厨电':
            pass
        else:
            self.searchpage.scroll_filter_item(types='brand')
        label = self.searchpage.get_brand_label(num=10)
        for i in range(len(label)):
            self.assertIsNotNone(label[i][2])

    @minium.ddt_case('0-1000', '1000-5000', '5000-1W', '1W-3W', '3W-5W', '5W+')
    def test_brandLib_filter_by_interaction(self, interaction):
        """
        测试企业版用户的品牌库可筛选总互动量
        """
        self.searchpage.select_tab(tab_name='品牌')
        self.searchpage.select_brand_filter(filter_types='品牌筛选', types='总互动量', value=interaction)
        time.sleep(2)
        try:
            info = self.searchpage.get_brand_info(num=10)
            if interaction == '5W+':
                for i in range(len(info)):
                    self.assertGreaterEqual(info[i][3], 50000)
            else:
                interaction_list = interaction.split('-')
                for i in range(len(info)):
                    self.assertGreaterEqual(info[i][3], Base.convert_to_float_with_unit(interaction_list[0]))
                    self.assertLessEqual(info[i][3], Base.convert_to_float_with_unit(interaction_list[1]))
        finally:
            self.capture('result')

    @minium.ddt_case('1-10', '10-30', '30-50', '50-100', '100+')
    def test_brandLib_filter_by_author_num(self, author_num):
        """
        测试企业版用户的品牌库可筛选种草博主数
        """
        self.searchpage.select_tab(tab_name='品牌')
        self.searchpage.select_brand_filter(filter_types='品牌筛选', types='种草博主数', value=author_num)
        time.sleep(2)
        try:
            info = self.searchpage.get_brand_info(num=10)
            if author_num == '100+':
                for i in range(len(info)):
                    self.assertGreaterEqual(info[i][4], 100)
            else:
                author_num_list = author_num.split('-')
                for i in range(len(info)):
                    self.assertGreaterEqual(info[i][4], float(author_num_list[0]))
                    self.assertLessEqual(info[i][4], float(author_num_list[1]))
        finally:
            self.capture('result')

    @minium.ddt_case('1-10', '10-30', '30-50', '50-100', '100+')
    def test_brandLib_filter_by_note_num(self, note_num):
        """
        测试企业版用户的品牌库可筛选总笔记数
        """
        self.searchpage.select_tab(tab_name='品牌')
        self.searchpage.select_brand_filter(filter_types='品牌筛选', types='总笔记数', value=note_num)
        time.sleep(2)
        try:
            info = self.searchpage.get_brand_info(num=10)
            if note_num == '100+':
                for i in range(len(info)):
                    self.assertGreaterEqual(info[i][5], 100)
            else:
                note_num_list = note_num.split('-')
                for i in range(len(info)):
                    self.assertGreaterEqual(info[i][5], float(note_num_list[0]))
                    self.assertLessEqual(info[i][5], float(note_num_list[1]))
        finally:
            self.capture('result')

    @minium.ddt_case('男性居多', '女性居多')
    def test_brandLib_filter_by_fans_gender(self, gender):
        """
        测试企业版用户的品牌库可筛选粉丝性别
        """
        self.searchpage.select_tab(tab_name='品牌')
        self.searchpage.select_brand_filter(filter_types='粉丝信息', types='粉丝性别', value=gender)
        time.sleep(2)
        info = self.searchpage.get_brand_info(num=10)
        self.assertEqual(len(info), 10)

    @minium.ddt_case(['广东省', '广州市'], ['天津市', '不限'], ['福建省', '泉州市'], ['山西省', '太原市'], ['江苏省', '苏州市'])
    def test_brandLib_filter_by_fans_area(self, area):
        """
        测试企业版用户的品牌库可筛选粉丝地区
        """
        self.searchpage.select_tab(tab_name='品牌')
        self.searchpage.select_brand_filter(filter_types='粉丝信息', types='粉丝地区', value=area)
        time.sleep(2)
        info = self.searchpage.get_brand_info(num=10)
        self.assertEqual(len(info), 10)

    @minium.ddt_case('笔记最多', '互动量最多')
    def test_kindLib_sort(self, sort_types):
        """
        测试企业版用户的品类库可筛选排序
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
        测试企业版用户的品类库可筛选时间
        """
        self.searchpage.select_tab(tab_name='品类')
        self.searchpage.kindLib_filter_by_times(times=times)
        time.sleep(2)
        info = self.searchpage.get_kind_info(num=10)
        self.assertEqual(len(info), 10)

    @minium.ddt_case('日用/宠物', '美食/饮食', '汽车/工具', '运动/娱乐', '美妆/装扮')
    def test_kindLib_filter_by_first_label(self, labels):
        """
        测试企业版用户的品类库可筛选一级标签
        """
        self.searchpage.select_tab(tab_name='品类')
        self.searchpage.kindLib_filter_by_label(first_label=labels, second_label='全部')
        time.sleep(2)
        label = self.searchpage.get_kind_label(num=10)
        for i in range(len(label)):
            self.assertIn(labels, label[i][2])

    @minium.ddt_case(('日用/宠物', '宠物'), ('美食/饮食', '乳品冲饮'), ('汽车/工具', '汽车'), ('运动/娱乐', '书刊/阅读'), ('美妆/装扮', '香水彩妆'))
    def test_kindLib_filter_by_second_label(self, labels):
        """
        测试企业版用户的品类库可筛选二级品类标签
        """
        first_label, second_label = labels
        self.searchpage.select_tab(tab_name='品类')
        self.searchpage.kindLib_filter_by_label(first_label=first_label, second_label=second_label)
        label = self.searchpage.get_kind_label(num=10)
        for i in range(len(label)):
            self.assertIn(second_label, label[i][2])

    @minium.ddt_case('美妆/装扮', '科技/厨电', '日用/宠物', '美食/饮食', '教育/母婴')
    def test_kindLib_filter_by_other_labels(self, labels):
        """
        测试企业版用户的品类库可筛选标签按钮
        """
        self.searchpage.select_tab(tab_name='品类')
        self.searchpage.kindLib_filter_by_other_labels(types=labels)
        if labels == '美妆/装扮' or labels == '科技/厨电':
            pass
        else:
            self.searchpage.scroll_filter_item(types='kind')
        label = self.searchpage.get_kind_label(num=10)
        for i in range(len(label)):
            self.assertIn(labels, label[i][2])

    def test_hotWordLib_sort(self):
        """
        测试企业版用户的热搜词库可筛选排序
        """
        self.searchpage.select_tab(tab_name='热搜词')
        self.searchpage.select_sort(types='热搜词', sort_types='热度值排序')
        time.sleep(2)
        info = self.searchpage.get_hot_word_info(num=10)
        for i in range(len(info) - 1):
            self.assertLessEqual(info[i + 1][4], info[i][4])

    @minium.ddt_case('时尚', '体育赛事', '科技数码', '美妆', '出行')
    def test_hotWordLib_filter_by_first_label(self, label):
        """
        测试企业版用户的热搜词库可筛选单个一级标签
        """
        self.searchpage.select_tab(tab_name='热搜词')
        self.searchpage.hotWordLib_filter_by_label(first_label=label, second_label='全部')
        time.sleep(2)
        info = self.searchpage.get_hot_word_info(num=10)
        self.assertEqual(len(info), 10)

    @minium.ddt_case(('美妆', '香水'), ('宠物', '狗'), ('摄影', '摄影器材'), ('母婴', '育儿经验'), ('美食', '美食VLOG'))
    def test_hotWordLib_filter_by_second_label(self, labels):
        """
        测试企业版用户的热搜词库可筛选单个二级标签
        """
        first, second = labels
        self.searchpage.select_tab(tab_name='热搜词')
        self.searchpage.hotWordLib_filter_by_label(first_label=first, second_label=second)
        time.sleep(2)
        info = self.searchpage.get_hot_word_info(num=10)
        self.assertEqual(len(info), 10)

    @minium.ddt_case('摄影', '减肥', '运动健身', '美妆')
    def test_hotWordLib_filter_by_other_label(self, label):
        """
        测试企业版用户的热搜词库可筛选标签按钮
        """
        self.searchpage.select_tab(tab_name='热搜词')
        self.searchpage.hotWordLib_filter_by_other_labels(types=label)
        time.sleep(2)
        info = self.searchpage.get_hot_word_info(num=10)
        self.assertEqual(len(info), 10)


