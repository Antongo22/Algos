from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        l, r = 0, 0

        while l < len(nums):
            while r + 1 < len(nums) and nums[r] + 1 == nums[r + 1]:
                r += 1

            if r == l:
                res.append(str(nums[l]))
            else:
                res.append(str(nums[l]) + "->" + str(nums[r]))

            l = r + 1
            r = l
        return res