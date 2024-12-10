from typing import *

class Solution:
    def good_first(self, nums, target):
        l, r = -1, len(nums) -1

        while r - l > 1:
            mid = (l+r) // 2

            if nums[mid] < target:
                l = mid
            else:
                r = mid
        return r if nums[r] == target else -1

    def good_last(self, nums, target):
        l, r = 0, len(nums)

        while r - l > 1:
            mid = (l+r) // 2

            if nums[mid] <= target:
                l = mid
            else:
                r = mid
        return l if nums[l] == target else -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        r = self.good_last(nums, target)
        l = self.good_first(nums, target)

        return [l, r]