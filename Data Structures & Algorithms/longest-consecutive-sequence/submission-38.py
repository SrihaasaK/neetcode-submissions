class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        s = set(nums)
        st = 0
        r = 1
        m = 1
        for i in s:
            if i - 1 not in s:
                st = i
                while st + 1 in s:
                    st += 1
                    r += 1
                m = max(m,r)
                r = 1
        return m
