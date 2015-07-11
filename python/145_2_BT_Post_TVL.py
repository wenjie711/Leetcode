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
    def postorderTraversal(self, root):
        result = []
        d = set([]) 
        s = Stack()
        if(root == None):
            return result
        d.add(root)
        s.push(root)
        while(not s.isEmpty()):
            p = s.peek()
            if p not in d:
                s.pop()
                result.append(p.val)
                continue
            if(p.right != None):
                s.push(p.right)
                d.add(p.right)
            if(p.left != None):
                s.push(p.left)
                d.add(p.left)
            d.remove(p)
        return result

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.left = n3
n1.right = n2
s = Solution()
print(s.postorderTraversal(n1))
