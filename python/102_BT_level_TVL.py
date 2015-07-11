#!/usr/bin/env python
#coding: utf-8
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Queue:
    def __init__(self):
        self.q = []
        self.c = 0

    def push(self, e):
        self.q.append(e)
        self.c = self.c + 1

    def pop(self):
        if(self.c != 0):
            self.c = self.c - 1
            return self.q.pop(0)
        else:
            return -1

    def isEmpty(self):
        if(self.c == 0):
            return True
        else:
            return False

    def size(self):
        return self.c


class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrder(self, root):
        result = []
        q = Queue() 
        if(root == None):
            return result
        q.push(root)
        while(not q.isEmpty()):
            n = q.size()
            l = []
            for i in range(n):
                t = q.pop()
                l.append(t.val)
                if(t.left != None):
                    q.push(t.left)
                if(t.right != None):
                    q.push(t.right)
            result.append(l)
        return result


n1 = TreeNode(3)
n2 = TreeNode(9)
n3 = TreeNode(20)
n4 = TreeNode(15)
n5 = TreeNode(7)
n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5
s = Solution()
print(s.levelOrder(n1))
