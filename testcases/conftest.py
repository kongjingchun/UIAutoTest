# encoding: utf-8
# @File  : conftest.py
# @Author: kongjingchun
# @Date  : 2025/12/18/15:24
# @Desc  :

import pytest

from config.driver_config import DriverConfig


@pytest.fixture()
def driver():
    get_driver = DriverConfig.driver_config()
    yield get_driver
    get_driver.quit()
