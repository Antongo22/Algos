class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        k -= 1
        
        res = 2_147_483_647
        
        for i in range(len(nums) - k):
            if nums[i+k] - nums[i] < res:
                res = nums[i+k] - nums[i]
        
        return res        