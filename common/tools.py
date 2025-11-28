# encoding: utf-8
# @File  : tools.py
# @Author: kongjingchun
# @Date  : 2025/11/28/18:30
# @Desc  : 工具类，提供常用的功能函数

import datetime
import os


def get_now_time():
    """
    获取当前时间

    Returns:
        datetime: 当前的日期时间对象
    """
    return datetime.datetime.now()


def get_project_path():
    """
    获取项目根路径

    通过当前文件的绝对路径，向上两级目录获取项目根路径

    Returns:
        str: 项目根目录的绝对路径
    """
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


if __name__ == '__main__':
    # 测试函数功能
    print(get_now_time())  # 打印当前时间
    print(get_project_path())  # 打印项目根路径
