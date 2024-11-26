class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_length = 1
        current_length = 1
        
        for i in range(1, len(nums) ):
            if nums[i-1] < nums[i]:
                current_length += 1
            else:
                current_length = 1
            if current_length > max_length:
                max_length = current_length
        return max_length        