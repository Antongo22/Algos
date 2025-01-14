from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1dict = defaultdict(int)
        for i in s1:
            s1dict[i] += 1

        s2dict = defaultdict(int)

        r = -1
        l = 0

        while l < len(s2):
            while r + 1 < len(s2) and s2dict.get(s2[r + 1], 0) + 1 <= s1dict.get(s2[r + 1], 0):
                s2dict[s2[r + 1]] += 1
                r += 1

            size = r - l + 1

            if size == len(s1):
                return True

            s2dict[s2[l]] -= 1
            if s2dict[s2[l]] == 0:
                del s2dict[s2[l]]
            l += 1
        return False