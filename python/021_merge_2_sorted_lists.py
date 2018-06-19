#!/usr/bin/env python
#coding: utf-8
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        l = ListNode(0)
        p = l
        while l1 and l2:
            if(l1.val < l2.val):
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1:
            p.next = l1
        if l2:
            p.next = l2
        return l.next

s = Solution()
l1 = ListNode(1)
l2 = ListNode(3)
l3 = ListNode(4)
l4 = ListNode(6)

m1 = ListNode(2)
m2 = ListNode(5)
m1.next = m2
l1.next = l2
l2.next = l3
l3.next = l4
p = s.mergeTwoLists(None,l1)
while(p != None):
    print p.val
    p = p.next
        




