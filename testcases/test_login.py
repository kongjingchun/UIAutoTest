# encoding: utf-8
# @File  : test_login.py
# @Author: kongjingchun
# @Date  : 2025/12/01/18:37
# @Desc  :
from time import sleep

from config.driver_config import DriverConfig
from page.LoginPage import LoginPage


class TestLogin:
    def test_login(self):
        driver = DriverConfig.driver_config()
        driver.get("http://120.53.230.254/login")
        sleep(3)
        LoginPage().login_input_value(driver, "用户名", "周杰伦")
        sleep(1)
        LoginPage().login_input_value(driver, "密码", "1234abcd!")
        sleep(2)
        LoginPage().click_login(driver, "登录")
        sleep(2)
        driver.quit()
