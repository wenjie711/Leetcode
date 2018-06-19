#!/usr/bin/env python
#coding: utf-8
class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    #把9+1＝10,前面的1给漏了
    def plusOne(self, digits):
        l = len(digits) - 1
        t = 1
        while(l >= 0):
            if(digits[l] + t >= 10):
                digits[l] = 0
                t = 1
            else:
                digits[l] += 1
                t = 0
                break
            l -= 1
        if(t == 1):
            digits.insert(0,1)
        return digits
s = Solution()
print s.plusOne([9])
            

