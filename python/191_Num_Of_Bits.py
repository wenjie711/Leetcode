#!/usr/bin/env python
#coding: utf-8
class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        num = 0
        while(n):
            n = n & (n - 1)
            num += 1
        return num

s = Solution()
print(s.hammingWeight(11))
