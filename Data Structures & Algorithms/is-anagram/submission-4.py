class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}
        for i in s:
            sdict[i] = sdict.setdefault(i, 0) + 1
        for i in t:
            tdict[i] = tdict.setdefault(i, 0) + 1
        return tdict == sdict