# 之前LeetCode遇到的一个关于二叉搜索树排序的题，需要先将给的前序遍历转成中序遍历才行
# 有两种方法，第一个就是先建立二叉树，再中序
# 这个并不难，反正就是根据root、left、right构建就行
# 第二种直接用栈，入栈的时候是前序，出栈就是中序
# 根左右变左根右
# pre_s = ["A", "B", "C"]
# 把下面一层补全就变成了下面这样
pre_s = ["A", "B", "null", "null", "C", "null", "null"]
# 把下一层的空算上其实是ABnullnullCnullnull
# 出栈是在前序遍历遇到空的时候，栈中弹出一个，如果是个完全二叉树，要记得把下一层的空都算上
# 所以弹出的时候是BAC
# 也就是中序遍历
def pre2mid(s):
    stack = []
    mid_s = []
    for i in range(len(s)):
        if s[i] != "null":
            stack.append(s[i])
        else:
            if len(stack) != 0:
                mid_s.append(stack.pop())
    return mid_s

print(pre2mid(pre_s))
# 如果是个完全二叉树没有去补全的话怎么办呢？
# 这就必须要树状结构了，而且不能给的list，需要给的是根节点，然后有left、right这些
# 中序遍历就是dfs
res = []
def dfs(root,res):
    if root == "":
        return ""
    dfs(root.left,res)
    res.append(root.value)
    dfs(root.right,res)

