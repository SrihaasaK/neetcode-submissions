class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        s = sorted(nums)
        res = []
        for i in range(len(s)):
            if i > 0 and s[i] == s[i-1]:
                continue                          # skip duplicate pivots
            if s[i] > 0:
                break                              # can't sum to 0 anymore, sorted ascending
            l, r = i + 1, len(s) - 1
            while l < r:
                su = s[i] + s[l] + s[r]
                if su == 0:
                    res.append([s[i], s[l], s[r]])
                    l += 1
                    r -= 1
                    while l < r and s[l] == s[l-1]:
                        l += 1                      # skip duplicate l
                    while l < r and s[r] == s[r+1]:
                        r -= 1                      # skip duplicate r
                elif su > 0:
                    r -= 1
                else:
                    l += 1
        return res