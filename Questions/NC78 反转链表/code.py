# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        prev=None
        cur=pHead
        while cur is not None:
            original_next=cur.next
            cur.next=prev
            prev=cur
            cur=original_next
        return prev
