# coding=utf-8
"""
**输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）。
"""
# 遇到这种树的问题其实一般就是用前序遍历和中序遍历，这个的话全部转化成中序遍历的字符串，然后判断包含不包含就行
# 中序遍历BAC


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot1 is None or pRoot2 is None:
            return False
        pRoot1_result,pRoot2_result=[],[]
        self.order_traversal(pRoot1,pRoot1_result)
        self.order_traversal(pRoot2,pRoot2_result)
        str1=''.join(str(i) for i in pRoot1_result)
        str2=''.join(str(i) for i in pRoot2_result)
        print(str1,str2)
        if str2 in str1:
            return True
        else:
            return False

    def order_traversal(self,root,result):
        if not root:
            return
        # 递归中序遍历
        self.order_traversal(root.left,result)
        result.append(root.val)
        self.order_traversal(root.right,result)


if __name__=='__main__':
    solution=Solution()
    pRootA1 = TreeNode(1)
    pRootA2 = TreeNode(2)
    pRootA3 = TreeNode(3)
    pRootA4 = TreeNode(4)
    pRootA5 = TreeNode(5)
    pRootA1.left=pRootA2
    pRootA1.right=pRootA3
    pRootA2.left=pRootA4
    pRootA2.right=pRootA5

    pRootB2 = TreeNode(2)
    pRootB4 = TreeNode(4)
    pRootB5 = TreeNode(5)
    pRootB2.left=pRootB4
    pRootB2.right = pRootB5
    ans=solution.HasSubtree(pRootA1,pRootB2)
    print(ans)