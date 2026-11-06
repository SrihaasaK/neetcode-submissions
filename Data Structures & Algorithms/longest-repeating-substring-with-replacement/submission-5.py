class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return s
        h = {}
        f = 0
        m = 0
        start = 0
        for end in range(len(s)):
            h[s[end]] = h.get(s[end], 0) + 1
            f = max(f, h[s[end]])
            while (end - start + 1) - f > k:
                h[s[start]] -= 1
                start += 1
            m = max(m, end-start + 1)
        return m
