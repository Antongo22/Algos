from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = -1
        zerocount = 0
        res = 0

        while l < len(nums):
            while r + 1 < len(nums) and (nums[r + 1] == 1 or zerocount < k):
                if nums[r + 1] == 0:
                    zerocount += 1
                r += 1

            res = max(res, r - l + 1)
            zerocount += -1 if nums[l] == 0 else 0
            l += 1
        return res