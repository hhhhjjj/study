# coding=utf-8
import os
import re
import ui_MAIN_UI


class App(object):
    def __init__(self):
        # 初始化对应关系
        self.correspondence = {}
        self.correspondence_ground = {}
        # 文件夹所在位置
        self.app_path = ""
        self.ground_path = ""

    def traverse_app(self, path):
        file_list = os.walk(path)
        # 开始遍历文件夹
        for dir_path, dir_name, file_name in file_list:
            # 显示文件夹内的所有文件名
            for file_name_in in file_name:
                if file_name_in == "":
                    app = parse_app(os.path.join(dir_path, ""))
                    self.correspondence[app] = dir_path
        print(self.correspondence)
        self.rename_app()

    def rename_app(self):
        # key在前，value在后
        for new_name, dir_name in self.correspondence.items():
            os.renames(dir_name, os.path.join(self.app_path, new_name))

    def traverse_ground(self, path):
        file_list = os.walk(path)
        # 开始遍历文件夹
        for dir_path, dir_name, file_name in file_list:
            # 显示文件夹内的所有文件名
            for file_name_in in file_name:
                if file_name_in == "":
                    ground = parse_ground(os.path.join(dir_path, ""))
                    self.correspondence_ground[ground] = dir_path
        print(self.correspondence_ground)
        self.rename_ground()

    def rename_ground(self):
        # key在前，value在后
        for new_name, dir_name in self.correspondence_ground.items():
            os.renames(dir_name, os.path.join(self.ground_path, new_name))


def parse_app(file_name):
    with open(file_name, "rb") as f:  # 注意这里要是rb，不然gbk读不出来
        for line in f:
            # 想想能不能提供接口日后来增加其他配置项
            if re.search(b'', line.strip()):
                return""
            elif re.search(b'', line.strip()):
                return ""
            elif re.search(b'', line.strip()):
                return ""
            elif re.search(b'', line.strip()):
                return ""
            elif re.search(b'', line.strip()):
                return ""
            elif re.search(b'', line.strip()):
                return ""
            elif re.search(b'', line.strip()):
                return ""


def parse_ground(file_name):
    with open(file_name, "rb") as f:  # 注意这里要是rb，不然gbk读不出来
        for line in f:
            # 想想能不能提供接口日后来增加其他配置项
            if re.search(b'', line.strip()):
                return""
            elif re.search(b'', line.strip()):
                return ""
            elif re.search(b'', line.strip()):
                return ""
            elif re.search(b'', line.strip()):
                return ""
            elif re.search(b'', line.strip()):
                return ""
            elif re.search(b'', line.strip()):
                return ""
            elif re.search(b'', line.strip()):
                return ""
            elif re.search(b'', line.strip()):
                return ""
            elif re.search(b'', line.strip()):
                return ""
            elif re.search(b'', line.strip()):
                return ""
            elif re.search(b'', line.strip()):
                return ""
            elif re.search(b'', line.strip()):
                return ""
            elif re.search(b'', line.strip()):
                return ""


App().traverse_app(r"")
# App().traverse_ground(r"")






