#!/usr/bin/env python
#coding: utf-8
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        return not self.stack


class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):
        result = []
        stack = Stack()
        if(root == None):
            return result
        stack.push(root)
        while(not stack.isEmpty()):
            p = stack.pop()
            result.append(p.val)
            if(p.right != None):
                stack.push(p.right)
            if(p.left != None):
                stack.push(p.left)

        return result

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.left = n3
n1.right = n2
s = Solution()
print(s.preorderTraversal(n1))


