class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            num1 = nums[i]
            if target - num1 in d:
                return [d[target-num1], i]
            
            if num1 not in d:
                d[num1] = i
            
            
            
            


