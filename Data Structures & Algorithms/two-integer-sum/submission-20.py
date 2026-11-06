class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i,v in enumerate(nums):
            d = target - v
            if d in h:
                return [h[d],i]
            h[v] = i