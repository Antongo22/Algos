from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0:1}
        current_prefix_sum = 0

        answ = 0

        for i in range(len(nums)):
            current_prefix_sum += nums[i]

            tmp_key = current_prefix_sum - k

            if tmp_key in prefix_sum:
                answ += prefix_sum[tmp_key]
            
            if current_prefix_sum not in prefix_sum:
                prefix_sum[current_prefix_sum] = 0

            prefix_sum[current_prefix_sum] += 1

        return answ

