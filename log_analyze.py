# coding=utf-8
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set(xlim=[0, 5], ylim=[0, 8], title='日志分析',
       ylabel='操作次数', xlabel='日期')
plt.show()

