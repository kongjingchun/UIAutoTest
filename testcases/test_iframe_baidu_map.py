# encoding: utf-8
# @File  : test_iframe_baidu_map.py
# @Author: kongjingchun
# @Date  : 2025/12/17/18:30
# @Desc  :
from time import sleep

from config.driver_config import DriverConfig
from page.IframeBaiduMapPage import IframeBaiduMapPage
from page.LeftMenuPage import LeftMenuPage
from page.LoginPage import LoginPage


class TestIframeBaiduMap:
    def test_iframe_baidu_map(self):
        driver = DriverConfig.driver_config()
        LoginPage().login(driver, "jay")
        sleep(2)
        LeftMenuPage().click_level_one_menu(driver, "iframe测试")
        sleep(2)
        IframeBaiduMapPage().switch_2_baidu_map_iframe(driver)
        sleep(2)
        IframeBaiduMapPage().input_baidu_map_search(driver,"科建大厦")
        sleep(2)
        IframeBaiduMapPage().click_baidu_map_search_button(driver)
        sleep(2)
        IframeBaiduMapPage().iframe_out(driver)
        sleep(2)
        LeftMenuPage().click_level_one_menu(driver, "交易市场")
        sleep(2)
        driver.quit()
