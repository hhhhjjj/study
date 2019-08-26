# （1）堆树是一颗完全二叉树；
# （2）堆树中某个节点的值总是不大于或不小于其孩子节点的值；
# （3）堆树中每个节点的子树都是堆树。
# 当父节点的键值总是大于或等于任何一个子节点的键值时为最大堆
# 其实就是递归比较左右根节点大小

#求最大堆树函数
def maxHeapTree(tree):
    if (isinstance(tree, Tree)):
        #对右子树求最大堆树
        maxHeapTree(tree.right)
        # 对左子树求最大堆树
        maxHeapTree(tree.left)
        #对该节点排序
        exchangeMaxTree(tree)
    return tree

#将树的左右节点以及根节点中选出最大的值，与根节点交换
def exchangeMaxTree(tree):
    #（右子树不存在 且 左子树存在 ）或 （ 左右子树都存在 且 左子树大于右子树情况下），根节点只需要和左子树进行比较
    if not isinstance(tree.right,Tree) and isinstance(tree.left,Tree)\
            or (isinstance(tree.left,Tree) and  tree.left.root > tree.right.root ):
        #和左子树比较节点大小
        if tree.root < tree.left.root:
            #交换两个节点的值
            tree.root, tree.left.root = tree.left.root, tree.root
            #交换完成后，可能会造成子树不满足最大树的概念，所以需要对子树重新进行最大堆树的步骤
            maxHeapTree(tree.left)
    #同理，不满足以上条件的，如果有右子树，就要判断右子树和根节点的大小
    elif isinstance(tree.right,Tree):
        if tree.root < tree.right.root:
            tree.root, tree.right.root = tree.right.root, tree.root
            maxHeapTree(tree.right)
def getHeapTreeLeven(tree):
    leven = 0
    while isinstance(tree, Tree):
        tree = tree.left
        leven += 1
    return leven

#递归打印树，没啥好说的，就是不停的递归左子树，右子树，然后输出根节点
#sep：输出左边留白长度
def printTree(tree, sep):
    if (isinstance(tree, Tree)):
        print(sep, tree.root, sep="")
        printTree(tree.left, sep + "  ")
        printTree(tree.right, sep + "  ")

#生成二叉树 tree树节点，datas二维数组数据源，leven树节点对应树的层级，num该节点位于该层级的第几节点
def toTree(tree, datas, leven, num):
    #第一级子树，直接将根节点设置为数组的第一个元素并进行向下传递
    if leven == 1:
        tree = Tree()
        tree.root = datas[0]
        #构建左子树，由于是根节点的左子树，所以默认位置为1
        toTree(tree, datas, 2, 1)
        #构建右子树，由于是根节点的右子树，所以默认位置为2
        toTree(tree, datas, 2, 2)
    else:
        #叶子节点对应数组的坐标计算公式
        index = 2 ** (leven - 1) - 2 + num
        #结束条件，如果满足该条件，说明该子节点对应的数组值越界，结束循环
        if index >= len(datas):
            return tree
        #index如果不能被2整除，说明该节点是左子树，反之右子树
        if (index % 2 == 1):
            tree.left = Tree()
            tree.left.root = datas[index]
            #构建该节点的左右子树，级别+位置为该节点位置的二倍为左子树
            toTree(tree.left, datas, leven + 1, num * 2 - 1)
            toTree(tree.left, datas, leven + 1, num * 2)
        else:
            tree.right = Tree()
            tree.right.root = datas[index]
            toTree(tree.right, datas, leven + 1, num * 2 - 1)
            toTree(tree.right, datas, leven + 1, num * 2)
    return tree


class Tree():
    root = 0
    left = 0
    right = 0

#测试
heap = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
tree = toTree(None, heap, 1, 0)
tree=maxHeapTree(tree)
printTree(tree,"")





