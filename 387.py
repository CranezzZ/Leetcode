'''
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

 

示例：

s = "leetcode"
返回 0

s = "loveleetcode"
返回 2
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        ddict = dict()
        for c in s:
            if c not in ddict.keys():
                ddict[c] = 1
            else:
                ddict[c] += 1
        for i in range(len(s)):
            if ddict[s[i]] == 1:
                return i
        return -1
