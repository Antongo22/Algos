from typing import *
    
class Solution:
    def good(self, num, target):
        return num <= target

    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums)

        while right - left > 1:
            mi = (right + left) // 2

            if self.good(nums[mi], target):
                left = mi
            else:
                right = mi

        return left if nums[left] == target else -1 