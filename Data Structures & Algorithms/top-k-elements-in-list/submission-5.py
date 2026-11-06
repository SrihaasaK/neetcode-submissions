class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        res = []
        for i in nums:
            d[i] = d.get(i, 0) + 1
        d = sorted(d.items(), key = lambda x: x[1])
        for i in range(1, k+1):
            res.append(d[len(d) - i][0])
        return res