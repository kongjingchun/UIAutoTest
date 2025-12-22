# encoding: utf-8
# @File  : test_api_login.py
# @Author: kongjingchun
# @Date  : 2025/12/22/18:01
# @Desc  :
from time import sleep

import allure
import pytest

from page.LoginPage import LoginPage


class TestApiLogin:
    @pytest.mark.login
    @allure.feature("api登录")
    @allure.description("api登录")
    def test_api_login(self, driver):
        with allure.step("登录jay"):
            LoginPage().api_login(driver,"jay")
            sleep(3)
        with allure.step("切换用户到william"):
            LoginPage().api_login(driver,"jay")
            sleep(3)