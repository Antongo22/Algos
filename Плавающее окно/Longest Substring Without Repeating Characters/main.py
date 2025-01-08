class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = -1

        res = 0

        chars = set()

        while l < len(s):
            while r + 1 < len(s) and s[r + 1] not in chars:
                chars.add(s[r + 1])
                r += 1

            res = max(res, r - l + 1)

            chars.remove(s[l])
            l += 1
        return res
