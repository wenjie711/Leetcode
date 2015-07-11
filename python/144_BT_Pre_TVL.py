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
    # @return {integer[]}
    def preorderTraversal(self, root):
        result = []
        return self.pt(root, result)
    

    def pt(self, root, result):
        if(root != None):
            result.append(root.val)
            if(root.left != None):
                self.pt(root.left, result)
            if(root.right != None):
                self.pt(root.right, result)
        return result

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.left = n3
n1.right = n2
s = Solution()
print(s.preorderTraversal(n1))


