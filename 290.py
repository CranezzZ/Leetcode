'''
给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。

这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

示例1:

输入: pattern = "abba", str = "dog cat cat dog"
输出: true
示例 2:

输入:pattern = "abba", str = "dog cat cat fish"
输出: false
示例 3:

输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false
示例 4:

输入: pattern = "abba", str = "dog dog dog dog"
输出: false
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sstr = s.split()
        ddict = {}
        ddict_reverse = {}
        if len(pattern) != len(sstr):
            return False
        for i in range(len(pattern)):
            if pattern[i] in ddict.keys():
                if ddict[pattern[i]] != sstr[i]:
                    return False
            else:
                ddict[pattern[i]] = sstr[i]
        for i in range(len(pattern)):
            if sstr[i] in ddict_reverse.keys():
                if ddict_reverse[sstr[i]] != pattern[i]:
                    return False
            else:
                ddict_reverse[sstr[i]] = pattern[i]
        return True
