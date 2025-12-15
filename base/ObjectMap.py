# encoding: utf-8
# @File  : ObjectMap.py
# @Author: kongjingchun
# @Date  : 2025/12/15/18:22
# @Desc  : 页面元素定位映射类，提供元素定位和等待功能
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ObjectMap:
    @staticmethod
    def element_get(driver: WebDriver, locate_type: By, locator_expression: str,
                    timeout: int = 10, is_visibility: bool = False) -> WebElement:
        """
        获取页面元素对象，支持超时等待和可见性判断

        Args:
            driver: 浏览器驱动对象
            locate_type: 元素定位方式 (By.ID, By.XPATH等)
            locator_expression: 元素定位表达式
            timeout: 超时时间(秒)，默认10秒
            is_visibility: 是否需要元素可见，默认False

        Returns:
            WebElement: 定位到的元素对象

        Raises:
            TimeoutException: 元素定位失败或超时
        """
        try:
            wait = WebDriverWait(driver, timeout)

            if is_visibility:
                # 等待元素可见
                condition = EC.visibility_of_element_located((locate_type, locator_expression))
            else:
                # 只等待元素存在（不一定可见）
                condition = EC.presence_of_element_located((locate_type, locator_expression))

            return wait.until(condition)
        except TimeoutException:
            visibility_text = "可见" if is_visibility else "存在"
            raise TimeoutException(
                f"元素定位失败（等待{visibility_text}），定位方式: {locate_type}，"
                f"定位表达式: {locator_expression}，超时时间: {timeout}秒"
            )
