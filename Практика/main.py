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
class Solution:
    def selectionoOfGoods(self, goods: List[int], buyerNeeds: List[int]) -> int:
        goods.sort()
        buyerNeeds.sort()

        pointer_goods = 0
        pointer_buyerNeeds = 0

        res = 0

        while pointer_goods <= len(goods) and pointer_buyerNeeds < len(buyerNeeds):
            current_good = goods[pointer_goods]

            if pointer_goods == len(goods) - 1:
                next_good = float('inf')
            else:
                next_good = goods[pointer_goods + 1]

            current_difference = abs(current_good - buyerNeeds[pointer_buyerNeeds])
            next_difference = abs(next_good - buyerNeeds[pointer_buyerNeeds])

            if current_difference <= next_difference:
                res += current_difference
                pointer_buyerNeeds += 1
            else:
                pointer_goods += 1


        return res

goods = [8, 3, 5, 7]
buyerNeeds = [5, 6, 7, 9]
new = Solution()
print(new.selectionoOfGoods(goods, buyerNeeds))