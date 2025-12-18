# encoding: utf-8
# @File  : test_add_goods.py
# @Author: kongjingchun
# @Date  : 2025/12/17/14:27
# @Desc  :
from time import sleep

import pytest

from config.driver_config import DriverConfig
from page.GoodsPage import GoodsPage
from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage

goods_list = [
    {"title": "测试商品", "details": "商品详情", "num": 3, "img": ["机器猫.jpg"], "price": 66, "status": "上架", "button": "提交"},
    {"title": "测试商品2", "details": "商品详情2", "num": 3, "img": ["机器猫.jpg"], "price": 88, "status": "下架", "button": "提交"},
]


class TestAddGoods:
    @pytest.mark.parametrize("goods_info", goods_list)
    def test_add_goods_001(self, driver, goods_info):
        LoginPage().login(driver, "jay")
        LeftMenuPage().click_level_one_menu(driver, "产品")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver, "新增二手商品")
        sleep(1)
        GoodsPage().add_new_goods(
            driver,
            goods_info["title"],
            goods_info["details"],
            goods_info["num"],
            goods_info["img"],
            goods_info["price"],
            goods_info["status"],
            goods_info["button"]
        )
        sleep(1)
