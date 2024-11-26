class Solution: 
    def rotateArr(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)

        self.rotateArr(nums, 0, len(nums) - 1)
        self.rotateArr(nums, 0, k - 1)
        self.rotateArr(nums, k, len(nums) - 1)
    

        