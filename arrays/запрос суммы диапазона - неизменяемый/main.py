class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_array = [0]
        
        for i in range(len(nums)):
            self.prefix_array.append(self.prefix_array[-1] + nums[i])
        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_array[right + 1] - self.prefix_array[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)