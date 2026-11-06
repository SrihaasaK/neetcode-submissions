class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lp = 0
        rp = len(heights) - 1
        m = min(heights[lp],heights[rp]) * (len(heights) - 1)
        while lp < rp:
            if heights[lp] <= heights[rp]:
                lp += 1
            elif heights[rp] < heights[lp]:
                rp -= 1
            m = max(m, min(heights[lp],heights[rp]) * (rp - lp))
        return m