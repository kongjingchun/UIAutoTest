# encoding: utf-8
# @File  : TradingMarketPage.py
# @Author: 孔敬淳
# @Date  : 2025/12/23/17:42
# @Desc  :
from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.TradingMarketBase import TradingMarketBase
from logs.log import log


class TradingMarketPage(TradingMarketBase, ObjectMap):

    def input_search_input(self, driver, text):
        log.info("搜索宝贝输入框输入 : " + text)
        search_input_path = TradingMarketBase.search_input()
        return self.element_input_value(driver, By.XPATH, search_input_path, text)

    def click_search_button(self, driver):
        log.info("点击搜索按钮")
        search_button_path = TradingMarketBase.search_button()
        return self.element_click(driver, By.XPATH, search_button_path)

    def click_product_card(self, driver, product_name):
        log.info("点击商品卡片")
        product_card_path = TradingMarketBase.product_card(product_name)
        return self.element_click(driver, By.XPATH, product_card_path)

    def click_i_want(self, driver):
        log.info("点击我想要")
        i_want_path = TradingMarketBase.i_want_buttton()
        self.scroll_to_element(driver, By.XPATH, i_want_path)
        return self.element_click(driver, By.XPATH, i_want_path)

    def input_buy_number(self, driver, number):
        log.info("输入购买数量")
        buy_number_path = TradingMarketBase.buy_number_input()
        return self.element_input_value(driver, By.XPATH, buy_number_path, number)

    def click_address(self, driver):
        log.info("点击收货地址")
        receive_address_path = TradingMarketBase.receive_address()
        return self.element_click(driver, By.XPATH, receive_address_path)

    def click_address_detail(self, driver, num=1, address_name=None):
        log.info("点击收货地址详情")
        if address_name:
            log.info("收货地址名称为：" + address_name)
            address_detail_path = TradingMarketBase.address_detail(address_name=address_name)
        else:
            log.info("收货地址序号为：" + str(num))
            address_detail_path = TradingMarketBase.address_detail(num=num)
        return self.element_click(driver, By.XPATH, address_detail_path)

    def click_confirm_button(self, driver):
        log.info("点击确认按钮")
        confirm_button_path = TradingMarketBase.bottom_button()
        return self.element_click(driver, By.XPATH, confirm_button_path)
