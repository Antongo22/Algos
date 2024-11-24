from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        arr = [0 for _ in range(len(A)+1)]
        c = 0

        res = []
        for i in range(len(A)):
            arr[A[i]] += 1
            arr[B[i]] += 1
            
            if A[i] == B[i]:
                c += 1
            else:
                if arr[A[i]] == 2:
                    c += 1
                if arr[B[i]] == 2:
                    c += 1
            res.append(c)

        return res