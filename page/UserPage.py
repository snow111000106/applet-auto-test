#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/5/10
# @Author : chenxuehong
# @Version：V 0.1
# @File : RankPage.py
# @desc :

from page.BasePage import BasePage
from conf import route
import time


class UserPage(BasePage):

    # 用户名称
    user_name = "/page/view/view[2]/view[1]/view/view/view[1]/text"
    # 点击登录按钮
    no_login = ("text", "点击登录")
    # 设置按钮
    set_btn = ("text", "设置")
    # 退出登录按钮
    logout_btn = ("text", "退出登录")
    # 确认退出按钮
    logout_btn_confirm = ("view", "确认")

    def is_user_name_exist(self):
        """ 判断登录按钮存在 """
        self.switch_to_tabbar(route.user_page)
        result = self.is_ele_exist(self.user_name)
        print(result)
        return result

    def logout(self):
        """ 退出登录 """
        try:
            self.switch_to_tabbar(route.user_page)
            self.get_element(self.set_btn[0], inner_text=self.set_btn[1]).click()
            self.get_element(self.logout_btn[0], inner_text=self.logout_btn[1]).click()
            self.get_element(self.logout_btn_confirm[0], inner_text=self.logout_btn_confirm[1]).click()
            return self
        except:
            print('退出登录失败')




