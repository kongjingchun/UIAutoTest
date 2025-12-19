# encoding: utf-8
# @File  : test_switch_window_handle.py
# @Author: kongjingchun
# @Date  : 2025/12/17/16:16
# @Desc  : 测试窗口切换功能
from time import sleep

import allure

from page.LoginPage import LoginPage
from page.ExternalLinkPage import ExternalLinkPage
from page.LeftMenuPage import LeftMenuPage


class TestSwitchWindowHandle:
    """测试窗口切换处理类"""

    @allure.description("测试窗口切换功能")
    @allure.epic("窗口切换epic")
    @allure.feature("窗口切换feature")
    @allure.story("窗口切换story")
    @allure.tag("窗口切换tag")
    def test_switch_window_handle(self, driver):
        with allure.step("登录"):
            LoginPage().login(driver, "jay")
        with allure.step("点击外链"):
            LeftMenuPage().click_level_one_menu(driver, "外链")
        with allure.step("点击跳转"):
            title = ExternalLinkPage().goto_imooc(driver)
            print("网址切换到" + title)
            assert "慕课网" in title
            sleep(3)
