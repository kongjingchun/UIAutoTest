# encoding: utf-8
# @File  : test_driver.py
# @Author: kongjingchun
# @Date  : 2025/12/01/15:02
# @Desc  :

from selenium import webdriver
from time import sleep
from common.tools import get_project_path, sep
from selenium.webdriver.chrome.service import Service

# 去除“Chrome正受到自动测试软件控制”的提示
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# options.add_argument('--disable-blink-features=AutomationControlled')

# 解决浏senium无法访问https的问题
# options.add_argument('--ignore-certificate-errors')

# 设置无痕模式
options.add_argument("--incognito")
# 禁用GPU加速，解决某些系统上的图形渲染问题
options.add_argument("--disable-gpu")
# 禁用沙箱模式，适用于容器化环境或权限受限的系统
options.add_argument("--no-sandbox")
# 禁用devshm使用，解决内存不足问题
options.add_argument("--disable-dev-shm-usage")

# 设置无头模式（无界面执行自动化测试）
# options.add_argument("--headless")

# 创建 ChromeDriver 服务，指定驱动程序路径
service = Service(executable_path=get_project_path() + sep(["driver_files", "chromedriver"], add_sep_before=True))

# 初始化 Chrome 浏览器实例，并设置窗口最大化
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()  # 将浏览器窗口最大化
# 导航到目标网页
driver.get("https://www.baidu.com/")

# 等待3秒，确保页面加载完成
sleep(3)

# 关闭浏览器并清理资源
driver.quit()
