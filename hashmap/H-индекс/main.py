from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        arr = [0 for _ in range(len(citations) + 1)]
        for i in range(len(citations)):
            arr[min(len(citations), citations[i])] += 1
        
        res = 0
        for i in range(len(citations), 0, -1):
            res += arr[i]
            if res >= i:
                return i

        return 0