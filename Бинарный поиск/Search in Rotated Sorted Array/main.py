from typing import List


class Solution:
    def findStart(self, nums: List[int]):
        l, r = -1, len(nums) - 1

        while r - l > 1:
            m = (l + r) // 2

            if nums[m] > nums[-1]:
                l = m
            else:
                r = m

        return r

    def search(self, nums: List[int], target: int) -> int:
        os = self.findStart(nums)
        l, r = os, len(nums) + os

        while r - l > 1:
            m = (l + r) // 2

            if nums[m % len(nums)] <= target:
                l = m
            else:
                r = m

        realLeft = l % len(nums)
        return realLeft if nums[realLeft] == target else -1

