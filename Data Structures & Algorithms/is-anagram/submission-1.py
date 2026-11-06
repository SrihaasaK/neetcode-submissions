class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sd = {}
        for i in s:
            sd.setdefault(i, 0)
            sd[i] += 1
        st = {}
        for j in t:
            st.setdefault(j,0)
            st[j] += 1
        return st == sd