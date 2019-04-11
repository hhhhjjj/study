# coding=utf-8
import sys
import io
import os
from xml.dom.minidom import parse
# 修改默认编码格式
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def traverse_file(path):
    file_list = os.walk(path)
    # 开始遍历文件夹
    for dir_path, dir_name, file_name in file_list:
        # 显示文件夹内的所有文件名
        for file_name_in in file_name:
            print(file_name_in)
            parse_text(os.path.join(dir_path, file_name_in))


def parse_text(file_path):
    # with open(file_path, "r", encoding="utf-8") as f:
    #     print(f.read())
    # 使用minidom解析器打开xml文档
    DOMTree = parse(file_path)
    # 树状解析
    collection = DOMTree.documentElement
    # 找到对应标签下面的文字
    text = collection.getElementsByTagName("text")[0].childNodes[0].data
    file.writelines(text)
    file.writelines("\n")


if os.path.exists("nlp.txt"):
    os.remove("nlp.txt")
new_file = open("nlp.txt", "w+", encoding="utf-8")
new_file.close()
file = open("nlp.txt", "r+", encoding="utf-8")
file.read()
traverse_file(r"文件夹地址")
file.close()





