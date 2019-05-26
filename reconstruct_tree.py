# coding=utf-8
# 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
# 例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
# 在搜索路线中，若访问结点均是第一次经过结点时进行的，则是前序遍历；若访问结点均是在第二次（或第三次）经过结点时进行的，
# 则是中序遍历（或后序遍历）。只要将搜索路线上所有在第一次、第二次和第三次经过的结点分别列表，即可分别得到该二叉树的前序序列、中序序列和后序序列。
#      A
# B          C
# 前序遍历ABC,中序BAC，后序BCA
# 中序就是看有没有左节点，有左节点就先放弃自己去左节点去


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 前序遍历的话第一个肯定是根节点，然后根据根节点在中序遍历的位置来推算其他的


class Solution:
    # 返回构造的TreeNode根节点

    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        else:
            flag = TreeNode(pre[0])
            # 递归一下左右
            flag.left = self.reConstructBinaryTree(pre[1:tin.index(pre[0])+1], tin[:tin.index(pre[0])])
            flag.right = self.reConstructBinaryTree(pre[tin.index(pre[0])+1:], tin[tin.index(pre[0])+1:])
        return flag


if __name__=='__main__':
    solution=Solution()
    pre=list(map(int,"1,2,4,7,3,5,6,8".split(',')))
    tin=list(map(int,"4,7,2,1,5,3,8,6".split(',')))
    ans=solution.reConstructBinaryTree(pre,tin)
    print(ans.val)
