class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                continue
            else:
                pre[i] = pre[i-1]*nums[i-1]
        suff = 1
        for i in range(len(nums) - 1, -1, -1):
            pre[i] = suff*pre[i]
            suff *= nums[i]
        return pre
