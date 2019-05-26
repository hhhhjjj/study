# coding=utf-8
# 栈又叫堆栈，只能在一端进行操作，后进先出
# 队列就是一端只能删除一端只能插入
# **用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
# 这个构造栈的话直接用列表就行，然后用append和pop
# 这个感觉就是从后进先出变成先进先出，把一个栈拿来进，然后弹出的到另外一个栈去，另外这一个拿来出


class Solution:
    def __init__(self):
        self.Stack1=[]
        self.Stack2=[]

    def push(self, node):
        # write code here
        self.Stack1.append(node)

    def pop(self):
        # return xx
        if self.Stack2==[]:
            while self.Stack1:
                self.Stack2.append(self.Stack1.pop())
            return self.Stack2.pop()
        return self.Stack2.pop()


if __name__=='__main__':
    solution = Solution()
    solution.push(1)
    solution.push(2)
    solution.push(3)
    print(solution.pop())
    print(solution.pop())
    print(solution.pop())





