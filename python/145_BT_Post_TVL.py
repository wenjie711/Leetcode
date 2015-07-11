#!/usr/bin/env python
#coding: utf-8
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def postorderTraversal(self, root):
        result = []
        if(root == None):
            return result
        l = self.postorderTraversal(root.left)
        for p in l:
            result.append(p)
        r = self.postorderTraversal(root.right)
        for p in r:
            result.append(p)
        result.append(root.val)
        return result

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.left = n3
n1.right = n2
s = Solution()
print(s.postorderTraversal(n1))
