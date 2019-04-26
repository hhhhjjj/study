# coding=utf-8
import time


# 如果没有文件就自动创建一个，一行是当前时间，第二行是操作
def write(operation):
    file = open(r"C:\H\log", "w")
    file.writelines(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    file.writelines("\n")
    file.writelines(operation)
    file.writelines("\n")


def get_name(func):
    def show_name(*args):
        # print(func.__name__)
        # print(*args)
        return func(*args)
    print(func.__name__)
    return show_name


class he(object):
    @get_name
    def test(self):
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        self.h()

    @get_name
    def h(self):
        print(1)


# he().test()
# he().h()
