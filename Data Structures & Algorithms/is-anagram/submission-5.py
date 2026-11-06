class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}
        for i in s:
            sdict[i] = sdict.setdefault(i, 0) + 1
        for i in t:
            if i in sdict.keys():
                sdict[i] -= 1
                if sdict[i] == 0:
                    del sdict[i]
            else:
                return False
        return len(sdict) == 0