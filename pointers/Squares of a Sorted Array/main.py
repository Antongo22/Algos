from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        pointer_start = 0
        pointer_end =  len(nums) - 1

        result_array = []

        while pointer_start <= pointer_end:
            if abs(nums[pointer_start]) > abs(nums[pointer_end]):
                result_array.append(nums[pointer_start] ** 2)
                pointer_start += 1

            else:
                result_array.append(nums[pointer_end] ** 2)
                pointer_end -= 1

        return list(reversed(result_array))
