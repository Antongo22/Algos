from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points)

        cur = points[0]
        res = 1

        for i in points:
            if max(cur[0], i[0]) <= min(cur[1], i[1]):
                cur = [max(cur[0], i[0]), min(cur[1], i[1])]
                continue

            cur = i
            res += 1

        return res