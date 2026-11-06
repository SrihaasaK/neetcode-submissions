class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sd = {}
        for i in s:
            sd[i] = sd.get(i,0) + 1
        st = {}
        for j in t:
            st[j] = st.get(j,0) + 1
        return st == sd