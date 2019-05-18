# coding=utf-8
import matplotlib.pyplot as plt
from pylab import *
import flash_ima
data_operation = {}


def analyze():
    # 打开日志文件构造字典
    with open(flash_ima.log_path, "r") as f:
        for line in f:
            data = line[:10]
            if data not in data_operation.keys():
                data_operation[data] = 1
            else:
                data_operation[data] = data_operation[data]+1

    mpl.rcParams['font.sans-serif'] = ['SimHei']
    # 只有加了这一句plt画出来的轴才能有中文
    # 画个白纸出来
    # 111表示1乘1网格，第一子图
    # 234就表示2乘3网格，第四子图
    plt.bar(range(len(list(data_operation))), data_operation.values(), color='rgb', tick_label=list(data_operation))
    plt.show()

