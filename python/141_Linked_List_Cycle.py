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
    def hasCycle(self, head):
        fast = head
        slow = head
        while(fast != None):
            if(fast.next != None):
                fast = fast.next.next
            else:
                return False
            slow = slow.next
            if(fast == slow):
                return True
        return False

