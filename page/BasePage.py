#!/usr/bin/env python
# @Software: PyCharm
# @Time : 2023/5/10
# @Author : chenxuehong
# @Version：V 0.1
# @File : BasePage.py
# @desc :

import time,minium, threading
from minium import Callback


class BasePage:
    def __init__(self, mini):
        self.mini = mini

    @property
    def current_page(self):
        """获取顶层页面"""
        return self.mini.app.get_current_page()

    @property
    def current_path(self) -> str:
        """获取当前页面route"""
        return self.mini.page.path

    def get_element(self, selector, inner_text=None, text_contains=None, value=None, max_timeout=20):
        """获取元素"""
        return self.mini.app.get_current_page().get_element(selector, inner_text=inner_text,
                                                            text_contains=text_contains,
                                                            value=value, max_timeout=max_timeout)

    def get_elements(self, selector, inner_text=None, max_timeout=20) -> list:
        """获取指定所有元素,返回元素列表"""
        return self.mini.page.get_elements(selector, inner_text=inner_text, max_timeout=max_timeout)

    def navigate_to_open(self, route):
        """跳转到指定页面,非tabbar页面"""
        self.mini.app.navigate_to(route)
        return self

    def redirect_to_open(self, route):
        """
        跳转到指定页面并关闭当前页面，非tabbar页面
        """
        self.mini.app.redirect_to(route)
        return self

    def switch_to_tabbar(self, route):
        """跳转到tabbar页面，关闭其他非tabbar页面 """
        self.mini.app.switch_tab(route)
        return self

    def relaunch_to_open(self, route):
        """ 关闭所有页面，打开到应用内的某个页面 """
        self.mini.app.relaunch(route)
        return self

    def get_all_page(self) -> list:
        """ 获取当前小程序页面栈 """
        page_list = self.mini.app.get_page_stack()
        return page_list

    def back(self, delta=1):
        """ 返回上一级页面，delta层级 """
        self.mini.app.navigate_back(delta)
        return self

    def back_mini(self):
        """ 返回小程序 """
        self.mini.native.back_to_miniprogram()
        return self

    def go_to_home(self):
        """跳转到首页"""
        self.mini.app.go_home()
        return self

    def get_context(self, ele) -> str:
        """获取元素内容"""
        context = self.get_element(ele).inner_text
        return context

    def scroll(self, high, duration=500):
        """滚动指定高度"""
        self.mini.page.scroll_to(scroll_top=high, duration=duration)

    def is_ele_exist(self, selector, inner_text=None, text_contains=None, value=None):
        """元素是否存在"""
        try:
            self.get_element(selector, max_timeout=5, inner_text=inner_text,
                             text_contains=text_contains, value=value)
            return True
        except:
            return False

    def wait_for_condition(self, condition, max_timeout=20) -> bool:
        """等待条件成立"""
        result = self.mini.page.wait_for(condition, max_timeout)
        return result

    def click_xy(self, x, y):
        """点击xy坐标"""
        self.mini.native.click_coordinate(x=x, y=y)
        return self



