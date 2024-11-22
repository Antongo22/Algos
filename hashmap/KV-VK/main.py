from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        fr = [[] for _ in range(len(nums) + 1)]

        for key in d:
            fr[d[key]].append(key)

        res = []
        for i in range(len(nums), 0, -1):
            for j in fr[i]:
                res.append(j)
                k -= 1
                if k <= 0:
                    return res

        return res