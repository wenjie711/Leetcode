#!/usr/bin/env python
#coding: utf-8
class Solution:
    # @param {integer} n
    # @return {integer}
    def numTrees(self, n):
        S = [1,]
        for i in range(1, n + 1):
            t = 0
            for j in range(i):
                t = S[j] * S[i - j - 1] + t
            S.append(t)
        return S[n]

s = Solution()
print(s.numTrees(2))
