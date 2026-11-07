class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = []
        heap = []
        for i,v in count.items():
            heapq.heappush(heap, (-v, i))
        for i in range(k):
            v = heapq.heappop(heap)
            res.append(v[1])
        return res



