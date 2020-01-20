# -*- coding: utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        # 这个是删除倒数第N个节点
        if head.next == None and n == 1:
            return None
        # 用哈希表记录位置
        positions = {}
        cur = head
        position = 0
        while cur.next is not None:
            positions[position] = cur
            cur = cur.next
            position += 1
        positions[position] = cur
        if n == 1:
            positions[position - 1].next = None
            return head
        # print(positions)
        if position - (n- 1) == 0:
            return head.next
        positions[position - (n- 1) - 1].next = positions[position - (n - 1) + 1]
        return head
        # print(head.next.val)

# 这个题目用双指针也可以

s1 = ListNode(1)
s2 = ListNode(2)
s3 = ListNode(3)
s1.next =s2
# s2.next =s3
print(Solution().removeNthFromEnd(s1, 1).val)







