# encoding: utf-8
# @File  : driver_config.py
# @Author: kongjingchun
# @Date  : 2025/12/01/17:52
# @Desc  :


from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from common.tools import get_project_path, sep


class DriverConfig:
    @staticmethod
    def driver_config():
        """
        初始化 Chrome 浏览器驱动，兼容 Selenium 4.36
        :return: WebDriver 实例
        """
        # 去除“Chrome正受到自动测试软件控制”的提示

        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # options.add_experimental_option('useAutomationExtension', False)
        # options.add_argument('--disable-blink-features=AutomationControlled')

        # 安全与证书相关（解决 HTTPS 警告）
        options.add_argument("--disable-features=HttpsFirstMode")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--allow-insecure-localhost")
        options.add_argument("--ignore-ssl-errors=true")
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--disable-web-security")
        options.add_argument("--disable-site-isolation-trials")
        options.add_argument("--disable-3d-apis")

        # 解决浏senium无法访问https的问题
        # options.add_argument('--ignore-certificate-errors')

        # 设置无痕模式
        # options.add_argument("--incognito")
        # 禁用GPU加速，解决某些系统上的图形渲染问题
        options.add_argument("--disable-gpu")
        # 禁用沙箱模式，适用于容器化环境或权限受限的系统
        options.add_argument("--no-sandbox")
        # 禁用devshm使用，解决内存不足问题
        options.add_argument("--disable-dev-shm-usage")

        # 设置无头模式（无界面执行自动化测试）
        # options.add_argument("--headless")

        # 创建 ChromeDriver 服务，指定驱动程序路径
        # service = Service(executable_path=get_project_path() + sep(["driver_files", "chromedriver"], add_sep_before=True))
        # driver = webdriver.Chrome(service=service, )

        # 初始化 Chrome 浏览器实例
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(url="https://mirrors.huaweicloud.com/chromedriver", latest_release_url="https://mirrors.huaweicloud.com/chromedriver/LATEST_RELEASE").install()),
                                  options=options)

        driver.maximize_window()  # 设置浏览器全屏
        driver.delete_all_cookies()  # 删除所有cookies
        return driver
