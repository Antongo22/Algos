from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pointer = 0

        res = ""
        while pointer != len(strs[0]):

            current_char = strs[0][pointer]

            for string in strs:
                if pointer == len(string):
                    return res

                if string[pointer] != current_char:
                    return res

            res += current_char
            pointer += 1

        return res