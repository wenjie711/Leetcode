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
    def deleteDuplicates(self, head):
       p = head
       while p:
           q = p.next
           if not q:
               break
           if q.val == p.val:
               p.next = q.next
           else:
               p = q 
       return head
   
    def deleteDuplicates2(self, head):
       if not head:
           return head
       p = head
       q = p.next
       while q:
           if(p.val == q.val):
               p.next = q.next
           else:
               p = q
           q = q.next 
       return head 


s = Solution()
l1 = ListNode(1)
l2 = ListNode(1)
l3 = ListNode(2)
l4 = ListNode(3)
l5 = ListNode(3)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
p = s.deleteDuplicates2(l1)
while(p != None):
    print p.val
    p = p.next
        





