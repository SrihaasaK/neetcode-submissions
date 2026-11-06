class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if (target - nums[i]) in nums:
                for j in range(len(nums)):
                    if (target - nums[i]) == nums[j] and i != j:
                        return [min(i,j), max(i,j)]
        return [0,1]