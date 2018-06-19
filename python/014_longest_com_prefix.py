#!/usr/bin/env python
#coding: utf-8
class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        result = ""
        #t用于判断目前最短的strs元素字符串是多短
        t = -1
        #m用于判断目前发现不一致的情况下，外层循环的i夜不用继续走下去了
        m = -1
        if(len(strs) == 0):
            return result
        for i in range(len(strs[0])):
            if(t == -1 and m == -1):
                for j in range(1, len(strs)):
                    if(i >= len(strs[j])):
                        if(t == -1 or len(strs[j]) < t):
                            t = len(strs[j])
                        continue
                    if(strs[0][i] != strs[j][i]):
                        m = 0
                        continue
                if(m != 0):
                    result += strs[0][i]
            else:
                break
        if(t == -1):
            return result
        return result[:t]
s = Solution()
print(s.longestCommonPrefix(["a","b"]))
print(s.longestCommonPrefix(["aa","a",""]))
print(s.longestCommonPrefix([]))
print(s.longestCommonPrefix(["abc", "abcd", "abc1asa"]))
