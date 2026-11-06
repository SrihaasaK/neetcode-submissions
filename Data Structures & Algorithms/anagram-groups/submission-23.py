class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            d.setdefault("".join(sorted(i)), []).append(i)
        res = []
        for i in d.values():
            res.append(i)
        return res