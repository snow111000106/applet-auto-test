#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/7/5
# @Author : chenxuehong
# @Version：V 0.1
# @File : test_vip_page.py
# @desc : 企业版-vip页面测试用例

import minium, time
from conf import config, route
from minium import Callback
from testcase.vip_6.BaseCase import BaseCase
from page.VipPage import VipPage
from common.base import Base


@minium.skipUnless(condition=config.platform != "ios", reason="仅ios无vip页面")
@minium.ddt_class
class VipPageTest(BaseCase):

    vippage = None

    def __init__(self, methodName='runTest'):
        super(VipPageTest, self).__init__(methodName)
        self.vippage = VipPage(self)

    @classmethod
    def setUpClass(cls):
        super(VipPageTest, cls).setUpClass()
        cls.vippage = VipPage(cls)
        cls.vippage.into_vip_center()

    def test_user_info(self):
        """
        测试用户信息正确
        """
        name, vip_name, vip_time = self.vippage.get_user_info()
        self.assertEqual(vip_name, Base.get_vip_info(6)['vip_name'])
        self.assertEqual(vip_time, Base.get_vip_info(6)['vip_time'])
        self.assertEqual(name, Base.get_vip_info(6)['mobile'])

    @minium.ddt_case((1, '12个月', '28999', '51588', '22589', True), (2, '3个月', '11999', '12897', '898', True),
                     (3, '1个月', '4299', '4299', None, False), (4, '24个月', '43999', '103176', '59177', True))
    def test_vip6_price(self, value):
        """
        测试企业版vip版本价格
        """
        self.vippage.switch_vip_tab(tab_name='企业版')
        time.sleep(2)
        card_id, re_pre, re_price, re_original_price, re_discount_amount, is_discount = value
        pre, price, original_price, discount_amount = self.vippage.get_vip_price_info(card_id=card_id, is_discount=is_discount)
        self.assertEqual(pre, re_pre)
        self.assertEqual(price, re_price)
        self.assertEqual(original_price, re_original_price)
        self.assertEqual(discount_amount, re_discount_amount)

    @minium.ddt_case((1, '12个月', '1999', '2396', '397', True), (2, '3个月', '599', '599', '0', True),
                     (3, '24个月', '3299', '4792', '1493', True))
    def test_vip5_price(self, value):
        """
        测试个人版vip版本价格
        """
        self.vippage.switch_vip_tab(tab_name='个人版')
        time.sleep(2)
        card_id, re_pre, re_price, re_original_price, re_discount_amount, is_discount = value
        pre, price, original_price, discount_amount = self.vippage.get_vip_price_info(card_id=card_id,is_discount=is_discount)
        self.assertEqual(pre, re_pre)
        self.assertEqual(price, re_price)
        self.assertEqual(original_price, re_original_price)
        self.assertEqual(discount_amount, re_discount_amount)

    @minium.ddt_case((1, '12个月', '16999', '26388', '9389', True), (2, '3个月', '5699', '6597', '898', True),
                     (3, '1个月', '2199', '2199', None, False), (4, '24个月', '27999', '52776', '24777', True))
    def test_vip4_price(self, value):
        """
        测试专业版vip版本价格
        """
        self.vippage.switch_vip_tab(tab_name='专业版')
        time.sleep(3)
        card_id, re_pre, re_price, re_original_price, re_discount_amount, is_discount = value
        pre, price, original_price, discount_amount = self.vippage.get_vip_price_info(card_id=card_id, is_discount=is_discount)
        self.assertEqual(pre, re_pre)
        self.assertEqual(price, re_price)
        self.assertEqual(original_price, re_original_price)
        self.assertEqual(discount_amount, re_discount_amount)

    @minium.ddt_case((1, '12个月', '5.6折优惠'), (2, '3个月', '9.3折优惠'), (4, '24个月', '4.3折优惠'))
    def test_vip6_tag(self, value):
        """
        测试企业版标签信息
        """
        card_id, re_pre, re_tag = value
        self.vippage.switch_vip_tab(tab_name='企业版')
        time.sleep(3)
        pre, tag = self.vippage.get_vip_tag_info(card_id=card_id)
        self.assertEqual(pre, re_pre)
        self.assertEqual(tag, re_tag)

    @minium.ddt_case((1, '12个月', '6.4折优惠'), (2, '3个月', '8.6折优惠'), (4, '24个月', '5.3折优惠'))
    def test_vip4_tag(self, value):
        """
        测试专业版标签信息
        """
        card_id, re_pre, re_tag = value
        self.vippage.switch_vip_tab(tab_name='专业版')
        time.sleep(3)
        pre, tag = self.vippage.get_vip_tag_info(card_id=card_id)
        self.assertEqual(pre, re_pre)
        self.assertEqual(tag, re_tag)

    @minium.ddt_case((1, '12个月', '8.3折优惠'), (3, '24个月', '6.9折优惠'))
    def test_vip5_tag(self, value):
        """
        测试个人版标签信息
        """
        card_id, re_pre, re_tag = value
        self.vippage.switch_vip_tab(tab_name='个人版')
        time.sleep(3)
        pre, tag = self.vippage.get_vip_tag_info(card_id=card_id)
        self.assertEqual(pre, re_pre)
        self.assertEqual(tag, re_tag)

    @minium.ddt_case(('agreement', route.agreement_page), ('vip_detail', route.vip_detail_page))
    def test_jump(self, value):
        """
        测试点击服务协议/特权对比可正常跳转
        """
        types, re_path = value
        self.vippage.click_ele(types=types)
        time.sleep(2)
        try:
            path = self.vippage.current_path
            self.assertEqual(path, re_path)
        finally:
            self.vippage.back()

    @minium.ddt_case(('author', ['博主数据', '博主详情近360天', '查看全部博主榜单', '全部博主库']),
                     ('note', ['笔记数据', '查看全部笔记榜单', '查看全部笔记库']),
                     ('brand', ['品牌数据', '品牌详情近360天', '查看全部品牌库', '查看全部品牌榜单']),
                     ('kind', ['品类数据', '品类详情近360天', '查看全部品类库', '查看全部品类榜单']),
                     ('monitor', ['添加监控', '品牌监控 500次/月', '博主监控 2000次/月', '笔记监控 2000次/月']),
                     ('account_equity', ['账户权益', '数据导出 500次/月', '详情页查看不限']))
    def test_vip6_context(self, value):
        """
        测试企业版vip权益概览显示正确
        """
        self.vippage.switch_vip_tab(tab_name='企业版')
        time.sleep(3)
        self.vippage.scroll(high=800, duration=1000)
        time.sleep(1)
        types, vip_overview = value
        context = self.vippage.get_vip_overview(types=types)
        try:
            self.assertEqual(context, vip_overview)
        finally:
            self.vippage.scroll(high=-800, duration=1000)

    @minium.ddt_case(('author', ['博主数据', '博主详情近180天', '博主榜单前500', '全部博主库']),
                     ('note', ['笔记数据', '笔记榜单前500', '查看全部笔记库']),
                     ('brand', ['品牌数据', '品牌详情近180天', '查看全部品牌库', '品牌榜单前500']),
                     ('kind', ['品类数据', '品类详情近180天', '查看全部品类库', '品类榜单前500']),
                     ('monitor', ['添加监控', '品牌监控 200次/月', '博主监控 1000次/月', '笔记监控 1000次/月']),
                     ('account_equity', ['账户权益', '数据导出 300次/月', '详情页查看不限']))
    def test_vip4_context(self, value):
        """
        测试专业版vip权益概览显示正确
        """
        self.vippage.switch_vip_tab(tab_name='专业版')
        time.sleep(2)
        self.vippage.scroll(high=800, duration=1000)
        time.sleep(1)
        types, vip_overview = value
        context = self.vippage.get_vip_overview(types=types)
        try:
            self.assertEqual(context, vip_overview)
        finally:
            self.vippage.scroll(high=-800, duration=1000)

    @minium.ddt_case(('author', ['博主数据', '博主详情近90天', '博主榜单前200', '博主库前200']),
                     ('note', ['笔记数据', '笔记榜单前200', '笔记库前200']),
                     ('brand', ['品牌数据', '品牌详情不可查看', '品牌库前200', '品牌榜单前200']),
                     ('kind', ['品类数据', '品类数据部分可看', '品类库前200', '品类榜单前200']),
                     ('monitor', ['添加监控', '品牌监控 30次/月', '博主监控 100次/月', '笔记监控 100次/月']),
                     ('account_equity', ['账户权益', '详情页查看500次/月', '查看全部笔记库']))
    def test_vip5_context(self, value):
        """
        测试个人版vip权益概览显示正确
        """
        self.vippage.switch_vip_tab(tab_name='个人版')
        time.sleep(3)
        self.vippage.scroll(high=800, duration=1000)
        time.sleep(1)
        types, vip_overview = value
        context = self.vippage.get_vip_overview(types=types)
        try:
            self.assertEqual(context, vip_overview)
        finally:
            self.vippage.scroll(high=-800, duration=1000)

    @minium.ddt_case(('个人版',  {'errMsg': 'showToast:ok'}), ('专业版',  {'errMsg': 'showToast:ok'}))
    def test_vip_order_limit(self, value):
        """
        测试企业版用户无法续费个人版和专业版
        """
        types, tips = value
        self.vippage.switch_vip_tab(tab_name=types)
        try:
            callback = Callback()  # 创建接口调用前callback实例
            self.vippage.hook_wx_method('showToast', callback=callback)
            self.vippage.click_ele(types='vip_btn')
            re = callback.get_callback_result(timeout=3)
            self.assertEqual(re, tips)
        finally:
            self.vippage.release_hook_wx_method('showToast')

    def test_qa(self):
        """
        测试常见问题与反馈
        """
        self.vippage.scroll(high=800, duration=1000)
        time.sleep(2)
        question = '购买会员失败？'
        q = self.vippage.get_qa_context()
        try:
            self.assertEqual(q, question)
        finally:
            self.vippage.scroll(high=-800, duration=1000)

    @minium.skipUnless(condition=config.platform != "ide", reason="ide不支持客服跳转")
    def test_customer_service_jump(self):
        """
        测试真机点击广告位跳转人工客服
        """
        self.vippage.scroll(high=500)
        self.vippage.click_ele(types='expand_btn')
        self.vippage.click_ele(types='customer_service')
        time.sleep(2)
        path = self.vippage.current_path
        try:
            self.assertEqual(path, route.vip_page)
        finally:
            self.vippage.back_mini()
            time.sleep(2)
            self.vippage.click_ele(types='expand_btn')
            self.vippage.scroll(high=-500)

    @minium.ddt_case((1, '企业版12个月', '28999'), (2, '企业版3个月', '11999'),
                     (3, '企业版1个月', '4299'), (4, '企业版24个月', '43999'))
    def test_pop_info(self, value):
        """"
        测试购买会员弹窗的信息是否显示正确
        """
        card_id, re_pre, re_price = value
        self.vippage.choose_vip_version(version='企业版', card_id=card_id)
        time.sleep(1)
        self.vippage.click_ele(types='vip_btn')
        time.sleep(2)
        period, price, times = self.vippage.get_vip_pop_info()
        try:
            self.assertEqual(period, re_pre)
            self.assertEqual(price, re_price)
        finally:
            self.vippage.click_ele(types='close_pop')

    @minium.ddt_case((1, '12'), (2, '3'),
                     (3, '1'), (4, '24'))
    def test_pop_info_overdue_time(self, value):
        """
        测试过期时间计算正确
        """
        card_id, buy_month = value
        name, vip_name, current_time = self.vippage.get_user_info()
        overdue_time = Base.calculate_overdue_time(now_time=current_time, month_num=buy_month)
        self.vippage.choose_vip_version(version='企业版', card_id=card_id)
        time.sleep(1)
        self.vippage.click_ele(types='vip_btn')
        time.sleep(1)
        period, price, times = self.vippage.get_vip_pop_info()
        try:
            self.assertEqual(times, overdue_time)
        finally:
            self.vippage.click_ele(types='close_pop')

    @minium.ddt_case(('企业版', '立即续费'), ('专业版', '立即开通'), ('个人版', '立即开通'))
    def test_vip_btn_info(self, value):
        """
        测试企业版用户查看vip续费按钮，文案显示正确
        """
        types, re_text = value
        self.vippage.switch_vip_tab(tab_name=types)
        time.sleep(1)
        text = self.vippage.get_vip_btn_context()
        self.assertEqual(text, re_text)

    @minium.skipUnless(condition=config.is_activity is True, reason="活动期间有优惠券入口")
    @minium.ddt_case((1, ['不使用优惠券', '818特惠 立减1600元']), (2, ['不使用优惠券', '818特惠 立减500元']),
                     (3, ['不使用优惠券', '818特惠 立减200元']), (4, ['不使用优惠券', '818特惠 立减4500元']))
    def test_coupon(self, value):
        """
        测试优惠券面额
        """
        card_id, re_coupon_list = value
        self.vippage.choose_vip_version(version='企业版', card_id=card_id)
        time.sleep(1)
        self.vippage.click_ele(types='vip_btn')
        time.sleep(1)
        self.vippage.click_ele(types='coupon_choose')
        try:
            coupon_list = self.vippage.get_coupon_list(num=2)
            self.assertEqual(coupon_list, re_coupon_list)
        finally:
            self.vippage.click_ele(types='coupon_cancel')
            self.vippage.click_ele(types='close_pop')

    @minium.skipUnless(condition=config.is_activity is True, reason="活动期间有优惠券入口")
    @minium.ddt_case((1, '818特惠 立减1600元'), (2, '818特惠 立减500元'),
                     (3, '818特惠 立减200元'), (4, '818特惠 立减4500元'))
    def test_cc_coupon_choose(self, value):
        """
        测试优惠券面额
        """
        card_id, re_coupon = value
        self.vippage.choose_vip_version(version='企业版', card_id=card_id)
        self.vippage.click_ele(types='vip_btn')
        coupon = self.vippage.return_coupon_price()
        self.assertEqual(coupon, '请选择优惠券')
        self.vippage.click_ele(types='coupon_choose')
        time.sleep(1)
        try:
            self.vippage.choose_coupon(types='confirm', value=[1])
            coupon = self.vippage.return_coupon_price()
            self.assertEqual(coupon, re_coupon)
        finally:
            self.vippage.click_ele(types='close_pop')





