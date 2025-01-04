from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:

        res = 0
        l = r = 0
        while r < len(seats):
            while r + 1 < len(seats) and seats[r + 1] == seats[r]:
                r += 1

            if seats[r] == 0:
                if l == 0 or r == len(seats) - 1:
                    res = max(res, r - l + 1)
                else:
                    res = max(res, (r - l + 2) // 2)

            l = r + 1
            r = l

        return res