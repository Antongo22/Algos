from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxV1 = -2_147_483_648
        maxV2 = -2_147_483_648
        for i in range(len(nums)):
            if nums[i] >= maxV1:
                maxV2 = maxV1
                maxV1 = nums[i]
            elif nums[i] > maxV2:
                maxV2 = nums[i]
                
        return (maxV1 - 1) * (maxV2 - 1)        
