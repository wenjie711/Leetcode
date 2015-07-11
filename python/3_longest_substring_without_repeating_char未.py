#!/usr/bin/env python
#coding: utf-8
class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        l = len(s)
        m = 0
        if l == 0:
            return 0
        p = 0
        t = set()
        t.add(s[p])
        m += 1
        q = p + 1
        while q < l:
            if s[q] in t:
                t.remove(s[q])
                p += 1
                t.remove(s[p])
            else:
                t.add(s[q])
                if len(t) > m:
                    m = len(t)
                q += 1
            print t
        return m

s = Solution()
print s.lengthOfLongestSubstring("pwwkew")
