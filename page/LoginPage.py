#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/5/10
# @Author : chenxuehong
# @Version：V 0.1
# @File : RankPage.py
# @desc :

from page.BasePage import BasePage
from conf import route, config


class LoginPage(BasePage):

    # 微信登录/注册
    wechat_login_btn = ('button', '微信登录/注册')
    # 暂不登录
    no_login_btn = ('/page/view/view[2]/view[2]', '暂不登录')
    # 手机号或账号登录
    select_btn = ("/page/view/view[2]/view[3]/button", "手机号或账号登录")
    # 输入手机号
    input_mobile = "[placeholder='请输入手机号']"
    # 发送验证码
    send_code_btn = "/page/view/view[2]/view[2]/button"
    # 输入验证码
    input_code = "[placeholder='请输入验证码']"
    # 输入密码
    input_pwd = "[placeholder='请输入密码']"
    # 登录按钮
    login_btn = "/page/view/view[3]/button"
    # 切换账号密码登录
    switch_to_account_login_btn = ("/page/view/view[4]/view", "账号密码登录")
    # 切换验证码登录
    switch_to_code_login_btn = ("/page/view/view[4]/view", "验证码登录")

    def input_key(self, ele, value):
        try:
            self.get_element(ele).input(value)
        except:
            print('输入错误，报错元素{}'.format(ele))

    def select_login_type(self, types):
        """ 选择登录方式 """
        try:
            if types == 'wechat':
                self.wechat_login()
            elif types == 'no_login':
                self.no_login()
            elif types == 'account':
                self.account_login()
            elif types == 'code':
                self.code_login()
            else:
                print('登录方式输入错误，请输入wechat,no_login,account,code四种登录方式')
        except:
            print('选择登录方式失败')

    def wechat_login(self):
        """ 微信登录 """
        try:
            self.navigate_to_open(route.login_index_page)
            self.get_element(selector=self.wechat_login_btn[0], text_contains=self.wechat_login_btn[1]).click()
            self.sleep()
        except:
            print('微信登录失败')

    def no_login(self):
        """ 暂不登录 """
        try:
            self.navigate_to_open(route.login_index_page)
            self.get_element(selector=self.no_login_btn[0], text_contains=self.no_login_btn[1]).click()
            self.sleep(1)
        except:
            print('暂不登录操作失败')

    def account_login(self):
        """ 账号密码登录 """
        try:
            self.navigate_to_open(route.login_login_page)
            self.input_key(ele=self.input_mobile, value=config.default_account)
            self.input_key(ele=self.input_pwd, value=config.default_pwd)
            self.get_element(self.login_btn).click()
            self.sleep()
        except:
            print('账号密码登录失败')

    def code_login(self):
        """ 验证码登录 """
        try:
            self.navigate_to_open(route.login_register_page)
            self.input_key(ele=self.input_mobile, value=config.default_account)
            self.input_key(ele=self.input_code, value=config.default_code)
            self.get_element(self.login_btn).click()
            self.sleep()
        except:
            print('验证码登录失败')

