class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi = prices[0]
        m = 0
        for i in prices[1:]:
            mi = min(mi, i)
            m = max(m, i - mi)
        return m