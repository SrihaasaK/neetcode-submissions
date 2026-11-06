class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]*len(nums)
        suff = [1]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                continue
            else:
                pre[i] = pre[i-1]*nums[i-1]
        for i in range(len(nums) - 1, -1, -1):
            if i == (len(nums) - 1):
                continue
            else:
                suff[i] = suff[i+1]*nums[i+1]
        res = []
        for i in range(len(pre)):
            res.append(pre[i]*suff[i])
        return res
