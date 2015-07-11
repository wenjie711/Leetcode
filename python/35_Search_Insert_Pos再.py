#!/usr/bin/env python
#coding: utf-8
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        l = len(nums)
        for i in range(l):
            if(target == nums[i]):
                return i
            if(target < nums[i]):
                return i
        return l
    
    #二分查找的实现
    def searchInsert2()

s = Solution()
print(s.searchInsert([],5))
print(s.searchInsert([1,3,5,6],5))
print(s.searchInsert([1,3,5,6],2))
print(s.searchInsert([1,3,5,6],7))
print(s.searchInsert([1,3,5,6],0))
