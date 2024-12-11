from typing import *


class Solution:
    def good(self, num, target):
        return num <= target

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_index = -1

        l, r = 0, len(matrix)
        while r - l > 1:
            mid = (l + r) // 2

            first, last = matrix[mid][0], matrix[mid][-1]
            if first <= target <= last:
                row_index = mid
                break
            elif target < first:
                r = mid
            else:
                l = mid
        else:
            if l < len(matrix) and matrix[l][0] <= target <= matrix[l][-1]:
                row_index = l
            else:
                return False

        l1, r1 = 0, len(matrix[row_index])

        while r1 - l1 > 1:
            mid1 = (l1 + r1) // 2

            if self.good(matrix[row_index][mid1], target):
                l1 = mid1
            else:
                r1 = mid1

        return matrix[row_index][l1] == target