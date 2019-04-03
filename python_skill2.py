# coding=utf-8
# 处理文件用with而不用try finally来解决没有文件或者关闭文件
print(list(map(lambda x: x * x, [1, 2, 3])))
# 这样就不用定义一个函数f（x）：return x*x这样子了，省的取名字麻烦
# 受保护的实例属性用_一个下划线开头，私有的用两个下划线__
# 不要通过len（）列表的方法来判断列表是否为空，应该采用if not list：这种方法将空值评估为false
# 尽量不要使用特别复杂难以理解的单行表达式
# 列表推导式的作用就是根据一份列表来制作另外一份，而且这个比map lambda要更加的简洁，当然尽量避免多级列表推导式
a = [1, 2, 3]
print(list(x * x for x in a))
# 这个就是少了个map 和 lamba
# 当输入的数据量非常多的时候，列表推导式很消耗内存，这时候用生成式更加好
# 生成器就是控制循环的迭代行为，就是不想把所有的数据全都遍历一遍
b = (x*x for x in a)
print(next(b))
print(next(b))
print(next(b))
# 这样子的话是惰性的，你不叫他他就不会往下接着走
# 用enumerate比range的好处是循环迭代时候还能返回index




