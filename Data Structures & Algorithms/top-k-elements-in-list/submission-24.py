class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = []
        buckets = [[] for _ in range(max(count.values()) + 1)]
        for i,v in count.items():
            buckets[v].append(i)
        j = max(count.values())
        for i in range(k):
            while len(buckets[j]) == 0:
                j -= 1
            res.append(buckets[j].pop())
        return res



