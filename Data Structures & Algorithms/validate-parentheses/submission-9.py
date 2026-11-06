class Solution:
    def isValid(self, s: str) -> bool:
        h = {'}':'{', ']':'[', ')':'('}
        a = deque()
        for i in s:
            if a and i in h and a[-1] == h[i]:
                a.pop()
            else:
                a.append(i)
        return len(a) == 0
            
        