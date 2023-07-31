#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/5/10
# @Author : chenxuehong
# @Version：V 0.1
# @File : UserPage.py
# @desc : 我的页面封装

import time
from page.BasePage import BasePage
from conf import route


class UserPage(BasePage):

    # 用户名称
    user_name = '/page/view/view[2]/view[1]/view/view/view[1]/text'
    # 用户头像
    user_avatar = '/page/view/view[2]/view[1]/view/img-lazy/u-image/view/image'
    # 用户会员版本名称
    user_vip_name = '/page/view/view[2]/view[1]/view/view/view[1]/view/view/text'
    # 用户会员到期时间
    user_vip_overdue = '/page/view/view[2]/view[1]/view/view/view[2]/text'
    # 会员中心按钮
    vip_btn = '/page/view/view[2]/view[2]/button'
    # 点击登录按钮
    login = ("text", "点击登录")
    # 我的收藏入口
    collect_btn = '/page/view/view[3]/view[1]/view[1]/view/text[1]'
    # 我的收藏底部文案
    my_collect_text = '/page/view/view[3]/view[1]/view[1]/view/text[2]'
    # 我的监控入口
    trace_btn = '/page/view/view[3]/view[1]/view[3]/view/text[1]'
    # 我的监控入口
    my_trace_text = '/page/view/view[3]/view[1]/view[3]/view/text[2]'
    # 联系客服按钮
    customer_service_btn = '/page/view/view[3]/view[2]/view[1]/button'
    # 进入设置按钮
    set_btn = '/page/view/view[3]/view[2]/view[2]/view/text'

    # 以下设置页面元素
    # 头像
    avatar = '/page/view/view[1]/view[1]/view/img-lazy/u-image/view/image'
    # 昵称
    nike_name = '/page/view/view[1]/view[2]/view/text'
    # 手机号
    mobile = '/page/view/view[2]/view[1]/view/text'
    # 绑定微信状态
    wechat_status = '/page/view/view[2]/view[2]/view/label'
    # 账号类型
    account_type = '/page/view/view[2]/view[3]/view/label'
    # 退出登录按钮
    logout_btn = ("text", "退出登录")
    # 确认退出按钮
    logout_btn_confirm = ("view", "确认")

    def into_user_center(self):
        """进入我的页面"""
        self.switch_to_tabbar(route.user_page)
        time.sleep(1)
        return self

    def is_user_name_exist(self):
        """ 判断用户名存在 """

        result = self.is_ele_exist(self.user_name)

        return result

    def get_user_info(self, is_common=0):
        """ 获取会员版本名称 """
        vip_name = self.get_context(ele=self.user_vip_name)
        user_name = self.get_context(self.user_name)
        if is_common == 0:
            vip_time = self.get_context(ele=self.user_vip_overdue)[4:]
        else:
            vip_time = None
        return vip_name, vip_time, user_name

    def get_ele_text(self, types):
        """
        获取我的页面文案
        types='vip_btn': 会员中心按钮文案
        types='my_collect': 我的收藏底部文案
        types='my_trace': 我的监控底部文案
        """
        if types == 'vip_btn':
            text = self.get_context(self.vip_btn)
        elif types == 'my_collect':
            text = self.get_context(self.my_collect_text)
        elif types == 'my_trace':
            text = self.get_context(self.my_trace_text)

        return text

    def click_ele(self, types):
        """点击跳转"""
        try:
            if types == 'vip_btn':
                self.get_element(self.vip_btn).click()
            elif types == 'my_collect':
                self.get_element(self.collect_btn).click()
            elif types == "my_trace":
                self.get_element(self.trace_btn).click()
            elif types == 'customer_service':
                self.get_element(self.customer_service_btn).click()
            elif types == 'my_set':
                self.get_element(self.set_btn).click()
            return self
        except Exception as e:
            print(e)

    def get_my_set_info(self):
        """获取设置页面用户信息"""
        nick_name = self.get_context(self.nike_name)
        mobil = self.get_context(self.mobile)
        wechat_status = self.get_context(self.wechat_status)
        account_types = self.get_context(self.account_type)
        return nick_name, mobil, wechat_status, account_types

    def logout(self):
        """ 退出登录 """
        try:
            self.into_user_center()
            self.click_ele(types='my_set')
            self.get_element(self.logout_btn[0], inner_text=self.logout_btn[1]).click()
            self.get_element(self.logout_btn_confirm[0], inner_text=self.logout_btn_confirm[1]).click()
            return self
        except:
            print('退出登录失败')




