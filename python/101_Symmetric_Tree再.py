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
    def isSymmetric(self, root):
        if(root == None):
            return True
        return self.isSymmetricIn(root.left, root.right)

    def isSymmetricIn(self, p ,q):
        if(p == None and q == None):
            return True
        if(p == None):
            return False
        if(q == None):
            return False
        if(q.val != p.val):
            return False
        return self.isSymmetricIn(p.left, q.right) and self.isSymmetricIn(p.right, q.left)

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(2)
n4 = TreeNode(3)
n5 = TreeNode(4)
n6 = TreeNode(4)
n7 = TreeNode(3)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
s = Solution()
print(s.isSymmetric(n1))
