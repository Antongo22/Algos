from typing import List


# 1
# def calculate( nums1: List[int], nums2: List[int]) -> List[int]:
#     carry = 0
#     result = []
#     p1 = len(nums1) - 1
#     p2 = len(nums2) - 1
#
#     while p1 >= 0 or p2 >= 0 or carry > 0:
#         value1 = nums1[p1] if p1 >= 0 else 0
#         value2 = nums2[p2] if p2 >= 0 else 0
#         sum_val = carry + value1 + value2
#         carry = sum_val // 10
#         num = sum_val % 10
#         result.append(num)
#         p1 -= 1
#         p2 -= 1
#
#     return result[::-1]
#
#
# arr = [1, 2, 3]
# arr2 = [3, 4, 5, 6]
#
# print(calculate(arr, arr2))


# 2
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         min_length = min(len(s) for s in strs)
#
#         res = ""
#
#         for i in range(min_length):
#             current_char = strs[0][i]
#             for s in strs:
#                 if s[i] != current_char:
#                     return res
#             res += current_char
#
#         return res