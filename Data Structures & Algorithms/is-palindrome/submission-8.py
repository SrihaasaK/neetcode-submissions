class Solution:
    def isPalindrome(self, s: str) -> bool:
        lp = 0
        st = ""
        for i in s.lower():
            if i.isalnum():
                st += i
        rp = len(st) - 1
        while lp <= rp:
            if st[lp] != st[rp]:
                return False
            else:
                lp += 1
                rp -= 1
        return True