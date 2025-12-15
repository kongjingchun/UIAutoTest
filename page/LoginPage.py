# encoding: utf-8
# @File  : LoginPage.py
# @Author: kongjingchun
# @Date  : 2025/12/01/18:31
# @Desc  :

from selenium.webdriver.common.by import By
from base.LoginBase import LoginBase


class LoginPage(LoginBase):
    def login_input_value(self, driver, input_placeholder, input_value):
        """
        在登录页面的输入框中填入指定值

        :param driver: WebDriver实例
        :param input_placeholder: 输入框的placeholder属性值
        :param input_value: 要输入的值
        :return: None
        """
        input_xpath = LoginBase.login_input(input_placeholder)  # 修正调用父类方法
        return driver.find_element(By.XPATH, input_xpath).send_keys(input_value)

    def click_login(self, driver, button_name):
        """
        点击登录页面的按钮

        :param driver: WebDriver实例
        :param button_name: 按钮显示文本
        :return: None
        """
        button_xpath = LoginBase.login_button(button_name)  # 修正调用父类方法
        return driver.find_element(By.XPATH, button_xpath).click()
