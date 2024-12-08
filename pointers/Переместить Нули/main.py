from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pointer_fast = 1
        pointer_slow = 0

        while pointer_fast < len(nums) and pointer_slow < len(nums):
            if pointer_fast == len(nums):
                nums[pointer_slow] = 0
                pointer_slow += 1
                continue

            if nums[pointer_fast] == 0:
                pointer_fast += 1
                continue

            if nums[pointer_slow] != 0:
                pointer_slow += 1
                continue
                
            if  pointer_fast <= pointer_slow:
                pointer_fast += 1
                continue

            nums[pointer_slow], nums[pointer_fast] = nums[pointer_fast], nums[pointer_slow]