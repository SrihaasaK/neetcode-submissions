class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        start = 0
        s = set(nums)
        maximum = 1
        running = 1
        for i in s:
            if i - 1 not in s:
                start = i
                while start + 1 in s:
                    start += 1
                    running += 1
                maximum = max(maximum, running)
                running = 1
        return maximum