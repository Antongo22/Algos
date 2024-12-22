from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        for point in intervals:
            if len(res) == 0:
                res.append(point)
                continue


            if res[-1][1] >= point[0]:
                if res[-1][1] < point[1]:
                    res[-1][1] = point[1]
            else:
                res.append(point)

        return res
