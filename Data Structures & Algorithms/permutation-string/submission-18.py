class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        h1 = {}
        win = {}
        for i in s1:
            h1[i] = h1.get(i,0) + 1
        for l in range(len(s2) - len(s1) + 1):
            r = l + len(s1)
            if l == 0:
                for i in s2[l:r]:
                    win[i] = win.get(i,0) + 1
            else:
                win[s2[l-1]] -= 1
                if win[s2[l-1]] == 0:
                    del win[s2[l-1]]
                win[s2[r-1]] = win.get(s2[r-1],0) + 1
            if win == h1:
                return True
        return False
            
            