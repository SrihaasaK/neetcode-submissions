class Solution:
    def isValid(self, s: str) -> bool:
        h = {'}':'{', ']':'[', ')':'('}
        a = deque()
        for i in range(len(s)):
            if i != 0:
                if len(a) > 0 and s[i] in h and a[-1] == h[s[i]]:
                    a.pop()
                else:
                    a.append(s[i])
            else:
                a.append(s[i])
        return len(a) == 0
            
        