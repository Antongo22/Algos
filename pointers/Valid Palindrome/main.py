from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer_start = 0
        pointer_end = len(numbers) - 1
        

        while pointer_start <= pointer_end:
            if numbers[pointer_end] + numbers[pointer_start] == target:
                return [pointer_start + 1, pointer_end + 1] 
            elif (numbers[pointer_end] - numbers[pointer_start]) - target > 0:
                pointer_end -= 1
            else:
                pointer_start += 1       