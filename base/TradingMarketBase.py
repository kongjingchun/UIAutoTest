# encoding: utf-8
# @File  : TradingMarketBase.py
# @Author: 孔敬淳
# @Date  : 2025/12/23/17:08
# @Desc  :

class TradingMarketBase:

    @staticmethod
    def search_input():
        return "//input[@class='el-input__inner']"

    @staticmethod
    def search_button():
        return "//div[@class='el-input el-input-group el-input-group--append el-input-group--prepend el-input--suffix']//button/parent::div"

    @staticmethod
    def product_card(product_name):
        return "//div[text()='" + product_name + "']/ancestor::div[@class='el-row']"

    @staticmethod
    def i_want_buttton():
        return "//span[text()='我想要']/.."

    @staticmethod
    def buy_number_input():
        return "//div[@class='el-input el-input--small']/input"


    @staticmethod
    def receive_address():
        return "//input[@placeholder='收货地址']/.."

    @staticmethod
    def address_detail(num=1, address_name=None):
        if address_name:
            return "//span[text()='" + address_name + "']/parent::li"
        else:
            return "//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[" + str(num) + "]"

    @staticmethod
    def bottom_button():
        return "//span[text()='确 定']/parent::button"
