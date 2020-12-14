'''
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ddict = {}
        cnt = 0
        llist = []
        for i in range(len(strs)):
            temp = sorted(strs[i])
            temp = "".join(temp)
            if temp in ddict.keys():
                llist[ddict[temp]].append(strs[i])
            else:
                ddict[temp] = cnt
                cnt += 1
                llist.append([strs[i]])
        return llist
        
