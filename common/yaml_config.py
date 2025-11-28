# encoding: utf-8
# @File  : yaml_config.py
# @Author: kongjingchun
# @Date  : 2025/11/28/16:54
# @Desc  :
import yaml


class GetConf:
    def __init__(self):
        with open("/Users/kongjingchun/Documents/code/study_code/Python/trading_system_autotest/config/environment.yaml", encoding="utf-8") as env_file:
            self.env_data = yaml.load(env_file, Loader=yaml.FullLoader)

    def get_username_password(self):
        username = self.env_data["username"]
        password = self.env_data["password"]
        return username, password


if __name__ == '__main__':
    print(GetConf().get_username_password())
