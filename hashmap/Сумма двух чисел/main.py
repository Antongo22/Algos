from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
	d = {} # значение - индекс значения
	for i in range(len(nums)):
		n = target - nums[i]
		if n in d:
			return [d[n], i]
		d[nums[i]] = i 
	return [-1,-1]