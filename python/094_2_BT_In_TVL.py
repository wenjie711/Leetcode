#!/usr/bin/env python
#coding: utf-8
class Stack:
    def __init__(self):
        self.stack = []
                
    def push(self, val):
        self.stack.append(val)
                                    
    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack) - 1]
                                                
    def isEmpty(self):
        return not self.stack

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def InorderTraversal(self, root):
        result = []
        s = Stack()
        p = root
        while(not s.isEmpty() or p != None):
            if(p != None):
                s.push(p)
                p = p.left
            else:
                t = s.pop()
                result.append(t.val)
                p = t.right
        return result

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.left = n3
n1.right = n2
s = Solution()
print(s.inorderTraversal(None))
