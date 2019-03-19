import time
from multiprocess import pool


def run(fn1):
    # 居然需要在这再import一次time，不然会报错
    import time
    time.sleep(1)
    return fn1*fn1


if __name__ == "__main__":
    testFL = [1, 2, 3, 4, 5, 6]
    print("顺序执行")
    s = time.time()
#     返回当前时间的时间戳
    for fn in testFL:
        run(fn)

    e1 = time.time()
    print("顺序执行的时间", int(e1 - s))
    print("创建多进程")
    my_pool = pool.Pool(5)
#     创建拥有5个进程数量的进程池
#     选择要处理的数据列表和处理列表的函数
    r1 = my_pool.map(run, testFL)
    my_pool.close()
    my_pool.join()
    e2 = time.time()
    print("并行执行时间", int(e2 - e1))
    print(r1)



