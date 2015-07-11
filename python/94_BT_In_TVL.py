#!/usr/bin/env python
#coding: utf-8
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def inorderTraversal(self, root):
        result = []
        if(root == None):
            return result
        if(root.left != None):
            left = self.inorderTraversal(root.left)
            for p in left:
                result.append(p)
        result.append(root.val)
        if(root.right != None):
            right = self.inorderTraversal(root.right)
            for p in right:
                result.append(p)
        return result

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.left = n3
n1.right = n2
s = Solution()
print(s.inorderTraversal(n1))
