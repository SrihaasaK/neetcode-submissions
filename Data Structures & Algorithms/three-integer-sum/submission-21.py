class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        s = sorted(nums)
        se = set()
        for i in range(len(s)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                val = (s[i],s[l],s[r])
                su = s[i] + s[l] + s[r]
                if su == 0 and val not in se:
                    se.add(val)
                    while l < r and s[l] == s[l-1]:
                        l += 1
                elif su > 0:
                    r -= 1
                elif su < 0:
                    l += 1
                else:
                    l+=1
        return list(se)
