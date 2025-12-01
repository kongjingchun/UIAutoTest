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


def sep(path, add_sep_before=False, add_sep_after=False):
    """
    构造路径字符串，在路径片段之间添加系统分隔符
    
    Args:
        path (list): 路径片段列表
        add_sep_before (bool): 是否在路径前添加分隔符，默认为True
        add_sep_after (bool): 是否在路径后添加分隔符，默认为True
    
    Returns:
        str: 处理后的路径字符串
    """
    all_path = os.sep.join(path)
    if add_sep_before:
        all_path = os.sep + all_path
    if add_sep_after:
        all_path = all_path + os.sep
    return all_path


if __name__ == '__main__':
    # 测试函数功能
    print(get_now_time())  # 打印当前时间
    print(get_project_path())  # 打印项目根路径
