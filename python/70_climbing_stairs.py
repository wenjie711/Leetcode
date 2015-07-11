#!/usr/bin/env python
#coding: utf-8
class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        c = n / 2
        r = 0
        for i in range(0, c + 1):
            j = (n - i * 2) + i
            r += self.C(i,j)
        return r

    def C(self, i, j):
        return self.factorial(j) / self.factorial(i) / self.factorial(j - i)

    def factorial(self, n):
        if(n == 1 or n == 0):
            return 1
        return n * self.factorial(n - 1)

s = Solution()
print s.climbStairs(10)
