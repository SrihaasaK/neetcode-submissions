class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        start = 0
        maxi = 0
        window = set()
        for i in range(len(s)):
            while s[i] in window:
                window.discard(s[start])
                start += 1
            window.add(s[i])
            maxi = max(maxi, len(window))
        return maxi
            