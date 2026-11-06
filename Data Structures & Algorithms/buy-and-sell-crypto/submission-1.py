class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi = prices[0]
        maxi = 0
        for i in prices[1:]:
            mi = min(mi, i)
            maxi = max(maxi, i - mi)
        return maxi