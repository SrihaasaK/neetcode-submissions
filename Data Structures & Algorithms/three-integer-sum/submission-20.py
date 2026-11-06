class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lp = 0
        rp = len(nums) - 1
        nums = sorted(nums)
        res = []
        for i,v in enumerate(nums):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            lp = i+1
            rp = len(nums) - 1
            while lp < rp:
                if v + nums[rp] + nums[lp] > 0:
                    rp -= 1
                elif v + nums[rp] + nums[lp] < 0:
                    lp += 1
                elif v + nums[rp] + nums[lp] == 0:
                    res.append([v,nums[rp],nums[lp]])
                    lp += 1
                    while lp < rp and nums[lp] == nums[lp - 1]:
                        lp += 1
        return res