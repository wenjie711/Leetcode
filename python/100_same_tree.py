#!/usr/bin/env python
#coding: utf-8
def isSameTree(self, p, q):
    if(p == None and q == None):
        return True
            if(p == None):
                return False
            if(q == None):
                return False
            if(q.val != p.val):
                return False
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))))))))
