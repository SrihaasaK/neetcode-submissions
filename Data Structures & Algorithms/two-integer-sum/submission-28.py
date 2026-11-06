class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        other = {}
        for i in range(len(nums)):
            if target - nums[i] in other:
                return [other[target - nums[i]], i]
            else:
                other[nums[i]] = i
        return [0,1]