from enum import unique
from typing import List


# массивы
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

# указатели
# 1
# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         ps = 0
#         pt = 0
#
#         while ps < len(s) and pt < len(t):
#             if s[ps] == t[pt]:
#                 ps += 1
#                 pt += 1
#             else:
#                 pt += 1
#
#         return ps == len(s)

# 2
# class Solution:
#     def selectionoOfGoods(self, goods: List[int], buyerNeeds: List[int]) -> int:
#         goods.sort()
#         buyerNeeds.sort()
#
#         pointer_goods = 0
#         pointer_buyerNeeds = 0
#
#         res = 0
#
#         while pointer_goods <= len(goods) and pointer_buyerNeeds < len(buyerNeeds):
#             current_good = goods[pointer_goods]
#
#             if pointer_goods == len(goods) - 1:
#                 next_good = float('inf')
#             else:
#                 next_good = goods[pointer_goods + 1]
#
#             current_difference = abs(current_good - buyerNeeds[pointer_buyerNeeds])
#             next_difference = abs(next_good - buyerNeeds[pointer_buyerNeeds])
#
#             if current_difference <= next_difference:
#                 res += current_difference
#                 pointer_buyerNeeds += 1
#             else:
#                 pointer_goods += 1
#
#
#         return res
#
# goods = [8, 3, 5, 7]
# buyerNeeds = [5, 6, 7, 9]
# new = Solution()
# print(new.selectionoOfGoods(goods, buyerNeeds))


# class Solution:
#     def diagonalSum(self, mat: List[List[int]]) -> int:
#         sum = 0
#
#         for i in range(len(mat)):
#             j = len(mat) - 1 - i
#
#             sum += mat[i][i] + mat[i][j]
#
#         if len(mat) % 2 != 0:
#             sum -= mat[(len(mat) - 1) // 2][(len(mat) - 1) // 2]
#
#         return sum
#


# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         res = []
#
#         for i in range(len(nums) - 2):
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
#
#             l, r = i + 1, len(nums) - 1
#
#             while l < r:
#                 total = nums[i] + nums[l] + nums[r]
#
#                 if total < 0:
#                     l += 1
#                 elif total > 0:
#                     r -= 1
#                 else:
#                     res.append([nums[i], nums[l], nums[r]])
#
#                     while l < r and nums[l] == nums[l + 1]:
#                         l += 1
#
#                     while l < r and nums[r] == nums[r - 1]:
#                         r -= 1
#
#                     l += 1
#                     r -= 1
#
#         return res


# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         nums.sort()
#
#         sum_res = float('inf')
#
#         for i in range(len(nums) - 2):
#             l, r = i + 1, len(nums) - 1
#
#             while l < r:
#                 cs = nums[i] + nums[l] + nums[r]
#
#                 if abs(target - cs) < abs(target - sum_res):
#                     sum_res = cs
#
#                 if cs < target:
#                     l += 1
#                 elif cs > target:
#                     r -= 1
#                 else:
#                     return sum_res
#         return  sum_res


# def calculate(s: List[str]) -> int:
#     res = 0
#     cur_num = 0
#     prev_num = 0
#     operator = "+"
#
#     for i, c in enumerate(s):
#         if c .isdigit():
#             cur_num = cur_num * 10 + int(c)
#
#         if (not c.isdigit() and c != " ") or i == len(s) - 1:
#             if operator == "+":
#                 res += prev_num
#                 prev_num =  cur_num
#             elif operator == "*":
#                 prev_num *= cur_num
#
#             operator = c
#             cur_num = 0
#
#     res += prev_num
#     return res
#



# def chanceOfMeatballPrecipitations(gene: str, k: int) -> float:
#     if len(gene) < k:
#         return 0.0
#
#     total, unique = len(gene) - k + 1, 0
#
#     unique_chars = set()
#
#     for i in range(k):
#         if gene[i] in unique_chars:
#             break
#         unique_chars.add(gene[i])
#     else:
#         unique += 1
#
#     for i in range(1, total):
#         unique_chars.discard(gene[i - 1])
#         if gene[i + k - 1] in unique_chars:
#             unique_chars.clear()
#             continue
#         unique_chars.add(gene[i + k - 1])
#         unique += 1
#
#
#     return unique / total























