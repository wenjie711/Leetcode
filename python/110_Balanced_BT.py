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
    # @return {boolean}
    def isBalanced(self, root):
        if(root == None):
            return True
        if(self.getHeight(root) == -1):
            return False
        return True

    def getHeight(self, root):
        if(root == None):
            return 0
        lh = self.getHeight(root.left)
        rh = self.getHeight(root.right)
        if(lh == -1 or rh == -1):
            return -1
        if(abs(lh - rh) > 1):
            return -1
        return 1 + max(lh, rh)

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.left = n2
n2.right = n3
s = Solution()
print(s.isBalanced(n1))
