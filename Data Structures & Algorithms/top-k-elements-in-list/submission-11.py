class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f = [[] for i in range(len(nums) + 1)]
        h = {}
        res = []
        for i in nums:
            h[i] = h.get(i,0) + 1
        for i,v in h.items():
            f[v].append(i)
        for i in range(len(nums), 0,-1):
            for j in f[i]:
                res.append(j)
                if len(res) == k:
                    return res
        return res
        
            