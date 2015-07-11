#!/usr/bin/env python
#coding: utf-8
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def detectCycle(self, head):
        fast = head
        slow = head
        while(fast != None):
            if(fast.next != None):
                fast = fast.next.next
            else:
                return None
            slow = slow.next
            if(fast == slow):
                break
        if(fast == None):
            return None
        slow = head
        while(slow != fast):
            slow = slow.next
            fast = fast.next
        return slow

