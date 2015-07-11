#!/usr/bin/env python
#coding: utf-8
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def sumNumbers(self, root):
        if not root:
            return 0
        return self.sumNumbersIn(root, 0)
    
    def sumNumbersIn(self, root, num):
        num = num * 10 + root.val
        if not root.left and not root.right:
            return num
        if not root.left:
            return self.sumNumbersIn(root.right, num)
        if not root.right:
            return self.sumNumbersIn(root.left, num)
        return self.sumNumbersIn(root.left, num) + self.sumNumbersIn(root.right, num)

s = Solution()
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.left = n2
n1.right = n3
print s.sumNumbers(None)
