class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            d[tuple(sorted(i))] = d.get(tuple(sorted(i)), [])
            d[tuple(sorted(i))].append(i)
        res = []
        for i in d.values():
            res.append(i)
        return res