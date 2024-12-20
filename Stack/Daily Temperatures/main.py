from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for _ in range(len(temperatures))]

        for i, temperature in enumerate(temperatures):

            while stack and stack[-1][1] < temperature:
                last = stack[-1]
                result[last[0]] = i - last[0]
                del stack[-1]

            stack.append([i, temperature])

        return result