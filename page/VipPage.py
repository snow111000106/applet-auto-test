#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/7/4
# @Author : chenxuehong
# @Version：V 0.1
# @File : VipPage.py
# @desc : vip续费页面封装

import time
from page.BasePage import BasePage
from conf import route


class VipPage(BasePage):

    # 用户头像
    user_avatar = '/page/view/view/view[1]/view/view/image'
    # 用户名称
    user_name = '/page/view/view/view[1]/view/view/view/view[1]/text'
    # 会员版本
    vip_name = '/page/view/view/view[1]/view/view/view/view[1]/view/text'
    # 会员到期时间
    vip_time = '/page/view/view/view[1]/view/view/view/view[2]'
    # 切换会员版本tab-企业版
    enterprise_vip_tab = '/page/view/view/view[2]/view/view[1]/view[1]/view/text'
    # 切换会员版本tab-专业版
    major_vip_tab = ('text', '专业版')
    # 切换会员版本tab-个人版
    personal_vip_tab = ('text', '个人版')
    # 年卡卡片
    card = {
        'periodic': '/page/view/view/view[2]/view/view[2]/view/view[{}]/view[1]',
        'price': '/page/view/view/view[2]/view/view[2]/view/view[{}]/view[2]/text[2]',
        'original_price': '/page/view/view/view[2]/view/view[2]/view/view[{}]/view[3]/text[2]',
        'discount_amount': '/page/view/view/view[2]/view/view[2]/view/view[{}]/view[4]/view'
    }
    # 优惠标签
    tag = '/page/view/view/view[2]/view/view[2]/view/view[{}]/view[5]/view/text'
    # 立即开通按钮
    vip_btn = '/page/view/view/view[2]/view/view[3]/view'
    # 协议按钮
    agreement_btn = '/page/view/view/view[2]/view/view[4]/view[2]'
    # 权益概览
    vip_overview = {
        'author': '/page/view/view/view[2]/rights-list/view/view[2]/view[1]/view/text[{}]',
        'note': '/page/view/view/view[2]/rights-list/view/view[2]/view[2]/view/text[{}]',
        'brand': '/page/view/view/view[2]/rights-list/view/view[2]/view[3]/view/text[{}]',
        'kind': '/page/view/view/view[2]/rights-list/view/view[2]/view[4]/view/text[{}]',
        'monitor': '/page/view/view/view[2]/rights-list/view/view[2]/view[5]/view/text[{}]',
        'account_equity': '/page/view/view/view[2]/rights-list/view/view[2]/view[6]/view/text[{}]'
    }
    # 查看特权对比
    vip_detail = '/page/view/view/view[2]/rights-list/view/view[1]/view[2]'
    # 常见问题与反馈
    question = '/page/view/view/view[2]/faq/view/view[2]/u-collapse/view/u-collapse-item/view/view[1]/view[1]/view/text'
    # 展开按钮
    expand_btn = '/page/view/view/view[2]/faq/view/view[2]/u-collapse/view/u-collapse-item/view/view[1]/' \
                 'view[2]/u-icon/view/text'
    # 联系客服
    customer_service = ('button', '联系客服')
    # 购买会员弹窗
    # 会员版本
    vip_period = '/page/view/u-popup/view/view/scroll-view/view/view[2]/view[1]/text'
    # 会员价格
    vip_price = '/page/view/u-popup/view/view/scroll-view/view/view[2]/view[2]/text[2]'
    # 有效期至
    vip_overdue_time = '/page/view/u-popup/view/view/scroll-view/view/view[2]/view[3]/text[2]'
    # 优惠券选择
    coupon_choose = '/page/view/u-popup/view/view/scroll-view/view/view[3]/view/view/view[2]'
    # 推荐人姓名输入框
    reference_name = '/page/view/u-popup/view/view/scroll-view/view/view[4]/u-input/view/input'
    # 立即续费按钮
    renew_btn = '/page/view/u-popup/view/view/scroll-view/view/view[6]/view'
    # 关闭弹窗
    close_pop = '/page/view/u-popup/view/view/view/u-icon/view/text'
    # 优惠券picker组件
    pick_coupon = '/page/view/u-popup/view/view/scroll-view/view/view[3]/u-picker/u-popup/view/view/' \
                  'scroll-view/view/view[2]/picker-view'
    # 优惠券
    coupons = '/page/view/u-popup/view/view/scroll-view/view/view[3]/u-picker/u-popup/view/view/' \
              'scroll-view/view/view[2]/picker-view/picker-view-column/view[{}]/view'
    # 确认选择优惠券
    coupon_confirm = '/page/view/u-popup/view/view/scroll-view/view/view[3]/u-picker/u-popup/view/view/' \
                     'scroll-view/view/view[1]/view[3]'
    # 取消选择优惠券
    coupon_cancel = '/page/view/u-popup/view/view/scroll-view/view/view[3]/u-picker/u-popup/view/view/' \
                    'scroll-view/view/view[1]/view[1]'

    def into_vip_center(self):
        """进入vip续费页面"""
        self.navigate_to_open(route.vip_page)
        time.sleep(1)
        return self

    def get_user_info(self):
        """获取vip页面用户信息"""
        name = self.get_context(self.user_name)
        vip_name = self.get_context(self.vip_name)
        vip_time = self.get_context(self.vip_time)

        return name, vip_name, vip_time[7:]

    def switch_vip_tab(self, tab_name):
        """切换各个会员版本"""
        try:
            if tab_name == '企业版':
                self.get_element(self.enterprise_vip_tab).click()
            if tab_name == '专业版':
                self.get_element(self.major_vip_tab[0], inner_text=self.major_vip_tab[1]).click()
            if tab_name == '个人版':
                self.get_element(self.personal_vip_tab[0], inner_text=self.personal_vip_tab[1]).click()
            return self
        except Exception as e:
            print(e)

    def get_vip_price_info(self, card_id, is_discount=True):
        """获取会员不同卡片的价格信息"""

        pre = self.get_context(self.card['periodic'].format(card_id))
        price = self.get_context(self.card['price'].format(card_id))
        original_price = self.get_context(self.card['original_price'].format(card_id))
        if is_discount is True:
            discount_amount = self.get_context(self.card['discount_amount'].format(card_id))[2:]
        else:
            discount_amount = None

        return pre, price, original_price, discount_amount

    def get_vip_tag_info(self, card_id):
        """获取会员不同卡片的标签信息"""

        pre = self.get_context(self.card['periodic'].format(card_id))
        tag_name = self.get_context(self.tag.format(card_id))
        return pre, tag_name

    def click_ele(self, types):
        """点击元素"""
        if types == 'agreement':
            self.get_element(self.agreement_btn).click()
        elif types == 'vip_detail':
            self.get_element(self.vip_detail).click()
        elif types == 'vip_btn':
            self.get_element(self.vip_btn).click()
        elif types == 'expand_btn':
            self.get_element(self.expand_btn).click()
        elif types == 'customer_service':
            self.get_element(self.customer_service[0], inner_text=self.customer_service[1]).click()
        elif types == 'close_pop':
            self.get_element(self.close_pop).click()
        elif types == 'coupon_choose':
            self.get_element(self.coupon_choose).click()
        elif types == 'coupon_confirm':
            self.get_element(self.coupon_confirm).click()
        elif types == 'coupon_cancel':
            self.get_element(self.coupon_cancel).click()
        else:
            print('click_ele，仅支持输入license/vip_detail/vip_renew/expand_btn/customer_service/close_pop')
        return self

    def choose_vip_version(self, version, card_id):
        """
        点击选择不同会员版本，version会员版本，card_id第几个卡片
        """
        self.switch_vip_tab(tab_name=version)
        self.get_element(self.card['periodic'].format(card_id)).click()

        return self

    def get_vip_overview(self, types):
        """获取权益概览列表数据"""
        context = []
        if types == 'author':
            for i in range(4):
                text = self.get_context(self.vip_overview['author'].format(i+1))
                context.append(text)
        elif types == 'note':
            for i in range(3):
                text = self.get_context(self.vip_overview['note'].format(i+1))
                context.append(text)
        elif types == 'brand':
            for i in range(4):
                text = self.get_context(self.vip_overview['brand'].format(i + 1))
                context.append(text)
        elif types == 'kind':
            for i in range(4):
                text = self.get_context(self.vip_overview['kind'].format(i + 1))
                context.append(text)
        elif types == 'monitor':
            for i in range(4):
                text = self.get_context(self.vip_overview['monitor'].format(i + 1))
                context.append(text)
        elif types == 'account_equity':
            for i in range(3):
                text = self.get_context(self.vip_overview['account_equity'].format(i + 1))
                context.append(text)
        return context

    def get_qa_context(self):
        """获取问题与反馈内容"""
        question = self.get_context(self.question)
        return question

    def get_vip_btn_context(self):
        """获取vip按钮文案的信息"""
        text = self.get_context(self.vip_btn)
        return text

    def get_vip_pop_info(self):
        """获取vip购买弹窗的信息"""
        period = self.get_context(self.vip_period)
        price = self.get_context(self.vip_price)
        times = self.get_context(self.vip_overdue_time)
        return period, price, times

    def get_coupon_list(self, num):
        """获取优惠券列表"""
        coupon_list = []
        for i in range(num):
            coupon = self.get_context(self.coupons.format(i+1))
            coupon_list.append(coupon)
        return coupon_list

    def return_coupon_price(self):
        """获取购买会员页优惠券选中面额"""
        coupon = self.get_context(self.coupon_choose)
        return coupon

    def choose_coupon(self, value, types):
        """选择/取消选择优惠券"""
        self.get_element(self.pick_coupon).trigger("change", {"value": value})
        time.sleep(1)
        if types == 'confirm':
            self.click_ele(types='coupon_confirm')
        elif types == 'cancel':
            self.click_ele(types='coupon_cancel')
        return self



