# coding=utf-8
# 装饰器就是在函数运行时增加功能且不影响函数原有的内容，还可以进行函数执行后的清理工作


def func1(func):
    def add_func():
        print("我添加的")
        # 返回函数调用
        return func()
#     实现闭包
    return add_func()


@func1
def func2():
    print("hello")
# 就是func1(func2)这样


func2
# 就是这样子，不应该加括号调用，加了括号就成了func1(func2)（）


def func3(func5):
    def func4(a, b):
        # 每次都这个套路来构建装饰器就行了,反正就拆开来看，但是这个被装饰的里面是有参数的，所以参数也要加进去，这样子就可以保留参数了
        return func5(a, b)
    return func4


@func3
def func(x, y):
    print("add func")
    print(x + y)


func(10, 20)


# 这样子来构建一个装饰器函数的参数接收函数，。因为装饰器函数只能是接收一个函数作为参数。@这个的时候往里面输入参数就行了
def arg_func(arg):
    def _func(func6):
        def _func1():
            if arg == "good":
                print("ok")
            if arg == "bad":
                print("no")
            return func6()
        return _func1
    return _func
