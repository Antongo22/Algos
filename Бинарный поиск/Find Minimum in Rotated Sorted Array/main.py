from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = -1, len(nums) - 1

        while r - l > 1:
            m = (r + l) // 2

            if nums[m] > nums[-1]:
                l = m
            else:
                r = m
        return nums[r]