#!/usr/bin/env python
#coding: utf-8
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        d={};
        for i in range(len(num)):
            if(target-num[i] in d):
                return (d[target-num[i]],i+1)
            d[num[i]]=i+1

