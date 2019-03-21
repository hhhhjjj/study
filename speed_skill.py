# coding=utf-8
import timeit
from collections import deque, defaultdict
# deque是双向队列，后面的是缺省字典
max = 100


# def way1():
#     mylist = []
#     for i in range(max):
#         mylist.append(i * i)
#   # 要记得有return
#     return mylist
#
#
# # 用列表推导式看起来快一些
# def way2():
#     mylist = [i * i for i in range(max)]
#     return mylist
#
#
# if __name__ == '__main__':
#     t1 = timeit.timeit("way1()", setup="from __main__ import way1")
#     # 要记得加括号才是调用函数，公众号出现了笔误，不过这个运行的巨慢无比,不知道为什么
#     print("way1", t1)
#     t2 = timeit.timeit("way2()", setup="from __main__ import way2")
#     print("way2", t2)


# def way1():
#     mylist = [i * i for i in range(1000)]
#     n = 0
#     for i in range(100000):
#         if i in mylist:
#             n += 1
#         else:
#             n += i*2
#     return n
#
#
# # 这样子看就字典块很多了，毕竟时间复杂度是1
# def way2():
#     myset = {i * i for i in range(1000)}
#     n = 0
#     for i in range(100000):
#         if i in myset:
#             n += 1
#         else:
#             n += i*2
#     return n
#
#
# if __name__ == '__main__':
#     t1 = timeit.timeit("way1()", setup="from __main__ import way1", number=10)
#     # 调用函数时候一定要记得加括号
#     print("way1", t1)
#     t2 = timeit.timeit("way2()", setup="from __main__ import way2", number=10)
#     print("way2", t2)


# def way1():
#     count = 0
#     for n in range(500):
#         for i in range(1000):
#             if n < 200:
#                 count += i
#             else:
#                 count += i * i
#     return count
#
#
# # 这种事交换if和for的位置，这个确实提升了速度
# def way2():
#     count = 0
#     for n in range(500):
#         if n <200:
#             for i in range(1000):
#                 count += 1
#         else:
#             for i in range(1000):
#                 count += i * i
#     return count
#
#
# if __name__ == '__main__':
#     t1 = timeit.timeit("way1()", setup="from __main__ import way1", number=10)
#     # 调用函数时候一定要记得加括号
#     print("way1", t1)
#     t2 = timeit.timeit("way2()", setup="from __main__ import way2", number=10)
#     print("way2", t2)


# def way1():
#     count = 0
#     for n in range(500):
#         for i in range(1000):
#             if n < 200:
#                 count += i
#             else:
#                 count += i * i
#     return count
#
#
# # 这种事交换if和for的位置，这个确实提升了速度
# def way2():
#     count = 0
#     for n in range(500):
#         if n <200:
#             for i in range(1000):
#                 count += 1
#         else:
#             for i in range(1000):
#                 count += i * i
#     return count
#
#
# if __name__ == '__main__':
#     t1 = timeit.timeit("way1()", setup="from __main__ import way1", number=10)
#     # 调用函数时候一定要记得加括号
#     print("way1", t1)
#     t2 = timeit.timeit("way2()", setup="from __main__ import way2", number=10)
#     print("way2", t2)


# def way1():
#     res = []
#     num = 100
#     for i in range(1000):
#         if i == 0:
#             num /= 20
#         else:
#             num /= i
#         res.append(num)
#     return res
#
#
# # 使用try来摆脱if的检查，但是这个计算出来的时间还长一些
# def way2():
#     res = []
#     num = 100
#     for i in range(1000):
#         try:
#             num /= i
#         except ZeroDivisionError as e:
#             num /= 10
#         finally:
#             res.append(num)
#     return res
#
#
# if __name__ == '__main__':
#     t1 = timeit.timeit("way1()", setup="from __main__ import way1", number=10)
#     # 调用函数时候一定要记得加括号
#     print("way1", t1)
#     t2 = timeit.timeit("way2()", setup="from __main__ import way2", number=10)
#     print("way2", t2)


# def way1():
#     mylist = list(range(10000))
#     for i in range(10000):
#         mylist.pop()
#     return mylist
#
#
# # 这个双向队列一般是需要大量从头或者从尾部删除、添加时候用的
# def way2():
#     mydeque = deque(range(10000))
#     for i in range(10000):
#         mydeque.pop()
#     return mydeque
#
#
# if __name__ == '__main__':
#     t1 = timeit.timeit("way1()", setup="from __main__ import way1", number=10)
#     # 调用函数时候一定要记得加括号
#     print("way1", t1)
#     t2 = timeit.timeit("way2()", setup="from __main__ import way2", number=10)
#     print("way2", t2)


def way1():
    d = {}
    chars = ['a', 'b', 'c', 'd', 'a'] * 1000
    for c in chars:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d


# 这个是缺省字典，如果访问不存在的key也不会报错，以后可以试试换字典数据结构,速度也要快许多
def way2():
    d = defaultdict(int)
    chars = ['a', 'b', 'c', 'd', 'a'] * 1000
    for c in chars:
        d[c] += 1
    return d


if __name__ == '__main__':
    t1 = timeit.timeit("way1()", setup="from __main__ import way1", number=10)
    # 调用函数时候一定要记得加括号
    print("way1", t1)
    t2 = timeit.timeit("way2()", setup="from __main__ import way2", number=10)
    print("way2", t2)

