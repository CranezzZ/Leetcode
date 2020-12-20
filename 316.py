'''
给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。

注意：该题与 1081 https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters 相同

 

示例 1：

输入：s = "bcabc"
输出："abc"
示例 2：

输入：s = "cbacdcbc"
输出："acdb"
'''

from collections import deque, Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        stack = deque()
        for c in s:
            count[c] -= 1
            if c in stack: continue
            while stack and stack[-1] > c:
                if count[stack[-1]] == 0:
                    break
                stack.pop()
            stack.append(c)
        return ''.join(stack)
