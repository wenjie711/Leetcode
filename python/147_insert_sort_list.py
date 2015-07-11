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
    def insertionSortList(self, head):
        if not head:
            return head
        p = head.next
        head.next = None
        tail = head
        while p:
            q = p.next
            t = head
            s = t
            if(p.val > tail.val):
                tail.next = p
                tail = p
                tail.next = None
            else:
                while(t and p.val > t.val):
                    s = t
                    t = t.next
                p.next = t
                if(t == head):
                    head = p
                else:
                    s.next = p
            p = q
        return head
        
s = Solution()
l1 = ListNode(1)
l2 = ListNode(3)
l3 = ListNode(4)
l4 = ListNode(6)
l5 = ListNode(2)
l6 = ListNode(5)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
p = s.insertionSortList(l1)
while(p != None):
    print p.val
    p = p.next
        





