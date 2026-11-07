class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        res = []
        buckets = [[] for _ in range(len(nums) + 1)]
        for i in nums:
            d[i] += 1
        for i,v in d.items():
            buckets[v].append(i)
        j = len(nums)
        for i in range(k):
            while len(buckets[j]) == 0:
                j-=1
            res.append(buckets[j].pop())
        return res


