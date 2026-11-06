class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sd = {}
        for i in s:
            sd.setdefault(i, 0)
            sd[i] += 1
        for j in t:
            if j not in sd:
                return False
            sd[j] -= 1
        for i in sd:
            if sd[i] > 0:
                return False
        return True
