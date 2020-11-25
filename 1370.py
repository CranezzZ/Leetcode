class Solution:
    def sortString(self, s: str) -> str:
        ss = sorted(s)
        ddict = dict()
        res = []
        for i in range(len(ss)):
            if ss[i] in ddict.keys():
                ddict[ss[i]] += 1
            else:
                ddict[ss[i]] = 1
        i = 0
        while len(ddict) > 0:
            for i in list(ddict.keys()):
                res.append(i)
                ddict[i] -= 1
                if ddict[i] == 0:
                    ddict.pop(i)
            for i in list(sorted(ddict.keys(), reverse = True)):
                res.append(i)
                ddict[i] -= 1
                if ddict[i] == 0:
                    ddict.pop(i)
        return ''.join(res)
