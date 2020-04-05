# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here

        out_list = []

        def recursion(self, listNode_):
            if listNode_ == None:
                return
            if listNode_.next != None:
                self.recursion(listNode_.next, out_list)
                out_list.append(listNode_.val)
                return
            else:
                out_list.append(listNode_.val)
                return
        self.recursion(listNode)
        return out_list
