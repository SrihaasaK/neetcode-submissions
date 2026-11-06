class Solution:

    def encode(self, strs: List[str]) -> str:
        e = ""
        for i in strs:
            e += str(len(i)) + "#" + i
        return e
    def decode(self, s: str) -> List[str]:
        r = []
        i = 0
        c = 0
        while i < len(s):
            if i <= len(s) - 1 and s[i] in "1234567890" and s[i+1] == "#":
                c = int(s[i])
                i += 2
            elif i <= len(s) - 1 and s[i] in "1234567890" and s[i+1] != "#":
                n = s[i]
                i += 1
                while i <= len(s) - 1 and s[i] != "#":
                    n += s[i]
                    i+=1
                c = int(n)
                i += 1
            r.append(s[i:i+c])
            i += c
            c = 0
        return r
