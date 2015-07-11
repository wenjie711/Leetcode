#!/usr/bin/env python
#coding: utf-8
class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        a = 0
        b = 0
        c = 0
        for i in range(len(nums)):
            if(nums[i] == 0):
                a += 1
            if(nums[i] == 1):
                b += 1
            if(nums[i] == 2):
                c += 1
            for i in range(a):
                nums[i] = 0
            for i in range(a, a + b):
                nums[i] = 1
            for i in range(a + b, a + b + c):
                nums[i] = 2
        print(nums)
#方案二：
#j可以利用三个指针的方法来求解。当i,j,k。k指向最后。
#1、当j为1的时候，就j++，不进行交换
#2、当j为0的时候，就和i处的元素交换，然后i++和j++。（这里的j++是因为保证了j前面的元素要么为0，要么为1，如果加强条件i==j时不交换，更省一点点时间）
#3、当j为2的时候，就和k处的元素交换，然后k--，但j不变，重新判断j处的新值（也可以判断k处的值再交换，不过增添了麻烦，直接交换比较好
    def sortColors2(self, nums):
        i = 0
        j = 0
        l = len(nums)
        k = l - 1
        while(j <= k):
            if(nums[j] == 0):
                self.swap(nums, i, j)
                i += 1
                j += 1
            elif(nums[j] == 1):
                j += 1
            else:
                if(j != k):
                    self.swap(nums, j, k)
                k -= 1
        print nums

    #注意i和j不能一样，否则会变成0
    def swap(self, nums, i, j):
        nums[i] ^= nums[j] 
        nums[j] ^= nums[i] 
        nums[i] ^= nums[j] 
s = Solution()
s.sortColors2([1,2,2,2,1,1,0,0,1,2,0,1,1])
