from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for wordI in range(len(strs)):
            arr = [0 for _ in range(26)]
            for char in strs[wordI]:
                arr[ord(char) - ord("a")] += 1

            if tuple(arr) not in d:
                d[tuple(arr)] = []

            d[tuple(arr)].append(strs[wordI])

        res = []
        for i in d:
            res.append(d[i])

        return res