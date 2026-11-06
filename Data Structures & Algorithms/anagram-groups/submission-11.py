class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        if len(strs) == 0:
            return [[""]]
        if len(strs) == 1:
            return [[strs[0]]]
        for i in strs:
            if tuple(sorted(i)) in strs:
                d[tuple(sorted(i))].append(i)
            d[tuple(sorted(i))] = d.get(tuple(sorted(i)), [])
            d[tuple(sorted(i))].append(i)
        res = []
        for i in d.values():
            res.append(i)
        return res