#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/9/22
# @Author : chenxuehong
# @Version：V 0.1
# @File : test_search.py
# @desc : 普通用户-搜索页面测试用例

import time
import minium
from common.base import Base
from testcase.vip_1.BaseCase import BaseCase
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

    def test_authorLib(self):
        """
        测试普通用户的博主库无法查看
        """
        self.searchpage.select_tab(tab_name='博主')
        status = self.searchpage.is_vip_have_authority(tab_name='blogger')
        self.assertTrue(status)

    @minium.ddt_case('粉丝数最多', '涨粉数最多', '赞藏最多')
    def test_authorLib_sort(self, sort_types):
        """
        测试普通用户的博主库无法切换排序
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_sort(types='博主', sort_types=sort_types)
        status = self.searchpage.is_vip_have_authority(tab_name='blogger')
        self.assertTrue(status)

    def test_authorLib_filter_by_one_first_label(self):
        """
        测试普通用户的博主库无法筛选单个博主一级标签
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.authorLib_filter_by_label(first_label='时尚', second_label='全部')
        status = self.searchpage.is_vip_have_authority(tab_name='blogger')
        self.assertTrue(status)

    def test_authorLib_filter_by_one_second_label(self):
        """
        测试普通用户的博主库无法筛选单个博主二级标签
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.authorLib_filter_by_label(first_label='美妆', second_label='香水')
        status = self.searchpage.is_vip_have_authority(tab_name='blogger')
        self.assertTrue(status)

    def test_authorLib_filter_by_multi_first_label(self):
        """
        测试普通用户的博主库无法筛选多个博主一级标签
        """
        self.searchpage.select_tab(tab_name='博主')
        first_label = ['游戏', '运动健身']
        self.searchpage.authorLib_filter_by_mult_first_author_label(first_label=first_label)
        status = self.searchpage.is_vip_have_authority(tab_name='blogger')
        self.assertTrue(status)

    def test_authorLib_filter_by_multi_second_label(self):
        """
        测试普通用户的博主库无法筛选多个博主二级标签
        """
        self.searchpage.select_tab(tab_name='博主')
        labels = [['时尚', ['发型', '鞋靴']], ['美妆', ['美甲', '香水']]]
        self.searchpage.authorLib_filter_by_mult_second_author_label(labels=labels)
        status = self.searchpage.is_vip_have_authority(tab_name='blogger')
        self.assertTrue(status)

    def test_authorLib_filter_by_one_fans_label(self):
        """
        测试普通用户的博主库无法筛选单个粉丝标签
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.authorLib_filter_by_fans_label(fans_labels='旅行达人')
        status = self.searchpage.is_vip_have_authority(tab_name='blogger')
        self.assertTrue(status)

    def test_authorLib_filter_by_multi_fans_label(self):
        """
        测试普通用户的博主库无法筛选多个粉丝标签
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.authorLib_filter_by_fans_label(
            fans_labels=['旅行达人', '爱美少女', '带娃宝妈', '追星族', '二次元萌宅'])
        status = self.searchpage.is_vip_have_authority(tab_name='blogger')
        self.assertTrue(status)

    @minium.ddt_case('图文为主', '视频为主')
    def test_authorLib_filter_by_content_form(self, types):
        """
        测试普通用户的博主库无法筛选内容形式
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.authorLib_filter_by_content_form(types=types)
        status = self.searchpage.is_vip_have_authority(tab_name='blogger')
        self.assertTrue(status)

    def test_authorLib_filter_by_90_note(self):
        """
        测试普通用户的博主库无法筛选近90天爆文数
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.authorLib_filter_by_note(types='1-10', note_types='近90天爆文数')
        status = self.searchpage.is_vip_have_authority(tab_name='blogger')
        self.assertTrue(status)

    def test_authorLib_filter_by_business_note(self):
        """
        测试普通用户的博主库无法筛选近90天商业笔记数
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.authorLib_filter_by_note(types='11-50', note_types='近90天商业笔记数')
        self.searchpage.scroll_filter_item(types='author')
        status = self.searchpage.is_vip_have_authority(tab_name='blogger')
        self.assertTrue(status)

    def test_authorLib_filter_by_brand_cooperate(self):
        """
        测试普通用户的博主库无法筛选有品牌合作
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.authorLib_filter_by_brand_cooperate()
        self.searchpage.scroll_filter_item(types='author')
        status = self.searchpage.is_vip_have_authority(tab_name='blogger')
        self.assertTrue(status)

    @minium.ddt_case('男', '女')
    def test_authorLib_filter_by_author_gender(self, gender):
        """
        测试普通用户的博主库无法筛选博主性别
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_author_filter(filter_types='博主信息', types='博主性别', value=gender)
        status = self.searchpage.is_vip_have_authority(tab_name='blogger')
        self.assertTrue(status)

    @minium.ddt_case('企业账号', '个人账号')
    def test_authorLib_filter_by_author_types(self, types):
        """
        测试普通用户的博主库无法筛选博主属性
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_author_filter(filter_types='博主信息', types='博主属性', value=types)
        status = self.searchpage.is_vip_have_authority(tab_name='blogger')
        self.assertTrue(status)

    def test_authorLib_filter_by_author_area(self):
        """
        测试普通用户的博主库无法筛选博主地区
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_author_filter(filter_types='博主信息', types='博主地区', value=['福建省', '厦门市'])
        status = self.searchpage.is_vip_have_authority(tab_name='blogger')
        self.assertTrue(status)

    def test_authorLib_filter_by_author_level(self):
        """
        测试普通用户的博主库无法筛选博主红薯等级
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_author_filter(filter_types='博主信息', types='红薯等级', value='银冠薯')
        status = self.searchpage.is_vip_have_authority(tab_name='blogger')
        self.assertTrue(status)

    def test_authorLib_filter_by_fans_level(self):
        """
        测试普通用户的博主库无法筛选粉丝量级
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_author_filter(filter_types='粉丝信息', types='粉丝量级', value='1W-10W')
        status = self.searchpage.is_vip_have_authority(tab_name='blogger')
        self.assertTrue(status)

    @minium.ddt_case('男性居多', '女性居多')
    def test_authorLib_filter_by_fans_gender(self, gender):
        """
        测试普通用户的博主库无法筛选粉丝性别
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_author_filter(filter_types='粉丝信息', types='粉丝性别', value=gender)
        status = self.searchpage.is_vip_have_authority(tab_name='blogger')
        self.assertTrue(status)

    def test_authorLib_filter_by_fans_area(self):
        """
        测试普通用户的博主库无法选粉丝地区
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_author_filter(filter_types='粉丝信息', types='粉丝地区', value=['辽宁省', '丹东市'])
        status = self.searchpage.is_vip_have_authority(tab_name='blogger')
        self.assertTrue(status)

    def test_authorLib_filter_by_fans_age(self):
        """
        测试普通用户的博主库无法筛选粉丝年龄
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_author_filter(filter_types='粉丝信息', types='粉丝年龄', value='18-24')
        status = self.searchpage.is_vip_have_authority(tab_name='blogger')
        self.assertTrue(status)

    def test_authorLib_filter_by_liked(self):
        """
        测试普通用户的博主库无法筛选赞藏总数
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_author_filter(filter_types='内容筛选', types='赞藏总数', value='10W-30W')
        status = self.searchpage.is_vip_have_authority(tab_name='blogger')
        self.assertTrue(status)

    @minium.ddt_case('有MCN机构', '有联系方式', '有直播带货')
    def test_authorLib_filter_by_senior(self, types):
        """
        测试普通用户的博主库无法筛选高级筛选
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_author_filter(filter_types='高级筛选', types=types, value=None)
        status = self.searchpage.is_vip_have_authority(tab_name='blogger')
        self.assertTrue(status)

    def test_authorLib_filter_by_price(self):
        """
        测试普通用户的博主库无法筛选报价区间
        """
        self.searchpage.select_tab(tab_name='博主')
        self.searchpage.select_author_filter(filter_types='高级筛选', types='报价区间', value='1000-5000')
        status = self.searchpage.is_vip_have_authority(tab_name='blogger')
        self.assertTrue(status)

    def test_noteLib(self):
        """
        测试普通用户可查看笔记库前50条数据
        """
        self.searchpage.select_tab(tab_name='笔记')
        status = self.searchpage.is_vip_have_authority(tab_name='note')
        self.assertFalse(status)
        self.searchpage.check_scroll(page=5)
        status = self.searchpage.is_vip_have_authority(tab_name='note', ids='52')
        self.assertTrue(status)

    @minium.ddt_case('互动量', '点赞数', '评论数', '收藏数')
    def test_noteLib_sort(self, sort_types):
        """
        测试普通用户的笔记库可以切换排序
        """
        self.searchpage.select_tab(tab_name='笔记')
        self.searchpage.select_sort(types='笔记', sort_types=sort_types)
        status = self.searchpage.is_vip_have_authority(tab_name='note')
        self.assertFalse(status)

    def test_noteLib_filter_by_first_label(self):
        """
        测试普通用户的笔记库无法筛选单个笔记一级标签
        """
        self.searchpage.select_tab(tab_name='笔记')
        self.searchpage.noteLib_filter_by_label(first_label='时尚', second_label='全部')
        status = self.searchpage.is_vip_have_authority(tab_name='note')
        self.assertTrue(status)

    def test_noteLib_filter_by_second_label(self):
        """
        测试普通用户的笔记库无法筛选单个笔记二级标签
        """
        self.searchpage.select_tab(tab_name='笔记')
        self.searchpage.noteLib_filter_by_label(first_label='美妆', second_label='香水')
        status = self.searchpage.is_vip_have_authority(tab_name='note')
        self.assertTrue(status)

    @minium.ddt_case('图文笔记', '视频笔记')
    def test_noteLib_filter_by_note_types(self, types):
        """
        测试普通用户的笔记库无法筛选笔记类型
        """
        self.searchpage.select_tab(tab_name='笔记')
        self.searchpage.noteLib_filter_by_note_types(types=types)
        status = self.searchpage.is_vip_have_authority(tab_name='note')
        self.assertTrue(status)

    @minium.ddt_case('6小时', '12小时', '24小时', '近3天', '近7天', '近15天', '近30天', '近90天')
    def test_noteLib_filter_by_create_time(self, create_time):
        """
        测试普通用户的笔记库无法筛选笔记发布时间
        """
        self.searchpage.select_tab(tab_name='笔记')
        self.searchpage.noteLib_filter_by_create_time(create_time=create_time)
        status = self.searchpage.is_vip_have_authority(tab_name='note')
        if create_time == '近30天':
            self.assertFalse(status)
        else:
            self.assertTrue(status)

    @minium.ddt_case('商业笔记', '低粉爆文')
    def test_noteLib_filter_by_note_btn(self, types):
        """
        测试普通用户的笔记库无法筛选商业笔记/低粉爆文
        """
        self.searchpage.select_tab(tab_name='笔记')
        self.searchpage.noteLib_filter_by_types(types=types)
        self.searchpage.scroll_filter_item(types='note')
        status = self.searchpage.is_vip_have_authority(tab_name='note')
        self.assertTrue(status)

    def test_noteLib_filter_by_interaction(self):
        """
        测试普通用户的笔记库无法筛选互动量
        """
        self.searchpage.select_tab(tab_name='笔记')
        self.searchpage.select_note_filter(filter_types='笔记筛选', types='互动量', value='5000-1W')
        status = self.searchpage.is_vip_have_authority(tab_name='note')
        self.assertTrue(status)

    def test_noteLib_filter_by_liked(self):
        """
        测试普通用户的笔记库无法筛选点赞数
        """
        self.searchpage.select_tab(tab_name='笔记')
        self.searchpage.select_note_filter(filter_types='笔记筛选', types='点赞数', value='200-500')
        status = self.searchpage.is_vip_have_authority(tab_name='note')
        self.assertTrue(status)

    @minium.ddt_case('男性居多', '女性居多')
    def test_noteLib_filter_by_fans_gender(self, gender):
        """
        测试普通用户的笔记库无法筛选粉丝性别
        """
        self.searchpage.select_tab(tab_name='笔记')
        self.searchpage.select_note_filter(filter_types='粉丝信息', types='粉丝性别', value=gender)
        status = self.searchpage.is_vip_have_authority(tab_name='note')
        self.assertTrue(status)

    def test_noteLib_filter_by_fans_area(self):
        """
        测试普通用户的笔记库无法筛选粉丝地区
        """
        self.searchpage.select_tab(tab_name='笔记')
        self.searchpage.select_note_filter(filter_types='粉丝信息', types='粉丝地区', value=['福建省', '泉州市'])
        status = self.searchpage.is_vip_have_authority(tab_name='note')
        self.assertTrue(status)

    def test_noteLib_filter_by_senior(self):
        """
        测试普通用户的笔记库无法筛选高级筛选-企业博主发文
        """
        self.searchpage.select_tab(tab_name='笔记')
        self.searchpage.select_note_filter(filter_types='高级筛选', types='企业博主发文', value=None)
        status = self.searchpage.is_vip_have_authority(tab_name='note')
        self.assertTrue(status)

    def test_brandLib(self):
        """
        测试普通用户的品牌库可查看前10条
        """
        self.searchpage.select_tab(tab_name='品牌')
        status = self.searchpage.is_vip_have_authority(tab_name='brand')
        self.assertFalse(status)
        self.searchpage.check_scroll(page=1)
        status = self.searchpage.is_vip_have_authority(tab_name='brand', ids='12')
        self.assertTrue(status)

    @minium.ddt_case('最近投放时间', '昨日互动增量', '总互动量', '总博主数', '总笔记数')
    def test_brandLib_sort(self, sort_types):
        """
        测试普通用户的品牌库无法切换排序
        """
        self.searchpage.select_tab(tab_name='品牌')
        self.searchpage.select_sort(types='品牌', sort_types=sort_types)
        status = self.searchpage.is_vip_have_authority(tab_name='brand')
        if sort_types == '最近投放时间':
            self.assertFalse(status)
        else:
            self.assertTrue(status)

    def test_brandLib_filter_by_first_label(self):
        """
        测试普通用户的品牌库无法筛选一级品牌标签
        """
        self.searchpage.select_tab(tab_name='品牌')
        self.searchpage.brandLib_filter_by_label(first_label='日用/宠物', second_label='全部')
        status = self.searchpage.is_vip_have_authority(tab_name='brand')
        self.assertTrue(status)

    def test_brandLib_filter_by_second_label(self):
        """
        测试普通用户的品牌库无法筛选二级品牌标签
        """
        self.searchpage.select_tab(tab_name='品牌')
        self.searchpage.brandLib_filter_by_label(first_label='汽车/工具', second_label='汽车')
        status = self.searchpage.is_vip_have_authority(tab_name='brand')
        self.assertTrue(status)

    def test_brandLib_filter_by_business(self):
        """
        测试普通用户的品牌库无法筛选有商业投放
        """
        self.searchpage.select_tab(tab_name='品牌')
        self.searchpage.brandLib_filter_by_business()
        status = self.searchpage.is_vip_have_authority(tab_name='brand')
        self.assertTrue(status)

    def test_brandLib_filter_by_other_labels(self):
        """
        测试普通用户的品牌库无法筛选标签按钮
        """
        self.searchpage.select_tab(tab_name='品牌')
        self.searchpage.brandLib_filter_by_other_labels(types='科技/厨电')
        status = self.searchpage.is_vip_have_authority(tab_name='brand')
        self.assertTrue(status)

    def test_brandLib_filter_by_interaction(self):
        """
        测试普通用户的品牌库无法筛选总互动量
        """
        self.searchpage.select_tab(tab_name='品牌')
        self.searchpage.select_brand_filter(filter_types='品牌筛选', types='总互动量', value='1W-3W')
        status = self.searchpage.is_vip_have_authority(tab_name='brand')
        self.assertTrue(status)

    def test_brandLib_filter_by_author_num(self):
        """
        测试普通用户的品牌库无法筛选种草博主数
        """
        self.searchpage.select_tab(tab_name='品牌')
        self.searchpage.select_brand_filter(filter_types='品牌筛选', types='种草博主数', value='30-50')
        status = self.searchpage.is_vip_have_authority(tab_name='brand')
        self.assertTrue(status)

    def test_brandLib_filter_by_note_num(self):
        """
        测试普通用户的品牌库无法筛选总笔记数
        """
        self.searchpage.select_tab(tab_name='品牌')
        self.searchpage.select_brand_filter(filter_types='品牌筛选', types='总笔记数', value='10-30')
        status = self.searchpage.is_vip_have_authority(tab_name='brand')
        self.assertTrue(status)

    @minium.ddt_case('男性居多', '女性居多')
    def test_brandLib_filter_by_fans_gender(self, gender):
        """
        测试普通用户的品牌库无法筛选粉丝性别
        """
        self.searchpage.select_tab(tab_name='品牌')
        self.searchpage.select_brand_filter(filter_types='粉丝信息', types='粉丝性别', value=gender)
        status = self.searchpage.is_vip_have_authority(tab_name='brand')
        self.assertTrue(status)

    def test_brandLib_filter_by_fans_area(self):
        """
        测试普通用户的品牌库无法筛选粉丝地区
        """
        self.searchpage.select_tab(tab_name='品牌')
        self.searchpage.select_brand_filter(filter_types='粉丝信息', types='粉丝地区', value=['山西省', '太原市'])
        status = self.searchpage.is_vip_have_authority(tab_name='brand')
        self.assertTrue(status)

    def test_kindLib(self):
        """
        测试普通用户的品类库可查看前10条
        """
        self.searchpage.select_tab(tab_name='品类')
        status = self.searchpage.is_vip_have_authority(tab_name='category')
        self.assertFalse(status)
        self.searchpage.check_scroll(page=1)
        status = self.searchpage.is_vip_have_authority(tab_name='category', ids='12')
        self.assertTrue(status)

    @minium.ddt_case('笔记最多', '互动量最多')
    def test_kindLib_sort(self, sort_types):
        """
        测试普通用户的品类库无法筛选排序
        """
        self.searchpage.select_tab(tab_name='品类')
        self.searchpage.select_sort(types='品类', sort_types=sort_types)
        if sort_types == '笔记最多':
            status = self.searchpage.is_vip_have_authority(tab_name='category', ids='12')
            self.assertTrue(status)
        else:
            status = self.searchpage.is_vip_have_authority(tab_name='category')
            self.assertTrue(status)

    @minium.ddt_case('近7天', '近15天', '近30天')
    def test_kindLib_filter_by_times(self, times):
        """
        测试普通用户的品类库可筛选30天以内的数据
        """
        self.searchpage.select_tab(tab_name='品类')
        self.searchpage.kindLib_filter_by_times(times=times)
        self.searchpage.check_scroll(page=1)
        status = self.searchpage.is_vip_have_authority(tab_name='category', ids='12')
        self.assertTrue(status)

    @minium.ddt_case('近90天', '近180天', '近360天')
    def test_kindLib_filter_by_times2(self, times):
        """
        测试普通用户的品类库无法筛选超过30天的数据
        """
        self.searchpage.select_tab(tab_name='品类')
        self.searchpage.kindLib_filter_by_times(times=times)
        status = self.searchpage.is_vip_have_authority(tab_name='category')
        self.assertTrue(status)

    def test_kindLib_filter_by_first_label(self):
        """
        测试普通用户的品类库无法筛选一级标签
        """
        self.searchpage.select_tab(tab_name='品类')
        self.searchpage.kindLib_filter_by_label(first_label='美食/饮食', second_label='全部')
        status = self.searchpage.is_vip_have_authority(tab_name='category')
        self.assertTrue(status)

    def test_kindLib_filter_by_second_label(self):
        """
        测试普通用户的品类库无法筛选二级品类标签
        """
        self.searchpage.select_tab(tab_name='品类')
        self.searchpage.kindLib_filter_by_label(first_label='美妆/装扮', second_label='香水彩妆')
        status = self.searchpage.is_vip_have_authority(tab_name='category')
        self.assertTrue(status)

    def test_kindLib_filter_by_other_labels(self):
        """
        测试普通用户的品类库无法筛选标签按钮
        """
        self.searchpage.select_tab(tab_name='品类')
        self.searchpage.kindLib_filter_by_other_labels(types='科技/厨电')
        status = self.searchpage.is_vip_have_authority(tab_name='category')
        self.assertTrue(status)

    def test_hotWordLib(self):
        """
        测试普通用户的热搜词库可查看前50条
        """
        self.searchpage.select_tab(tab_name='热搜词')
        status = self.searchpage.is_vip_have_authority(tab_name='hot-word')
        self.assertFalse(status)
        self.searchpage.check_scroll(page=5)
        status = self.searchpage.is_vip_have_authority(tab_name='hot-word', ids='3')
        self.assertTrue(status)

    def test_hotWordLib_filter_by_first_label(self):
        """
        测试普通用户的热搜词库无法筛选单个一级标签
        """
        self.searchpage.select_tab(tab_name='热搜词')
        self.searchpage.hotWordLib_filter_by_label(first_label='体育赛事', second_label='全部')
        status = self.searchpage.is_vip_have_authority(tab_name='hot-word')
        self.assertTrue(status)

    def test_hotWordLib_filter_by_second_label(self):
        """
        测试普通用户的热搜词库无法筛选单个二级标签
        """
        self.searchpage.select_tab(tab_name='热搜词')
        self.searchpage.hotWordLib_filter_by_label(first_label='美妆', second_label='香水')
        status = self.searchpage.is_vip_have_authority(tab_name='hot-word')
        self.assertTrue(status)

    @minium.ddt_case('摄影', '减肥', '运动健身', '美妆')
    def test_hotWordLib_filter_by_other_label(self, label):
        """
        测试普通用户的热搜词库无法筛选标签按钮
        """
        self.searchpage.select_tab(tab_name='热搜词')
        self.searchpage.hotWordLib_filter_by_other_labels(types=label)
        status = self.searchpage.is_vip_have_authority(tab_name='hot-word')
        self.assertTrue(status)


