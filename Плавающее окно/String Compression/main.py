from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        res = []

        l = r = 0

        while r < len(chars):
            while r + 1 < len(chars) and chars[r] == chars[r + 1]:
                r += 1

            res.append(chars[r])
            if r - l + 1 > 1:
                for c in str(r - l + 1):
                    res.append(c)
            l = r + 1
            r = l

        for i in range(len(res)):
            chars[i] = res[i]

        return len(res)
