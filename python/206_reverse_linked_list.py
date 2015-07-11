#!/usr/bin/env python
#coding: utf-8
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if(head == None):
            return None
        p = head.next
        h = head
        while(p != None):
             q = p.next
             p.next = h
             h = p
             p = q
        head.next = None
        return h

    def reverseList2(self, head):
        h = None
        p = head
        while(p != None):
            q = p.next
            p.next = h
            h = p
            p = q
        return h
    #递归算法
    def reverseList3(self, head):
        return self.reverseListInt(head, None)
        
    def reverseListInt(self, head, new):
        if not head:
            return new
        p = head.next
        head.next = new
        return self.reverseListInt(p, head)
s = Solution()
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l1.next = l2
l2.next = l3
l3.next = l4
p = s.reverseList3(l1)
while(p != None):
    print p.val
    p = p.next
        

