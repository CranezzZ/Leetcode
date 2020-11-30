'''
给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。

若可行，输出任意可行的结果。若不可行，返回空字符串。

示例 1:

输入: S = "aab"
输出: "aba"
示例 2:

输入: S = "aaab"
输出: ""
'''

class Solution:
    def reorganizeString(self, S: str) -> str:
        import math
        sstr = ""
        llist = []
        lllist = []
        for i in range(26):
            llist.append([chr(ord('a') + i), 0])
        for i in range(len(S)):
            llist[ord(S[i]) - ord('a')][1] += 1
        llist.sort(key = lambda x: x[1], reverse = True)
        for i in range(len(llist)):
            for j in range(llist[i][1]):
                lllist.append(llist[i][0]) 
        #print(lllist)
        mid = math.ceil(len(S) / 2)
        llist1 = lllist[0: mid]
        llist2 = lllist[mid:]
        #print(llist1)
        #print(llist2)
        if llist1[0] == llist2[0]:
            return ""
        for i in range(len(llist2)):
            llist1[2 * i + 1: 2 * i + 1] = llist2[i]
        for i in range(len(llist1)):
            sstr += llist1[i]
        return sstr
