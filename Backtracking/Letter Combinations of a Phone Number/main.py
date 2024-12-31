from typing import List

class Solution:
    def addinlist(self, index, digits, res, curcomb, nums):
        if index == len(digits):
            res.append("".join(curcomb))
            return

        dig = digits[index]
        for letter in nums[dig]:
            curcomb.append(letter)

            self.addinlist(index + 1, digits, res, curcomb, nums)

            curcomb.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        nums = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        self.addinlist(0, digits, res, [], nums)
        return res
