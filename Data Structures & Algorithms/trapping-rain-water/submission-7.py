class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        lm, rm = [0]*len(height), [0]*len(height)
        for i in range(len(height)):
            if i == 0:
                lm[i] = height[i]
            else:
                lm[i] = max(lm[i-1], height[i])
        for i in range(len(height) - 1,-1,-1):
            if i == (len(height) - 1):
                rm[i] = height[i]
            else:
                rm[i] = max(rm[i+1], height[i])
        for i in range(len(height) - 1):
            res += min(lm[i], rm[i]) - height[i]
        return res
