class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        array_sum = sum(nums)
        left_sum = 0
        
        for i in range(len(nums)):
            c_num = nums[i]
            right_sum = array_sum - left_sum - c_num
            
            if right_sum == left_sum:
                return i
            
            left_sum += c_num 
        
        return -1    
           