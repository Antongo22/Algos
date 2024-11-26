from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_growing = True
        is_decreasing = True
        
        for i in range(1, len(nums)):
            is_growing = nums[i-1] <= nums[i] and is_growing
            is_decreasing = nums[i-1] >= nums[i] and is_decreasing
            
        return is_growing or is_decreasing  