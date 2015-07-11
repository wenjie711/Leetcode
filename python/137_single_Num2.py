#!/usr/bin/env python
#coding: utf-8
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        one = 0
        two = 0
        three = 0
        for i in range(len(nums)):
            two |= one & nums[i]
            one ^= nums[i]
            three = two & one
            one ^= three
            two ^= three
        return one
s = Solution()
print(s.singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2]))
