from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []

        for i in nums:
            if i < 0:
                negative.append(i ** 2)
            else:
                positive.append(i ** 2)

        pointer_positive = 0
        pointer_negative =  len(negative) - 1

        result_array = []

        while pointer_positive < len(positive) or pointer_negative >= 0:
            if pointer_positive >= len(positive):
                result_array.append(negative[pointer_negative])
                pointer_negative -= 1
                continue

            if pointer_negative < 0:
                result_array.append(positive[pointer_positive])
                pointer_positive += 1
                continue

            if positive[pointer_positive] <= negative[pointer_negative]:
                result_array.append(positive[pointer_positive])
                pointer_positive += 1
            else:
                result_array.append(negative[pointer_negative])
                pointer_negative -= 1

        return result_array
