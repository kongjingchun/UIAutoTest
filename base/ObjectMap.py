# encoding: utf-8
# @File  : ObjectMap.py
# @Author: kongjingchun
# @Date  : 2025/12/15/18:22
# @Desc  : 页面元素定位映射类，提供元素定位和等待功能
from typing import Optional
from urllib.parse import urljoin
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.yaml_config import GetConf


class ObjectMap:
    def wait_for_element(self, driver: WebDriver, locate_type: By, locator_expression: str,
                         timeout: int = 10, is_visibility: bool = False) -> WebElement:
        """
        等待并获取页面元素对象，支持超时等待和可见性判断

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

    def wait_page_load(self, driver: WebDriver, timeout: int = 30) -> bool:
        """
        等待页面加载完成
        检查页面 document.readyState 状态，以及 jQuery（如果存在）是否加载完成

        Args:
            driver: 浏览器驱动对象
            timeout: 超时时间(秒)，默认30秒

        Returns:
            bool: 页面加载完成返回True

        Raises:
            TimeoutException: 页面加载超时
        """
        try:
            wait = WebDriverWait(driver, timeout)

            # 等待页面 document.readyState 为 complete
            def page_ready(driver):
                return driver.execute_script("return document.readyState") == "complete"

            # 等待页面加载完成
            wait.until(lambda d: page_ready(d))

            # 如果页面使用了 jQuery，等待 jQuery 加载完成
            try:
                wait.until(lambda d: d.execute_script("return typeof jQuery !== 'undefined' && jQuery.active == 0"))
            except TimeoutException:
                # 如果页面没有使用 jQuery，忽略此错误
                pass

            return True
        except TimeoutException:
            raise TimeoutException(f"页面加载超时，超时时间: {timeout}秒")

    def element_disappear(self, driver: WebDriver, locate_type: By, locator_expression: str,
                          timeout: int = 10) -> bool:
        """
        等待元素消失（不可见或从DOM中移除）
        常用于等待加载动画、提示信息等元素消失

        Args:
            driver: 浏览器驱动对象
            locate_type: 元素定位方式 (By.ID, By.XPATH等)
            locator_expression: 元素定位表达式
            timeout: 超时时间(秒)，默认10秒

        Returns:
            bool: 元素消失返回True

        Raises:
            TimeoutException: 元素未在指定时间内消失
        """
        try:
            wait = WebDriverWait(driver, timeout)

            # 等待元素不可见或从DOM中移除
            # invisibility_of_element_located 会处理元素不存在的情况
            condition = EC.invisibility_of_element_located((locate_type, locator_expression))

            wait.until(condition)
            return True
        except TimeoutException:
            raise TimeoutException(
                f"元素未消失（超时），定位方式: {locate_type}，"
                f"定位表达式: {locator_expression}，超时时间: {timeout}秒"
            )

    def element_appear(self, driver: WebDriver, locate_type: By, locator_expression: str,
                       timeout: int = 30) -> bool:
        """
        等待元素出现（可见或从DOM中加载）
        常用于等待加载动画、提示信息等元素出现

        Args:
            driver: 浏览器驱动对象
            locate_type: 元素定位方式 (By.ID, By.XPATH等)
            locator_expression: 元素定位表达式
            timeout: 超时时间(秒)，默认30秒

        Returns:
            bool: 元素出现返回True

        Raises:
            TimeoutException: 元素未在指定时间内出现
        """
        try:
            wait = WebDriverWait(driver, timeout)
            condition = EC.presence_of_element_located((locate_type, locator_expression))
            wait.until(condition)
            return True
        except TimeoutException:
            raise TimeoutException(
                f"元素未出现（超时），定位方式: {locate_type}，"
                f"定位表达式: {locator_expression}，超时时间: {timeout}秒"
            )

    def page_wait(self, driver: WebDriver, url: str,
                  locate_disappear_type: Optional[By] = None,
                  locator_disappear_expression: Optional[str] = None,
                  locate_appear_type: Optional[By] = None,
                  locator_appear_expression: Optional[str] = None,
                  base_url: Optional[str] = None,
                  timeout: int = 30) -> bool:
        """
        导航到指定URL并等待页面元素状态变化
        先等待页面加载完成，然后等待指定元素消失（如果提供），最后等待指定元素出现（如果提供）

        Args:
            driver: 浏览器驱动对象
            url: 要访问的URL（相对路径或绝对路径）
            locate_disappear_type: 元素消失的元素定位方式 (By.ID, By.XPATH等)，为None则跳过
            locator_disappear_expression: 元素消失的元素定位表达式
            locate_appear_type: 元素出现的元素定位方式 (By.ID, By.XPATH等)，为None则跳过
            locator_appear_expression: 元素出现的元素定位表达式
            base_url: 基础URL，如果为None则从配置文件读取
            timeout: 超时时间(秒)，默认30秒

        Returns:
            bool: 操作成功返回True

        Raises:
            TimeoutException: 页面加载或元素等待超时
            ValueError: URL参数无效
        """
        try:
            # 构建完整URL
            if base_url is None:
                base_url = GetConf().get_url()

            # 使用 urljoin 处理URL拼接，更可靠
            if url.startswith(("http://", "https://")):
                full_url = url
            else:
                # 确保 base_url 以 / 结尾，以便 urljoin 正确工作
                if not base_url.endswith("/"):
                    base_url += "/"
                full_url = urljoin(base_url, url.lstrip("/"))

            # 导航到URL
            driver.get(full_url)

            # 等待页面加载完成
            ObjectMap.wait_page_load(driver, timeout=timeout)

            # 如果提供了消失元素的定位信息，等待元素消失
            if all([locate_disappear_type, locator_disappear_expression]):
                ObjectMap.element_disappear(driver, locate_disappear_type,
                                            locator_disappear_expression, timeout=timeout)

            # 如果提供了出现元素的定位信息，等待元素出现
            if all([locate_appear_type, locator_appear_expression]):
                ObjectMap.element_appear(driver, locate_appear_type,
                                         locator_appear_expression, timeout=timeout)

            return True

        except TimeoutException as e:
            print(f"页面导航或元素等待超时: {e}")
            return False
        except ValueError as e:
            print(f"URL参数无效: {e}")
            return False
        except Exception as e:
            print(f"导航到地址时出现异常: {str(e)}")
            return False

    def element_is_display(self, driver: WebDriver, locate_type: By, locator_expression: str) -> bool:
        """
        检查元素是否在页面上显示

        Args:
            driver: 浏览器驱动对象
            locate_type: 元素定位方式 (By.ID, By.XPATH等)
            locator_expression: 元素定位表达式

        Returns:
            bool: 元素存在且显示返回True，否则返回False
        """
        try:
            driver.find_element(locate_type, locator_expression)
            return True
        except NoSuchElementException:
            print(f"元素未找到: {locate_type}，{locator_expression}")
            return False
        except Exception as e:
            print(f"检查元素显示状态时发生错误: {e}")
            return False

    def element_fill_value(self, driver: WebDriver, locate_type: By, locator_expression: str, 
                          value: str, timeout: int = 10, clear_before_fill: bool = True) -> bool:
        """
        向页面元素填充值（输入文本）
        支持自动处理换行符（\n），如果值以换行符结尾，会在输入后自动按回车键
        
        Args:
            driver: 浏览器驱动对象
            locate_type: 元素定位方式 (By.ID, By.XPATH等)
            locator_expression: 元素定位表达式
            value: 要填充的值（字符串）
            timeout: 等待元素出现的超时时间(秒)，默认10秒
            clear_before_fill: 填充前是否清空元素原有内容，默认True
            
        Returns:
            bool: 填充成功返回True，失败返回False
        """
        element = None
        try:
            # 等待页面加载完成，确保页面已就绪
            self.wait_page_load(driver)
            
            # 等待元素出现并获取元素对象（确保元素可见）
            element = self.element_appear(driver, locate_type, locator_expression, 
                                           timeout=timeout)
            
            # 先清空元素原有内容
            element.clear()
            
            # 将输入值转换为字符串
            input_value = str(value)
            
            # 处理换行符：如果值以 \n 结尾，先输入去掉换行符的内容，然后按回车键
            # 这样可以模拟用户在输入框中输入内容后按回车的行为
            if input_value.endswith("\n"):
                # 输入去掉换行符的内容
                element.send_keys(input_value[:-1])
                # 按回车键
                element.send_keys(Keys.ENTER)
            else:
                # 直接输入内容
                element.send_keys(input_value)
            
            return True
            
        except TimeoutException as e:
            # 元素未在超时时间内出现或不可见
            print(f"填充元素值失败：元素未在{timeout}秒内出现，定位方式: {locate_type}，"
                  f"定位表达式: {locator_expression}，错误: {e}")
            return False
        except StaleElementReferenceException as e:
            # 元素引用已失效（元素可能已被重新渲染）
            print(f"填充元素值失败：元素引用已过时，定位方式: {locate_type}，"
                  f"定位表达式: {locator_expression}，错误: {e}")
            return False
        except Exception as e:
            # 其他异常（如元素不可交互、输入失败等）
            print(f"填充元素值失败：发生未知错误，定位方式: {locate_type}，"
                  f"定位表达式: {locator_expression}，错误: {str(e)}")
            return False
        