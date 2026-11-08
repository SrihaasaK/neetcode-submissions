class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for i in strs:
            res.append(str(len(i)) + "#" + i)
        return "".join(res)
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            l = int(s[i:j])
            res.append(s[j+1:l+j+1])
            i = l + j + 1
        return res