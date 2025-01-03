from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0

        l, r = 0, 0

        while r < len(nums):
            while r + 1 < len(nums) and nums[r + 1] == nums[r]:
                r += 1

            if nums[r] == 1:
                res = max(res, r - l + 1)

            l = r + 1
            r = r + 1
        return res